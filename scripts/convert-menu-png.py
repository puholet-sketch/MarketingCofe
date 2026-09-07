#!/usr/bin/env python3
"""Convert generated PNG to menu JPG and copy to both repos."""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

MAX_SIDE = 960
QUALITY = 85

MARKETING_ROOT = Path(r"D:\projects\MarketingCofe\menu\assets\images")
SYNC_ROOT = Path(r"D:\projects\coffee-friends-menu-sync\assets\images")


def convert_and_copy(png_path: Path, category: str, filename: str) -> None:
    with Image.open(png_path) as im:
        im = im.convert("RGB")
        w, h = im.size
        scale = min(1.0, MAX_SIDE / max(w, h))
        if scale < 1.0:
            im = im.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
        for root in (MARKETING_ROOT, SYNC_ROOT):
            out = root / category / filename
            out.parent.mkdir(parents=True, exist_ok=True)
            im.save(out, "JPEG", quality=QUALITY, optimize=True, progressive=True)
    print(f"OK {category}/{filename}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: convert-menu-png.py <png_path> <drinks|food> <filename.jpg>")
        sys.exit(1)
    convert_and_copy(Path(sys.argv[1]), sys.argv[2], sys.argv[3])
