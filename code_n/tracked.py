"""Tracked data structures that count operations automatically.

Players use these instead of raw lists/dicts so that every comparison,
access, and swap is counted toward their complexity score.
"""

from typing import Any, Iterator
from .counter import get_counter


class TrackedValue:
    """A value proxy that records normal Python comparisons.

    Comparison operators (==, !=, <, <=, >, >=) all record a `compare`
    operation, because that's the only way to teach the player the cost
    of an O(n log n) or O(n^2) search.

    Conversions (``int(...)``, ``float(...)``, ``__index__``, ``bool(...)``)
    and arithmetic (``+ - * / // % **``) are intentionally NOT counted.
    A player using ``int(data[i])`` to do integer arithmetic should not
    be punished for the conversion — only the read that produced
    ``data[i]`` and the comparison that drove the branch cost ops.

    Iteration (``for x in tv``) delegates to the underlying value, also
    without counting; iterators are not really "reads" in the algorithmic
    sense, and counting them would distort the complexity picture.

    If you need to bypass a tracked value entirely, use ``.raw`` (the
    bare value) or call ``unwrap_tracked(value)`` (works for either
    TrackedValue or anything else).
    """

    def __init__(self, value: Any, label: str):
        self._value = value
        self._label = label

    @property
    def raw(self) -> Any:
        """Return the underlying value, bypassing all tracking."""
        return self._value

    @property
    def label(self) -> str:
        return self._label

    def _other_value(self, other: Any) -> Any:
        if isinstance(other, TrackedValue):
            return other.raw
        return other

    def _other_label(self, other: Any) -> str:
        if isinstance(other, TrackedValue):
            return f"{other.label}={other.raw}"
        return repr(other)

    def _compare(self, other: Any, operator: str, result: bool) -> bool:
        get_counter().compare(f"{self._label}={self._value} {operator} {self._other_label(other)}")
        return result

    def __lt__(self, other: Any) -> bool:
        other_value = self._other_value(other)
        return self._compare(other, "<", self._value < other_value)

    def __le__(self, other: Any) -> bool:
        other_value = self._other_value(other)
        return self._compare(other, "<=", self._value <= other_value)

    def __eq__(self, other: Any) -> bool:
        other_value = self._other_value(other)
        return self._compare(other, "==", self._value == other_value)

    def __ne__(self, other: Any) -> bool:
        other_value = self._other_value(other)
        return self._compare(other, "!=", self._value != other_value)

    def __gt__(self, other: Any) -> bool:
        other_value = self._other_value(other)
        return self._compare(other, ">", self._value > other_value)

    def __ge__(self, other: Any) -> bool:
        other_value = self._other_value(other)
        return self._compare(other, ">=", self._value >= other_value)

    def __hash__(self) -> int:
        return hash(self._value)

    # --- conversions: deliberate "do not count" choices. See class docstring. ---

    def __bool__(self) -> bool:
        return bool(self._value)

    def __int__(self) -> int:
        return int(self._value)

    def __float__(self) -> float:
        return float(self._value)

    def __index__(self) -> int:
        return self._value.__index__()

    def __iter__(self):
        return iter(self._value)

    def __len__(self) -> int:
        return len(self._value)

    def __getitem__(self, key: Any) -> Any:
        return self._value[key]

    def __contains__(self, item: Any) -> bool:
        return item in self._value

    def __getattr__(self, name: str) -> Any:
        return getattr(self._value, name)

    def __repr__(self) -> str:
        return repr(self._value)

    def __str__(self) -> str:
        return str(self._value)

    def __format__(self, format_spec: str) -> str:
        return format(self._value, format_spec)

    def _binary(self, other: Any, operation):
        return operation(self._value, self._other_value(other))

    def _reverse_binary(self, other: Any, operation):
        return operation(self._other_value(other), self._value)

    def __add__(self, other: Any):
        return self._binary(other, lambda left, right: left + right)

    def __radd__(self, other: Any):
        return self._reverse_binary(other, lambda left, right: left + right)

    def __sub__(self, other: Any):
        return self._binary(other, lambda left, right: left - right)

    def __rsub__(self, other: Any):
        return self._reverse_binary(other, lambda left, right: left - right)

    def __mul__(self, other: Any):
        return self._binary(other, lambda left, right: left * right)

    def __rmul__(self, other: Any):
        return self._reverse_binary(other, lambda left, right: left * right)

    def __truediv__(self, other: Any):
        return self._binary(other, lambda left, right: left / right)

    def __rtruediv__(self, other: Any):
        return self._reverse_binary(other, lambda left, right: left / right)

    def __floordiv__(self, other: Any):
        return self._binary(other, lambda left, right: left // right)

    def __rfloordiv__(self, other: Any):
        return self._reverse_binary(other, lambda left, right: left // right)

    def __mod__(self, other: Any):
        return self._binary(other, lambda left, right: left % right)

    def __rmod__(self, other: Any):
        return self._reverse_binary(other, lambda left, right: left % right)

    def __pow__(self, other: Any):
        return self._binary(other, lambda left, right: left ** right)

    def __rpow__(self, other: Any):
        return self._reverse_binary(other, lambda left, right: left ** right)

    def __neg__(self):
        return -self._value

    def __pos__(self):
        return +self._value

    def __abs__(self):
        return abs(self._value)


def unwrap_tracked(value: Any) -> Any:
    if isinstance(value, TrackedValue):
        return value.raw
    return value


class TrackedList:
    """A list wrapper that counts all operations (reads, writes, comparisons, swaps)."""

    def __init__(self, data: list[Any] | None = None):
        self._data = list(data) if data else []

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, index: int) -> Any:
        if isinstance(index, slice):
            indices = range(*index.indices(len(self._data)))
            values = []
            for item_index in indices:
                get_counter().read(f"list[{item_index}]")
                values.append(self._data[item_index])
            return TrackedList(values)
        get_counter().read(f"list[{index}]")
        return TrackedValue(self._data[index], f"list[{index}]")

    def __setitem__(self, index: int, value: Any):
        value = unwrap_tracked(value)
        if isinstance(index, slice):
            values = [unwrap_tracked(item) for item in value]
            start, stop, step = index.indices(len(self._data))
            for item_index in range(start, stop, step):
                get_counter().write(f"list[{item_index}] = <slice>")
            self._data[index] = values
            return
        get_counter().write(f"list[{index}] = {value}")
        self._data[index] = value

    def __iter__(self) -> Iterator:
        for index in range(len(self._data)):
            yield self[index]

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
        value = unwrap_tracked(value)
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
        value = unwrap_tracked(value)
        get_counter().write(f"list.append({value})")
        self._data.append(value)

    def pop(self, index: int = -1) -> Any:
        actual_index = index if index >= 0 else len(self._data) + index
        value = self._data[actual_index]
        get_counter().write(f"list.pop({actual_index}) -> {value}")
        return self._data.pop(index)

    def insert(self, index: int, value: Any):
        value = unwrap_tracked(value)
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
    """A 2D grid wrapper that counts row/column access."""

    def __init__(self, width: int, height: int, default: Any = 0):
        self._data = [[default] * width for _ in range(height)]
        self.width = width
        self.height = height

    def __getitem__(self, key: Any) -> Any:
        if isinstance(key, tuple):
            x_coord, y_coord = key
            return self.get(x_coord, y_coord)
        return TrackedGridRow(self, key)

    def __setitem__(self, key: Any, value: Any):
        if not isinstance(key, tuple):
            raise TypeError("Assign grid cells with grid[y][x] = value or grid[x, y] = value")
        x_coord, y_coord = key
        self.set(x_coord, y_coord, value)

    def get(self, x: int, y: int) -> Any:
        get_counter().read(f"grid[{x},{y}]")
        return TrackedValue(self._data[y][x], f"grid[{x},{y}]")

    def set(self, x: int, y: int, value: Any):
        value = unwrap_tracked(value)
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


class TrackedGridRow:
    """A row proxy that lets players write grid[row][column]."""

    def __init__(self, grid: TrackedGrid, y_coord: int):
        self._grid = grid
        self._y_coord = y_coord

    def __getitem__(self, x_coord: int) -> Any:
        return self._grid.get(x_coord, self._y_coord)

    def __setitem__(self, x_coord: int, value: Any):
        self._grid.set(x_coord, self._y_coord, value)

    def __iter__(self) -> Iterator:
        for x_coord in range(self._grid.width):
            yield self[x_coord]

    def __len__(self) -> int:
        return self._grid.width


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
