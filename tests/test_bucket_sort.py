from src.sorts.bucket_sort import bucket_sort


def test_empty():
    assert bucket_sort([]) == []


def test_single():
    result = bucket_sort([5.0])
    assert result == [5.0]


def test_sorted():
    assert bucket_sort([1.0, 2.0, 3.0, 4.0, 5.0]) == [1.0, 2.0, 3.0, 4.0, 5.0]


def test_normal():
    result = bucket_sort([5.5, 2.2, 9.9, 1.1, 5.5, 6.6])
    assert result == [1.1, 2.2, 5.5, 5.5, 6.6, 9.9]


def test_reverse():
    result = bucket_sort([5.5, 2.2, 9.9, 1.1, 5.5, 6.6], reverse=True)
    assert result == [9.9, 6.6, 5.5, 5.5, 2.2, 1.1]


def test_buckets_num():
    result = bucket_sort([5.5, 2.2, 9.9, 1.1], buckets_num=2)
    assert result == [1.1, 2.2, 5.5, 9.9]
