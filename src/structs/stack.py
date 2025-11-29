import array
from pathlib import Path


class Node:
    def __init__(self, value: int, next=None, current_min=None):
        self.value = value
        self.next = next
        self.current_min = current_min


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, x: int) -> None:
        if self.top is None:
            new_node = Node(x, None, x)
        else:
            current_min = min(x, self.top.current_min)
            new_node = Node(x, self.top, current_min)
        self.top = new_node
        self.size += 1

    def pop(self) -> int:
        if self.top is None:
            raise IndexError("Stack is empty")
        x = self.top.value
        self.top = self.top.next
        self.size -= 1
        return x

    def peek(self) -> int:
        if self.top is None:
            raise IndexError("Stack is empty")
        return self.top.value

    def min(self) -> int:
        if self.top is None:
            raise IndexError("Stack is empty")
        return self.top.current_min

    def is_empty(self) -> bool:
        return self.size == 0
        # Или
        # return self.top is None

    def __len__(self) -> int:
        return self.size

    def save_to_file(self, filepath: Path) -> None:
        filepath.parent.mkdir(parents=True, exist_ok=True)

        values: list[int] = []
        node = self.top
        while node is not None:
            values.append(node.value)
            node = node.next

        arr = array.array("i", values)

        with filepath.open("wb") as f:
            arr.tofile(f)

    def load_from_file(self, filepath: Path) -> None:
        if not filepath.exists() or filepath.stat().st_size == 0:
            self.top = None
            self.size = 0
            return

        arr = array.array("i")
        with filepath.open("rb") as f:
            count = filepath.stat().st_size // arr.itemsize
            arr.fromfile(f, count)

        for value in reversed(arr):
            self.push(value)
