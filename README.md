# MarketingCofe

Цифровое меню для кофепоинта за витражом: бюджетное железо + красивые слайды напитков.

## Быстрый старт

1. **Железо** — см. [docs/display-setup.md](docs/display-setup.md): HDMI-рекламный плеер + монитор + флешка (не portable monitor с Ozon).
2. **Меню** — заполните [menu/data/drinks.json](menu/data/drinks.json), добавьте фото в `menu/assets/images/drinks/`.
3. **Белый фон** — при необходимости прогоните `python scripts/white-bg-menu-images.py --in-place`, затем `python scripts/compress-menu-images.py`.
4. **Просмотр** — из папки `menu` запустите `../scripts/serve-menu.ps1` или `python -m http.server 8080`, откройте http://localhost:8080/board.html
5. **Ролик** — полный экран (F11), запись Win+G или OBS → MP4 на флешку.

## Структура

```
.ai/           — контекст проекта
docs/          — инструкции по железу и контенту
menu/          — HTML-слайды и данные напитков
scripts/       — вспомогательные скрипты
```

## Следующие шаги

- [ ] Подставить реальное название кофепоинта в `drinks.json` → `brand`
- [ ] При желании заменить white-studio batch на полноценную AI/фото-пересъёмку hero-позиций
- [ ] Выбрать и купить HDMI-плеер с автозапуском
- [ ] Записать `menu.mp4` и проверить на флешке
