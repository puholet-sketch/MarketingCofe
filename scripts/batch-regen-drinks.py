#!/usr/bin/env python3
"""Helper: print full prompts for drink regeneration from manifest."""
import json
from pathlib import Path

manifest = json.loads(Path(__file__).with_name("menu-image-prompts.json").read_text(encoding="utf-8"))
style = manifest["style"]
for item in manifest["drinks"]:
    stem = Path(item["file"]).stem
    print(f"{stem}\t{style} {item['prompt']}")
