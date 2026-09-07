#!/usr/bin/env python3
"""Импорт menu.json из COFEPOINT → drinks.json + food.json для витрины MarketingCofe."""

import json
from pathlib import Path

COFE = Path(r"D:\projects\COFEPOINT\assets\data\menu.json")
MENU_DIR = Path(__file__).resolve().parent.parent / "menu" / "data"
DRINKS_OUT = MENU_DIR / "drinks.json"
FOOD_OUT = MENU_DIR / "food.json"

DESCRIPTIONS = {
    "espresso": "классический шот, насыщенный и ароматный",
    "amerikano": "эспрессо с водой — чистый вкус без молока",
    "kapuchino": "эспрессо, молоко и бархатная молочная пенка",
    "flet_uayt": "двойной эспрессо и молоко с тонким слоем пенки",
    "latte": "нежный кофе с большим количеством молока",
    "mokko": "шоколад, эспрессо и взбитое молоко",
    "raf": "сливочный кофе на сливках с ванилью",
    "bambl_kofe": "эспрессо, апельсин и карамель — слоистый хит",
    "glyase": "холодный кофе со льдом и мороженым",
    "frapuchino": "взбитый холодный кофе со льдом",
    "medovyy_staut": "холодный кофе с мёдом и пенкой стаута",
    "espresso_tonik": "эспрессо на тонике — бодрящий и игристый",
    "milksheyk": "густой молочный коктейль",
    "ays_mokko": "шоколадный кофе со льдом",
    "matcha": "японская матча на молоке — классика",
    "kakao": "тёплое какао с молоком",
    "kakao_bryut": "насыщенное какао без лишней сладости",
    "goryachiy_shokolad": "густой горячий шоколад",
    "raf_avtorskiy": "авторский раф с сезонным акцентом",
    "ays_latte": "латте со льдом — освежающий кофе",
    "limonady": "домашние лимонады — выбирайте вкус",
    "fresh_350_ml": "свежевыжатый фруктовый сок",
    "fresh_450_ml": "большая порция свежего фреша",
    "malina_imbir": "малина и имбирь — согревающий чай",
    "glintveyn_b_a": "безалкогольный глинтвейн с пряностями",
    "oblepiha_imbir": "облепиха, имбирь — яркий и согревающий",
    "apelsin_imbir": "апельсин с имбирём — цитрус и тепло",
    "imbirnyy_pryanik": "имбирный пряник — сезонный фруктовый чай",
    "ganpauder": "зелёный чай с дымным ароматом",
    "tseylon": "чёрный чай цейлон — классика",
    "te_guan_in": "улун с цветочным ароматом",
    "molochnyy_ulun": "молочный улун — сливочные ноты",
    "puer": "выдержанный пуэр — глубокий вкус",
}

FOOD_DESCRIPTIONS = {
    "kruassany": "хрустящие слоёные круассаны — классика кофейни",
    "batonchik": "домашний батончик — уютный перекус к кофе",
    "pechene": "рассыпчатое печенье — идеально к чаю и латте",
    "sochnik": "нежная творожная начинка в мягком тесте",
    "trubochka_so_sguschenkoy": "хрустящая вафля с нежной сгущёнкой внутри",
    "iriska": "карамельная ириска — сладкая ностальгия",
    "konfety_dabl_babl_v_assortimente": "жвачка в баночках — яркие вкусы на выбор",
    "sendvichi": "свежий хлеб, сытная начинка — к обеду или перекусу",
    "chiabatta": "хрустящая чиабатта с сочной начинкой",
    "rolly": "лаваш-ролл с начинкой — удобно взять с собой",
    "zavtraki": "сытный завтрак — начните день с аппетита",
    "goryachee": "тёплое блюдо на каждый день — сытно и по-домашнему",
    "salaty": "свежие салаты с сезонными овощами",
    "orehi_kulek_v_assortimente": "ореховый микс в бумажном кульке — лёгкий перекус",
}

FOOD_VOLUME = {
    "batonchik": "120 г — 120 ₽ · 150 г — 150 ₽",
    "kruassany": "свежая выпечка",
    "pechene": "порция",
    "sochnik": "порция",
    "trubochka_so_sguschenkoy": "порция",
    "iriska": "порция",
    "konfety_dabl_babl_v_assortimente": "ассортимент",
    "sendvichi": "на выбор начинки",
    "chiabatta": "на выбор начинки",
    "rolly": "на выбор начинки",
    "zavtraki": "порция",
    "goryachee": "порция",
    "salaty": "порция",
    "orehi_kulek_v_assortimente": "ассортимент",
}

