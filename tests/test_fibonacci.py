import pytest
from src.algos.fibonacci import fibonacci_iterative, fibonacci_recursive


def test_iterative_zero():
    assert fibonacci_iterative(0) == 0


def test_iterative_one():
    assert fibonacci_iterative(1) == 1


def test_iterative_small():
    assert fibonacci_iterative(5) == 5
    assert fibonacci_iterative(6) == 8
    assert fibonacci_iterative(7) == 13


def test_iterative_medium():
    assert fibonacci_iterative(10) == 55
    assert fibonacci_iterative(20) == 6765


def test_iterative_negative():
    with pytest.raises(ValueError):
        fibonacci_iterative(-1)


def test_recursive_zero():
    assert fibonacci_recursive(0) == 0


def test_recursive_one():
    assert fibonacci_recursive(1) == 1


def test_recursive_small():
    assert fibonacci_recursive(5) == 5
    assert fibonacci_recursive(6) == 8
    assert fibonacci_recursive(7) == 13


def test_recursive_medium():
    assert fibonacci_recursive(10) == 55


def test_recursive_negative():
    with pytest.raises(ValueError):
        fibonacci_recursive(-1)
