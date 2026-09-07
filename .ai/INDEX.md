# INDEX - MarketingCofe

| Путь | Назначение |
|------|------------|
| `.ai/CONTEXT.md` | Краткий контекст проекта |
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

## Asset deploy (2026-08-12)

- Commit: **61e871d** on `coffee-friends-menu` main (full v4 regen)
- Prior: **afbbefa** (partial plastic-cup), **7938b35** (interim), **0906236** (restore-ai)
- **ASSET_VER:** `20260812-v4`
- **60** images under `assets/images/`; none >500 KB; all <100 KB
- **46** drinks + **14** food JPGs fully regenerated (plastic cup no lid, white studio)