FOOD_TAGS = {
    "pastry": ["dessert", "preorder"],
    "sandwich": ["sandwich", "preorder"],
    "hot": ["hot", "preorder"],
    "food": ["preorder"],
}

FOOD_IMAGE_MAP = {
    "konfety_dabl_babl_v_assortimente": "konfety_dabl_babl.jpg",
    "orehi_kulek_v_assortimente": "orehi_kulek.jpg",
}

FOOD_GROUP_ORDER = [
    ("pastry", "Десерты"),
    ("sandwich", "Сэндвичи"),
    ("hot", "Еда"),
    ("food", "Еда"),
]

MATCHA_VARIANTS = [
    {
        "id": "matcha-classic",
        "name": "Матча классическая",
        "volume": "350 мл",
        "price": "от 300 ₽",
        "description": "японская зелёная матча на молоке",
        "image": "assets/images/drinks/matcha-classic.jpg",
        "tags": ["hot", "matcha"],
    },
    {
        "id": "matcha-blue",
        "name": "Голубая матча",
        "volume": "350 мл",
        "price": "от 320 ₽",
        "description": "матча латте небесно-голубого цвета",
        "image": "assets/images/drinks/matcha-blue.jpg",
        "tags": ["cold", "matcha", "signature"],
    },
    {
        "id": "matcha-red",
        "name": "Красная матча",
        "volume": "350 мл",
        "price": "от 320 ₽",
        "description": "матча с малиной — яркий и ягодный",
        "image": "assets/images/drinks/matcha-red.jpg",
        "tags": ["cold", "matcha", "signature"],
    },
    {
        "id": "matcha-pink",
        "name": "Розовая матча",
        "volume": "350 мл",
        "price": "от 320 ₽",
        "description": "нежная клубничная матча на молоке",
        "image": "assets/images/drinks/matcha-pink.jpg",
        "tags": ["cold", "matcha", "signature"],
    },
    {
        "id": "matcha-mango-chili",
        "name": "Манго чили матча",
        "volume": "400 мл",
        "price": "от 380 ₽",
        "description": "прохладная матча с манго и острой ноткой",
        "image": "assets/images/drinks/matcha-mango-chili.jpg",
        "tags": ["cold", "matcha", "signature"],
    },
]

GROUP_ORDER = [
    ("signature", "Авторские"),
    ("coffee", "Кофе"),
    ("cold_coffee", "Холодный кофе"),
    ("seasonal", "Сезонные"),
    ("tea", "Чай"),
    ("lemonade", "Лимонады"),
]

IMAGE_MAP = {
    "kapuchino": "cappuccino.jpg",
    "latte": "latte.jpg",
    "flet_uayt": "flat-white.jpg",
    "raf": "raf.jpg",
    "raf_avtorskiy": "raf-signature.jpg",
    "bambl_kofe": "bumble-coffee.jpg",
    "ays_latte": "iced-latte.jpg",
    "frapuchino": "frappuccino.jpg",
    "espresso_tonik": "espresso-tonic.jpg",
    "medovyy_staut": "honey-stout.jpg",
    "kakao": "cocoa.jpg",
    "mokko": "mocha.jpg",
    "amerikano": "americano.jpg",
    "limonady": "lemonade.jpg",
    "matcha": "matcha-classic.jpg",
}


def fmt_volume(item: dict, *, food: bool = False) -> str:
    item_id = item["id"]
    if food and item_id in FOOD_VOLUME:
        return FOOD_VOLUME[item_id]
    vols = item.get("volumes") or []
    if vols:
        unit = "г" if food else "мл"
        parts = [f"{v['ml']} {unit} — {v['price']} ₽" for v in vols]
        return " · ".join(parts)
    return f"от {item['priceFrom']} ₽"


def fmt_price(item: dict) -> str:
    vols = item.get("volumes") or []
    if len(vols) == 1:
        return f"{vols[0]['price']} ₽"
    if vols:
        return f"от {item['priceFrom']} ₽"
    return f"от {item['priceFrom']} ₽"


