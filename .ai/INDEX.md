# INDEX - MarketingCofe

| Путь | Назначение |
|------|------------|
| `.ai/CONTEXT.md` | Краткий контекст проекта |
| `.ai/IMAGE_GEN_RULES.md` | **Канон генерации фото** (plastic cup, white studio, pipeline) |
| `.ai/state.json` | Машинное состояние |
| `docs/display-setup.md` | Монитор, плеер, монтаж на изображение |
| `docs/menu-workflow.md` | Как собрать контент и выкатить на флеш |
| `menu/data/drinks.json` | Каталог напитков |
| `menu/data/food.json` | Каталог еды (из COFEPOINT preorderFood) |
| `menu/board.html` | Автопрокрутка слайдов (напитки + еда) |
| `menu/assets/css/menu.css` | Стили: gold price, badge, tags, 9:16 |
| `menu/assets/images/drinks/` | Фото напитков (white studio, JPEG) |
| `menu/assets/images/food/` | Фото еды (white studio, JPEG) |
| `D:/projects/coffee-friends-menu-sync/` | Зеркало GitHub `coffee-friends-menu` (deploy source) |
| `scripts/import-cofepoint-menu.py` | Импорт COFEPOINT → drinks.json + food.json |
| `scripts/compress-menu-images.py` | Сжатие JPG (max 960px, q78) |
| `scripts/convert-menu-png.py` | PNG→JPG (q85, max 960px) + копия в оба репо |
| `scripts/batch-regen-drinks.py` | Вывод полных промптов из manifest |
| `scripts/menu-image-prompts.json` | AI-промпты для 46 drinks + 14 food |
| `scripts/white-bg-menu-images.py` | Белая студия: сегментация фона и нормализация JPG (deprecated) |
| `scripts/serve-menu.ps1` | Локальный сервер меню |
| `C:/Users/user/.cursor/projects/d-projects-COFEPOINT/assets/test-espresso-tonic.png` | Локальный QA-кадр (не в репозитории меню) |
| `.ai/data/seasonal-drinks-draft-2026-08.md` | Черновик сезонных: имена, цены, техкарты |
| `.ai/data/barista-techcards-chat.txt` | Текст техкарт для чата бариста (готово к копированию) |

## Asset deploy

- Public: `puholet-sketch/coffee-friends-menu` + mirror `coffee-menu`
- Image canon: `.ai/IMAGE_GEN_RULES.md` / `scripts/menu-image-prompts.json`
- **Do not use** `scripts/white-bg-menu-images.py` (GrabCut)
