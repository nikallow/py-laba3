from src.sorts.insertion_sort import insertion_sort


def bucket_sort(
    a: list[float], buckets_num: int | None = None, reverse=False
) -> list[float]:
    n = len(a)
    if buckets_num is None:
        buckets_num = n
    buckets: list[list[float]] = [[] for _ in range(buckets_num)]
    min_num, max_num = min(a), max(a)

    for num in a:
        norm = (num - min_num) / (max_num - min_num)
        idx = min(int(n * norm), buckets_num - 1)
        buckets[idx].append(num)

    for bucket in buckets:
        insertion_sort(bucket, reverse=reverse)

    res = []
    for bucket in buckets:
        res.extend(bucket)

    return res
