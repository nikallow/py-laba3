from pathlib import Path

from pydantic import TypeAdapter

from src.sorts.bubble_sort import bubble_sort
from src.sorts.bucket_sort import bucket_sort
from src.sorts.counting_sort import counting_sort
from src.sorts.heap_sort import heap_sort
from src.sorts.insertion_sort import insertion_sort
from src.sorts.quick_sort import quick_sort
from src.sorts.radix_sort import radix_sort

SORTS = {
    "bubble": {
        "func": bubble_sort,
        "type": "both",
        "params": [],
    },
    "quick": {
        "func": quick_sort,
        "type": "both",
        "params": [],
    },
    "counting": {
        "func": counting_sort,
        "type": "int",
        "params": ["base"],
    },
    "radix": {
        "func": radix_sort,
        "type": "int",
        "params": ["base"],
    },
    "heap": {
        "func": heap_sort,
        "type": "both",
        "params": [],
    },
    "insertion": {
        "func": insertion_sort,
        "type": "both",
        "params": [],
    },
    "bucket": {
        "func": bucket_sort,
        "type": "float",
        "params": [],
    },
}

TYPE_MAP = {
    "int": TypeAdapter(int),
    "float": TypeAdapter(float),
}

STORAGE_DIR = Path("storage")
QUEUE_DIR = STORAGE_DIR / "queues"
STACK_DIR = STORAGE_DIR / "stacks"
