import pytest
from src.algos.factorial import factorial_iterative, factorial_recursive


def test_iterative_zero():
    assert factorial_iterative(0) == 1


def test_iterative_one():
    assert factorial_iterative(1) == 1


def test_iterative_small():
    assert factorial_iterative(5) == 120


def test_iterative_medium():
    assert factorial_iterative(10) == 3628800


def test_iterative_negative():
    with pytest.raises(ValueError):
        factorial_iterative(-1)


def test_recursive_zero():
    assert factorial_recursive(0) == 1


def test_recursive_one():
    assert factorial_recursive(1) == 1


def test_recursive_small():
    assert factorial_recursive(5) == 120


def test_recursive_medium():
    assert factorial_recursive(10) == 3628800


def test_recursive_negative():
    with pytest.raises(ValueError):
        factorial_recursive(-1)
