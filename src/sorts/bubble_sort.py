def bubble_sort(a: list[int], reverse: bool = False) -> list[int]:
    arr = a[:]
    n = len(arr)
    compare = (lambda x, y: x > y) if not reverse else (lambda x, y: x < y)

    for i in range(n):
        was_swapped = False
        for j in range(n - 1 - i):
            if compare(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                was_swapped = True
        if not was_swapped:
            break

    return arr
