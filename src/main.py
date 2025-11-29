from pathlib import Path
from typing import Annotated, Any, Literal

import typer

from src.algos.factorial import factorial_iterative, factorial_recursive
from src.algos.fibonacci import fibonacci_iterative, fibonacci_recursive
from src.constants import QUEUE_DIR, SORTS, STACK_DIR, TYPE_MAP
from src.structs.queue import Queue
from src.structs.stack import Stack

app = typer.Typer()


@app.command()
def factorial_cli(
    n: int = typer.Argument(..., min=0, help="НЕ отрицательное число"),
    recursive: bool = typer.Option(False, "--recursive", "-r"),
):
    if recursive:
        try:
            typer.echo(f"Факториал {n} = {factorial_recursive(n)}")
        except RecursionError as e:
            typer.secho(f"Ошибка: {e}", fg=typer.colors.RED)
            raise typer.Exit(1) from None
    else:
        typer.echo(f"Факториал {n} = {factorial_iterative(n)}")


@app.command()
def fibonacci_cli(
    n: int = typer.Argument(..., min=0, help="НЕ отрицательное число"),
    recursive: bool = typer.Option(False, "--recursive", "-r"),
):
    if recursive:
        try:
            typer.echo(f"Число Фибоначчи на {n} позиции = {fibonacci_recursive(n)}")
        except RecursionError as e:
            typer.secho(f"Ошибка: {e}", fg=typer.colors.RED)
            raise typer.Exit(1) from None
    else:
        typer.echo(f"Число Фибоначчи на {n} позиции = {fibonacci_iterative(n)}")


