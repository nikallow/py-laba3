from src.sorts.radix_sort import radix_sort


def test_empty():
    assert radix_sort([]) == []


def test_single():
    assert radix_sort([5]) == [5]


def test_sorted():
    assert radix_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_normal():
    assert radix_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]


def test_reverse():
    assert radix_sort([5, 2, 9, 1, 5, 6], reverse=True) == [9, 6, 5, 5, 2, 1]


def test_base_16():
    assert radix_sort([15, 3, 9, 1, 5, 6], base=16) == [1, 3, 5, 6, 9, 15]


def test_base_2():
    assert radix_sort([8, 4, 2, 1, 16], base=2) == [1, 2, 4, 8, 16]
