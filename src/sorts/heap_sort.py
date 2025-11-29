def heap_sort[T: (int, float)](a: list[T], reverse: bool = False) -> list[T]:
    if not a:
        return a[:]
    arr = a[:]
    n = len(arr)

    # Тут была шутка в jupyter, кода на лабе писали
    # Нет смысла проверять бездетные ноды, начинаем с i = n//2-1
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, reverse)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, reverse)  # Чиним ветки

    return arr


def heapify[T: (int, float)](a: list[T], n: int, i: int, reverse: bool = False) -> None:
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
