def fibonacci_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("n не может быть отрицательным")
    elif n < 2:
        return n
    else:
        prev2, prev1 = 0, 1
        for _ in range(2, n + 1):
            curr = prev2 + prev1
            prev2, prev1 = prev1, curr
        return curr


def fibonacci_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("n не может быть отрицательным")
    elif n < 2:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
