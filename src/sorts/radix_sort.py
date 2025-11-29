from src.sorts.counting_sort import counting_sort


def radix_sort(a: list[int], base: int = 10, reverse: bool = False) -> list[int]:
    if not a:
        return a

    max_num = max(a)

    exp = 1
    while max_num // exp >= 1:
        a = counting_sort(a, exp=exp, base=base)
        exp *= base

    if reverse:
        a = a[::-1]
    return a