@app.command()
def sort_cli(
    numbers: Annotated[list[str], typer.Argument(help="Список чисел")],
    sort: str = typer.Option("quick", "--sort", help="Тип сортировки"),
    nums_type: Literal["int", "float"] = typer.Option(
        "int", "--type", "-t", help="Тип данных: int | float"
    ),
    reverse: bool = typer.Option(False, "--reverse", "-r"),
    base: int = typer.Option(10, "--base", "-b"),
):
    if sort not in SORTS:
        typer.secho(f"{sort}_sort не найдена", fg=typer.colors.RED)
        raise typer.Exit(1)

    sort_spec = SORTS[sort]
    sort_type = sort_spec["type"]

    # Проверка на поддерживаемость
    if sort_type != "both" and sort_type != nums_type:
        typer.secho(
            # Английский короче по объёму
            f"{sort}_sort поддерживает только {sort_type}. Use --type={sort_type}",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    # Преобразование в числа
    adapter: Any = TYPE_MAP[nums_type]
    parsed = []
    for x in numbers:
        try:
            parsed.append(adapter.validate_python(x))
        except Exception as e:
            typer.secho(f"Ошибка преобразования данных: {e}", fg=typer.colors.RED)
            raise typer.Exit(1) from e

    # Доп аргументы
    kwargs: dict[str, Any] = {"reverse": reverse}
    params: Any = sort_spec.get("params", [])
    if "base" in params:
        kwargs["base"] = base

    func: Any = sort_spec["func"]
    result = func(parsed, **kwargs)

    typer.echo(f"{sort}_sort: {result}")


# Вспомогательные функции
def load_stack(name: str) -> tuple[Stack, Path]:
    filepath = STACK_DIR / f"{name}.bin"
    s = Stack()
    s.load_from_file(filepath)
    return s, filepath


def load_queue(name: str) -> tuple[Queue, Path]:
    filepath = QUEUE_DIR / f"{name}.bin"
    q = Queue()
    q.load_from_file(filepath)
    return q, filepath


# Stack
@app.command(help="Добавить элемент в стек")
def stack_push(
    value: int = typer.Argument(..., help="Добавляемое число"),
    name: str = typer.Option("default", "--name", "-n", help="Имя стека"),
):
    s, filepath = load_stack(name)
    s.push(value)
    s.save_to_file(filepath)
    typer.echo(f"Pushed {value} to stack '{name}'")


@app.command(help="Удалить и вернуть верхний элемент стека")
def stack_pop(
    name: str = typer.Option("default", "--name", "-n", help="Имя стека"),
):
    s, filepath = load_stack(name)
    try:
        val = s.pop()
        s.save_to_file(filepath)
        typer.echo(f"Popped from stack '{name}': {val}")
    except IndexError as e:
        typer.secho(f"Stack '{name}' error: {e}", fg=typer.colors.RED)
        raise typer.Exit(1)


@app.command(help="Посмотреть верхний элемент стека")
def stack_peek(
    name: str = typer.Option("default", "--name", "-n", help="Имя стека"),
):
    s, _ = load_stack(name)
    try:
        typer.echo(f"Top of stack '{name}': {s.peek()}")
    except IndexError as e:
        typer.secho(f"Stack '{name}' error: {e}", fg=typer.colors.RED)
        raise typer.Exit(1)


@app.command(help="Получить минимальный элемент стека")
def stack_min(
    name: str = typer.Option("default", "--name", "-n", help="Имя стека"),
):
    s, _ = load_stack(name)
    try:
        typer.echo(f"Minimum of stack '{name}': {s.min()}")
    except IndexError as e:
        typer.secho(f"Stack '{name}' error: {e}", fg=typer.colors.RED)
        raise typer.Exit(1)


@app.command(help="Проверить, пуст ли стек")
def stack_is_empty(
    name: str = typer.Option("default", "--name", "-n", help="Имя стека"),
):
    s, _ = load_stack(name)
    state = "empty" if s.is_empty() else "not empty"
    typer.echo(f"Stack '{name}' is {state}")


@app.command(help="Получить длину стека")
def stack_len(
    name: str = typer.Option("default", "--name", "-n", help="Имя стека"),
):
    s, _ = load_stack(name)
    typer.echo(f"Length of stack '{name}': {s.__len__()}")


# Queue
@app.command(help="Добавить элемент в очередь")
def queue_enqueue(
    value: int = typer.Argument(..., help="Добавляемое число"),
    name: str = typer.Option("default", "--name", "-n", help="Имя очереди"),
):
    q, filepath = load_queue(name)
    q.enqueue(value)
    q.save_to_file(filepath)
    typer.echo(f"Enqueued {value} to queue '{name}'")


@app.command(help="Удалить и вернуть первый элемент очереди")
def queue_dequeue(
    name: str = typer.Option("default", "--name", "-n", help="Имя очереди"),
):
    q, filepath = load_queue(name)
    try:
        val = q.dequeue()
        q.save_to_file(filepath)
        typer.echo(f"Dequeued from queue '{name}': {val}")
    except IndexError as e:
        typer.secho(f"Queue '{name}' error: {e}", fg=typer.colors.RED)
        raise typer.Exit(1)


@app.command(help="Посмотреть первый элемент очереди")
def queue_front(
    name: str = typer.Option("default", "--name", "-n", help="Имя очереди"),
):
    q, _ = load_queue(name)
    try:
        typer.echo(f"Front of queue '{name}': {q.front()}")
    except IndexError as e:
        typer.secho(f"Queue '{name}' error: {e}", fg=typer.colors.RED)
        raise typer.Exit(1)


@app.command(help="Пуста ли очередь")
def queue_is_empty(
    name: str = typer.Option("default", "--name", "-n", help="Имя очереди"),
):
    q, _ = load_queue(name)
    state = "empty" if q.is_empty() else "not empty"
    typer.echo(f"Queue '{name}' is {state}")


@app.command(help="Получить длину очереди")
def queue_len(
    name: str = typer.Option("default", "--name", "-n", help="Имя очереди"),
):
    q, _ = load_queue(name)
    typer.echo(f"Length of queue '{name}': {q.__len__()}")


if __name__ == "__main__":
    app()
