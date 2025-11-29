from src.sorts.insertion_sort import insertion_sort


def bucket_sort(
    a: list[float], buckets_num: int | None = None, reverse=False
) -> list[float]:
    n = len(a)
    if n <= 1:
        return a[:]

    min_num, max_num = min(a), max(a)
    if min_num == max_num:
        return a[:]

    # Самый эффективный варик, когда кол-во корзин == кол-ву элементов
    if buckets_num is None:
        buckets_num = n
    buckets: list[list[float]] = [[] for _ in range(buckets_num)]

    for num in a:
        # Нормализация
        norm = (num - min_num) / (max_num - min_num)
        # На случай выхода из количества корзин
        idx = min(int(n * norm), buckets_num - 1)
        buckets[idx].append(num)

    # Сортировка корзин
    #  (для таких маленьких списков best эффект сорт вставкой)
    for i in range(len(buckets)):
        buckets[i] = insertion_sort(buckets[i], reverse=reverse)

    res = []
    if not reverse:
        for bucket in buckets:
            res.extend(bucket)
    else:
        for bucket in reversed(buckets):
            res.extend(bucket)

    return res
