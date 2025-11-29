from typing import Annotated, Any, Literal

import typer

from src.algos.factorial import factorial_iterative, factorial_recursive
from src.algos.fibonacci import fibonacci_iterative, fibonacci_recursive
from src.constants import SORTS, TYPE_MAP

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


if __name__ == "__main__":
    app()
