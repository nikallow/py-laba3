import pytest
from src.structs.queue import Queue


def test_enqueue_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3


def test_front():
    q = Queue()
    q.enqueue(5)
    q.enqueue(10)
    assert q.front() == 5
    q.dequeue()
    assert q.front() == 10


def test_is_empty():
    q = Queue()
    assert q.is_empty()
    q.enqueue(1)
    assert not q.is_empty()
    q.dequeue()
    assert q.is_empty()


def test_len():
    q = Queue()
    assert len(q) == 0
    q.enqueue(1)
    q.enqueue(2)
    assert len(q) == 2
    q.dequeue()
    assert len(q) == 1


def test_dequeue_empty():
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()


def test_front_empty():
    q = Queue()
    with pytest.raises(IndexError):
        q.front()
