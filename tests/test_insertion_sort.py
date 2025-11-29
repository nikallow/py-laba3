from src.sorts.insertion_sort import insertion_sort


def test_empty():
    assert insertion_sort([]) == []


def test_single():
    assert insertion_sort([5]) == [5]


def test_sorted():
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_normal():
    assert insertion_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]


def test_reverse():
    assert insertion_sort([5, 2, 9, 1, 5, 6], reverse=True) == [9, 6, 5, 5, 2, 1]


def test_float():
    assert insertion_sort([3.5, 1.2, 9.8, 2.1]) == [1.2, 2.1, 3.5, 9.8]
