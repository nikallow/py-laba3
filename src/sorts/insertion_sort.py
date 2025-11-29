def insertion_sort[T: (int, float)](a: list[T], reverse: bool = False) -> list[T]:
    if not a:
        return a[:]

    arr = a[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        if not reverse:
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
        else:
            while j >= 0 and arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1

        arr[j + 1] = key
    return arr


# Любимое очевидно
