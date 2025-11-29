def bubble_sort(a: list[int], reverse: bool = False) -> list[int]:
    n = len(a)
    compare = (lambda x, y: x > y) if not reverse else (lambda x, y: x < y)

    for i in range(n):
        was_swapped = False
        for j in range(n - 1 - i):
            if compare(a[j], a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                was_swapped = True
        if not was_swapped:
            break

    return a
