# Правила генерации фото меню (live-эталон)

updated: 2026-09-07  
source_of_truth: `scripts/menu-image-prompts.json` → поле `style` + per-item `prompt`  
deploy: `coffee-friends-menu` / `coffee-menu` GitHub Pages

## Обязательно (как на сайте сейчас)

### Фон и кадр
- Чистый белый seamless `#FFFFFF`
- Мягкая контактная тень
- Продукт по центру, занимает **70–85%** кадра
- Ракурс ~**35°**, студийный свет, боковая/контровая подсветка жидкости
- Ultra realistic, appetizing
- **Без** текста, лого, watermark, рук
- Гарниры — минимальные, вкусные, рядом с продуктом (не на крышке)

### Напитки (drinks) — ЖЁСТКО
- Прозрачный **пластиковый takeaway-стакан**
- **БЕЗ крышки** (no lid / no dome / no straw hole cover)
- **Открытый верх** — видны пена / лёд / поверхность напитка
- Не стекло, не керамика, не бумажный стакан с рукавом

### Еда (food)
- Белая студия; тарелка / бокс / пергамент — ок
- Тот же белый фон и свет

### Техпроцесс
1. `GenerateImage` aspect **3:4**
2. Промпт = `style` + item `prompt` из `menu-image-prompts.json`
3. `scripts/convert-menu-png.py <png> drinks|food <file.jpg>` → MarketingCofe + sync
4. При необходимости `scripts/compress-menu-images.py` (или точечно q78)
5. Запись в `menu/data/drinks.json` / `food.json` (`image`, `name`, `price`, …)
6. Новинка: `"new": true` (бейдж); снять флаг когда устареет
7. Бамп `ASSET_VER` в `board.html` + CSS `?v=`
8. Sync → push `coffee-friends-menu` и `coffee-menu`

## Запрещено
- `scripts/white-bg-menu-images.py` (GrabCut) — **не использовать**
- Бежевый студийный фон, стеклянные бокалы, крышки на напитках
- Фиолетовые SaaS-клише / dark-mode фон

## Добавление позиции
1. Техкарта / цена / категория согласованы
2. Добавить entry в JSON + строку в `menu-image-prompts.json`
3. Сгенерировать фото по правилам выше
4. Deploy + Ctrl+F5 на TV

## Удаление позиции
1. Убрать из `drinks.json` / `food.json`
2. Опционально: JPG и prompt оставить в архиве или удалить
3. Бамп `ASSET_VER`, push обоих зеркал
