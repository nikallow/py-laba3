from typing import Annotated

import typer

from src.algos.factorial import factorial_iterative, factorial_recursive
from src.algos.fibonacci import fibonacci_iterative, fibonacci_recursive
from src.sorts.bubble_sort import bubble_sort
from src.sorts.bucket_sort import bucket_sort
from src.sorts.counting_sort import counting_sort
from src.sorts.heap_sort import heap_sort
from src.sorts.insertion_sort import insertion_sort
from src.sorts.quick_sort import quick_sort
from src.sorts.radix_sort import radix_sort

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
def bubble_sort_cli(
    numbers: Annotated[list[int], typer.Argument(help="Список чисел (int)")],
    reverse: bool = typer.Option(False, "--reverse", "-r"),
):
    typer.echo(f"Результат bubble_sort: {bubble_sort(numbers, reverse=reverse)}")


@app.command()
def quick_sort_cli(
    numbers: Annotated[list[int], typer.Argument(help="Список чисел (int)")],
    reverse: bool = typer.Option(False, "--reverse", "-r"),
):
    typer.echo(f"Результат quick_sort: {quick_sort(numbers, reverse=reverse)}")


@app.command()
def counting_sort_cli(
    numbers: Annotated[list[int], typer.Argument(help="Список чисел (int)")],
    base: int = typer.Option(10, "--base", "-b", help="Основание системы счисления"),
    reverse: bool = typer.Option(False, "--reverse", "-r"),
):
    typer.echo(
        f"Результат counting_sort: {counting_sort(numbers, base=base, reverse=reverse)}"
    )


@app.command()
def radix_sort_cli(
    numbers: Annotated[list[int], typer.Argument(help="Список чисел (int)")],
    base: int = typer.Option(10, "--base", "-b", help="Основание системы счисления"),
    reverse: bool = typer.Option(False, "--reverse", "-r"),
):
    typer.echo(
        f"Результат radix_sort: {radix_sort(numbers, base=base, reverse=reverse)}"
    )


@app.command()
def heap_sort_cli(
    numbers: Annotated[list[int], typer.Argument(help="Список чисел (int)")],
    reverse: bool = typer.Option(False, "--reverse", "-r"),
):
    typer.echo(f"Результат heap_sort: {heap_sort(numbers, reverse=reverse)}")


@app.command()
def insertion_sort_cli(
    numbers: Annotated[list[float], typer.Argument(help="Список чисел (int)")],
    reverse: bool = typer.Option(False, "--reverse", "-r"),
):
    typer.echo(f"Результат heap_sort: {insertion_sort(numbers, reverse=reverse)}")


@app.command()
def bucket_sort_cli(
    numbers: Annotated[list[float], typer.Argument(help="Список чисел (int)")],
    reverse: bool = typer.Option(False, "--reverse", "-r"),
):
    typer.echo(f"Результат bucket_sort: {bucket_sort(numbers, reverse=reverse)}")


if __name__ == "__main__":
    app()
