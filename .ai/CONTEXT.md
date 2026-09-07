# MarketingCofe — CoffeeFriends digital menu

context_version: 22
updated: 2026-09-07

## Цель

Цифровая вывеска CoffeeFriends (БЦ Китеж): HTML-слайды напитков и еды, white studio + золото в UI.

## Статус

- Live: `ASSET_VER=20260907-caption-max` — подписи max по ширине/высоте, без переносов; TV rotate ⟳
- **Правило фото (зафиксировано):** `.ai/IMAGE_GEN_RULES.md` + `scripts/menu-image-prompts.json` → `style`
  - белый `#FFFFFF`, soft shadow, 3:4
  - напитки: **plastic takeaway cup, NO lid, open top**
  - еда: тарелка/бокс на white studio
  - **не** GrabCut (`white-bg-menu-images.py`)
- Каталог: `menu/data/drinks.json`, `menu/data/food.json`; новинки `"new": true`
- Deploy: `coffee-friends-menu` + зеркало `coffee-menu`; исходник `MarketingCofe`

## Следующий шаг

При add/remove позиций — строго по `.ai/IMAGE_GEN_RULES.md`.
