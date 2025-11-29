# Лаба по Python №3

## Установка и запуск
```bash
uv venv

source .venv/bin/activate # Для Linux/MacOS
source .venv\Scripts\activate # Для Windows

uv sync
```
```bash
uv run -m src.main # Запуск шелла
uv run pytest # Запуск тестов
```

```bash
uv run -m src.main bubble-sort-cmd 5 2 9 1 5 6 --reverse
```
