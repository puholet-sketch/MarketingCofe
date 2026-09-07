# Запуск локального просмотра меню (board.html + drinks.json)
$root = Split-Path $PSScriptRoot -Parent
$menuDir = Join-Path $root "menu"
Set-Location $menuDir

Write-Host "Меню: http://localhost:8080/board.html" -ForegroundColor Green
Write-Host "Ctrl+C для остановки" -ForegroundColor Gray

if (Get-Command python -ErrorAction SilentlyContinue) {
  python -m http.server 8080
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
  py -m http.server 8080
} else {
  Write-Host "Python не найден. Установите Python или откройте board.html через Live Server в VS Code." -ForegroundColor Yellow
  Start-Process "board.html"
}
