#!/usr/bin/env python3
"""Build markdown for midterm/final PDFs with screenshots."""

from __future__ import annotations

import re
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive" / "canvas-submissions"
SHOTS = ROOT / "docs" / "screenshots"
DOCS = ROOT / "docs"

PDF_OUT = {
    "ia455-midterm final.pdf": "ia455-midterm.md",
    "ia455-final.pdf": "ia455-final-exam.md",
}


def slugify(stem: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")
    return s[:80]


def extract_images() -> None:
    SHOTS.mkdir(parents=True, exist_ok=True)
    for pdf_name in PDF_OUT:
        pdf = ARCHIVE / pdf_name
        if not pdf.exists():
            continue
        reader = PdfReader(pdf)
        base = slugify(pdf.stem)
        for pi, page in enumerate(reader.pages, start=1):
            for ii, img in enumerate(page.images, start=1):
                ext = ".png" if img.name.lower().endswith(".png") else ".jpg"
                (SHOTS / f"{base}-p{pi}-img{ii}{ext}").write_bytes(img.data)


def build(pdf_name: str, out_name: str) -> None:
    pdf = ARCHIVE / pdf_name
    reader = PdfReader(pdf)
    base = slugify(pdf.stem)
    rel = pdf.relative_to(ROOT).as_posix().replace(" ", "%20")
    title = pdf.stem
    lines: list[str] = [
        f"# {title}",
        "",
        f"**Source:** [`{pdf.name}`](../{rel})  ",
        "**Course:** IA 455 - Incident Response (EMU)  ",
        "**Author:** Julio Barros",
        "",
    ]
    for pi, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()
        imgs = sorted(p.name for p in SHOTS.glob(f"{base}-p{pi}-img*"))
        if text or imgs:
            lines.extend([f"## Page {pi}", ""])
        if text:
            lines.append(text)
            lines.append("")
        for img in imgs:
            lines.append(f"![{title} p{pi}](screenshots/{img})")
            lines.append("")
    (DOCS / out_name).write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    print(f"wrote docs/{out_name}")


def main() -> None:
    extract_images()
    for pdf_name, out_name in PDF_OUT.items():
        if (ARCHIVE / pdf_name).exists():
            build(pdf_name, out_name)


if __name__ == "__main__":
    main()
