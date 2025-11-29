def quick_sort(a: list[int], reverse: bool = False) -> list[int]:
    arr = a[:]
    n = len(arr)
    compare = (lambda x, y: x < y) if not reverse else (lambda x, y: x > y)

    if n <= 1:
        return arr

    pivot = arr[n // 2]

    left = [e for e in arr if compare(e, pivot)]
    middle = [e for e in arr if e == pivot]
    right = [e for e in arr if compare(pivot, e)]

    return quick_sort(left, reverse) + middle + quick_sort(right, reverse)
