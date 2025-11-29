# Лаба по Python №3

## Установка и запуск
```bash
uv venv

source .venv/bin/activate # Для Linux/MacOS
source .venv\Scripts\activate # Для Windows

uv sync
```

## Тесты
```bash
uv run pytest
```

## CLI Команды

### Алгоритмы

#### Факториал
```bash
# Итеративный
uv run -m src.main factorial-cli 5

# Рекурсивный
uv run -m src.main factorial-cli 5 --recursive
```

#### Фибоначчи
```bash
# Итеративный
uv run -m src.main fibonacci-cli 5

# Рекурсивный
uv run -m src.main fibonacci-cli 5 -r
```

### Сортировки
По умолчанию используется `--type int`

**Следующие сортировки поддерживают и int, и float:**
- `bubble` - пузырьковая сортировка
- `quick` - быстрая сортировка
- `heap` - пирамидальная сортировка
- `insertion` - сортировка вставками

**Только int:**
- `counting` - сортировка подсчётом (поддерживает `--base`)
- `radix` - поразрядная сортировка (поддерживает `--base`)

**Только float:**
- `bucket` - блочная сортировка

**Поддерживаемые флаги:**
- `--reverse` / `-r` - сортировка в обратном порядке (все сортировки)
- `--base` / `-b` - основание системы счисления (только `counting` и `radix`, по умолчанию 10)
- `--type` / `-t` - тип данных: `int` или `float` (по умолчанию `int`)

```bash
# Быстрая сортировка (по умолчанию)
uv run -m src.main sort-cli 5 2 9 1 5 6

# Пузырьковая сортировка с реверсом
uv run -m src.main sort-cli 5 2 9 1 5 6 --sort bubble --reverse

# Counting sort с другим base
uv run -m src.main sort-cli 15 3 9 1 5 6 --sort counting --base 16

# Radix sort с base=2
uv run -m src.main sort-cli 8 4 2 1 16 --sort radix -b 2

# Bucket sort для float
uv run -m src.main sort-cli 5.5 2.2 9.9 1.1 --sort bucket --type float

# Heap sort
uv run -m src.main sort-cli 5 2 9 1 5 6 --sort heap

# Insertion sort (Дополнительно для bucket_sort)
uv run -m src.main sort-cli 5 2 9 1 5 6 --sort insertion -r
```
### Stack

```bash
# Добавить элемент
uv run -m src.main stack-push 5 -n mystack
uv run -m src.main stack-push 10 -n mystack
uv run -m src.main stack-push 9 -n mystack


# Удалить и вернуть верхний элемент
uv run -m src.main stack-pop --name mystack

# Посмотреть верхний элемент
uv run -m src.main stack-peek -n mystack

# Получить минимум
uv run -m src.main stack-min -n mystack

# Проверить, пуст ли стек
uv run -m src.main stack-is-empty -n mystack

# Получить длину
uv run -m src.main stack-len -n mystack
```

### Queue

```bash
# Добавить элемент
uv run -m src.main queue-enqueue 42 -n myqueue
uv run -m src.main queue-enqueue 10 -n myqueue

# Удалить и вернуть первый элемент
uv run -m src.main queue-dequeue --name myqueue

# Посмотреть первый элемент
uv run -m src.main queue-front -n myqueue

# Проверить, пуста ли очередь
uv run -m src.main queue-is-empty -n myqueue

# Получить длину
uv run -m src.main queue-len -n myqueue
```
И опять лаба не до конца, так как планирование... Конечно, можно перекинуть вину на вакцинацию и хакатон, но всё же
