import json
from pathlib import Path


def main() -> None:
    root = Path("d:/projects/MarketingCofe")
    # board.html живёт в menu/, поэтому пути вида "assets/images/..." физически
    # лежат в menu/assets/...
    board_root = root / "menu"
    checks = [
        ("drinks", "menu/data/drinks.json", "drinks"),
        # food.json структура: categories[].items
        ("food", "menu/data/food.json", "items"),
    ]

    missing = []
    total_images_ref = 0

    for kind, rel_json, array_key in checks:
        data = json.loads((root / rel_json).read_text(encoding="utf-8"))
        cats = data.get("categories", [])

        n = 0
        miss = 0
        for cat in cats:
            items = cat.get(array_key) or []
            for it in items:
                n += 1
                total_images_ref += 1
                rel = it.get("image")
                if not rel:
                    continue
                img = board_root / rel
                if not img.exists():
                    miss += 1
                    missing.append(str(img))

        print(f"{kind}: items={n}, missing={miss}")

    print(f"TOTAL missing: {len(missing)}")
    if missing:
        print("Sample missing paths:")
        for p in missing[:15]:
            print(" -", p)
        raise SystemExit(1)


if __name__ == "__main__":
    main()

