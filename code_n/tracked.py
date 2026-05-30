"""Tracked data structures that count operations automatically.

Players use these instead of raw lists/dicts so that every comparison,
access, and swap is counted toward their complexity score.
"""

from typing import Any, Iterator
from .counter import get_counter, OpType


class TrackedList:
    """A list wrapper that counts all operations (reads, writes, comparisons, swaps)."""

    def __init__(self, data: list[Any] | None = None):
        self._data = list(data) if data else []

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, index: int) -> Any:
        get_counter().read(f"list[{index}]")
        return self._data[index]

    def __setitem__(self, index: int, value: Any):
        get_counter().write(f"list[{index}] = {value}")
        self._data[index] = value

    def __iter__(self) -> Iterator:
        for i, item in enumerate(self._data):
            get_counter().read(f"iter list[{i}]")
            yield item

    def __repr__(self) -> str:
        return f"TrackedList({self._data})"

    def compare(self, i: int, j: int) -> int:
        """Compare elements at indices i and j. Returns -1, 0, or 1."""
        get_counter().compare(f"list[{i}]={self._data[i]} vs list[{j}]={self._data[j]}")
        a, b = self._data[i], self._data[j]
        if a < b:
            return -1
        elif a > b:
            return 1
        return 0

    def compare_value(self, i: int, value: Any) -> int:
        """Compare element at index i with a value. Returns -1, 0, or 1."""
        get_counter().compare(f"list[{i}]={self._data[i]} vs {value}")
        a = self._data[i]
        if a < value:
            return -1
        elif a > value:
            return 1
        return 0

    def swap(self, i: int, j: int):
        """Swap elements at indices i and j."""
        get_counter().swap(f"list[{i}]<->list[{j}]")
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def append(self, value: Any):
        get_counter().write(f"list.append({value})")
        self._data.append(value)

    def pop(self, index: int = -1) -> Any:
        actual_index = index if index >= 0 else len(self._data) + index
        value = self._data[actual_index]
        get_counter().write(f"list.pop({actual_index}) -> {value}")
        return self._data.pop(index)

    def insert(self, index: int, value: Any):
        get_counter().write(f"list.insert({index}, {value})")
        self._data.insert(index, value)

    @property
    def raw(self) -> list:
        """Access raw data without counting (for verification only)."""
        return list(self._data)

    def is_sorted(self) -> bool:
        """Check if list is sorted (not counted - used for verification)."""
        return all(self._data[i] <= self._data[i + 1] for i in range(len(self._data) - 1))


class TrackedGrid:
    """A 2D array wrapper that counts operations."""

    def __init__(self, width: int, height: int, default: Any = 0):
        self._data = [[default] * width for _ in range(height)]
        self.width = width
        self.height = height

    def get(self, x: int, y: int) -> Any:
        get_counter().read(f"grid[{x},{y}]")
        return self._data[y][x]

    def set(self, x: int, y: int, value: Any):
        get_counter().write(f"grid[{x},{y}] = {value}")
        self._data[y][x] = value

    def compare(self, x1: int, y1: int, x2: int, y2: int) -> int:
        """Compare two grid cells."""
        a = self._data[y1][x1]
        b = self._data[y2][x2]
        get_counter().compare(f"grid[{x1},{y1}]={a} vs grid[{x2},{y2}]={b}")
        if a < b:
            return -1
        elif a > b:
            return 1
        return 0

    def swap(self, x1: int, y1: int, x2: int, y2: int):
        get_counter().swap(f"grid[{x1},{y1}]<->grid[{x2},{y2}]")
        self._data[y1][x1], self._data[y2][x2] = self._data[y2][x2], self._data[y1][x1]

    @property
    def raw(self) -> list[list]:
        """Access raw data without counting."""
        return [row[:] for row in self._data]

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height


class TrackedQueue:
    """A queue that counts operations."""

    def __init__(self):
        self._data: list[Any] = []

    def enqueue(self, value: Any):
        get_counter().write(f"queue.enqueue({value})")
        self._data.append(value)

    def dequeue(self) -> Any:
        get_counter().read("queue.dequeue()")
        if not self._data:
            raise IndexError("Queue is empty")
        return self._data.pop(0)

    def peek(self) -> Any:
        get_counter().read("queue.peek()")
        if not self._data:
            raise IndexError("Queue is empty")
        return self._data[0]

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return len(self._data) == 0


class TrackedStack:
    """A stack that counts operations."""

    def __init__(self):
        self._data: list[Any] = []

    def push(self, value: Any):
        get_counter().write(f"stack.push({value})")
        self._data.append(value)

    def pop(self) -> Any:
        get_counter().read("stack.pop()")
        if not self._data:
            raise IndexError("Stack is empty")
        return self._data.pop()

    def peek(self) -> Any:
        get_counter().read("stack.peek()")
        if not self._data:
            raise IndexError("Stack is empty")
        return self._data[-1]

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return len(self._data) == 0


class TrackedSet:
    """A set that counts operations."""

    def __init__(self):
        self._data: set = set()

    def add(self, value: Any):
        get_counter().write(f"set.add({value})")
        self._data.add(value)

    def contains(self, value: Any) -> bool:
        get_counter().read(f"set.contains({value})")
        return value in self._data

    def remove(self, value: Any):
        get_counter().write(f"set.remove({value})")
        self._data.discard(value)

    def __len__(self) -> int:
        return len(self._data)

    def __contains__(self, value: Any) -> bool:
        return self.contains(value)
