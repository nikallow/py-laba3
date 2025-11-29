import pytest
from src.structs.stack import Stack


def test_push_pop():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1


def test_peek():
    s = Stack()
    s.push(5)
    s.push(10)
    assert s.peek() == 10
    assert s.peek() == 10


def test_min():
    s = Stack()
    s.push(5)
    assert s.min() == 5
    s.push(3)
    assert s.min() == 3
    s.push(7)
    assert s.min() == 3
    s.pop()
    assert s.min() == 3


def test_is_empty():
    s = Stack()
    assert s.is_empty()
    s.push(1)
    assert not s.is_empty()
    s.pop()
    assert s.is_empty()


def test_len():
    s = Stack()
    assert len(s) == 0
    s.push(1)
    s.push(2)
    assert len(s) == 2
    s.pop()
    assert len(s) == 1


def test_pop_empty():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()


def test_peek_empty():
    s = Stack()
    with pytest.raises(IndexError):
        s.peek()


def test_min_empty():
    s = Stack()
    with pytest.raises(IndexError):
        s.min()
