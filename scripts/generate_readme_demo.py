"""Generate docs/demo.gif — IR phase workflow for README."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "demo.gif"

W, H = 720, 200
BG = (18, 22, 32)
ACCENT = (56, 189, 248)
TEXT = (226, 232, 240)
MUTED = (148, 163, 184)

PHASES = [
    ("Prepare", "Virtual lab + sensors"),
    ("Detect", "Logs, alerts, PCAP"),
    ("Analyze", "Memory + disk artifacts"),
    ("Contain", "Isolate affected hosts"),
    ("Recover", "Restore + harden"),
]


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for name in ("segoeui.ttf", "arial.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def frame(active: int) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    title_font = load_font(22)
    label_font = load_font(14)
    sub_font = load_font(11)

    draw.text((24, 16), "IA455 — Incident response workflow", fill=TEXT, font=title_font)

    box_w = 120
    gap = 12
    start_x = 24
    y = 72

    for i, (name, sub) in enumerate(PHASES):
        x = start_x + i * (box_w + gap)
        fill = ACCENT if i == active else (40, 48, 66)
        outline = ACCENT if i == active else MUTED
        draw.rounded_rectangle((x, y, x + box_w, y + 56), radius=8, fill=fill, outline=outline, width=2)
        tw = draw.textlength(name, font=label_font)
        draw.text((x + (box_w - tw) / 2, y + 10), name, fill=TEXT if i == active else MUTED, font=label_font)
        sw = draw.textlength(sub, font=sub_font)
        draw.text((x + (box_w - sw) / 2, y + 32), sub, fill=TEXT if i == active else MUTED, font=sub_font)

        if i < len(PHASES) - 1:
            ax = x + box_w + 2
            draw.line((ax, y + 28, ax + gap - 4, y + 28), fill=MUTED, width=2)
            draw.polygon([(ax + gap - 6, y + 24), (ax + gap - 2, y + 28), (ax + gap - 6, y + 32)], fill=MUTED)

    return img


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    frames = [frame(i) for i in range(len(PHASES))]
    frames[0].save(
        OUT,
        save_all=True,
        append_images=frames[1:],
        duration=900,
        loop=0,
        optimize=True,
    )
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
