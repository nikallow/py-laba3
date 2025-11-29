def heap_sort(a: list[int], reverse: bool = False) -> list[int]:
    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i, reverse)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0, reverse)

    return a


def heapify(a: list[int], n: int, i: int, reverse: bool = False) -> None:
    compare = (lambda x, y: x > y) if not reverse else (lambda x, y: x < y)

    best = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and compare(a[left], a[best]):
        best = left

    if right < n and compare(a[right], a[best]):
        best = right

    if best != i:
        a[i], a[best] = a[best], a[i]

        heapify(a, n, best, reverse)
