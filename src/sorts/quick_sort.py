def quick_sort(a: list[int], reverse: bool = False) -> list[int]:
    n = len(a)
    compare = (lambda x, y: x < y) if not reverse else (lambda x, y: x > y)

    if n <= 1:
        return a

    pivot = a[n // 2]

    left = [e for e in a if compare(e, pivot)]
    middle = [e for e in a if e == pivot]
    right = [e for e in a if compare(pivot, e)]

    return quick_sort(left, reverse) + middle + quick_sort(right, reverse)
