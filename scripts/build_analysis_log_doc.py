#!/usr/bin/env python3
"""Create docs/full-analysis-log.md excerpt from archive log."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / "archive" / "canvas-submissions" / "full_analysis.log"
OUT = ROOT / "docs" / "full-analysis-log.md"

KEEP = (
    "Volatility",
    "imageinfo",
    "pslist",
    "netscan",
    "connscan",
    "dlllist",
    "malfind",
    "hashdump",
    "filescan",
    "cmdline",
    "Win7SP1x64",
    "MemoryDump",
)


def main() -> None:
    data = LOG.read_bytes()
    lines = [s.decode("ascii", errors="ignore") for s in re.findall(rb"[ -~]{4,}", data)]
    picked: list[str] = []
    for line in lines:
        if any(k in line for k in KEEP) and len(line) < 200:
            if line not in picked:
                picked.append(line)
        if len(picked) >= 60:
            break

    body = "\n".join(
        [
            "# full_analysis.log — Volatility session excerpt",
            "",
            f"**Source:** [`full_analysis.log`](../archive/canvas-submissions/full_analysis.log)  ",
            "**Course:** IA 455 - Incident Response (EMU)  ",
            "**Author:** Julio Barros",
            "",
            "Terminal capture from memory forensics work (`script` output). Below: filtered lines showing Volatility 2 commands and framework output (full log is binary-heavy with ANSI escapes).",
            "",
            "```text",
            *picked[:50],
            "```",
            "",
            "See also [assignment-2-memory-forensics.md](assignment-2-memory-forensics.md) for the structured lab write-up.",
            "",
        ]
    )
    OUT.write_text(body, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
