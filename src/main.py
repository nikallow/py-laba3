import typer

from algos.factorial import factorial_iterative, factorial_recursive
from algos.fibonacci import fibonacci_iterative, fibonacci_recursive

app = typer.Typer()


@app.command()
def factorial(
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
def fibonacci(
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


if __name__ == "__main__":
    app()