def food_display_name(item: dict) -> str:
    name = item["name"]
    if item["id"] == "orehi_kulek_v_assortimente":
        return 'Орехи «Кулёк»'
    if item["id"] == "konfety_dabl_babl_v_assortimente":
        return "Конфеты дабл бабл"
    return name


def build_drinks(src: dict) -> dict:
    drinks = src["drinksNow"]
    by_group: dict[str, list] = {g: [] for g, _ in GROUP_ORDER}

    for item in drinks:
        g = item["group"]
        if g not in by_group:
            by_group[g] = []

        img_file = IMAGE_MAP.get(item["id"], f"{item['id']}.jpg")
        entry = {
            "id": item["id"],
            "name": item["name"],
            "volume": fmt_volume(item),
            "price": fmt_price(item),
            "description": DESCRIPTIONS.get(item["id"], item.get("groupLabel", "")),
            "image": f"assets/images/drinks/{img_file}",
            "tags": [],
        }
        if g in ("cold_coffee", "seasonal") and "айс" in item["name"].lower():
            entry["tags"].append("cold")
        elif g == "coffee":
            entry["tags"].append("hot")
        if item["id"] == "matcha":
            entry["tags"].append("matcha")

        by_group.setdefault(g, []).append(entry)

    categories = [{"id": "signature", "title": "Авторские", "drinks": MATCHA_VARIANTS}]
    for gid, title in GROUP_ORDER:
        if gid == "signature":
            continue
        items = by_group.get(gid, [])
        if items:
            categories.append({"id": gid, "title": title, "drinks": items})

    return {
        "brand": {
            "name": "CoffeeFriends",
            "tagline": "БЦ Китеж · 2\u00A0и\u00A011\u00A0этаж",
            "accent": "Coffee",
            "accentGold": "Friends",
        },
        "settings": {
            "slideDurationSec": 5,
            "orientation": "portrait",
            "aspectWidth": 9,
            "aspectHeight": 16,
            "width": 1080,
            "height": 1920,
            "showPrice": True,
        },
        "categories": categories,
    }


def build_food(src: dict) -> dict:
    food_items = src.get("preorderFood") or []
    by_group: dict[str, list] = {g: [] for g, _ in FOOD_GROUP_ORDER}

    for item in food_items:
        g = item["group"]
        img_file = FOOD_IMAGE_MAP.get(item["id"], f"{item['id']}.jpg")
        if g == "sandwich":
            title_group = "sandwich"
        elif g == "pastry":
            title_group = "pastry"
        else:
            title_group = "hot_food" if g in ("hot", "food") else g

        entry = {
            "id": item["id"],
            "name": food_display_name(item),
            "volume": fmt_volume(item, food=True),
            "price": fmt_price(item),
            "description": FOOD_DESCRIPTIONS.get(item["id"], item.get("groupLabel", "")),
            "image": f"assets/images/food/{img_file}",
            "tags": list(FOOD_TAGS.get(g, ["preorder"])),
        }
        if item["id"] == "salaty" and "hot" in entry["tags"]:
            entry["tags"] = ["preorder"]

        bucket = "hot_food" if g in ("hot", "food") else g
        by_group.setdefault(bucket, []).append(entry)

    category_titles = {
        "pastry": "Десерты",
        "sandwich": "Сэндвичи",
        "hot_food": "Еда",
    }
    category_order = ["pastry", "sandwich", "hot_food"]
    categories = []
    for cid in category_order:
        items = by_group.get(cid, [])
        if items:
            categories.append({"id": cid, "title": category_titles[cid], "items": items})

    return {"categories": categories}


def main() -> None:
    src = json.loads(COFE.read_text(encoding="utf-8"))

    drinks = build_drinks(src)
    food = build_food(src)

    DRINKS_OUT.write_text(json.dumps(drinks, ensure_ascii=False, indent=2), encoding="utf-8")
    FOOD_OUT.write_text(json.dumps(food, ensure_ascii=False, indent=2), encoding="utf-8")

    drink_count = sum(len(c["drinks"]) for c in drinks["categories"])
    food_count = sum(len(c["items"]) for c in food["categories"])
    print(f"Written {drink_count} drinks → {DRINKS_OUT}")
    print(f"Written {food_count} food items → {FOOD_OUT}")


if __name__ == "__main__":
    main()
