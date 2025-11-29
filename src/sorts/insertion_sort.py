def insertion_sort(a: list[float], reverse: bool = False) -> list[float]:
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        if not reverse:
            while j >= 0 and a[j] > key:
                a[j + 1] = a[j]
                j -= 1
        else:
            while j >= 0 and a[j] < key:
                a[j + 1] = a[j]
                j -= 1

        a[j + 1] = key
    return a
