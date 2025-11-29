import array
from pathlib import Path


class Queue:
    def __init__(self) -> None:
        self.queue: list[int] = []
        self.size = 0

    def enqueue(self, x: int) -> None:
        self.queue.append(x)
        self.size += 1

    def dequeue(self) -> int:
        if self.size == 0:
            raise IndexError("Queue is empty")
        self.size -= 1
        return self.queue.pop(0)

    def front(self) -> int:
        if self.size == 0:
            raise IndexError("Queue is empty")
        return self.queue[0]

    def is_empty(self) -> bool:
        return self.size == 0

    def __len__(self) -> int:
        return self.size

    def save_to_file(self, filepath: Path) -> None:
        filepath.parent.mkdir(parents=True, exist_ok=True)
        arr = array.array("i", self.queue)
        with filepath.open("wb") as f:
            arr.tofile(f)

    def load_from_file(self, filepath: Path) -> None:
        if not filepath.exists() or filepath.stat().st_size == 0:
            self.queue = []
            self.size = 0
            return

        arr = array.array("i")
        with filepath.open("rb") as f:
            count = filepath.stat().st_size // arr.itemsize
            arr.fromfile(f, count)

        self.queue = arr.tolist()
        self.size = len(self.queue)
