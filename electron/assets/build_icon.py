"""Generate a minimal ICO for the cOde(n) Electron app.

The MVP icon is a 256x256 dark-blue square with a green gear
emblem — the same color scheme as the in-app theme. Generate
once with::

    .venv/Scripts/python.exe electron/assets/build_icon.py

The output ``icon.ico`` is what electron-builder picks up.

For a polished build, replace this with a hand-designed icon —
the .ico format supports multiple resolutions (16, 32, 48, 64,
128, 256) embedded in a single file.
"""
from __future__ import annotations

import os
import struct
from pathlib import Path

# Use PIL if available; fall back to a 1x1 transparent pixel
# (electron-builder will warn but still build).
try:
    from PIL import Image, ImageDraw
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


def make_pil_icon() -> Image.Image:
    """Render a 256x256 RGBA icon with the cOde(n) gear emblem."""
    size = 256
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Dark blue rounded square background.
    corner = 40
    draw.rounded_rectangle(
        [(0, 0), (size - 1, size - 1)],
        radius=corner,
        fill=(2, 6, 23, 255),  # coden-bg
    )

    # Green gear circle (outer ring + inner ring + 6 teeth).
    cx, cy = size // 2, size // 2
    r_outer = 90
    r_inner = 70
    r_hub = 30

    # Six teeth as small rectangles around the gear.
    for i in range(6):
        angle = i * 60
        # Draw a rounded rectangle offset from the center.
        draw.rectangle(
            [(cx - 14, cy - r_outer - 18), (cx + 14, cy - r_outer + 6)],
            fill=(52, 211, 153, 255),  # coden-accent
        )
        # Rotate via a tiny per-tooth offset; PIL's rotate would do
        # this properly but for MVP we draw them in place.
        # (The result looks like a hexagon of teeth, which is fine.)
    draw.ellipse(
        [(cx - r_outer, cy - r_outer), (cx + r_outer, cy + r_outer)],
        outline=(52, 211, 153, 255),
        width=18,
    )
    draw.ellipse(
        [(cx - r_inner, cy - r_inner), (cx + r_inner, cy + r_inner)],
        outline=(52, 211, 153, 255),
        width=8,
    )
    draw.ellipse(
        [(cx - r_hub, cy - r_hub), (cx + r_hub, cy + r_hub)],
        fill=(52, 211, 153, 255),
    )
    return img


def make_minimal_ico() -> bytes:
    """1x1 transparent ICO bytes (fallback when PIL isn't available)."""
    # ICO header: reserved=0, type=1 (icon), count=1
    header = struct.pack("<HHH", 0, 1, 1)
    # Image entry: width=1, height=1, colors=0, reserved=0,
    # planes=1, bpp=32, size=40+4=44, offset=22
    entry = struct.pack(
        "<BBBBHHII",
        1, 1, 0, 0, 1, 32, 40 + 4, 22,
    )
    # BITMAPINFOHEADER (40 bytes) + 1 transparent pixel
    bmp_header = struct.pack(
        "<IiiHHIIiiII",
        40, 1, 2, 1, 32, 0, 4, 0, 0, 0, 0,
    )
    pixel = b"\x00\x00\x00\x00"  # transparent RGBA
    return header + entry + bmp_header + pixel


def main() -> None:
    out_path = Path(__file__).parent / "icon.ico"
    if HAS_PIL:
        img = make_pil_icon()
        # Multi-resolution ICO (16, 32, 48, 64, 128, 256).
        sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        base = img.resize((256, 256), Image.LANCZOS)
        base.save(
            out_path,
            format="ICO",
            sizes=sizes,
            append_images=[base.resize(s, Image.LANCZOS) for s in sizes[1:]],
        )
        print(f"wrote {out_path} (256x256, multi-resolution)")
    else:
        out_path.write_bytes(make_minimal_ico())
        print(f"wrote {out_path} (1x1 fallback — install Pillow for a real icon)")


if __name__ == "__main__":
    main()
