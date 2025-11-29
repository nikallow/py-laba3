from src.sorts.counting_sort import counting_sort


def radix_sort(a: list[int], base: int = 10, reverse: bool = False) -> list[int]:
    arr = a[:]

    max_num = max(arr)

    exp = 1
    while max_num // exp >= 1:
        arr = counting_sort(arr, exp=exp, base=base)
        exp *= base

    if reverse:
        arr = arr[::-1]
    return arr
