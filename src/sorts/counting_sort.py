def counting_sort(
    a: list[int], exp: int | None = None, base: int = 10, reverse: bool = False
) -> list[int]:
    if not a:
        return a[:]

    # Сортировка по разряду (для radix sort)
    if exp is not None:
        freq = [0] * base
        for num in a:
            digit = (num // exp) % base
            freq[digit] += 1

        # Префиксные сумы для позиций
        if not reverse:
            for i in range(1, base):
                freq[i] += freq[i - 1]
        else:
            for i in range(base - 2, -1, -1):
                freq[i] += freq[i + 1]

        res = [0] * len(a)

        if not reverse:
            for num in reversed(a):
                digit = (num // exp) % base
                freq[digit] -= 1
                res[freq[digit]] = num
        else:
            for num in a:
                digit = (num // exp) % base
                freq[digit] -= 1
                res[freq[digit]] = num

        return res

    # Классика
    max_val = max(a)
    freq = [0] * (max_val + 1)
    for el in a:
        freq[el] += 1

    if not reverse:
        for i in range(1, len(freq)):
            freq[i] += freq[i - 1]
    else:
        for i in range(len(freq) - 2, -1, -1):
            freq[i] += freq[i + 1]

    res = [0] * len(a)

    if not reverse:
        for el in reversed(a):
            freq[el] -= 1
            res[freq[el]] = el
    else:
        for el in a:
            freq[el] -= 1
            res[freq[el]] = el

    return res
