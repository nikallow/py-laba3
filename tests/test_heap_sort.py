from src.sorts.heap_sort import heap_sort


def test_empty():
    assert heap_sort([]) == []


def test_single():
    assert heap_sort([5]) == [5]


def test_sorted():
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_normal():
    assert heap_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]


def test_reverse():
    assert heap_sort([5, 2, 9, 1, 5, 6], reverse=True) == [9, 6, 5, 5, 2, 1]


def test_float():
    assert heap_sort([3.5, 1.2, 9.8, 2.1]) == [1.2, 2.1, 3.5, 9.8]


def test_float_reverse():
    assert heap_sort([3.5, 1.2, 9.8, 2.1], reverse=True) == [9.8, 3.5, 2.1, 1.2]
