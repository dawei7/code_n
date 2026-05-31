"""Operation counter for measuring algorithmic complexity.

Tracks comparisons, swaps, reads, writes, and function calls.
Determines the O() complexity class by analyzing growth rate.
"""

import math
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Optional


class OpType(Enum):
    COMPARE = "compare"
    SWAP = "swap"
    READ = "read"
    WRITE = "write"
    CALL = "call"


@dataclass
class OpRecord:
    op_type: OpType
    detail: str = ""


class ComplexityClass(Enum):
    O_1 = "O(1)"
    O_LOG_N = "O(log n)"
    O_N = "O(n)"
    O_N_LOG_N = "O(n log n)"
    O_N2 = "O(n²)"
    O_N3 = "O(n³)"
    O_2N = "O(2ⁿ)"
    UNKNOWN = "O(?)"


@dataclass
class OpStats:
    comparisons: int = 0
    swaps: int = 0
    reads: int = 0
    writes: int = 0
    calls: int = 0
    total: int = 0


class OperationLimitExceeded(RuntimeError):
    """Raised when player code uses more operations than the challenge allows."""

    def __init__(self, total: int, limit: int, complexity: ComplexityClass):
        self.total = total
        self.limit = limit
        self.complexity = complexity
        super().__init__(
            f"Stopped: used {total} operations, which is above the {limit} operation budget for {complexity.value}."
        )


class OperationCounter:
    """Counts individual operations performed by player code."""

    def __init__(self):
        self._ops: list[OpRecord] = []
        self._enabled = True
        self._snapshots: list[int] = []
        self._operation_limit: Optional[int] = None
        self._limit_complexity = ComplexityClass.UNKNOWN
        self._progress_callback: Optional[Callable[[int, Optional[int]], None]] = None
        self._progress_interval = 250
        self._last_progress_count = 0

    def reset(self):
        self._ops.clear()
        self._snapshots.clear()
        self.clear_operation_limit()
        self.clear_progress_callback()

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value

    def record(self, op_type: OpType, detail: str = ""):
        if self._enabled:
            self._ops.append(OpRecord(op_type, detail))
            total = len(self._ops)
            self._notify_progress(total)
            if self._operation_limit is not None and total > self._operation_limit:
                raise OperationLimitExceeded(total, self._operation_limit, self._limit_complexity)

    def set_operation_limit(self, limit: int, complexity: ComplexityClass):
        self._operation_limit = limit
        self._limit_complexity = complexity

    def clear_operation_limit(self):
        self._operation_limit = None
        self._limit_complexity = ComplexityClass.UNKNOWN

    def set_progress_callback(self, callback: Callable[[int, Optional[int]], None], interval: int = 250):
        self._progress_callback = callback
        self._progress_interval = max(1, interval)
        self._last_progress_count = 0

    def clear_progress_callback(self):
        self._progress_callback = None
        self._last_progress_count = 0

    def _notify_progress(self, total: int):
        if not self._progress_callback:
            return
        should_update = total == 1 or total - self._last_progress_count >= self._progress_interval
        if self._operation_limit is not None and total >= self._operation_limit:
            should_update = True
        if should_update:
            self._last_progress_count = total
            self._progress_callback(total, self._operation_limit)

    def compare(self, detail: str = ""):
        self.record(OpType.COMPARE, detail)

    def swap(self, detail: str = ""):
        self.record(OpType.SWAP, detail)

    def read(self, detail: str = ""):
        self.record(OpType.READ, detail)

    def write(self, detail: str = ""):
        self.record(OpType.WRITE, detail)

    def call(self, detail: str = ""):
        self.record(OpType.CALL, detail)

    def snapshot(self):
        """Take a snapshot of current operation count (for per-step tracking)."""
        self._snapshots.append(len(self._ops))

    @property
    def stats(self) -> OpStats:
        s = OpStats()
        for op in self._ops:
            if op.op_type == OpType.COMPARE:
                s.comparisons += 1
            elif op.op_type == OpType.SWAP:
                s.swaps += 1
            elif op.op_type == OpType.READ:
                s.reads += 1
            elif op.op_type == OpType.WRITE:
                s.writes += 1
            elif op.op_type == OpType.CALL:
                s.calls += 1
        s.total = len(self._ops)
        return s

    @property
    def total_ops(self) -> int:
        return len(self._ops)

    @property
    def ops_log(self) -> list[OpRecord]:
        return list(self._ops)

    def classify(self, n: int) -> ComplexityClass:
        """Classify the complexity based on operation count and input size n."""
        if n <= 1:
            return ComplexityClass.UNKNOWN

        total = len(self._ops)
        if total == 0:
            return ComplexityClass.O_1

        ratio = total / n

        # Thresholds for classification
        if total <= 5:
            return ComplexityClass.O_1
        elif ratio <= 0.5 and total <= math.log2(n) * 3 + 5:
            return ComplexityClass.O_LOG_N
        elif ratio <= 4.0:
            return ComplexityClass.O_N
        elif ratio <= math.log2(n) * 6:
            return ComplexityClass.O_N_LOG_N
        elif total <= n * n * 8:
            return ComplexityClass.O_N2
        elif total <= n * n * n * 8:
            return ComplexityClass.O_N3
        else:
            return ComplexityClass.O_2N

    def meets_threshold(self, n: int, max_class: ComplexityClass) -> bool:
        """Check if the operation count is within the allowed complexity class."""
        total = len(self._ops)
        return total <= self.limit_for(n, max_class)

    @staticmethod
    def limit_for(n: int, max_class: ComplexityClass) -> int:
        """Return the operation budget for a required complexity class."""
        limits = {
            ComplexityClass.O_1: 10,
            ComplexityClass.O_LOG_N: int(math.log2(max(n, 2)) * 3) + 10,
            ComplexityClass.O_N: n * 4 + 10,
            ComplexityClass.O_N_LOG_N: int(n * math.log2(max(n, 2)) * 6) + 10,
            ComplexityClass.O_N2: n * n * 8 + 10,
            ComplexityClass.O_N3: n * n * n * 8 + 10,
            ComplexityClass.O_2N: 2**min(n, 25) + 10,
        }
        return limits.get(max_class, 10**12)


# Global counter instance
_global_counter = OperationCounter()


def get_counter() -> OperationCounter:
    return _global_counter


def reset_counter():
    _global_counter.reset()
