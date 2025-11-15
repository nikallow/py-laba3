def factorial_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("n не может быть отрицательным.")
    elif n == 0:
        return 1
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("n не может быть отрицательным.")
    elif n == 0:
        return 1
    return n * factorial_recursive(n - 1)
