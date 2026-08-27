"""The engine runner â€” runs a player's solution against a challenge.

This is the single point of integration between the FastAPI server
and the Python engine. It is the only file that:

* exec()'s player code
* calls into the engine's :class:`engine.challenge.Challenge`
* runs the player's ``solve()`` under a tracer (the tracer
  enforces a step limit that catches infinite loops)
* converts the verifier's verdict + calibrated runtime comparison
  into the Pydantic response model in :mod:`server.app.schemas`

Design notes
------------

**One temp file per run.** The engine's tracer uses
``func.__code__.co_filename`` to filter frames to the player's
file. A real file gives each run a unique filename (so two
concurrent runs with the same source don't collide). The
temp file is cleaned up in a ``finally`` block.

**No source wrapping.** The player source is compiled and exec'd verbatim in
the same minimal namespace shape used by the optimal reference. The runtime op counter (and its
``TrackedList`` / ``TrackedGrid`` wrappers) was removed in
v0.8.5. The player's input is now a plain list / dict / set.

**Complexity verification is explicit.** Multi-tier benchmark packages compare
how the user/reference runtime ratio grows with authored input size, tolerating
constant-factor implementation differences. Strict non-scaling certificates
cover only bounded or proof-optimal source contracts and are reported as
certificates, never as runtime measurements. Legacy single-tier packages use
``runtime <= 1.5 * optimal_reference_runtime`` until migrated.

**Step limit is a safety cap.** The tracer raises
``ExecutionStepLimitExceeded`` after a bounded number of Python line events to
catch infinite loops. Ordinary cases use 100,000 events; authored benchmarks
and certificate-backed workloads use the larger runtime cap so terminating
legal algorithms with high required complexity can finish. The cap is
independent of the complexity verdict.

**The trace is internal-only.** Per-step trace frames are no
longer shipped to the frontend; the in-app debugger streams
through DAP instead. The engine still uses the tracer for the
step limit; the trace exists only as a local variable in
``run_player_code`` and is discarded after the run.
"""
from __future__ import annotations

import logging
import math
import runpy
import shutil
import json
import re
import tempfile
import time
from collections import Counter, deque
from dataclasses import dataclass, field
from itertools import pairwise
from pathlib import Path
from typing import Any, Optional

from challenges.registry import CHALLENGE_REGISTRY
from engine.languages import language_extension, normalize_language
from engine.execution_trace import (
    ExecutionStepLimitExceeded,
    ExecutionTrace,
    run_with_trace,
)
from server.app.optimal_sources import load_optimal_source
from server.app.challenge_packages import leetcode_complexity_certificate_status
from server.app.validated_cases import ValidatedCase

from .external_programs import run_function_program
from .special_environments import run_special_environment
from .schemas import RunCaseResult, RunResponse
from .trace_codec import to_json_safe


log = logging.getLogger(__name__)


# Safety cap on Python line events. Independent of the
# complexity budget â€” purely an infinite-loop guard. 100,000
# events is the ordinary fast-failure threshold. Benchmarks and verified
# certificate workloads get enough room for a terminating implementation whose
# legal complexity is too expensive for that threshold; infinite loops remain
# bounded in both paths.
_STEP_LIMIT = 100_000
_RUNTIME_STEP_LIMIT = 1_000_000
_VALIDATED_CASE_STEP_LIMIT_OVERRIDES = {
    # The accepted palindrome-root enumeration reaches roughly 200,000 line
    # events at the legal upper bound while still completing quickly.
    "lc_906": _RUNTIME_STEP_LIMIT,
    # The accepted bounded-width digit DP examines up to len(str(k)) prefixes
    # at each of 100,000 legal positions; it terminates in linear time but
    # crosses the general-purpose line-event guard on that maximum input.
    "lc_1416": 10_000_000,
    # The accepted nested ternary search deliberately performs 70 iterations
    # per axis to meet the floating-point error bound.
    "lc_1515": 10_000_000,
    # The accepted O(n^2 k) compression DP reaches the legal n = 100 case.
    "lc_1531": _RUNTIME_STEP_LIMIT,
    # The accepted base-three assignment DP explores the legal slot-state
    # space with an explicit loop and crosses the generic line-event guard.
    "lc_2172": _RUNTIME_STEP_LIMIT,
    # The legal segment-tree update stream performs O(q log n) terminating
    # merge work and can exceed the benchmark line-event guard.
    "lc_2213": 10_000_000,
    # The accepted smallest-prime-factor sieve scans the legal value domain
    # with nested terminating loops and crosses the generic line-event guard.
    "lc_2584": 10_000_000,
    # The accepted five-state digit DP explores the complete legal bound when
    # memoized states cannot be pruned by an app-only optimization.
    "lc_2827": _RUNTIME_STEP_LIMIT,
    # The accepted end-indexed dynamic program visits all 100,000 legal house
    # positions even when the offer list is sparse.
    "lc_2830": _RUNTIME_STEP_LIMIT,
    # The accepted bitmask DP checks every value for every subset at legal
    # n = 12, which is bounded but exceeds the generic traced-line guard.
    "lc_2992": _RUNTIME_STEP_LIMIT,
    # The accepted 26-by-26 matrix exponentiation performs the complete
    # logarithmic squaring loop even for a short input string.
    "lc_3337": 10_000_000,
    # The accepted two-state adjacency DP fills every (position, pair-count)
    # state at the legal n = 750 bound and exceeds the generic trace cap.
    "lc_3339": 10_000_000,
    # The accepted digit DP enumerates every feasible digit-sum target and its
    # memoized factor states across the complete nine-digit legal domain.
    "lc_3490": 10_000_000,
    # The accepted pair of Walsh-Hadamard transforms visits every butterfly
    # at the legal 2,048-value spectrum width.
    "lc_3514": _RUNTIME_STEP_LIMIT,
    # The accepted unbounded-change DP scans the available prime prefix for
    # every total through the legal target n = 1,000.
    "lc_3610": _RUNTIME_STEP_LIMIT,
    # The accepted forward-length and reverse-index passes each scan the legal
    # 100,000-character operation string once.
    "lc_3614": _RUNTIME_STEP_LIMIT,
    # The accepted record-minimum scan visits all 100,000 legal student ranks.
    "lc_3616": _RUNTIME_STEP_LIMIT,
    # The accepted index sieve and partition sum scan the full 100,000-element
    # legal array even when every value is zero.
    "lc_3618": _RUNTIME_STEP_LIMIT,
    # The accepted island scan examines every cell of the legal 100,000-cell
    # grid, including an all-water instance with no early component work.
    "lc_3619": _RUNTIME_STEP_LIMIT,
    # The accepted totient sieve visits prime multiples through the legal
    # value bound before processing divisor-indexed Fenwick updates.
    "lc_3671": 10_000_000,
    # The accepted smallest-prime-factor and square-free-kernel tables cover
    # every value through the legal maximum of 100,000.
    "lc_3715": 10_000_000,
    # The accepted primality sieve and backward next-prime table scan through
    # twice the legal maximum value before processing the input array.
    "lc_3896": _RUNTIME_STEP_LIMIT,
    # The accepted modular evaluator visits every bit in the legal
    # 200,000-bit concatenation after sorting its run descriptors.
    "lc_3897": _RUNTIME_STEP_LIMIT,
    # The clear accepted prefix/suffix-loop interpolation DP deliberately keeps
    # its O(n^3) transitions explicit across the complete legal n = 200 domain.
    "lc_3916": 25_000_000,
    # The accepted divisor sieve scans the complete legal value domain even
    # when only a small number of values are present as candidate divisors.
    "lc_3927": _RUNTIME_STEP_LIMIT,
    # The accepted divisor-count and smallest-prime-factor sieves cover every
    # value through the legal maximum before evaluating all candidates.
    "lc_3953": 10_000_000,
}
_RUNTIME_TARGET_SECONDS = 0.05
_RUNTIME_MAX_WALL_SECONDS = 2.0
_RUNTIME_MIN_TRIALS = 7
_RUNTIME_MAX_TRIALS = 21
_RUNTIME_EXTERNAL_TIMEOUT_SECONDS = 5.0
_RUNTIME_LIMIT_REFERENCE_MULTIPLIER = 1.50
_RUNTIME_SCALING_MAX_EXTRA_EXPONENT = 0.15
_RUNTIME_SCALING_MAX_CONSTANT_RATIO = 8.0
_RUNTIME_MAX_AMPLIFICATION = 1000
_RUNTIME_STDIN_MAX_AMPLIFICATION = 20_000


@dataclass
class RuntimeCheck:
    checked: bool = False
    passed: bool = False
    user_ms: Optional[float] = None
    reference_ms: Optional[float] = None
    ratio: Optional[float] = None
    limit_ms: Optional[float] = None
    trials: int = 0
    n: Optional[int] = None
    seed: Optional[int] = None
    message: str = ""
    benchmark_correct: bool = True
    scaling_data: list[dict[str, float | int]] = field(default_factory=list)


@dataclass
class ComplexityCheck:
    checked: bool = False
    passed: bool = False
    method: str = ""
    message: str = ""


def _complexity_certificate_check(challenge_id: str) -> ComplexityCheck:
    status = leetcode_complexity_certificate_status(challenge_id)
    if not status.complete:
        return ComplexityCheck()
    label = status.method.replace("_", " ")
    return ComplexityCheck(
        checked=True,
        passed=True,
        method=status.method,
        message=f"Complexity verified by {label} certificate. {status.summary}",
    )


def _benchmark_n(challenge: Any, requested_n: int) -> int:
    return max(2, min(challenge.max_n, max(requested_n, challenge.max_n)))


def _runtime_limit_ms(reference_ms: Optional[float], language: str) -> float:
    del language
    return max(reference_ms or 0.0, 0.0) * _RUNTIME_LIMIT_REFERENCE_MULTIPLIER


def _runtime_iterations_for_ms(reference_ms: Optional[float], *, max_amplification: int = _RUNTIME_MAX_AMPLIFICATION) -> int:
    ref = reference_ms or 0.0
    if ref <= 0:
        return 1
    import math

    target_ms = _RUNTIME_TARGET_SECONDS * 1000.0
    return max(1, min(max_amplification, int(math.ceil(target_ms / ref))))


def _returns_in_place(returns_hint: str, spec: Any = None) -> bool:
    if spec is not None and getattr(spec, "id", "").startswith("lc_"):
        try:
            from challenges.algorithms.leetcode import load_full_leetcode_spec
            full_spec = load_full_leetcode_spec(spec.id)
            if full_spec and getattr(full_spec, "returns", None):
                returns_hint = full_spec.returns
        except Exception:
            pass
    text = returns_hint.strip().lower()
    text = re.sub(r"^-\s*", "", text)
    return bool(
        re.match(r"^(?:returns?\s+)?`?(?:none|void)`?(?:\s|[;.,:-]|$)", text)
        or re.match(r"^returns?\s+nothing(?:\s|[;.,:-]|$)", text)
        or re.match(r"^no\s+(?:value|return\s+value)\s+is\s+returned(?:\s|[;.,:-]|$)", text)
    )


class _JudgeTreeNode:
    def __init__(
        self,
        val: Any = 0,
        left: "_JudgeTreeNode | None" = None,
        right: "_JudgeTreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next: _JudgeTreeNode | None = None
        self.parent: _JudgeTreeNode | None = None


class _JudgeListNode:
    def __init__(self, val: Any = 0, next: "_JudgeListNode | None" = None):
        self.val = val
        self.next = next


class _JudgePolyNode:
    def __init__(
        self,
        coefficient: int = 0,
        power: int = 0,
        next: "_JudgePolyNode | None" = None,
    ):
        self.coefficient = coefficient
        self.power = power
        self.next = next


class _JudgeRopeTreeNode:
    def __init__(
        self,
        len: int = 0,
        val: str = "",
        left: "_JudgeRopeTreeNode | None" = None,
        right: "_JudgeRopeTreeNode | None" = None,
    ):
        self.len = len
        self.val = val
        self.left = left
        self.right = right


class _JudgeStreet:
    def __init__(self, doors: list[Any]):
        self._doors = [bool(value) for value in doors]
        self._position = 0

    def openDoor(self) -> None:
        self._doors[self._position] = True

    def closeDoor(self) -> None:
        self._doors[self._position] = False

    def isDoorOpen(self) -> bool:
        return self._doors[self._position]

    def moveRight(self) -> None:
        self._position = (self._position + 1) % len(self._doors)

    def moveLeft(self) -> None:
        self._position = (self._position - 1) % len(self._doors)


class _JudgeCategoryHandler:
    def __init__(self, categories: list[Any]):
        self._categories = categories

    def haveSameCategory(self, a: int, b: int) -> bool:
        if not (0 <= a < len(self._categories) and 0 <= b < len(self._categories)):
            return False
        return self._categories[a] == self._categories[b]


class _JudgeBigArray:
    def __init__(self, values: list[Any]):
        self._values = values

    def size(self) -> int:
        return len(self._values)

    def at(self, index: int) -> Any:
        return self._values[index]


class _JudgeNode:
    """Mutable compatibility node for judge interfaces with generic ``Node``."""

    def __init__(
        self,
        val: Any = 0,
        next: "_JudgeNode | None" = None,
        random: "_JudgeNode | None" = None,
    ):
        self.val = val
        self.next = next
        self.prev: _JudgeNode | None = None
        self.child: _JudgeNode | None = None
        self.left: _JudgeNode | None = None
        self.right: _JudgeNode | None = None
        self.parent: _JudgeNode | None = None
        self.random = random
        self.neighbors: list[_JudgeNode] = []
        self.children: list[_JudgeNode] = []


class _JudgeNestedInteger:
    """Compatibility object for LeetCode's read-only ``NestedInteger`` API."""

    def __init__(self, value: Any = None):
        if isinstance(value, int) and not isinstance(value, bool):
            self._integer: int | None = value
            self._list: list[_JudgeNestedInteger] | None = None
        else:
            self._integer = None
            self._list = (
                []
                if value is None
                else [_JudgeNestedInteger(item) for item in value]
            )

    def isInteger(self) -> bool:
        return self._integer is not None

    def getInteger(self) -> int | None:
        return self._integer

    def add(self, element: "_JudgeNestedInteger") -> None:
        if self._list is None:
            self._integer = None
            self._list = []
        self._list.append(element)

    def setInteger(self, value: int) -> None:
        self._integer = value
        self._list = None

    def getList(self) -> list["_JudgeNestedInteger"] | None:
        return self._list


class _JudgeImmutableListNode:
    """Read-only linked-list interface used by LeetCode 1265."""

    def __init__(
        self,
        value: Any,
        next_node: "_JudgeImmutableListNode | None" = None,
        printed_values: list[Any] | None = None,
    ):
        self._value = value
        self._next_node = next_node
        self._printed_values = printed_values if printed_values is not None else []

    def getNext(self) -> "_JudgeImmutableListNode | None":
        return self._next_node

    def printValue(self) -> None:
        self._printed_values.append(self._value)

    @property
    def printed_values(self) -> tuple[Any, ...]:
        return tuple(self._printed_values)


class _JudgeQuadNode:
    def __init__(
        self,
        val: bool,
        is_leaf: bool,
        top_left: "_JudgeQuadNode | None" = None,
        top_right: "_JudgeQuadNode | None" = None,
        bottom_left: "_JudgeQuadNode | None" = None,
        bottom_right: "_JudgeQuadNode | None" = None,
    ):
        self.val = val
        self.isLeaf = is_leaf
        self.topLeft = top_left
        self.topRight = top_right
        self.bottomLeft = bottom_left
        self.bottomRight = bottom_right


class _JudgeRobot:
    """Hidden-room simulator for LeetCode's Robot control interface."""

    _DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))

    def __init__(self, room: list[list[int]], row: int, col: int, direction: int = 0):
        if not room or not all(isinstance(line, list) and line for line in room):
            raise ValueError("robot room must be a nonempty matrix")
        width = len(room[0])
        if any(len(line) != width or any(cell not in {0, 1} for cell in line) for line in room):
            raise ValueError("robot room must be a rectangular binary matrix")
        if not 0 <= row < len(room) or not 0 <= col < width or room[row][col] != 1:
            raise ValueError("robot start must be an open room cell")
        self._room = room
        self._row = row
        self._col = col
        self._start = (row, col)
        self._direction = direction % 4
        self._cleaned: set[tuple[int, int]] = set()

    def move(self) -> bool:
        delta_row, delta_col = self._DIRECTIONS[self._direction]
        next_row = self._row + delta_row
        next_col = self._col + delta_col
        if (
            not 0 <= next_row < len(self._room)
            or not 0 <= next_col < len(self._room[0])
            or self._room[next_row][next_col] == 0
        ):
            return False
        self._row = next_row
        self._col = next_col
        return True

    def turnLeft(self) -> None:
        self._direction = (self._direction - 1) % 4

    def turnRight(self) -> None:
        self._direction = (self._direction + 1) % 4

    def clean(self) -> None:
        self._cleaned.add((self._row, self._col))

    @property
    def cleaned_cells(self) -> frozenset[tuple[int, int]]:
        return frozenset(self._cleaned)

    @property
    def reachable_cells(self) -> frozenset[tuple[int, int]]:
        reachable = {self._start}
        pending = [self._start]
        while pending:
            row, col = pending.pop()
            for delta_row, delta_col in self._DIRECTIONS:
                next_row = row + delta_row
                next_col = col + delta_col
                cell = (next_row, next_col)
                if (
                    0 <= next_row < len(self._room)
                    and 0 <= next_col < len(self._room[0])
                    and self._room[next_row][next_col] == 1
                    and cell not in reachable
                ):
                    reachable.add(cell)
                    pending.append(cell)
        return frozenset(reachable)


class _JudgeGridMaster:
    """Stateful hidden-grid simulator for LeetCode's GridMaster API."""

    _DIRECTIONS = {
        "U": (-1, 0),
        "R": (0, 1),
        "D": (1, 0),
        "L": (0, -1),
    }

    def __init__(
        self,
        grid: list[list[int]],
        *,
        start: list[int] | tuple[int, int] | None = None,
        target: list[int] | tuple[int, int] | None = None,
        weighted: bool = False,
    ):
        if not grid or not all(isinstance(row, list) and row for row in grid):
            raise ValueError("GridMaster grid must be a nonempty matrix")
        width = len(grid[0])
        if any(len(row) != width for row in grid):
            raise ValueError("GridMaster grid must be rectangular")

        marker_start = None
        marker_target = None
        for row, values in enumerate(grid):
            for column, value in enumerate(values):
                if value == -1:
                    marker_start = (row, column)
                elif value == 2 and not weighted:
                    marker_target = (row, column)

        self._grid = grid
        self._weighted = weighted
        self._position = self._coordinate(start, marker_start, "start")
        self._target = self._coordinate(target, marker_target, "target")
        if not self._is_open(*self._position) or not self._is_open(*self._target):
            raise ValueError("GridMaster start and target must be open cells")

    @staticmethod
    def _coordinate(
        supplied: list[int] | tuple[int, int] | None,
        marker: tuple[int, int] | None,
        name: str,
    ) -> tuple[int, int]:
        value = supplied if supplied is not None else marker
        if (
            not isinstance(value, (list, tuple))
            or len(value) != 2
            or any(not isinstance(item, int) or isinstance(item, bool) for item in value)
        ):
            raise ValueError(f"GridMaster {name} must be a two-integer coordinate")
        return int(value[0]), int(value[1])

    def _is_open(self, row: int, column: int) -> bool:
        return (
            0 <= row < len(self._grid)
            and 0 <= column < len(self._grid[0])
            and self._grid[row][column] != 0
        )

    def _neighbor(self, direction: str) -> tuple[int, int]:
        if direction not in self._DIRECTIONS:
            raise ValueError("GridMaster direction must be U, R, D, or L")
        row_delta, column_delta = self._DIRECTIONS[direction]
        return self._position[0] + row_delta, self._position[1] + column_delta

    def canMove(self, direction: str) -> bool:
        return self._is_open(*self._neighbor(direction))

    def move(self, direction: str) -> bool | int:
        neighbor = self._neighbor(direction)
        if not self._is_open(*neighbor):
            return -1 if self._weighted else False
        self._position = neighbor
        return self._grid[neighbor[0]][neighbor[1]] if self._weighted else True

    def isTarget(self) -> bool:
        return self._position == self._target

    def __repr__(self) -> str:
        return f"Robot(cleaned={len(self._cleaned)}/{len(self.reachable_cells)})"


class _JudgePoint:
    """Coordinate object used by LeetCode's Sea interface."""

    def __init__(self, x: int, y: int):
        if any(not isinstance(value, int) or isinstance(value, bool) for value in (x, y)):
            raise ValueError("point coordinates must be integers")
        self.x = x
        self.y = y


class _JudgeSea:
    """Hidden-ship simulator for LeetCode's Sea query interface."""

    def __init__(self, ships: list[list[int]], max_queries: int = 400):
        if not isinstance(ships, list):
            raise ValueError("sea ships must be a list of coordinate pairs")
        parsed: set[tuple[int, int]] = set()
        for point in ships:
            if (
                not isinstance(point, list)
                or len(point) != 2
                or any(not isinstance(value, int) or isinstance(value, bool) for value in point)
            ):
                raise ValueError("every sea ship must be an integer coordinate pair")
            parsed.add((point[0], point[1]))
        if len(parsed) != len(ships):
            raise ValueError("sea ships must occupy distinct coordinates")
        if not isinstance(max_queries, int) or isinstance(max_queries, bool) or max_queries < 0:
            raise ValueError("sea max_queries must be a non-negative integer")
        self._ships = frozenset(parsed)
        self._max_queries = max_queries
        self._query_count = 0

    def hasShips(self, topRight: _JudgePoint, bottomLeft: _JudgePoint) -> bool:
        def parse_point(point: Any, name: str) -> tuple[int, int]:
            try:
                x = point.x
                y = point.y
            except AttributeError as exc:
                raise ValueError(f"{name} must be a Point") from exc
            if any(not isinstance(value, int) or isinstance(value, bool) for value in (x, y)):
                raise ValueError(f"{name} must contain integer coordinates")
            return x, y

        right, top = parse_point(topRight, "topRight")
        left, bottom = parse_point(bottomLeft, "bottomLeft")
        if left > right or bottom > top:
            raise ValueError("sea query rectangle must have ordered corners")
        self._query_count += 1
        if self._query_count > self._max_queries:
            raise RuntimeError(f"Sea.hasShips exceeded the {self._max_queries}-query limit")
        return any(left <= x <= right and bottom <= y <= top for x, y in self._ships)

    @property
    def query_count(self) -> int:
        return self._query_count


class _JudgeBinaryMatrix:
    """Read-only binary-matrix interface used by LeetCode 1428."""

    def __init__(self, matrix: list[list[int]], max_queries: int = 1000):
        if not isinstance(matrix, list) or not matrix:
            raise ValueError("binary matrix must be nonempty")
        if not all(isinstance(row, list) and row for row in matrix):
            raise ValueError("binary matrix rows must be nonempty lists")
        width = len(matrix[0])
        if any(
            len(row) != width or any(value not in {0, 1} for value in row)
            for row in matrix
        ):
            raise ValueError("binary matrix must be rectangular and contain only zeroes and ones")
        if any(row != sorted(row) for row in matrix):
            raise ValueError("binary matrix rows must be sorted in non-decreasing order")
        if not isinstance(max_queries, int) or isinstance(max_queries, bool) or max_queries < 0:
            raise ValueError("binary matrix max_queries must be a non-negative integer")
        self._matrix = tuple(tuple(row) for row in matrix)
        self._max_queries = max_queries
        self._query_count = 0

    def get(self, row: int, col: int) -> int:
        if any(not isinstance(value, int) or isinstance(value, bool) for value in (row, col)):
            raise ValueError("BinaryMatrix.get indices must be integers")
        if not 0 <= row < len(self._matrix) or not 0 <= col < len(self._matrix[0]):
            raise ValueError("BinaryMatrix.get indices are outside the matrix")
        self._query_count += 1
        if self._query_count > self._max_queries:
            raise RuntimeError(
                f"BinaryMatrix.get exceeded the {self._max_queries}-query limit"
            )
        return self._matrix[row][col]

    def dimensions(self) -> list[int]:
        return [len(self._matrix), len(self._matrix[0])]

    @property
    def query_count(self) -> int:
        return self._query_count

    def __repr__(self) -> str:
        rows, cols = self.dimensions()
        return f"BinaryMatrix({rows}x{cols}, queries={self._query_count})"


class _JudgeInfiniteStream:
    """Sequential binary-stream interface used by LeetCode 3023."""

    def __init__(self, bits: list[int], max_reads: int | None = None):
        if not isinstance(bits, list) or not bits:
            raise ValueError("infinite stream fixture must contain at least one bit")
        if any(
            not isinstance(bit, int) or isinstance(bit, bool) or bit not in (0, 1)
            for bit in bits
        ):
            raise ValueError("infinite stream fixture values must be 0 or 1")
        if max_reads is None:
            max_reads = len(bits)
        if (
            not isinstance(max_reads, int)
            or isinstance(max_reads, bool)
            or not 0 <= max_reads <= len(bits)
        ):
            raise ValueError("infinite stream max_reads must fit the authored fixture")
        self.__bits = tuple(bits)
        self._max_reads = max_reads
        self._read_count = 0

    def next(self) -> int:
        if self._read_count >= self._max_reads:
            raise RuntimeError(
                f"InfiniteStream.next exceeded the {self._max_reads}-read fixture limit"
            )
        bit = self.__bits[self._read_count]
        self._read_count += 1
        return bit

    @property
    def read_count(self) -> int:
        return self._read_count

    def __repr__(self) -> str:
        return f"InfiniteStream(reads={self._read_count}, limit={self._max_reads})"


class _JudgeFontInfo:
    """Font-metric interface used by LeetCode 1618."""

    def __init__(
        self,
        heights: dict[str, int],
        widths: dict[str, dict[str, int]] | None = None,
        uniform_widths: dict[str, int] | None = None,
        max_queries: int = 100_000,
    ):
        if not isinstance(heights, dict) or not heights:
            raise ValueError("font info heights must be a nonempty mapping")
        if not isinstance(widths, dict):
            widths = {}
        if not isinstance(uniform_widths, dict):
            uniform_widths = {}
        if not isinstance(max_queries, int) or isinstance(max_queries, bool) or max_queries < 0:
            raise ValueError("font info max_queries must be a non-negative integer")

        self._heights = self._parse_metric_map(heights, "height")
        self._uniform_widths = self._parse_metric_map(uniform_widths, "uniform width")
        self._widths: dict[int, dict[str, int]] = {}
        for raw_font, raw_metrics in widths.items():
            font = self._parse_font(raw_font)
            if not isinstance(raw_metrics, dict):
                raise ValueError("font-specific widths must be character mappings")
            parsed: dict[str, int] = {}
            for character, value in raw_metrics.items():
                if not isinstance(character, str) or len(character) != 1 or not character.islower():
                    raise ValueError("font width keys must be lowercase characters")
                parsed[character] = self._parse_metric(value, "width")
            self._widths[font] = parsed

        available_width_fonts = set(self._uniform_widths) | set(self._widths)
        if set(self._heights) != available_width_fonts:
            raise ValueError("font info must define height and width metrics for the same fonts")
        ordered_fonts = sorted(self._heights)
        if any(
            self._heights[left] > self._heights[right]
            for left, right in zip(ordered_fonts, ordered_fonts[1:])
        ):
            raise ValueError("font heights must be non-decreasing by font size")

        self._max_queries = max_queries
        self._query_count = 0

    @staticmethod
    def _parse_font(value: object) -> int:
        try:
            font = int(value)
        except (TypeError, ValueError) as exc:
            raise ValueError("font sizes must be positive integers") from exc
        if isinstance(value, bool) or font <= 0 or str(font) != str(value):
            raise ValueError("font sizes must be positive integers")
        return font

    @staticmethod
    def _parse_metric(value: object, name: str) -> int:
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise ValueError(f"font {name} values must be non-negative integers")
        return value

    @classmethod
    def _parse_metric_map(cls, values: dict[str, int], name: str) -> dict[int, int]:
        return {
            cls._parse_font(font): cls._parse_metric(value, name)
            for font, value in values.items()
        }

    def _record_query(self) -> None:
        self._query_count += 1
        if self._query_count > self._max_queries:
            raise RuntimeError(
                f"FontInfo exceeded the {self._max_queries}-query limit"
            )

    def getWidth(self, fontSize: int, ch: str) -> int:
        if not isinstance(fontSize, int) or isinstance(fontSize, bool):
            raise ValueError("FontInfo fontSize must be an integer")
        if not isinstance(ch, str) or len(ch) != 1 or not ch.islower():
            raise ValueError("FontInfo ch must be one lowercase character")
        self._record_query()
        if fontSize not in self._heights:
            raise ValueError("FontInfo fontSize has no authored metrics")
        if ch in self._widths.get(fontSize, {}):
            return self._widths[fontSize][ch]
        if fontSize in self._uniform_widths:
            return self._uniform_widths[fontSize]
        raise ValueError("FontInfo character has no authored width")

    def getHeight(self, fontSize: int) -> int:
        if not isinstance(fontSize, int) or isinstance(fontSize, bool):
            raise ValueError("FontInfo fontSize must be an integer")
        self._record_query()
        if fontSize not in self._heights:
            raise ValueError("FontInfo fontSize has no authored metrics")
        return self._heights[fontSize]

    @property
    def query_count(self) -> int:
        return self._query_count

    def __repr__(self) -> str:
        return f"FontInfo(fonts={len(self._heights)}, queries={self._query_count})"


class _JudgeMountainArray:
    """Read-only mountain-array simulator for LeetCode 1095."""

    def __init__(self, values: list[int], max_queries: int = 100):
        if not isinstance(values, list) or len(values) < 3:
            raise ValueError("MountainArray requires at least three values")
        if any(not isinstance(value, int) or isinstance(value, bool) for value in values):
            raise ValueError("MountainArray values must be integers")
        if not isinstance(max_queries, int) or isinstance(max_queries, bool) or max_queries < 0:
            raise ValueError("MountainArray max_queries must be a non-negative integer")
        self.__values = tuple(values)
        self._max_queries = max_queries
        self._query_count = 0

    def get(self, index: int) -> int:
        if not isinstance(index, int) or isinstance(index, bool):
            raise ValueError("MountainArray index must be an integer")
        if not 0 <= index < len(self.__values):
            raise ValueError("MountainArray index is outside the array")
        self._query_count += 1
        if self._query_count > self._max_queries:
            raise RuntimeError(
                f"MountainArray.get exceeded the {self._max_queries}-query limit"
            )
        return self.__values[index]

    def length(self) -> int:
        return len(self.__values)

    @property
    def query_count(self) -> int:
        return self._query_count

    def __repr__(self) -> str:
        return f"MountainArray(length={len(self.__values)}, queries={self._query_count})"


class _JudgeHtmlParser:
    """URL-adjacency simulator for LeetCode 1236."""

    def __init__(self, urls: list[str], edges: list[list[int]]):
        if not isinstance(urls, list) or any(not isinstance(url, str) for url in urls):
            raise ValueError("HtmlParser urls must be a list of strings")
        if len(set(urls)) != len(urls):
            raise ValueError("HtmlParser urls must be unique")
        self.__outgoing = {url: [] for url in urls}
        if not isinstance(edges, list):
            raise ValueError("HtmlParser edges must be a list")
        for edge in edges:
            if (
                not isinstance(edge, list)
                or len(edge) != 2
                or any(not isinstance(index, int) or isinstance(index, bool) for index in edge)
            ):
                raise ValueError("HtmlParser edges must contain two integer indices")
            source, destination = edge
            if not (0 <= source < len(urls) and 0 <= destination < len(urls)):
                raise ValueError("HtmlParser edge index is outside the URL list")
            self.__outgoing[urls[source]].append(urls[destination])

    def getUrls(self, url: str) -> list[str]:
        return list(self.__outgoing.get(url, ()))

    def __repr__(self) -> str:
        return f"HtmlParser(pages={len(self.__outgoing)})"


class _JudgeCustomFunction:
    """Monotone-function simulator for LeetCode 1237."""

    def __init__(self, function_id: int):
        if not isinstance(function_id, int) or isinstance(function_id, bool):
            raise ValueError("CustomFunction id must be an integer")
        if not 1 <= function_id <= 9:
            raise ValueError("CustomFunction id must be between 1 and 9")
        self._function_id = function_id

    def f(self, x: int, y: int) -> int:
        functions = (
            None,
            lambda a, b: a + b,
            lambda a, b: a * b,
            lambda a, b: a * a + b,
            lambda a, b: a + b * b,
            lambda a, b: a * a + b * b,
            lambda a, b: (a + b) * (a + b),
            lambda a, b: a * a * a + b * b * b,
            lambda a, b: a * a * b,
            lambda a, b: a * b * b,
        )
        return functions[self._function_id](x, y)


class _JudgeArrayReader:
    """Hidden-array simulator for LeetCode 1533's sum-comparison API."""

    def __init__(self, array: list[int], max_queries: int = 20):
        if not isinstance(array, list) or not 2 <= len(array) <= 500_000:
            raise ValueError("ArrayReader array length must be between 2 and 500000")
        if any(not isinstance(value, int) or isinstance(value, bool) for value in array):
            raise ValueError("ArrayReader values must be integers")
        if any(not 1 <= value <= 100 for value in array):
            raise ValueError("ArrayReader values must be between 1 and 100")
        smallest = min(array)
        larger = [index for index, value in enumerate(array) if value != smallest]
        if len(larger) != 1 or array[larger[0]] <= smallest:
            raise ValueError("ArrayReader requires exactly one value larger than all others")
        if any(value != smallest for index, value in enumerate(array) if index != larger[0]):
            raise ValueError("all non-maximum ArrayReader values must be equal")
        if not isinstance(max_queries, int) or isinstance(max_queries, bool) or max_queries < 0:
            raise ValueError("ArrayReader max_queries must be a non-negative integer")
        prefix = [0]
        for value in array:
            prefix.append(prefix[-1] + value)
        self.__prefix = tuple(prefix)
        self._length = len(array)
        self._max_queries = max_queries
        self._query_count = 0

    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
        if any(
            not isinstance(value, int) or isinstance(value, bool)
            for value in (l, r, x, y)
        ):
            raise ValueError("ArrayReader.compareSub indices must be integers")
        if not (0 <= l <= r < self._length and 0 <= x <= y < self._length):
            raise ValueError("ArrayReader.compareSub indices are outside the array")
        self._query_count += 1
        if self._query_count > self._max_queries:
            raise RuntimeError(
                f"ArrayReader.compareSub exceeded the {self._max_queries}-query limit"
            )
        left_sum = self.__prefix[r + 1] - self.__prefix[l]
        right_sum = self.__prefix[y + 1] - self.__prefix[x]
        return (left_sum > right_sum) - (left_sum < right_sum)

    def length(self) -> int:
        return self._length

    @property
    def query_count(self) -> int:
        return self._query_count

    def __repr__(self) -> str:
        return f"ArrayReader(length={self._length}, queries={self._query_count})"


class _JudgeMajorityReader:
    """Hidden binary-array simulator for LeetCode 1538's query API."""

    def __init__(self, array: list[int], max_queries: int | None = None):
        if not isinstance(array, list) or not 5 <= len(array) <= 100_000:
            raise ValueError("majority ArrayReader length must be between 5 and 100000")
        if any(
            not isinstance(value, int)
            or isinstance(value, bool)
            or value not in (0, 1)
            for value in array
        ):
            raise ValueError("majority ArrayReader values must be 0 or 1")
        if max_queries is None:
            max_queries = 2 * len(array)
        if not isinstance(max_queries, int) or isinstance(max_queries, bool) or max_queries < 0:
            raise ValueError("majority ArrayReader max_queries must be a non-negative integer")
        self.__array = tuple(array)
        self._max_queries = max_queries
        self._query_count = 0

    def query(self, a: int, b: int, c: int, d: int) -> int:
        if any(
            not isinstance(value, int) or isinstance(value, bool)
            for value in (a, b, c, d)
        ):
            raise ValueError("ArrayReader.query indices must be integers")
        if not 0 <= a < b < c < d < len(self.__array):
            raise ValueError("ArrayReader.query requires four increasing valid indices")
        self._query_count += 1
        if self._query_count > self._max_queries:
            raise RuntimeError(
                f"ArrayReader.query exceeded the {self._max_queries}-query limit"
            )
        ones = sum(self.__array[index] for index in (a, b, c, d))
        if ones in (0, 4):
            return 4
        if ones == 2:
            return 0
        return 2

    def length(self) -> int:
        return len(self.__array)

    @property
    def query_count(self) -> int:
        return self._query_count

    def __repr__(self) -> str:
        return f"ArrayReader(length={len(self.__array)}, queries={self._query_count})"


class _JudgeMaster:
    """Hidden-word simulator for LeetCode's Master guessing interface."""

    def __init__(self, secret: str, words: list[str], allowed_guesses: int):
        if not isinstance(secret, str) or not isinstance(words, list):
            raise ValueError("master fixture requires a secret and word list")
        if secret not in words:
            raise ValueError("master secret must occur in the word list")
        if len(set(words)) != len(words) or any(not isinstance(word, str) or len(word) != 6 for word in words):
            raise ValueError("master words must be unique six-letter strings")
        if allowed_guesses < 0:
            raise ValueError("master allowed_guesses must be non-negative")
        self._secret = secret
        self._words = frozenset(words)
        self._allowed_guesses = allowed_guesses
        self._guess_count = 0
        self._found = False

    def guess(self, word: str) -> int:
        self._guess_count += 1
        if word not in self._words:
            return -1
        matches = sum(left == right for left, right in zip(word, self._secret))
        if matches == 6:
            self._found = True
        return matches

    @property
    def found(self) -> bool:
        return self._found

    @property
    def guess_count(self) -> int:
        return self._guess_count

    @property
    def allowed_guesses(self) -> int:
        return self._allowed_guesses

    def __repr__(self) -> str:
        return f"Master(found={self._found}, guesses={self._guess_count}/{self._allowed_guesses})"


def _get_spec_inputs(spec: Any) -> dict[str, Any]:
    raw_inputs = getattr(spec, "inputs", {}) or {}
    inputs = dict(raw_inputs) if isinstance(raw_inputs, (list, tuple, dict)) else {}
    spec_id = getattr(spec, "id", "")
    if spec_id.startswith("lc_") and (not inputs or set(inputs.keys()) == {"value"}):
        try:
            from challenges.algorithms.leetcode import load_full_leetcode_spec
            full_spec = load_full_leetcode_spec(spec_id)
            if full_spec and full_spec.inputs:
                return dict(full_spec.inputs)
        except Exception:
            pass
    return inputs


def _returns_tree(returns_hint: str, spec: Any = None) -> bool:
    text = str(returns_hint).lower()
    if (
        "treenode" in text
        or "tree node" in text
        or "root node" in text
        or ("root" in text and "tree" in text)
    ):
        return True
    if spec is not None and getattr(spec, "id", "").startswith("lc_"):
        try:
            from challenges.algorithms.leetcode import load_full_leetcode_spec
            full_spec = load_full_leetcode_spec(spec.id)
            if full_spec and full_spec.returns and full_spec.returns != returns_hint:
                return _returns_tree(full_spec.returns)
        except Exception:
            pass
    return False


def _returns_list_node(returns_hint: str, spec: Any = None) -> bool:
    text = str(returns_hint).lower()
    if (
        "listnode" in text
        or "polynode" in text
        or "list node" in text
        or "linked list" in text
        or "linked-list" in text
        or re.search(
            r"\breturns?\s+(?:the\s+)?(?:new\s+|modified\s+|original\s+|resulting\s+)?head\b",
            text,
        )
        is not None
    ):
        return True
    if spec is not None and getattr(spec, "id", "").startswith("lc_"):
        try:
            from challenges.algorithms.leetcode import load_full_leetcode_spec
            full_spec = load_full_leetcode_spec(spec.id)
            if full_spec and full_spec.returns and full_spec.returns != returns_hint:
                return _returns_list_node(full_spec.returns)
        except Exception:
            pass
    return False


def _tree_param_names(spec: Any) -> list[str]:
    inputs = _get_spec_inputs(spec)
    target_names = set(_tree_node_target_param_names(spec))
    names: list[str] = []
    for name, hint in inputs.items():
        if str(name) in target_names:
            continue
        lowered_name = str(name).lower()
        if lowered_name in {"root", "subroot", "sub_root", "trees", "tree"}:
            names.append(str(name))
            continue
        if lowered_name in {"p", "q"} and getattr(spec, "id", "") == "lc_100":
            names.append(str(name))
            continue
        text = str(hint).lower()
        normalized_text = text.replace("-", " ")
        root_node_hint = re.search(r"(?<!non-)root node", text) is not None
        if (
            "treenode" in text
            or "tree node" in normalized_text
            or re.search(r"\btree root\b", normalized_text) is not None
            or root_node_hint
            or "root of" in text
        ):
            names.append(str(name))
    return names


def _tree_node_target_param_names(spec: Any) -> list[str]:
    inputs = _get_spec_inputs(spec)
    has_root_param = any("root" in str(k).lower() for k in inputs)
    if not has_root_param:
        return []
    names: list[str] = []
    for name, hint in inputs.items():
        lowered_name = str(name).lower()
        text = str(hint).lower()
        if "root" in text:
            continue
        names_target_node = lowered_name in {"p", "q", "u", "target", "leaf"}
        describes_target_node = "target" in text
        if "root" not in lowered_name and (names_target_node or describes_target_node) and (
            "treenode" in text or "tree node" in text or ("node" in text and "tree" in text)
        ):
            names.append(str(name))
    return names


def _list_node_param_names(spec: Any) -> list[str]:
    inputs = _get_spec_inputs(spec)
    names: list[str] = []
    for name, hint in inputs.items():
        lowered_name = str(name).lower()
        if lowered_name in {"head", "head1", "head2", "heada", "headb", "head_a", "head_b", "list1", "list2", "l1", "l2"}:
            names.append(str(name))
            continue
        text = str(hint).lower()
        node_shaped_name = (
            lowered_name in {"head", "node"}
            or lowered_name.startswith("head")
            or lowered_name.endswith("_head")
        )
        node_shaped_hint = (
            "listnode" in text
            or "list node" in text
            or "head node" in text
            or "linked-list" in text
            or "doubly linked list" in text
        )
        if (node_shaped_name and ("linked list" in text or "linked-list" in text)) or node_shaped_hint:
            names.append(str(name))
    return names


def _list_node_collection_param_names(spec: Any) -> list[str]:
    inputs = _get_spec_inputs(spec)
    names: list[str] = []
    for name, hint in inputs.items():
        text = str(hint).lower()
        if (
            ("linked-list heads" in text or "linked list heads" in text)
            and ("array" in text or "list" in text)
        ):
            names.append(str(name))
    return names


def _nary_node_param_names(spec: Any) -> list[str]:
    inputs = _get_spec_inputs(spec)
    names: list[str] = []
    for name, hint in inputs.items():
        text = str(hint).lower().replace("–", "-")
        if "n-ary" in text and ("node" in text or "root" in text):
            names.append(str(name))
    return names


def _nary_node_collection_param_names(spec: Any) -> list[str]:
    inputs = _get_spec_inputs(spec)
    names: list[str] = []
    for name, hint in inputs.items():
        text = str(hint).lower().replace("–", "-")
        if "n-ary" in text and "node" in text and (
            "list of" in text or "collection" in text
        ):
            names.append(str(name))
    return names


def _random_binary_tree_param_names(spec: Any) -> list[str]:
    spec_id = getattr(spec, "id", "")
    if spec_id == "lc_1485":
        return ["root"]
    inputs = _get_spec_inputs(spec)
    names: list[str] = []
    for name, hint in inputs.items():
        text = str(hint).lower()
        if "random" in text and ("node" in text or "tree" in text or "pointer" in text):
            names.append(str(name))
    return names


def _big_array_param_names(spec: Any) -> list[str]:
    inputs = _get_spec_inputs(spec)
    return [
        str(name)
        for name, hint in inputs.items()
        if "bigarray" in str(hint).lower()
    ]


def _list_node_from_values(values: Any) -> Any:
    if values is None:
        return None
    cycle_position = -1
    if isinstance(values, dict) and set(values) >= {"values", "node_index"}:
        raw_values = values.get("values")
        node_index = values.get("node_index")
        if not isinstance(raw_values, list) or not isinstance(node_index, int):
            return values
        nodes = [_JudgeNode(value) for value in raw_values]
        for index in range(1, len(nodes)):
            nodes[index - 1].next = nodes[index]
            nodes[index].prev = nodes[index - 1]
        return nodes[node_index] if 0 <= node_index < len(nodes) else values
    if isinstance(values, dict):
        raw_values = values.get("values")
        raw_position = values.get("pos", -1)
        if not isinstance(raw_values, list) or not isinstance(raw_position, int):
            return values
        values = raw_values
        cycle_position = raw_position
    if not isinstance(values, list):
        return values
    if all(
        isinstance(entry, list)
        and len(entry) == 2
        and isinstance(entry[1], list)
        for entry in values
    ):
        return _multilevel_list_from_fixture(values)
    nodes = [_JudgeListNode(value) for value in values]
    for index in range(1, len(nodes)):
        nodes[index - 1].next = nodes[index]
    if nodes and 0 <= cycle_position < len(nodes):
        nodes[-1].next = nodes[cycle_position]
    return nodes[0] if nodes else None


def _poly_node_from_terms(terms: Any) -> Any:
    if terms is None:
        return None
    if not isinstance(terms, list):
        return terms
    dummy = _JudgePolyNode()
    tail = dummy
    for term in terms:
        if (
            not isinstance(term, list)
            or len(term) != 2
            or any(
                not isinstance(value, int) or isinstance(value, bool)
                for value in term
            )
        ):
            return terms
        tail.next = _JudgePolyNode(term[0], term[1])
        tail = tail.next
    return dummy.next


def _multilevel_list_from_fixture(entries: list[Any]) -> Any:
    head: _JudgeNode | None = None
    previous: _JudgeNode | None = None
    for value, child_entries in entries:
        node = _JudgeNode(value)
        node.prev = previous
        node.child = _multilevel_list_from_fixture(child_entries) if child_entries else None
        if previous is None:
            head = node
        else:
            previous.next = node
        previous = node
    return head


def _nary_nodes_from_records(records: Any) -> tuple[Any, dict[Any, Any], list[Any]]:
    if not isinstance(records, list) or not all(
        isinstance(record, list)
        and len(record) == 2
        and isinstance(record[1], list)
        for record in records
    ):
        return records, {}, []
    nodes = {record[0]: _JudgeNode(record[0]) for record in records}
    child_values: set[Any] = set()
    ordered_nodes: list[Any] = []
    for value, children in records:
        node = nodes[value]
        node.children = [nodes[child] for child in children]
        child_values.update(children)
        ordered_nodes.append(node)
    root_value = next((value for value in nodes if value not in child_values), None)
    return nodes.get(root_value), nodes, ordered_nodes


def _nary_node_from_fixture(fixture: Any) -> Any:
    if fixture is None:
        return None
    if fixture and isinstance(fixture, list) and isinstance(fixture[0], list):
        root, _nodes, _ordered = _nary_nodes_from_records(fixture)
        return root
    if (
        not isinstance(fixture, list)
        or len(fixture) != 2
        or not isinstance(fixture[1], list)
    ):
        return fixture
    node = _JudgeNode(fixture[0])
    node.children = [_nary_node_from_fixture(child) for child in fixture[1]]
    return node


def _nested_integer_list_from_fixture(fixture: Any) -> Any:
    if not isinstance(fixture, list):
        return fixture
    return [_JudgeNestedInteger(value) for value in fixture]


def _nested_integer_to_fixture(value: Any) -> Any:
    if not hasattr(value, "isInteger"):
        return value
    if value.isInteger():
        return value.getInteger()
    nested = value.getList()
    return [] if nested is None else [_nested_integer_to_fixture(item) for item in nested]


def _nary_node_to_fixture(root: Any) -> Any:
    if root is None:
        return None
    if not hasattr(root, "val") or not isinstance(getattr(root, "children", None), list):
        return root
    return [
        getattr(root, "val"),
        [_nary_node_to_fixture(child) for child in getattr(root, "children")],
    ]


def _nary_node_to_records(root: Any) -> Any:
    if root is None:
        return []
    records: list[list[Any]] = []
    queue = [root]
    for node in queue:
        children = list(getattr(node, "children", []))
        records.append([getattr(node, "val"), [getattr(child, "val") for child in children]])
        queue.extend(children)
    return records


def _random_binary_tree_from_fixture(values: Any) -> Any:
    if not isinstance(values, list):
        return values
    nodes = [
        None if entry is None else _JudgeNode(entry[0])
        for entry in values
    ]
    child_index = 1
    for node in nodes:
        if node is None:
            continue
        if child_index < len(nodes):
            node.left = nodes[child_index]
            child_index += 1
        if child_index < len(nodes):
            node.right = nodes[child_index]
            child_index += 1
    for index, entry in enumerate(values):
        if nodes[index] is None or entry is None:
            continue
        random_index = entry[1]
        nodes[index].random = (
            nodes[random_index]
            if isinstance(random_index, int) and 0 <= random_index < len(nodes)
            else None
        )
    return nodes[0] if nodes else None


def _random_binary_tree_to_fixture(root: Any) -> Any:
    if root is None:
        return []
    nodes: list[Any] = [root]
    cursor = 0
    while cursor < len(nodes):
        node = nodes[cursor]
        cursor += 1
        if node is None:
            continue
        nodes.append(getattr(node, "left", None))
        nodes.append(getattr(node, "right", None))
    while nodes and nodes[-1] is None:
        nodes.pop()
    indices = {id(node): index for index, node in enumerate(nodes) if node is not None}
    return [
        None
        if node is None
        else [
            getattr(node, "val"),
            indices.get(id(getattr(node, "random", None))),
        ]
        for node in nodes
    ]


def _node_graphs_are_disjoint(first: Any, second: Any) -> bool:
    def identities(root: Any) -> set[int]:
        seen: set[int] = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None or id(node) in seen:
                continue
            seen.add(id(node))
            stack.extend(
                getattr(node, attribute, None)
                for attribute in ("left", "right", "random")
            )
        return seen

    return identities(first).isdisjoint(identities(second))


def _immutable_list_node_from_values(values: Any) -> Any:
    if not isinstance(values, list):
        return values
    printed_values: list[Any] = []
    head: _JudgeImmutableListNode | None = None
    for value in reversed(values):
        head = _JudgeImmutableListNode(value, head, printed_values)
    return head


def _prepare_shared_list_nodes(kwargs: dict[str, Any], names: list[str] | tuple[str, ...]) -> set[str]:
    encoded: list[tuple[str, dict[str, Any]]] = []
    for name in names:
        value = kwargs.get(name)
        if isinstance(value, dict) and "prefix" in value and "shared" in value:
            encoded.append((name, value))
    if len(encoded) < 2:
        return set()

    shared_values = encoded[0][1].get("shared")
    if not isinstance(shared_values, list):
        return set()
    if any(payload.get("shared") != shared_values for _, payload in encoded[1:]):
        return set()

    shared_head = _list_node_from_values(shared_values)
    decoded: set[str] = set()
    for name, payload in encoded:
        prefix_values = payload.get("prefix")
        if not isinstance(prefix_values, list):
            return set()
        prefix_head = _list_node_from_values(prefix_values)
        if prefix_head is None:
            kwargs[name] = shared_head
        else:
            tail = prefix_head
            while tail.next is not None:
                tail = tail.next
            tail.next = shared_head
            kwargs[name] = prefix_head
        decoded.add(name)
    return decoded


def _list_node_to_values(head: Any) -> Any:
    if isinstance(head, list):
        if all(
            item is None or all(hasattr(item, attr) for attr in ("val", "next"))
            for item in head
        ):
            return [_list_node_to_values(item) for item in head]
        return head
    if head is None:
        return []
    if not all(hasattr(head, attr) for attr in ("val", "next")):
        return head
    result: list[Any] = []
    seen: set[int] = set()
    node = head
    while node is not None:
        marker = id(node)
        if marker in seen:
            break
        seen.add(marker)
        result.append(getattr(node, "val"))
        node = getattr(node, "next", None)
    return result


def _poly_node_to_terms(head: Any) -> Any:
    if head is None:
        return []
    if not all(hasattr(head, attr) for attr in ("coefficient", "power", "next")):
        return head
    result: list[list[int]] = []
    seen: set[int] = set()
    node = head
    while node is not None:
        marker = id(node)
        if marker in seen:
            break
        seen.add(marker)
        result.append([getattr(node, "coefficient"), getattr(node, "power")])
        node = getattr(node, "next", None)
    return result


def _tree_from_level_order(values: Any) -> Any:
    if values is None:
        return None
    if isinstance(values, dict) and {"len", "val", "left", "right"} <= set(values):
        return _JudgeRopeTreeNode(
            values["len"],
            values["val"],
            _tree_from_level_order(values["left"]),
            _tree_from_level_order(values["right"]),
        )
    corruption = None
    if isinstance(values, dict) and "values" in values:
        corruption = values.get("corrupt_right")
        values = values["values"]
    if not isinstance(values, list):
        return values
    if not values:
        return None
    nodes = [None if value is None else _JudgeTreeNode(value) for value in values]
    child_index = 1
    for node in nodes:
        if node is None:
            continue
        if child_index < len(nodes):
            node.left = nodes[child_index]
            child_index += 1
        if child_index < len(nodes):
            node.right = nodes[child_index]
            child_index += 1
    root = nodes[0]
    if corruption is not None:
        if not isinstance(corruption, dict) or set(corruption) != {
            "from_value",
            "to_value",
        }:
            raise ValueError(
                "corrupt_right must contain exactly from_value and to_value"
            )
        source = _tree_node_with_value(root, corruption["from_value"])
        target = _tree_node_with_value(root, corruption["to_value"])
        if source is None or target is None:
            raise ValueError("corrupt_right endpoints must occur in the tree")
        source.right = target
    return root


def _tree_node_with_value(root: Any, value: Any) -> Any:
    if root is None:
        return None
    stack = [root]
    while stack:
        node = stack.pop()
        if getattr(node, "val", object()) == value:
            return node
        right = getattr(node, "right", None)
        left = getattr(node, "left", None)
        if right is not None:
            stack.append(right)
        if left is not None:
            stack.append(left)
    return None


def _quad_tree_from_fixture(fixture: Any) -> Any:
    if not isinstance(fixture, dict) or not isinstance(fixture.get("leaf"), bool):
        return fixture
    if fixture["leaf"]:
        return _JudgeQuadNode(bool(fixture.get("value")), True)

    children = fixture.get("children")
    if not isinstance(children, list) or len(children) != 4:
        raise ValueError("quad-tree fixture requires four children for an internal node")
    converted = [_quad_tree_from_fixture(child) for child in children]
    if any(not isinstance(child, _JudgeQuadNode) for child in converted):
        raise ValueError("quad-tree fixture children must be nested quad-tree objects")
    return _JudgeQuadNode(True, False, *converted)


def _parent_tree_nodes_from_values(values: Any) -> list[Any]:
    if not isinstance(values, list) or not values:
        raise ValueError("parent-tree fixture requires a nonempty level-order tree")

    nodes = [None if value is None else _JudgeTreeNode(value) for value in values]
    child_index = 1
    for node in nodes:
        if node is None:
            continue
        if child_index < len(nodes):
            node.left = nodes[child_index]
            if node.left is not None:
                node.left.parent = node
            child_index += 1
        if child_index < len(nodes):
            node.right = nodes[child_index]
            if node.right is not None:
                node.right.parent = node
            child_index += 1

    return nodes


def _parent_tree_node_from_fixture(fixture: Any) -> Any:
    if not isinstance(fixture, dict) or "tree" not in fixture:
        return fixture
    values = fixture.get("tree")
    target_index = fixture.get("target_index")
    nodes = _parent_tree_nodes_from_values(values)
    if not isinstance(target_index, int) or not 0 <= target_index < len(nodes):
        raise ValueError("parent-tree fixture target_index is outside the level-order tree")

    target = nodes[target_index]
    if target is None:
        raise ValueError("parent-tree fixture target_index must select a node")
    return target


def _parent_tree_pair_from_fixtures(p_fixture: Any, q_fixture: Any) -> tuple[Any, Any] | None:
    if (
        not isinstance(p_fixture, dict)
        or "tree" not in p_fixture
        or not isinstance(q_fixture, dict)
        or q_fixture.get("same_tree_as") != "p"
    ):
        return None

    nodes = _parent_tree_nodes_from_values(p_fixture.get("tree"))
    targets: list[Any] = []
    for fixture in (p_fixture, q_fixture):
        target_index = fixture.get("target_index")
        if not isinstance(target_index, int) or not 0 <= target_index < len(nodes):
            raise ValueError("parent-tree fixture target_index is outside the level-order tree")
        target = nodes[target_index]
        if target is None:
            raise ValueError("parent-tree fixture target_index must select a node")
        targets.append(target)
    return targets[0], targets[1]


def _parent_tree_root_and_leaf_from_fixtures(
    root_fixture: Any,
    leaf_fixture: Any,
) -> tuple[Any, Any] | None:
    if (
        not isinstance(root_fixture, dict)
        or "tree" not in root_fixture
        or not isinstance(leaf_fixture, dict)
        or leaf_fixture.get("same_tree_as") != "root"
    ):
        return None

    nodes = _parent_tree_nodes_from_values(root_fixture.get("tree"))
    target_index = leaf_fixture.get("target_index")
    if not isinstance(target_index, int) or not 0 <= target_index < len(nodes):
        raise ValueError("parent-tree leaf target_index is outside the level-order tree")
    leaf = nodes[target_index]
    if leaf is None:
        raise ValueError("parent-tree leaf target_index must select a node")
    if leaf.left is not None or leaf.right is not None:
        raise ValueError("parent-tree leaf target_index must select a leaf node")
    return nodes[0], leaf


def _tree_root_and_targets_from_fixtures(
    root_fixture: Any,
    targets_fixture: Any,
) -> tuple[Any, list[Any]] | None:
    if (
        not isinstance(root_fixture, dict)
        or "tree" not in root_fixture
        or not isinstance(targets_fixture, dict)
        or targets_fixture.get("same_tree_as") != "root"
    ):
        return None

    nodes = [
        None if value is None else _JudgeTreeNode(value)
        for value in root_fixture.get("tree", [])
    ]
    if not nodes or nodes[0] is None:
        raise ValueError("shared-tree fixture requires a nonempty tree")

    child_index = 1
    for node in nodes:
        if node is None:
            continue
        if child_index < len(nodes):
            node.left = nodes[child_index]
            child_index += 1
        if child_index < len(nodes):
            node.right = nodes[child_index]
            child_index += 1

    target_indices = targets_fixture.get("target_indices")
    if not isinstance(target_indices, list) or not target_indices:
        raise ValueError("shared-tree fixture requires nonempty target_indices")
    targets: list[Any] = []
    for target_index in target_indices:
        if not isinstance(target_index, int) or not 0 <= target_index < len(nodes):
            raise ValueError("shared-tree target_index is outside the level-order tree")
        target = nodes[target_index]
        if target is None:
            raise ValueError("shared-tree target_index must select a node")
        targets.append(target)
    return nodes[0], targets


def _cloned_tree_triplet_from_fixture(fixture: Any) -> tuple[Any, Any, Any]:
    if not isinstance(fixture, dict) or "tree" not in fixture:
        raise ValueError("cloned-tree fixture requires a level-order tree")
    values = fixture.get("tree")
    target_index = fixture.get("target_index")
    if not isinstance(values, list) or not values:
        raise ValueError("cloned-tree fixture requires a nonempty level-order tree")
    if not isinstance(target_index, int) or not 0 <= target_index < len(values):
        raise ValueError("cloned-tree fixture target_index is outside the level-order tree")

    original_nodes = [
        None if value is None else _JudgeTreeNode(value) for value in values
    ]
    cloned_nodes = [
        None if value is None else _JudgeTreeNode(value) for value in values
    ]
    child_index = 1
    for original, cloned in zip(original_nodes, cloned_nodes, strict=True):
        if original is None:
            continue
        if child_index < len(values):
            original.left = original_nodes[child_index]
            cloned.left = cloned_nodes[child_index]
            child_index += 1
        if child_index < len(values):
            original.right = original_nodes[child_index]
            cloned.right = cloned_nodes[child_index]
            child_index += 1

    target = original_nodes[target_index]
    if target is None:
        raise ValueError("cloned-tree fixture target_index must select a node")
    return original_nodes[0], cloned_nodes[0], target


def _trim_level_order(values: list[Any]) -> list[Any]:
    result = list(values)
    while result and result[-1] is None:
        result.pop()
    return result


def _tree_to_level_order(root: Any) -> Any:
    if isinstance(root, list):
        return _trim_level_order(root)
    if root is None:
        return []
    if not all(hasattr(root, attr) for attr in ("val", "left", "right")):
        return root
    result: list[Any] = []
    queue: deque[Any | None] = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
            continue
        result.append(getattr(node, "val"))
        queue.append(getattr(node, "left", None))
        queue.append(getattr(node, "right", None))
    return _trim_level_order(result)


def _tree_inorder_values(root: Any) -> list[Any]:
    if root is None:
        return []
    return _tree_inorder_values(getattr(root, "left", None)) + [getattr(root, "val")] + _tree_inorder_values(
        getattr(root, "right", None)
    )


def _tree_height_if_balanced(root: Any) -> int | None:
    if root is None:
        return 0
    left = _tree_height_if_balanced(getattr(root, "left", None))
    right = _tree_height_if_balanced(getattr(root, "right", None))
    if left is None or right is None or abs(left - right) > 1:
        return None
    return max(left, right) + 1


def _balanced_bst_matches_values(level_order: Any, values: Any) -> bool:
    if not isinstance(values, list):
        return False
    root = _tree_from_level_order(level_order)
    return _tree_inorder_values(root) == values and _tree_height_if_balanced(root) is not None


def _pre_post_tree_match(actual: Any, preorder: Any, postorder: Any) -> bool:
    if (
        not isinstance(actual, list)
        or not isinstance(preorder, list)
        or not isinstance(postorder, list)
        or len(preorder) != len(postorder)
    ):
        return False
    root = _tree_from_level_order(actual)
    if _tree_to_level_order(root) != _trim_level_order(actual):
        return False

    actual_preorder: list[Any] = []
    actual_postorder: list[Any] = []

    def traverse(node: Any) -> None:
        if node is None:
            return
        actual_preorder.append(getattr(node, "val", None))
        traverse(getattr(node, "left", None))
        traverse(getattr(node, "right", None))
        actual_postorder.append(getattr(node, "val", None))

    traverse(root)
    return actual_preorder == preorder and actual_postorder == postorder


def _unordered_list_matches(actual: Any, expected: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(expected, list):
        return False

    def key(value: Any) -> str:
        try:
            return json.dumps(value, sort_keys=True)
        except TypeError:
            return repr(value)

    return sorted(actual, key=key) == sorted(expected, key=key)


def _unordered_string_match(actual: Any, expected: Any) -> bool:
    if not isinstance(actual, str) or not isinstance(expected, str):
        return False
    return sorted(actual) == sorted(expected)


def _alien_dictionary_order_match(
    actual: Any,
    expected: Any,
    words: Any,
) -> bool:
    if not isinstance(actual, str) or not isinstance(words, list):
        return False
    if expected == "":
        return actual == ""
    if not all(isinstance(word, str) for word in words):
        return False

    characters = {character for word in words for character in word}
    if len(actual) != len(characters) or set(actual) != characters:
        return False
    position = {character: index for index, character in enumerate(actual)}
    for first, second in zip(words, words[1:]):
        if len(first) > len(second) and first.startswith(second):
            return False
        for left, right in zip(first, second):
            if left != right:
                if position[left] >= position[right]:
                    return False
                break
    return True


def _character_pair_rearrangement_match(
    actual: Any,
    original: Any,
    x: Any,
    y: Any,
) -> bool:
    if (
        not isinstance(actual, str)
        or not isinstance(original, str)
        or not isinstance(x, str)
        or len(x) != 1
        or not isinstance(y, str)
        or len(y) != 1
        or x == y
        or len(actual) != len(original)
        or Counter(actual) != Counter(original)
    ):
        return False

    first_x = actual.find(x)
    last_y = actual.rfind(y)
    return first_x == -1 or last_y == -1 or last_y < first_x


def _unordered_table_matches(actual: Any, expected: Any) -> bool:
    if not isinstance(actual, dict) or not isinstance(expected, dict):
        return False
    if actual.get("columns") != expected.get("columns"):
        return False
    return _unordered_list_matches(actual.get("rows"), expected.get("rows"))


def _unordered_nested_list_matches(actual: Any, expected: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(expected, list):
        return False

    def normalize(groups: list[Any]) -> list[str] | None:
        normalized: list[str] = []
        for group in groups:
            if not isinstance(group, list):
                return None
            ordered = sorted(group, key=lambda value: json.dumps(value, sort_keys=True))
            normalized.append(json.dumps(ordered, sort_keys=True))
        return sorted(normalized)

    return normalize(actual) == normalize(expected)


def _ordered_groups_unordered_items_match(actual: Any, expected: Any) -> bool:
    if (
        not isinstance(actual, list)
        or not isinstance(expected, list)
        or len(actual) != len(expected)
    ):
        return False

    return all(
        _unordered_list_matches(actual_group, expected_group)
        for actual_group, expected_group in zip(actual, expected, strict=True)
    )


def _ordered_results_unordered_lists_match(actual: Any, expected: Any) -> bool:
    """Preserve result positions while ignoring order within list-valued results."""

    if (
        not isinstance(actual, list)
        or not isinstance(expected, list)
        or len(actual) != len(expected)
    ):
        return False

    for actual_result, expected_result in zip(actual, expected, strict=True):
        if isinstance(expected_result, list):
            if not _unordered_list_matches(actual_result, expected_result):
                return False
        elif actual_result != expected_result:
            return False
    return True


def _duplicate_subtrees_match(actual: Any, expected: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(expected, list):
        return False
    serialized: list[list[Any]] = []
    for node in actual:
        if node is None or not all(hasattr(node, attribute) for attribute in ("val", "left", "right")):
            return False
        serialized.append(_tree_to_level_order(node))
    return _unordered_list_matches(serialized, expected)


def _beautiful_arrangement_ii_match(actual: Any, n: Any, k: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(n, int) or not isinstance(k, int):
        return False
    if len(actual) != n or any(isinstance(value, bool) or not isinstance(value, int) for value in actual):
        return False
    if set(actual) != set(range(1, n + 1)):
        return False
    return len({abs(left - right) for left, right in zip(actual, actual[1:])}) == k


def _beautiful_array_match(actual: Any, n: Any) -> bool:
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        return False
    if not isinstance(actual, list) or len(actual) != n:
        return False
    if any(not isinstance(value, int) or isinstance(value, bool) for value in actual):
        return False
    if sorted(actual) != list(range(1, n + 1)):
        return False

    position = [0] * (n + 1)
    for index, value in enumerate(actual):
        position[value] = index
    for first in range(1, n + 1):
        for second in range(first + 1, n + 1):
            if (first + second) % 2:
                continue
            midpoint = (first + second) // 2
            left = min(position[first], position[second])
            right = max(position[first], position[second])
            if left < position[midpoint] < right:
                return False
    return True


def _di_string_match(actual: Any, pattern: Any) -> bool:
    if not isinstance(pattern, str) or any(character not in {"I", "D"} for character in pattern):
        return False
    n = len(pattern)
    if not isinstance(actual, list) or len(actual) != n + 1:
        return False
    if any(not isinstance(value, int) or isinstance(value, bool) for value in actual):
        return False
    if sorted(actual) != list(range(n + 1)):
        return False
    return all(
        (left < right) if character == "I" else (left > right)
        for left, right, character in zip(actual[:-1], actual[1:], pattern, strict=True)
    )


def _shortest_superstring_match(actual: Any, expected: Any, words: Any) -> bool:
    if not isinstance(actual, str) or not isinstance(expected, str):
        return False
    if not isinstance(words, list) or any(not isinstance(word, str) for word in words):
        return False
    return len(actual) == len(expected) and all(word in actual for word in words)


def _shortest_common_supersequence_match(actual: Any, left: Any, right: Any) -> bool:
    if not isinstance(actual, str) or not isinstance(left, str) or not isinstance(right, str):
        return False

    def is_subsequence(candidate: str, container: str) -> bool:
        position = 0
        for character in container:
            if position < len(candidate) and candidate[position] == character:
                position += 1
        return position == len(candidate)

    previous = [0] * (len(right) + 1)
    for left_character in left:
        current = [0] * (len(right) + 1)
        for column, right_character in enumerate(right, start=1):
            if left_character == right_character:
                current[column] = previous[column - 1] + 1
            else:
                current[column] = max(previous[column], current[column - 1])
        previous = current

    minimum_length = len(left) + len(right) - previous[-1]
    return (
        len(actual) == minimum_length
        and is_subsequence(left, actual)
        and is_subsequence(right, actual)
    )


def _stamping_sequence_match(actual: Any, expected: Any, stamp: Any, target: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(expected, list):
        return False
    if not isinstance(stamp, str) or not isinstance(target, str) or not stamp or len(stamp) > len(target):
        return False
    if not actual:
        return not expected
    if len(actual) > 10 * len(target):
        return False
    if any(not isinstance(index, int) or isinstance(index, bool) for index in actual):
        return False

    built = ["?"] * len(target)
    for start in actual:
        if not 0 <= start <= len(target) - len(stamp):
            return False
        for offset, character in enumerate(stamp):
            built[start + offset] = character
    return "".join(built) == target


def _pancake_sort_match(actual: Any, values: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(values, list) or not values:
        return False
    if len(actual) > 10 * len(values):
        return False
    if any(not isinstance(length, int) or isinstance(length, bool) for length in actual):
        return False

    working = list(values)
    for length in actual:
        if not 1 <= length <= len(working):
            return False
        working[:length] = reversed(working[:length])
    return working == sorted(values)


def _string_without_triples_match(actual: Any, a: Any, b: Any) -> bool:
    if (
        not isinstance(actual, str)
        or not isinstance(a, int)
        or isinstance(a, bool)
        or not isinstance(b, int)
        or isinstance(b, bool)
        or a < 0
        or b < 0
    ):
        return False
    return (
        len(actual) == a + b
        and actual.count("a") == a
        and actual.count("b") == b
        and "aaa" not in actual
        and "bbb" not in actual
    )


def _reformatted_string_match(actual: Any, source: Any) -> bool:
    if not isinstance(actual, str) or not isinstance(source, str):
        return False
    digit_count = sum(character.isdigit() for character in source)
    letter_count = len(source) - digit_count
    if abs(digit_count - letter_count) > 1:
        return actual == ""
    return (
        len(actual) == len(source)
        and Counter(actual) == Counter(source)
        and all(left.isdigit() != right.isdigit() for left, right in zip(actual, actual[1:]))
    )


def _missing_binary_string_match(actual: Any, originals: Any) -> bool:
    if not isinstance(actual, str) or not isinstance(originals, list):
        return False
    expected_length = len(originals)
    return (
        len(actual) == expected_length
        and all(character in "01" for character in actual)
        and actual not in originals
    )


def _missing_rolls_match(
    actual: Any,
    observed: Any,
    mean: Any,
    missing_count: Any,
) -> bool:
    if (
        not isinstance(observed, list)
        or any(not isinstance(value, int) or isinstance(value, bool) for value in observed)
        or not isinstance(mean, int)
        or isinstance(mean, bool)
        or not isinstance(missing_count, int)
        or isinstance(missing_count, bool)
        or missing_count < 1
        or not isinstance(actual, list)
    ):
        return False

    required_sum = mean * (len(observed) + missing_count) - sum(observed)
    feasible = missing_count <= required_sum <= 6 * missing_count
    if not feasible:
        return actual == []

    return (
        len(actual) == missing_count
        and all(
            isinstance(value, int)
            and not isinstance(value, bool)
            and 1 <= value <= 6
            for value in actual
        )
        and sum(actual) == required_sum
    )


def _subset_sums_reconstruction_match(actual: Any, length: Any, originals: Any) -> bool:
    if (
        not isinstance(length, int)
        or isinstance(length, bool)
        or length < 0
        or not isinstance(actual, list)
        or len(actual) != length
        or any(not isinstance(value, int) or isinstance(value, bool) for value in actual)
        or not isinstance(originals, list)
        or any(not isinstance(value, int) or isinstance(value, bool) for value in originals)
    ):
        return False

    generated = [0]
    for value in actual:
        generated += [total + value for total in generated]
    return Counter(generated) == Counter(originals)


def _question_mark_replacement_match(actual: Any, source: Any) -> bool:
    if not isinstance(actual, str) or not isinstance(source, str) or len(actual) != len(source):
        return False
    return (
        all("a" <= character <= "z" for character in actual)
        and all(original == "?" or original == replacement for original, replacement in zip(source, actual))
        and all(left != right for left, right in zip(actual, actual[1:]))
    )


def _longest_happy_string_match(actual: Any, a: Any, b: Any, c: Any) -> bool:
    counts = (a, b, c)
    if (
        not isinstance(actual, str)
        or any(not isinstance(count, int) or isinstance(count, bool) or count < 0 for count in counts)
        or any(character not in "abc" for character in actual)
    ):
        return False

    total = sum(counts)
    largest = max(counts)
    nonmajority = total - largest
    optimal_length = min(total, 3 * nonmajority + 2)
    return (
        len(actual) == optimal_length
        and actual.count("a") <= a
        and actual.count("b") <= b
        and actual.count("c") <= c
        and "aaa" not in actual
        and "bbb" not in actual
        and "ccc" not in actual
    )


def _ordered_unordered_groups_match(actual: Any, expected: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(expected, list) or len(actual) != len(expected):
        return False
    return all(
        _unordered_list_matches(actual_group, expected_group)
        for actual_group, expected_group in zip(actual, expected, strict=True)
    )


def _circular_doubly_tree_match(actual: Any, expected: Any) -> bool:
    if not isinstance(expected, list):
        return False
    if not expected:
        return actual is None
    if actual is None or not all(hasattr(actual, attribute) for attribute in ("val", "left", "right")):
        return False

    current = actual
    previous = getattr(actual, "left", None)
    for value in expected:
        if current is None or getattr(current, "val", None) != value:
            return False
        if getattr(current, "left", None) is not previous:
            return False
        previous = current
        current = getattr(current, "right", None)

    return (
        current is actual
        and getattr(actual, "left", None) is previous
        and getattr(previous, "right", None) is actual
    )


def _circular_sorted_insertion_match(actual: Any, original: Any, insert_val: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(original, dict):
        return False
    orig_vals = original.get("values", [])
    pos = int(original.get("pos", 0))
    if len(actual) != len(orig_vals) + 1:
        return False
    if not orig_vals:
        return actual == [insert_val]

    def is_circular_sorted(arr: list[int]) -> bool:
        descents = 0
        n = len(arr)
        for i in range(n):
            if arr[i] > arr[(i + 1) % n]:
                descents += 1
        return descents <= 1

    if not is_circular_sorted(actual):
        return False

    orig_head = orig_vals[pos] if pos < len(orig_vals) else orig_vals[0]
    if actual[0] != orig_head and actual[0] != insert_val:
        return False

    orig_rotated = orig_vals[pos:] + orig_vals[:pos]
    for i in range(len(actual)):
        if actual[i] == insert_val:
            candidate = actual[:i] + actual[i + 1 :]
            if candidate[i % len(candidate):] + candidate[:i % len(candidate)] == orig_rotated:
                return True
            if candidate == orig_rotated:
                return True
    return False


def _quad_tree_match(actual: Any, expected: Any) -> bool:
    if not isinstance(expected, dict) or not isinstance(expected.get("leaf"), bool):
        return False
    if actual is None or not all(
        hasattr(actual, attribute)
        for attribute in ("val", "isLeaf", "topLeft", "topRight", "bottomLeft", "bottomRight")
    ):
        return False
    if bool(getattr(actual, "isLeaf")) != expected["leaf"]:
        return False
    if expected["leaf"]:
        return bool(getattr(actual, "val")) == bool(expected.get("value"))

    children = expected.get("children")
    if not isinstance(children, list) or len(children) != 4:
        return False
    return all(
        _quad_tree_match(getattr(actual, attribute), child)
        for attribute, child in zip(
            ("topLeft", "topRight", "bottomLeft", "bottomRight"),
            children,
            strict=True,
        )
    )


def _flattened_multilevel_list_match(actual: Any, expected: Any) -> bool:
    if not isinstance(expected, list):
        return False
    if not expected:
        return actual is None
    if actual is None or getattr(actual, "prev", None) is not None:
        return False

    current = actual
    previous = None
    for value in expected:
        if current is None or getattr(current, "val", None) != value:
            return False
        if getattr(current, "prev", None) is not previous or getattr(current, "child", None) is not None:
            return False
        previous = current
        current = getattr(current, "next", None)
    return current is None


def _all_one_trace_match(actual: Any, operations: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(operations, list):
        return False
    counts: dict[str, int] = {}
    result_index = 0
    for operation in operations:
        if not isinstance(operation, list) or not operation or not isinstance(operation[0], str):
            return False
        name = operation[0]
        if name == "inc" and len(operation) == 2 and isinstance(operation[1], str):
            key = operation[1]
            counts[key] = counts.get(key, 0) + 1
        elif name == "dec" and len(operation) == 2 and isinstance(operation[1], str):
            key = operation[1]
            if key not in counts:
                return False
            counts[key] -= 1
            if counts[key] == 0:
                del counts[key]
        elif name in {"getMaxKey", "getMinKey"} and len(operation) == 1:
            if result_index >= len(actual) or not isinstance(actual[result_index], str):
                return False
            returned = actual[result_index]
            result_index += 1
            if not counts:
                if returned != "":
                    return False
                continue
            target = (max if name == "getMaxKey" else min)(counts.values())
            if returned not in counts or counts[returned] != target:
                return False
        else:
            return False
    return result_index == len(actual)


def _largest_divisible_subset_match(actual: Any, expected: Any, values: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(expected, list) or not isinstance(values, list):
        return False
    if len(actual) != len(expected) or Counter(actual) - Counter(values):
        return False
    if any(not isinstance(value, int) or isinstance(value, bool) or value <= 0 for value in actual):
        return False
    return all(
        left % right == 0 or right % left == 0
        for index, left in enumerate(actual)
        for right in actual[index + 1 :]
    )


def _k_smallest_pairs_match(actual: Any, nums1: Any, nums2: Any, k: Any) -> bool:
    if (
        not isinstance(actual, list)
        or not isinstance(nums1, list)
        or not isinstance(nums2, list)
        or not isinstance(k, int)
        or isinstance(k, bool)
        or k < 0
    ):
        return False
    required = min(k, len(nums1) * len(nums2))
    if len(actual) != required:
        return False
    if required == 0:
        return True

    normalized: list[tuple[int, int]] = []
    for pair in actual:
        if (
            not isinstance(pair, (list, tuple))
            or len(pair) != 2
            or any(not isinstance(value, int) or isinstance(value, bool) for value in pair)
        ):
            return False
        normalized.append((pair[0], pair[1]))

    left_counts = Counter(nums1)
    right_counts = Counter(nums2)
    used = Counter(normalized)
    if any(count > left_counts[left] * right_counts[right] for (left, right), count in used.items()):
        return False

    def count_at_most(limit: int) -> int:
        right_index = len(nums2) - 1
        total = 0
        for left in nums1:
            while right_index >= 0 and left + nums2[right_index] > limit:
                right_index -= 1
            total += right_index + 1
        return total

    low = nums1[0] + nums2[0]
    high = nums1[-1] + nums2[-1]
    while low < high:
        middle = (low + high) // 2
        if count_at_most(middle) >= required:
            high = middle
        else:
            low = middle + 1
    return all(left + right <= low for left, right in normalized)


def _phone_directory_trace_match(actual: Any, max_numbers: Any, operations: Any) -> bool:
    if (
        not isinstance(actual, list)
        or not isinstance(max_numbers, int)
        or isinstance(max_numbers, bool)
        or max_numbers < 0
        or not isinstance(operations, list)
    ):
        return False
    available = set(range(max_numbers))
    output_index = 0
    for operation in operations:
        if not isinstance(operation, list) or not operation or not isinstance(operation[0], str):
            return False
        name = operation[0]
        if name == "get":
            if output_index >= len(actual):
                return False
            value = actual[output_index]
            output_index += 1
            if available:
                if not isinstance(value, int) or isinstance(value, bool) or value not in available:
                    return False
                available.remove(value)
            elif value != -1:
                return False
        elif name == "check":
            if len(operation) != 2 or output_index >= len(actual):
                return False
            value = actual[output_index]
            output_index += 1
            if not isinstance(value, bool) or value != (operation[1] in available):
                return False
        elif name == "release":
            if len(operation) != 2 or not isinstance(operation[1], int) or not 0 <= operation[1] < max_numbers:
                return False
            available.add(operation[1])
        else:
            return False
    return output_index == len(actual)


def _randomized_set_trace_match(actual: Any, operations: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(operations, list) or len(actual) != len(operations):
        return False
    values: set[int] = set()
    for result, operation in zip(actual, operations, strict=True):
        if not isinstance(operation, list) or not operation or not isinstance(operation[0], str):
            return False
        name = operation[0]
        if name == "insert":
            if len(operation) != 2 or not isinstance(result, bool):
                return False
            value = operation[1]
            expected = value not in values
            if result != expected:
                return False
            values.add(value)
        elif name == "remove":
            if len(operation) != 2 or not isinstance(result, bool):
                return False
            value = operation[1]
            expected = value in values
            if result != expected:
                return False
            values.discard(value)
        elif name == "getRandom":
            if len(operation) != 1 or not values or result not in values:
                return False
        else:
            return False
    return True


def _randomized_collection_trace_match(actual: Any, operations: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(operations, list) or len(actual) != len(operations):
        return False
    counts: Counter[int] = Counter()
    for result, operation in zip(actual, operations, strict=True):
        if not isinstance(operation, list) or not operation or not isinstance(operation[0], str):
            return False
        name = operation[0]
        if name == "insert":
            if len(operation) != 2 or not isinstance(result, bool):
                return False
            value = operation[1]
            expected = counts[value] == 0
            if result != expected:
                return False
            counts[value] += 1
        elif name == "remove":
            if len(operation) != 2 or not isinstance(result, bool):
                return False
            value = operation[1]
            expected = counts[value] > 0
            if result != expected:
                return False
            if expected:
                counts[value] -= 1
                if counts[value] == 0:
                    del counts[value]
        elif name == "getRandom":
            if len(operation) != 1 or not counts or counts[result] <= 0:
                return False
        else:
            return False
    return True


def _linked_list_random_draws_match(actual: Any, head: Any, draws: Any) -> bool:
    if (
        not isinstance(actual, list)
        or not isinstance(head, list)
        or not head
        or isinstance(draws, bool)
        or not isinstance(draws, int)
        or draws < 0
        or len(actual) != draws
    ):
        return False
    values = set(head)
    return all(value in values for value in actual)


def _shuffle_array_trace_match(actual: Any, nums: Any, operations: Any) -> bool:
    if (
        not isinstance(actual, list)
        or not isinstance(nums, list)
        or not isinstance(operations, list)
        or len(actual) != len(operations)
    ):
        return False
    expected_counts = Counter(nums)
    for result, operation in zip(actual, operations, strict=True):
        if not isinstance(result, list):
            return False
        if operation == "reset":
            if result != nums:
                return False
        elif operation == "shuffle":
            if Counter(result) != expected_counts:
                return False
        else:
            return False
    return True


def _random_flip_matrix_trace_match(actual: Any, rows: Any, cols: Any, operations: Any) -> bool:
    if (
        not isinstance(rows, int)
        or isinstance(rows, bool)
        or rows <= 0
        or not isinstance(cols, int)
        or isinstance(cols, bool)
        or cols <= 0
        or not isinstance(operations, list)
        or not isinstance(actual, list)
        or len(actual) != len(operations)
    ):
        return False

    flipped: set[tuple[int, int]] = set()
    for operation, result in zip(operations, actual):
        if operation == "reset":
            if result is not None:
                return False
            flipped.clear()
            continue
        if operation != "flip" or not isinstance(result, (list, tuple)) or len(result) != 2:
            return False
        row, col = result
        if (
            not isinstance(row, int)
            or isinstance(row, bool)
            or not isinstance(col, int)
            or isinstance(col, bool)
            or not 0 <= row < rows
            or not 0 <= col < cols
            or (row, col) in flipped
        ):
            return False
        flipped.add((row, col))
    return True


def _random_pick_indices_match(actual: Any, nums: Any, targets: Any) -> bool:
    if (
        not isinstance(actual, list)
        or not isinstance(nums, list)
        or not isinstance(targets, list)
        or len(actual) != len(targets)
    ):
        return False
    for index, target in zip(actual, targets, strict=True):
        if (
            isinstance(index, bool)
            or not isinstance(index, int)
            or not 0 <= index < len(nums)
            or nums[index] != target
        ):
            return False
    return True


def _queue_reconstruction_match(actual: Any, people: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(people, list) or len(actual) != len(people):
        return False
    try:
        actual_pairs = [tuple(person) for person in actual]
        input_pairs = [tuple(person) for person in people]
    except TypeError:
        return False
    if any(
        len(person) != 2
        or isinstance(person[0], bool)
        or not isinstance(person[0], int)
        or isinstance(person[1], bool)
        or not isinstance(person[1], int)
        for person in actual_pairs + input_pairs
    ):
        return False
    if Counter(actual_pairs) != Counter(input_pairs):
        return False
    return all(
        sum(1 for previous_height, _ in actual_pairs[:index] if previous_height >= height) == count
        for index, (height, count) in enumerate(actual_pairs)
    )


def _abbreviation_matches_word(abbreviation: Any, word: Any) -> tuple[bool, int]:
    if not isinstance(abbreviation, str) or not isinstance(word, str):
        return False, 0
    word_index = 0
    abbr_index = 0
    token_count = 0
    while abbr_index < len(abbreviation):
        token_count += 1
        character = abbreviation[abbr_index]
        if character.isdigit():
            if character == "0":
                return False, token_count
            skipped = 0
            while abbr_index < len(abbreviation) and abbreviation[abbr_index].isdigit():
                skipped = skipped * 10 + int(abbreviation[abbr_index])
                abbr_index += 1
            word_index += skipped
            if word_index > len(word):
                return False, token_count
        else:
            if word_index >= len(word) or word[word_index] != character:
                return False, token_count
            word_index += 1
            abbr_index += 1
    return word_index == len(word), token_count


def _minimum_unique_abbreviation_match(
    actual: Any,
    expected: Any,
    target: Any,
    dictionary: Any,
) -> bool:
    valid, actual_length = _abbreviation_matches_word(actual, target)
    expected_valid, expected_length = _abbreviation_matches_word(expected, target)
    if not valid or not expected_valid or not isinstance(dictionary, list):
        return False
    if any(
        len(word) == len(target) and _abbreviation_matches_word(actual, word)[0]
        for word in dictionary
        if isinstance(word, str)
    ):
        return False
    return actual_length == expected_length


def _anagram_groups_match(actual: Any, expected: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(expected, list):
        return False

    def normalize(groups: list[Any]) -> list[tuple[str, ...]] | None:
        normalized: list[tuple[str, ...]] = []
        for group in groups:
            if not isinstance(group, list) or not all(isinstance(word, str) for word in group):
                return None
            normalized.append(tuple(sorted(group)))
        return sorted(normalized)

    return normalize(actual) == normalize(expected)


def _accounts_merge_match(actual: Any, expected: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(expected, list):
        return False

    def normalize(accounts: list[Any]) -> list[tuple[str, tuple[str, ...]]] | None:
        normalized: list[tuple[str, tuple[str, ...]]] = []
        for account in accounts:
            if (
                not isinstance(account, list)
                or len(account) < 2
                or not all(isinstance(value, str) for value in account)
            ):
                return None
            emails = account[1:]
            if emails != sorted(emails) or len(emails) != len(set(emails)):
                return None
            normalized.append((account[0], tuple(emails)))
        return sorted(normalized)

    return normalize(actual) == normalize(expected)


def _frequency_sorted_string_match(actual: Any, original: Any) -> bool:
    if not isinstance(actual, str) or not isinstance(original, str):
        return False
    frequencies = Counter(original)
    if Counter(actual) != frequencies:
        return False
    return all(
        frequencies[actual[index - 1]] >= frequencies[actual[index]]
        for index in range(1, len(actual))
    )


def _custom_sorted_string_match(actual: Any, order: Any, original: Any) -> bool:
    if not isinstance(actual, str) or not isinstance(order, str) or not isinstance(original, str):
        return False
    if Counter(actual) != Counter(original):
        return False
    ranks = {character: index for index, character in enumerate(order)}
    ordered_ranks = [ranks[character] for character in actual if character in ranks]
    return all(
        ordered_ranks[index - 1] <= ordered_ranks[index]
        for index in range(1, len(ordered_ranks))
    )


def _gray_code_match(actual: Any, bits: Any) -> bool:
    if not isinstance(bits, int) or bits < 1 or not isinstance(actual, list):
        return False
    size = 1 << bits
    if (
        len(actual) != size
        or actual[0] != 0
        or any(not isinstance(value, int) or not 0 <= value < size for value in actual)
        or len(set(actual)) != size
    ):
        return False

    for left, right in zip(actual, actual[1:] + actual[:1]):
        difference = left ^ right
        if difference == 0 or difference & (difference - 1):
            return False
    return True


def _circular_gray_code_match(actual: Any, bits: Any, start: Any) -> bool:
    if (
        not isinstance(bits, int)
        or bits < 1
        or not isinstance(start, int)
        or isinstance(start, bool)
        or not isinstance(actual, list)
    ):
        return False
    size = 1 << bits
    if (
        not 0 <= start < size
        or len(actual) != size
        or actual[0] != start
        or any(not isinstance(value, int) or not 0 <= value < size for value in actual)
        or len(set(actual)) != size
    ):
        return False

    for left, right in zip(actual, actual[1:] + actual[:1]):
        difference = left ^ right
        if difference == 0 or difference & (difference - 1):
            return False
    return True


def _advantage_shuffle_match(actual: Any, nums1: Any, nums2: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(nums1, list) or not isinstance(nums2, list):
        return False
    if len(actual) != len(nums1) or len(nums1) != len(nums2):
        return False
    if any(not isinstance(value, int) or isinstance(value, bool) for value in actual):
        return False
    if Counter(actual) != Counter(nums1):
        return False

    sorted_targets = sorted(nums2)
    matched_targets = 0
    for value in sorted(nums1):
        if matched_targets < len(sorted_targets) and value > sorted_targets[matched_targets]:
            matched_targets += 1

    actual_advantage = sum(
        value > target for value, target in zip(actual, nums2)
    )
    return actual_advantage == matched_targets


def _parity_partition_match(actual: Any, original: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(original, list):
        return False
    if any(
        not isinstance(value, int) or isinstance(value, bool)
        for value in actual + original
    ):
        return False
    if Counter(actual) != Counter(original):
        return False

    seen_odd = False
    for value in actual:
        if value % 2:
            seen_odd = True
        elif seen_odd:
            return False
    return True


def _indexed_parity_match(actual: Any, original: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(original, list):
        return False
    if any(
        not isinstance(value, int) or isinstance(value, bool)
        for value in actual + original
    ):
        return False
    if Counter(actual) != Counter(original):
        return False
    return all(value % 2 == index % 2 for index, value in enumerate(actual))


def _three_equal_binary_parts_match(actual: Any, arr: Any) -> bool:
    if not isinstance(actual, (list, tuple)) or len(actual) != 2:
        return False
    if not isinstance(arr, list) or len(arr) < 3:
        return False
    if any(not isinstance(value, int) or isinstance(value, bool) for value in actual):
        return False
    if any(not isinstance(bit, int) or isinstance(bit, bool) or bit not in (0, 1) for bit in arr):
        return False

    left_end, right_start = actual
    if [left_end, right_start] == [-1, -1]:
        total_ones = sum(arr)
        if total_ones == 0:
            return False
        if total_ones % 3:
            return True
        ones_per_part = total_ones // 3
        one_positions = [index for index, bit in enumerate(arr) if bit]
        first = one_positions[0]
        second = one_positions[ones_per_part]
        third = one_positions[2 * ones_per_part]
        significant_length = len(arr) - third
        exists = (
            first + significant_length <= second
            and second + significant_length <= third
            and arr[first : first + significant_length]
            == arr[second : second + significant_length]
            == arr[third:]
        )
        return not exists

    if not (0 <= left_end and left_end + 1 < right_start < len(arr)):
        return False

    def normalized(part: list[int]) -> list[int]:
        first_one = next((index for index, bit in enumerate(part) if bit), len(part))
        return part[first_one:]

    first_part = normalized(arr[: left_end + 1])
    second_part = normalized(arr[left_end + 1 : right_start])
    third_part = normalized(arr[right_start:])
    return first_part == second_part == third_part


def _three_equal_parts_match(actual: Any, expected: Any, bits: Any) -> bool:
    if (
        not isinstance(actual, (list, tuple))
        or len(actual) != 2
        or not isinstance(bits, list)
    ):
        return False
    if any(not isinstance(index, int) or isinstance(index, bool) for index in actual):
        return False
    if any(bit not in (0, 1) or isinstance(bit, bool) for bit in bits):
        return False

    first_end, third_start = actual
    if first_end == -1 and third_start == -1:
        return expected == [-1, -1]
    if not (0 <= first_end and first_end + 1 < third_start < len(bits)):
        return False

    def significant_part(start: int, end: int) -> list[int]:
        while start < end and bits[start] == 0:
            start += 1
        return bits[start:end]

    first = significant_part(0, first_end + 1)
    second = significant_part(first_end + 1, third_start)
    third = significant_part(third_start, len(bits))
    return first == second == third


def _fair_candy_swap_match(actual: Any, alice_sizes: Any, bob_sizes: Any) -> bool:
    if (
        not isinstance(actual, (list, tuple))
        or len(actual) != 2
        or not isinstance(alice_sizes, list)
        or not isinstance(bob_sizes, list)
    ):
        return False
    alice_box, bob_box = actual
    if any(
        not isinstance(value, int) or isinstance(value, bool)
        for value in (alice_box, bob_box)
    ):
        return False
    if alice_box not in alice_sizes or bob_box not in bob_sizes:
        return False
    return (
        sum(alice_sizes) - alice_box + bob_box
        == sum(bob_sizes) - bob_box + alice_box
    )


def _de_bruijn_sequence_match(actual: Any, n: Any, k: Any) -> bool:
    if (
        not isinstance(actual, str)
        or not isinstance(n, int)
        or isinstance(n, bool)
        or not isinstance(k, int)
        or isinstance(k, bool)
        or n < 1
        or not 1 <= k <= 10
    ):
        return False

    combination_count = k**n
    if len(actual) != combination_count + n - 1:
        return False

    alphabet = {str(digit) for digit in range(k)}
    if any(character not in alphabet for character in actual):
        return False

    windows = {actual[index : index + n] for index in range(combination_count)}
    return len(windows) == combination_count


def _sudoku_solution_match(actual: Any, clues: Any) -> bool:
    digits = set("123456789")
    if (
        not isinstance(actual, list)
        or not isinstance(clues, list)
        or len(actual) != 9
        or len(clues) != 9
    ):
        return False
    if any(not isinstance(row, list) or len(row) != 9 for row in actual):
        return False
    if any(not isinstance(row, list) or len(row) != 9 for row in clues):
        return False
    if any(value not in digits for row in actual for value in row):
        return False
    for row in range(9):
        for column in range(9):
            clue = clues[row][column]
            if clue != "." and actual[row][column] != clue:
                return False
    if any(set(row) != digits for row in actual):
        return False
    if any({actual[row][column] for row in range(9)} != digits for column in range(9)):
        return False
    for box_row in range(0, 9, 3):
        for box_column in range(0, 9, 3):
            if {
                actual[row][column]
                for row in range(box_row, box_row + 3)
                for column in range(box_column, box_column + 3)
            } != digits:
                return False
    return True


def _distance_order_cells_match(actual: Any, rows: Any, cols: Any, r_center: Any, c_center: Any) -> bool:
    if not all(isinstance(value, int) for value in (rows, cols, r_center, c_center)):
        return False
    if not isinstance(actual, list) or len(actual) != rows * cols:
        return False

    seen: set[tuple[int, int]] = set()
    previous_distance = -1
    for cell in actual:
        if (
            not isinstance(cell, (list, tuple))
            or len(cell) != 2
            or not isinstance(cell[0], int)
            or not isinstance(cell[1], int)
        ):
            return False
        row, col = cell
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False
        point = (row, col)
        if point in seen:
            return False
        seen.add(point)
        distance = abs(row - r_center) + abs(col - c_center)
        if distance < previous_distance:
            return False
        previous_distance = distance
    return True


def _balanced_factor_decomposition_match(
    actual: Any,
    expected: Any,
    n: Any,
    k: Any,
) -> bool:
    if (
        not isinstance(actual, list)
        or not isinstance(expected, list)
        or not isinstance(n, int)
        or isinstance(n, bool)
        or not isinstance(k, int)
        or isinstance(k, bool)
        or len(actual) != k
        or not expected
    ):
        return False
    if any(not isinstance(value, int) or isinstance(value, bool) or value <= 0 for value in actual):
        return False
    return (
        math.prod(actual) == n
        and max(actual) - min(actual) == max(expected) - min(expected)
    )


def _absolute_value_sorted_match(actual: Any, original: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(original, list):
        return False
    if any(not isinstance(value, int) or isinstance(value, bool) for value in actual):
        return False
    return Counter(actual) == Counter(original) and all(
        abs(actual[index - 1]) <= abs(actual[index])
        for index in range(1, len(actual))
    )


def _wiggle_sort_matches(actual: Any, original: Any, *, strict: bool = True) -> bool:
    if not isinstance(actual, list) or not isinstance(original, list):
        return False
    if sorted(actual) != sorted(original):
        return False
    for index in range(1, len(actual)):
        if index % 2 == 1:
            if actual[index - 1] > actual[index] or (strict and actual[index - 1] == actual[index]):
                return False
        elif actual[index - 1] < actual[index] or (strict and actual[index - 1] == actual[index]):
            return False
    return True


def _not_average_neighbors_match(actual: Any, original: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(original, list):
        return False
    if Counter(actual) != Counter(original):
        return False
    return all(
        2 * actual[index] != actual[index - 1] + actual[index + 1]
        for index in range(1, len(actual) - 1)
    )


def _distant_barcodes_match(actual: Any, original: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(original, list):
        return False
    if Counter(actual) != Counter(original):
        return False
    return all(actual[index] != actual[index - 1] for index in range(1, len(actual)))


def _maximum_bob_points_match(
    actual: Any,
    expected: Any,
    num_arrows: Any,
    alice_arrows: Any,
) -> bool:
    if (
        not isinstance(actual, list)
        or len(actual) != 12
        or not isinstance(expected, int)
        or isinstance(expected, bool)
        or not isinstance(num_arrows, int)
        or isinstance(num_arrows, bool)
        or not isinstance(alice_arrows, list)
        or len(alice_arrows) != 12
    ):
        return False
    if any(not isinstance(value, int) or isinstance(value, bool) or value < 0 for value in actual):
        return False
    if sum(actual) != num_arrows:
        return False
    score = sum(
        section
        for section in range(12)
        if actual[section] > alice_arrows[section]
    )
    return score == expected


def _rearranged_k_distance_match(actual: Any, expected: Any, original: Any, distance: Any) -> bool:
    if (
        not isinstance(actual, str)
        or not isinstance(expected, str)
        or not isinstance(original, str)
        or not isinstance(distance, int)
        or isinstance(distance, bool)
        or distance < 0
    ):
        return False
    if not actual:
        return expected == ""
    if Counter(actual) != Counter(original):
        return False

    last_position: dict[str, int] = {}
    for index, character in enumerate(actual):
        previous = last_position.get(character)
        if previous is not None and index - previous < distance:
            return False
        last_position[character] = index
    return True


def _reconstruct_two_row_matrix_match(actual: Any, upper: Any, lower: Any, colsum: Any, expected: Any) -> bool:
    if expected == []:
        return actual == []
    if not isinstance(actual, list) or len(actual) != 2:
        return False
    if not all(isinstance(row, list) and len(row) == len(colsum) for row in actual):
        return False
    if not all(value in {0, 1} for row in actual for value in row):
        return False
    return (
        sum(actual[0]) == upper
        and sum(actual[1]) == lower
        and [actual[0][index] + actual[1][index] for index in range(len(colsum))] == colsum
    )


def _matrix_margins_match(actual: Any, row_sums: Any, column_sums: Any) -> bool:
    if not isinstance(row_sums, list) or not isinstance(column_sums, list):
        return False
    if not isinstance(actual, list) or len(actual) != len(row_sums):
        return False
    if not all(isinstance(row, list) and len(row) == len(column_sums) for row in actual):
        return False
    if not all(
        isinstance(value, int) and not isinstance(value, bool) and value >= 0
        for row in actual
        for value in row
    ):
        return False
    return (
        [sum(row) for row in actual] == row_sums
        and [sum(actual[row][column] for row in range(len(row_sums))) for column in range(len(column_sums))]
        == column_sums
    )


def _grid_layout_match(actual: Any, n: Any, edges: Any) -> bool:
    """Accept any rectangular placement whose grid adjacencies equal the graph."""

    if type(n) is not int or n < 1 or not isinstance(edges, list):
        return False
    graph_edges: set[tuple[int, int]] = set()
    for edge in edges:
        if (
            not isinstance(edge, list)
            or len(edge) != 2
            or any(type(node) is not int or not 0 <= node < n for node in edge)
            or edge[0] == edge[1]
        ):
            return False
        graph_edges.add(tuple(sorted(edge)))

    if not isinstance(actual, list) or not actual or not isinstance(actual[0], list) or not actual[0]:
        return False
    columns = len(actual[0])
    if any(not isinstance(row, list) or len(row) != columns for row in actual):
        return False

    values = [node for row in actual for node in row]
    if (
        len(values) != n
        or any(type(node) is not int or not 0 <= node < n for node in values)
        or set(values) != set(range(n))
    ):
        return False

    layout_edges: set[tuple[int, int]] = set()
    for row_index, row in enumerate(actual):
        for column_index, node in enumerate(row):
            if row_index + 1 < len(actual):
                layout_edges.add(tuple(sorted((node, actual[row_index + 1][column_index]))))
            if column_index + 1 < columns:
                layout_edges.add(tuple(sorted((node, row[column_index + 1]))))
    return layout_edges == graph_edges


def _last_marked_nodes_match(actual: Any, edges: Any) -> bool:
    """Accept any farthest vertex for every possible starting vertex."""

    if not isinstance(edges, list):
        return False
    n = len(edges) + 1
    if (
        not isinstance(actual, list)
        or len(actual) != n
        or any(type(node) is not int or not 0 <= node < n for node in actual)
    ):
        return False

    graph: list[list[int]] = [[] for _ in range(n)]
    for edge in edges:
        if (
            not isinstance(edge, list)
            or len(edge) != 2
            or any(type(node) is not int or not 0 <= node < n for node in edge)
            or edge[0] == edge[1]
        ):
            return False
        left, right = edge
        graph[left].append(right)
        graph[right].append(left)

    def distances(start: int) -> tuple[int, list[int]]:
        dist = [-1] * n
        dist[start] = 0
        queue = deque([start])
        farthest = start
        while queue:
            node = queue.popleft()
            if dist[node] > dist[farthest]:
                farthest = node
            for neighbor in graph[node]:
                if dist[neighbor] == -1:
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)
        return farthest, dist

    endpoint_a, connected = distances(0)
    if any(distance == -1 for distance in connected):
        return False
    endpoint_b, dist_a = distances(endpoint_a)
    _, dist_b = distances(endpoint_b)

    depth = [-1] * n
    parent = [-1] * n
    depth[0] = 0
    queue = deque([0])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor == parent[node]:
                continue
            if depth[neighbor] != -1:
                return False
            parent[neighbor] = node
            depth[neighbor] = depth[node] + 1
            queue.append(neighbor)

    ancestors = [parent]
    for _ in range(1, n.bit_length()):
        previous = ancestors[-1]
        ancestors.append([
            -1 if previous[node] == -1 else previous[previous[node]]
            for node in range(n)
        ])

    def distance(left: int, right: int) -> int:
        original_left, original_right = left, right
        if depth[left] < depth[right]:
            left, right = right, left
        difference = depth[left] - depth[right]
        for level in range(difference.bit_length()):
            if difference >> level & 1:
                left = ancestors[level][left]
        if left != right:
            for level in range(len(ancestors) - 1, -1, -1):
                if ancestors[level][left] != ancestors[level][right]:
                    left = ancestors[level][left]
                    right = ancestors[level][right]
            left = parent[left]
        lca = left
        return depth[original_left] + depth[original_right] - 2 * depth[lca]

    return all(
        distance(start, chosen) == max(dist_a[start], dist_b[start])
        for start, chosen in enumerate(actual)
    )


def _condition_matrix_match(
    actual: Any,
    k: Any,
    row_conditions: Any,
    column_conditions: Any,
) -> bool:
    if (
        type(k) is not int
        or k < 1
        or not isinstance(row_conditions, list)
        or not isinstance(column_conditions, list)
    ):
        return False

    def has_topological_order(conditions: list[Any]) -> bool:
        adjacency = [[] for _ in range(k + 1)]
        indegree = [0] * (k + 1)
        for condition in conditions:
            if (
                not isinstance(condition, list)
                or len(condition) != 2
                or any(type(value) is not int or not 1 <= value <= k for value in condition)
            ):
                return False
            before, after = condition
            adjacency[before].append(after)
            indegree[after] += 1
        queue = [value for value in range(1, k + 1) if indegree[value] == 0]
        processed = 0
        for value in queue:
            processed += 1
            for neighbor in adjacency[value]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return processed == k

    possible = has_topological_order(row_conditions) and has_topological_order(column_conditions)
    if actual == []:
        return not possible
    if not possible or not isinstance(actual, list) or len(actual) != k:
        return False
    if any(not isinstance(row, list) or len(row) != k for row in actual):
        return False

    positions: dict[int, tuple[int, int]] = {}
    for row_index, row in enumerate(actual):
        for column_index, value in enumerate(row):
            if type(value) is not int or not 0 <= value <= k:
                return False
            if value:
                if value in positions:
                    return False
                positions[value] = (row_index, column_index)
    if set(positions) != set(range(1, k + 1)):
        return False
    return all(
        positions[before][0] < positions[after][0]
        for before, after in row_conditions
    ) and all(
        positions[left][1] < positions[right][1]
        for left, right in column_conditions
    )


def _group_people_match(actual: Any, group_sizes: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(group_sizes, list):
        return False
    seen: set[int] = set()
    for group in actual:
        if not isinstance(group, list) or not group:
            return False
        size = len(group)
        for index in group:
            if not isinstance(index, int) or index < 0 or index >= len(group_sizes) or index in seen:
                return False
            if group_sizes[index] != size:
                return False
            seen.add(index)
    return seen == set(range(len(group_sizes)))


def _unique_sum_zero_match(actual: Any, n: Any) -> bool:
    return (
        isinstance(n, int)
        and isinstance(actual, list)
        and len(actual) == n
        and all(isinstance(value, int) and not isinstance(value, bool) for value in actual)
        and len(set(actual)) == n
        and sum(actual) == 0
    )


def _no_zero_sum_match(actual: Any, n: Any) -> bool:
    return (
        isinstance(n, int)
        and isinstance(actual, list)
        and len(actual) == 2
        and all(
            isinstance(value, int)
            and not isinstance(value, bool)
            and value > 0
            and "0" not in str(value)
            for value in actual
        )
        and sum(actual) == n
    )


def _color_red_triangle_match(actual: Any, n: Any) -> bool:
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        return False
    if not isinstance(actual, list):
        return False

    minimum_size = 1
    for row in range(2, n + 1):
        offset = (n - row) % 4
        start = offset % 3 + 1
        if offset % 2:
            minimum_size += 1
        else:
            minimum_size += len(range(start, 2 * row, 2))

    red: set[tuple[int, int]] = set()
    for coordinate in actual:
        if (
            not isinstance(coordinate, list)
            or len(coordinate) != 2
            or not all(isinstance(value, int) and not isinstance(value, bool) for value in coordinate)
        ):
            return False
        row, column = coordinate
        if row < 1 or row > n or column < 1 or column > 2 * row - 1:
            return False
        red.add((row, column))

    if len(red) != minimum_size or len(actual) != minimum_size:
        return False

    neighbors: dict[tuple[int, int], list[tuple[int, int]]] = {}
    for row in range(1, n + 1):
        for column in range(1, 2 * row):
            adjacent: list[tuple[int, int]] = []
            if column > 1:
                adjacent.append((row, column - 1))
            if column < 2 * row - 1:
                adjacent.append((row, column + 1))
            if column % 2 == 1 and row < n:
                adjacent.append((row + 1, column + 1))
            elif column % 2 == 0:
                adjacent.append((row - 1, column - 1))
            neighbors[(row, column)] = adjacent

    red_neighbor_count: dict[tuple[int, int], int] = {}
    ready: deque[tuple[int, int]] = deque()
    for coordinate, adjacent in neighbors.items():
        if coordinate in red:
            continue
        count = sum(neighbor in red for neighbor in adjacent)
        red_neighbor_count[coordinate] = count
        if count >= 2:
            ready.append(coordinate)

    while ready:
        coordinate = ready.popleft()
        if coordinate in red or red_neighbor_count[coordinate] < 2:
            continue
        red.add(coordinate)
        for neighbor in neighbors[coordinate]:
            if neighbor not in red:
                red_neighbor_count[neighbor] += 1
                if red_neighbor_count[neighbor] == 2:
                    ready.append(neighbor)

    return len(red) == n * n


def _sufficient_team_match(actual: Any, expected: Any, req_skills: Any, people: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(expected, list):
        return False
    if not isinstance(req_skills, list) or not isinstance(people, list):
        return False
    if len(actual) > len(expected) or len(actual) != len(set(actual)):
        return False
    covered: set[Any] = set()
    for index in actual:
        if not isinstance(index, int) or index < 0 or index >= len(people):
            return False
        skills = people[index]
        if not isinstance(skills, list):
            return False
        covered.update(skills)
    return set(req_skills).issubset(covered)


def _vps_split_match(actual: Any, sequence: Any) -> bool:
    if not isinstance(sequence, str) or not isinstance(actual, list) or len(actual) != len(sequence):
        return False
    if not all(isinstance(group, int) and not isinstance(group, bool) and group in {0, 1} for group in actual):
        return False

    balances = [0, 0]
    group_depths = [0, 0]
    original_depth = 0
    depth = 0
    for character, group in zip(sequence, actual):
        if character == "(":
            depth += 1
            original_depth = max(original_depth, depth)
            balances[group] += 1
            group_depths[group] = max(group_depths[group], balances[group])
        elif character == ")":
            depth -= 1
            balances[group] -= 1
            if depth < 0 or balances[group] < 0:
                return False
        else:
            return False

    return (
        depth == 0
        and balances == [0, 0]
        and max(group_depths) == (original_depth + 1) // 2
    )


def _forest_roots_match(actual: Any, expected: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(expected, list):
        return False
    normalized = [_tree_to_level_order(root) for root in actual]
    return _unordered_list_matches(normalized, expected)


def _unique_bsts_match(actual: Any, n: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(n, int) or isinstance(n, bool) or n < 1:
        return False
    expected_count = math.comb(2 * n, n) // (n + 1)
    if len(actual) != expected_count:
        return False

    structures: set[str] = set()
    expected_inorder = list(range(1, n + 1))
    for root in actual:
        level_order = _tree_to_level_order(root)
        if not isinstance(level_order, list) or _tree_inorder_values(root) != expected_inorder:
            return False
        structures.add(json.dumps(level_order, separators=(",", ":")))
    return len(structures) == expected_count


def _next_right_pointers_match(actual: Any, original: Any) -> bool:
    if actual is None:
        return original == [] or original is None
    if _tree_to_level_order(actual) != _tree_to_level_order(original):
        return False

    level = [actual]
    while level:
        next_level: list[Any] = []
        for index, node in enumerate(level):
            expected_next = level[index + 1] if index + 1 < len(level) else None
            if getattr(node, "next", None) is not expected_next:
                return False
            left = getattr(node, "left", None)
            right = getattr(node, "right", None)
            if left is not None:
                next_level.append(left)
            if right is not None:
                next_level.append(right)
        level = next_level
    return True


def _float_close_match(actual: Any, expected: Any, tolerance: Any) -> bool:
    if isinstance(actual, bool) or isinstance(expected, bool):
        return False
    if not isinstance(actual, (int, float)) or not isinstance(expected, (int, float)):
        return False
    try:
        allowed = float(tolerance)
    except (TypeError, ValueError):
        allowed = 1e-5
    return abs(float(actual) - float(expected)) <= max(0.0, allowed)


def _float_list_close_match(actual: Any, expected: Any, tolerance: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(expected, list) or len(actual) != len(expected):
        return False
    return all(
        _float_close_match(actual_value, expected_value, tolerance)
        for actual_value, expected_value in zip(actual, expected, strict=True)
    )


def _float_matrix_close_match(actual: Any, expected: Any, tolerance: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(expected, list) or len(actual) != len(expected):
        return False
    return all(
        _float_list_close_match(actual_row, expected_row, tolerance)
        for actual_row, expected_row in zip(actual, expected, strict=True)
    )


def _avoid_flood_match(actual: Any, expected: Any, rains: Any) -> bool:
    if expected == []:
        return actual == []
    if not isinstance(actual, list) or not isinstance(rains, list) or len(actual) != len(rains):
        return False
    full: set[int] = set()
    for action, lake in zip(actual, rains):
        if not isinstance(lake, int) or isinstance(lake, bool):
            return False
        if lake > 0:
            if action != -1 or lake in full:
                return False
            full.add(lake)
            continue
        if not isinstance(action, int) or isinstance(action, bool) or action <= 0:
            return False
        full.discard(action)
    return True


def _minimum_subsequence_match(actual: Any, nums: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(nums, list):
        return False
    if not all(isinstance(value, int) and not isinstance(value, bool) for value in actual):
        return False
    if any(actual[index] < actual[index + 1] for index in range(len(actual) - 1)):
        return False
    remaining = Counter(nums)
    for value in actual:
        if remaining[value] <= 0:
            return False
        remaining[value] -= 1
    if sum(actual) <= sum(value * count for value, count in remaining.items()):
        return False

    sorted_values = sorted(nums, reverse=True)
    total = sum(sorted_values)
    chosen = 0
    minimum_length = 0
    for value in sorted_values:
        chosen += value
        minimum_length += 1
        if chosen > total - chosen:
            break
    return len(actual) == minimum_length


def _maximum_even_split_match(actual: Any, final_sum: Any) -> bool:
    if (
        isinstance(final_sum, bool)
        or not isinstance(final_sum, int)
        or not isinstance(actual, list)
    ):
        return False
    if final_sum % 2:
        return actual == []
    if (
        not actual
        or any(
            isinstance(value, bool)
            or not isinstance(value, int)
            or value <= 0
            or value % 2
            for value in actual
        )
        or len(actual) != len(set(actual))
        or sum(actual) != final_sum
    ):
        return False

    maximum_count = (math.isqrt(1 + 4 * final_sum) - 1) // 2
    return len(actual) == maximum_count


def _minimum_unique_rows_matrix_match(actual: Any, nums: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(nums, list):
        return False
    if not nums:
        return actual == []

    expected_counts = Counter(nums)
    required_rows = max(expected_counts.values())
    if len(actual) != required_rows:
        return False

    flattened: list[Any] = []
    for row in actual:
        if not isinstance(row, list) or not row:
            return False
        if len(row) != len(set(row)):
            return False
        flattened.extend(row)
    return Counter(flattened) == expected_counts


def _smallest_string_from_lcp(lcp: Any) -> str | None:
    if not isinstance(lcp, list):
        return None
    n = len(lcp)
    if n == 0:
        return ""
    if any(not isinstance(row, list) or len(row) != n for row in lcp):
        return None

    labels = [-1] * n
    next_label = 0
    for i in range(n):
        if labels[i] != -1:
            continue
        if next_label >= 26:
            return ""
        for j in range(i, n):
            if not isinstance(lcp[i][j], int) or isinstance(lcp[i][j], bool):
                return None
            if lcp[i][j] > 0:
                labels[j] = next_label
        next_label += 1

    produced = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        if lcp[i][i] != n - i:
            return ""
        for j in range(n - 1, -1, -1):
            if not isinstance(lcp[i][j], int) or isinstance(lcp[i][j], bool):
                return None
            if labels[i] == labels[j]:
                produced[i][j] = produced[i + 1][j + 1] + 1
            if produced[i][j] != lcp[i][j]:
                return ""

    return "".join(chr(ord("a") + label) for label in labels)


def _lcp_string_match(actual: Any, lcp: Any) -> bool:
    expected = _smallest_string_from_lcp(lcp)
    return isinstance(actual, str) and expected is not None and actual == expected


def _good_subset_matrix_match(actual: Any, grid: Any, expected: Any) -> bool:
    if expected == []:
        return actual == []
    if not isinstance(grid, list) or not grid or not all(isinstance(row, list) for row in grid):
        return False
    if not isinstance(actual, list) or not actual:
        return False
    if actual != sorted(actual) or len(actual) != len(set(actual)):
        return False
    row_count = len(grid)
    col_count = len(grid[0])
    if any(not isinstance(index, int) or isinstance(index, bool) or index < 0 or index >= row_count for index in actual):
        return False
    for row in grid:
        if len(row) != col_count or any(value not in {0, 1} for value in row):
            return False
    allowed = len(actual) // 2
    for col in range(col_count):
        if sum(grid[row][col] for row in actual) > allowed:
            return False
    return True


def _neither_min_nor_max_match(actual: Any, nums: Any, expected: Any) -> bool:
    if expected == -1:
        return actual == -1
    if not isinstance(actual, int) or isinstance(actual, bool):
        return False
    if not isinstance(nums, list) or not nums:
        return False
    return actual in nums and min(nums) < actual < max(nums)


def _alternating_groups_subsequence_match(actual: Any, words: Any, groups: Any, expected: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(words, list) or not isinstance(groups, list):
        return False
    if len(words) != len(groups):
        return False
    if len(actual) != len(expected):
        return False

    states: set[tuple[int, Any]] = {(-1, None)}
    for item_index, item in enumerate(actual):
        next_states: set[tuple[int, Any]] = set()
        for previous_index, previous_group in states:
            for index in range(previous_index + 1, len(words)):
                if words[index] != item:
                    continue
                group = groups[index]
                if item_index == 0 or group != previous_group:
                    next_states.add((index, group))
        if not next_states:
            return False
        states = next_states
    return True


def _hamming_alternating_subsequence_match(actual: Any, words: Any, groups: Any, expected: Any) -> bool:
    if not _alternating_groups_subsequence_match(actual, words, groups, expected):
        return False
    if len(actual) <= 1:
        return True
    for left, right in zip(actual, actual[1:]):
        if not isinstance(left, str) or not isinstance(right, str) or len(left) != len(right):
            return False
        if sum(a != b for a, b in zip(left, right)) != 1:
            return False
    return True


def _index_value_pair_match(actual: Any, nums: Any, index_difference: Any, value_difference: Any) -> bool:
    if not isinstance(actual, list) or len(actual) != 2:
        return False
    if not isinstance(nums, list):
        return False
    if not all(isinstance(index, int) and not isinstance(index, bool) for index in actual):
        return False
    if actual == [-1, -1]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (
                    abs(i - j) >= index_difference
                    and abs(nums[i] - nums[j]) >= value_difference
                ):
                    return False
        return True
    i, j = actual
    return (
        0 <= i < len(nums)
        and 0 <= j < len(nums)
        and abs(i - j) >= index_difference
        and abs(nums[i] - nums[j]) >= value_difference
    )


def _peak_index_match(actual: Any, nums: Any) -> bool:
    if isinstance(actual, bool) or not isinstance(actual, int) or not isinstance(nums, list):
        return False
    if not 0 <= actual < len(nums):
        return False
    return (actual == 0 or nums[actual] > nums[actual - 1]) and (
        actual == len(nums) - 1 or nums[actual] > nums[actual + 1]
    )


def _peak_grid_match(actual: Any, matrix: Any) -> bool:
    if (
        not isinstance(actual, (list, tuple))
        or len(actual) != 2
        or any(isinstance(value, bool) or not isinstance(value, int) for value in actual)
        or not isinstance(matrix, list)
        or not matrix
        or not all(isinstance(row, list) and row for row in matrix)
    ):
        return False
    row, column = actual
    if not (0 <= row < len(matrix) and 0 <= column < len(matrix[row])):
        return False
    value = matrix[row][column]
    neighbors = (
        matrix[row - 1][column] if row > 0 else -1,
        matrix[row + 1][column] if row + 1 < len(matrix) else -1,
        matrix[row][column - 1] if column > 0 else -1,
        matrix[row][column + 1] if column + 1 < len(matrix[row]) else -1,
    )
    return all(value > neighbor for neighbor in neighbors)


def _closest_leaf_match(actual: Any, root_fixture: Any, target_value: Any) -> bool:
    if isinstance(actual, bool) or not isinstance(actual, int):
        return False
    root = _tree_from_level_order(root_fixture)
    if root is None:
        return False

    parent = {root: None}
    target = None
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.val == target_value:
            target = node
        for child in (node.left, node.right):
            if child is not None:
                parent[child] = node
                queue.append(child)

    if target is None:
        return False

    queue = deque([target])
    seen = {target}
    while queue:
        closest_values = set()
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left is None and node.right is None:
                closest_values.add(node.val)
            for neighbor in (node.left, node.right, parent[node]):
                if neighbor is not None and neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        if closest_values:
            return actual in closest_values
    return False


def _anagram_mapping_match(actual: Any, left: Any, right: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(left, list) or not isinstance(right, list):
        return False
    if len(actual) != len(left) or len(left) != len(right):
        return False
    return all(
        isinstance(mapped_index, int)
        and not isinstance(mapped_index, bool)
        and 0 <= mapped_index < len(right)
        and left[index] == right[mapped_index]
        for index, mapped_index in enumerate(actual)
    )


def _split_bst_match(actual: Any, expected: Any) -> bool:
    if not isinstance(actual, (list, tuple)) or len(actual) != 2:
        return False
    if not isinstance(expected, list) or len(expected) != 2:
        return False
    return [_tree_to_level_order(root) for root in actual] == expected


def _robot_room_cleaner_match(actual: Any, expected: Any) -> bool:
    if not isinstance(actual, _JudgeRobot):
        return False
    reachable = actual.reachable_cells
    if isinstance(expected, int) and not isinstance(expected, bool) and expected != len(reachable):
        return False
    return actual.cleaned_cells == reachable


def _h2o_groups_match(actual: Any) -> bool:
    return (
        isinstance(actual, str)
        and len(actual) % 3 == 0
        and all(Counter(actual[index:index + 3]) == Counter("HHO") for index in range(0, len(actual), 3))
    )


def _bounded_blocking_queue_match(actual: Any, expected: Any) -> bool:
    if not isinstance(actual, dict) or not isinstance(expected, dict):
        return False
    dequeued = actual.get("dequeued")
    if not isinstance(dequeued, list) or actual.get("final_size") != expected.get("final_size"):
        return False
    if "dequeued" in expected:
        return dequeued == expected["dequeued"]
    if "dequeued_multiset" in expected:
        return Counter(dequeued) == Counter(expected["dequeued_multiset"])
    return True


def _dining_philosophers_match(actual: Any, expected: Any) -> bool:
    if not isinstance(actual, dict) or not isinstance(expected, dict):
        return False
    calls = actual.get("calls")
    if not isinstance(calls, list) or actual.get("violations"):
        return False
    expected_calls = expected.get("calls")
    if isinstance(expected_calls, int) and len(calls) != expected_calls:
        return False
    required = {"pick-left", "pick-right", "eat", "put-left", "put-right"}
    for call in calls:
        if not isinstance(call, dict) or not isinstance(call.get("events"), list):
            return False
        events = call["events"]
        if len(events) != 5 or set(events) != required:
            return False
        if events.index("eat") < max(events.index("pick-left"), events.index("pick-right")):
            return False
        if events.index("eat") > min(events.index("put-left"), events.index("put-right")):
            return False
    return True


def _crawler_concurrency_match(actual: Any, expected: Any) -> bool:
    if not isinstance(actual, dict) or not isinstance(expected, dict):
        return False
    graph = actual.get("graph")
    start = actual.get("start_url")
    urls = actual.get("urls")
    fetches = actual.get("fetches")
    if not isinstance(graph, dict) or not isinstance(start, str) or not isinstance(urls, list) or not isinstance(fetches, list):
        return False
    hostname = start.split("/", 3)[2]
    reachable = {start}
    pending = [start]
    while pending:
        url = pending.pop()
        for neighbor in graph.get(url, []):
            if neighbor.split("/", 3)[2] == hostname and neighbor not in reachable:
                reachable.add(neighbor)
                pending.append(neighbor)
    if not (
        set(urls) == reachable
        and len(urls) == len(set(urls))
        and set(fetches) == reachable
        and len(fetches) == len(set(fetches))
    ):
        return False
    properties = expected.get("properties", [])
    if "overlapping-parser-calls" in properties and actual.get("max_active", 0) <= 1:
        return False
    if "bounded-workers" in properties and actual.get("max_active", 0) > 8:
        return False
    expected_urls = expected.get("urls")
    return expected_urls is None or set(urls) == set(expected_urls)


def _immutable_list_print_match(actual: Any, expected: Any) -> bool:
    if isinstance(actual, list) and isinstance(expected, list):
        return actual == expected
    return (
        isinstance(actual, _JudgeImmutableListNode)
        and isinstance(expected, list)
        and list(actual.printed_values) == expected
    )


def _traffic_light_match(actual: Any, expected: Any) -> bool:
    if not isinstance(actual, dict) or not isinstance(expected, dict):
        return False
    events = actual.get("events")
    expected_cars = expected.get("cars")
    if not isinstance(events, list) or not isinstance(expected_cars, list) or actual.get("violations"):
        return False
    crossed = [event.get("car") for event in events if isinstance(event, dict) and event.get("kind") == "cross"]
    return Counter(crossed) == Counter(expected_cars) and len(crossed) == len(expected_cars)


def _longest_palindromic_substring_match(actual: Any, expected: Any, s: Any) -> bool:
    if not isinstance(actual, str) or not isinstance(expected, str) or not isinstance(s, str):
        return False
    return len(actual) == len(expected) and actual == actual[::-1] and actual in s


def _decode_encoded_string(s: str) -> str:
    stack: list[tuple[str, int]] = []
    curr_str = ""
    i = 0
    while i < len(s):
        ch = s[i]
        if ch.isdigit():
            if ch == '0' and (i == 0 or not s[i - 1].isdigit()):
                return ""
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            stack.append((curr_str, num))
            curr_str = ""
            continue
        elif ch == '[':
            i += 1
            continue
        elif ch == ']':
            if not stack:
                return ""
            prev_str, num = stack.pop()
            curr_str = prev_str + curr_str * num
            i += 1
        else:
            curr_str += ch
            i += 1
    return curr_str if not stack else ""


def _shortest_string_encoding_match(actual: Any, expected: Any, s: Any) -> bool:
    if not isinstance(actual, str) or not isinstance(expected, str) or not isinstance(s, str):
        return False
    if len(actual) != len(expected):
        return False
    return _decode_encoded_string(actual) == s


def _fibonacci_split_match(actual: Any, expected: Any, digits: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(digits, str):
        return False
    if not actual:
        return actual == expected
    if len(actual) < 3:
        return False
    if any(
        not isinstance(value, int)
        or isinstance(value, bool)
        or value < 0
        or value >= 2**31
        for value in actual
    ):
        return False
    if any(actual[index - 2] + actual[index - 1] != actual[index] for index in range(2, len(actual))):
        return False
    return "".join(str(value) for value in actual) == digits


def _master_guessed_match(actual: Any) -> bool:
    return (
        isinstance(actual, _JudgeMaster)
        and actual.found
        and actual.guess_count <= actual.allowed_guesses
    )


def _majority_index_match(actual: Any, reader_fixture: Any) -> bool:
    if not isinstance(actual, int) or isinstance(actual, bool):
        return False
    if not isinstance(reader_fixture, dict):
        return False
    values = reader_fixture.get("array")
    if not isinstance(values, list):
        return False
    ones = sum(values)
    zeros = len(values) - ones
    if ones == zeros:
        return actual == -1
    majority = 1 if ones > zeros else 0
    return 0 <= actual < len(values) and values[actual] == majority


def _most_similar_path_match(
    actual: Any,
    n_value: Any,
    roads_value: Any,
    names_value: Any,
    target_value: Any,
) -> bool:
    if not isinstance(n_value, int) or isinstance(n_value, bool) or n_value <= 0:
        return False
    if not isinstance(roads_value, list) or not isinstance(names_value, list):
        return False
    if not isinstance(target_value, list) or not isinstance(actual, list):
        return False
    if len(names_value) != n_value or len(actual) != len(target_value):
        return False
    if not target_value:
        return actual == []

    graph: list[list[int]] = [[] for _ in range(n_value)]
    edges: set[tuple[int, int]] = set()
    for road in roads_value:
        if (
            not isinstance(road, list)
            or len(road) != 2
            or not all(isinstance(city, int) and not isinstance(city, bool) for city in road)
        ):
            return False
        left, right = road
        if not (0 <= left < n_value and 0 <= right < n_value) or left == right:
            return False
        graph[left].append(right)
        graph[right].append(left)
        edges.add((min(left, right), max(left, right)))

    if any(not isinstance(city, int) or isinstance(city, bool) or not 0 <= city < n_value for city in actual):
        return False
    if any((min(left, right), max(left, right)) not in edges for left, right in zip(actual, actual[1:])):
        return False

    infinity = len(target_value) + 1
    previous = [int(names_value[city] != target_value[0]) for city in range(n_value)]
    for wanted in target_value[1:]:
        current = [infinity] * n_value
        for city in range(n_value):
            if graph[city]:
                current[city] = int(names_value[city] != wanted) + min(
                    previous[neighbor] for neighbor in graph[city]
                )
        previous = current

    actual_cost = sum(
        names_value[city] != wanted
        for city, wanted in zip(actual, target_value)
    )
    return actual_cost == min(previous)


def _adjacent_path_match(actual: Any, pairs: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(pairs, list):
        return False
    if len(actual) != len(pairs) + 1:
        return False
    if any(not isinstance(value, int) or isinstance(value, bool) for value in actual):
        return False
    if len(set(actual)) != len(actual):
        return False

    vertices: set[int] = set()
    edges: Counter[frozenset[int]] = Counter()
    for pair in pairs:
        if (
            not isinstance(pair, list)
            or len(pair) != 2
            or any(not isinstance(value, int) or isinstance(value, bool) for value in pair)
            or pair[0] == pair[1]
        ):
            return False
        vertices.update(pair)
        edges[frozenset(pair)] += 1

    if set(actual) != vertices:
        return False
    for left, right in zip(actual, actual[1:]):
        edge = frozenset((left, right))
        if edges[edge] == 0:
            return False
        edges[edge] -= 1
    return all(count == 0 for count in edges.values())


def _sequential_grid_path_cover_match(
    actual: Any,
    expected: Any,
    grid: Any,
    k: Any,
) -> bool:
    if expected == []:
        return actual == []
    if (
        not isinstance(grid, list)
        or not grid
        or not all(isinstance(row, list) and row for row in grid)
        or any(len(row) != len(grid[0]) for row in grid)
        or not isinstance(k, int)
        or isinstance(k, bool)
        or k < 1
        or not isinstance(actual, list)
    ):
        return False

    rows = len(grid)
    columns = len(grid[0])
    if len(actual) != rows * columns:
        return False

    path: list[tuple[int, int]] = []
    for position in actual:
        if (
            not isinstance(position, list)
            or len(position) != 2
            or any(not isinstance(value, int) or isinstance(value, bool) for value in position)
        ):
            return False
        row, column = position
        if not 0 <= row < rows or not 0 <= column < columns:
            return False
        path.append((row, column))

    if len(set(path)) != rows * columns:
        return False
    if any(
        abs(left_row - right_row) + abs(left_column - right_column) != 1
        for (left_row, left_column), (right_row, right_column) in zip(path, path[1:])
    ):
        return False

    checkpoints = [grid[row][column] for row, column in path if grid[row][column] != 0]
    return checkpoints == list(range(1, k + 1))


def _modified_graph_edges_match(
    actual: Any,
    expected: Any,
    n: Any,
    original_edges: Any,
    source: Any,
    destination: Any,
    target: Any,
) -> bool:
    if expected == []:
        return actual == []
    if (
        not isinstance(n, int)
        or isinstance(n, bool)
        or n <= 0
        or not isinstance(source, int)
        or isinstance(source, bool)
        or not isinstance(destination, int)
        or isinstance(destination, bool)
        or not 0 <= source < n
        or not 0 <= destination < n
        or source == destination
        or not isinstance(target, int)
        or isinstance(target, bool)
        or target <= 0
        or not isinstance(original_edges, list)
        or not isinstance(actual, list)
        or len(actual) != len(original_edges)
    ):
        return False

    def parse_edge(edge: Any) -> tuple[int, int, int] | None:
        if (
            not isinstance(edge, list)
            or len(edge) != 3
            or any(not isinstance(value, int) or isinstance(value, bool) for value in edge)
        ):
            return None
        left, right, weight = edge
        if not 0 <= left < n or not 0 <= right < n or left == right:
            return None
        return left, right, weight

    originals: dict[tuple[int, int], int] = {}
    for edge in original_edges:
        parsed = parse_edge(edge)
        if parsed is None:
            return False
        left, right, weight = parsed
        key = (min(left, right), max(left, right))
        if key in originals or (weight != -1 and weight <= 0):
            return False
        originals[key] = weight

    graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    seen: set[tuple[int, int]] = set()
    for edge in actual:
        parsed = parse_edge(edge)
        if parsed is None:
            return False
        left, right, weight = parsed
        key = (min(left, right), max(left, right))
        if key in seen or key not in originals:
            return False
        seen.add(key)
        original_weight = originals[key]
        if original_weight == -1:
            if not 1 <= weight <= 2_000_000_000:
                return False
        elif weight != original_weight:
            return False
        graph[left].append((right, weight))
        graph[right].append((left, weight))

    if seen != set(originals):
        return False

    distances = [math.inf] * n
    distances[source] = 0
    visited = [False] * n
    for _ in range(n):
        node = min(
            (index for index in range(n) if not visited[index]),
            key=distances.__getitem__,
            default=-1,
        )
        if node == -1 or distances[node] == math.inf:
            break
        visited[node] = True
        for neighbor, weight in graph[node]:
            candidate = distances[node] + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate

    return distances[destination] == target


def _valid_pair_arrangement_match(actual: Any, pairs: Any) -> bool:
    if not isinstance(actual, list) or not isinstance(pairs, list):
        return False
    if len(actual) != len(pairs):
        return False

    def directed_edge(value: Any) -> tuple[int, int] | None:
        if (
            not isinstance(value, list)
            or len(value) != 2
            or any(not isinstance(item, int) or isinstance(item, bool) for item in value)
            or value[0] == value[1]
        ):
            return None
        return value[0], value[1]

    original_edges = [directed_edge(pair) for pair in pairs]
    arranged_edges = [directed_edge(pair) for pair in actual]
    if any(edge is None for edge in original_edges + arranged_edges):
        return False

    original_counter = Counter(original_edges)
    arranged_counter = Counter(arranged_edges)
    if arranged_counter != original_counter:
        return False
    return all(
        left[1] == right[0]
        for left, right in zip(arranged_edges, arranged_edges[1:])
    )


def _maximum_sum_subsequence_match(actual: Any, nums: Any, k: Any) -> bool:
    if (
        not isinstance(actual, list)
        or not isinstance(nums, list)
        or not isinstance(k, int)
        or isinstance(k, bool)
        or len(actual) != k
        or not 0 <= k <= len(nums)
        or any(not isinstance(value, int) or isinstance(value, bool) for value in actual)
        or any(not isinstance(value, int) or isinstance(value, bool) for value in nums)
    ):
        return False

    candidate_index = 0
    for value in nums:
        if candidate_index < k and value == actual[candidate_index]:
            candidate_index += 1
    if candidate_index != k:
        return False

    return sum(actual) == sum(sorted(nums, reverse=True)[:k])


def _recovered_original_array_match(actual: Any, nums: Any) -> bool:
    if (
        not isinstance(actual, list)
        or not isinstance(nums, list)
        or len(actual) * 2 != len(nums)
        or any(
            isinstance(value, bool) or not isinstance(value, int) or value <= 0
            for value in actual
        )
    ):
        return False

    observed = Counter(nums)
    smallest = min(nums)
    for original in set(actual):
        k = original - smallest
        if k <= 0:
            continue
        generated = Counter()
        for value in actual:
            generated[value - k] += 1
            generated[value + k] += 1
        if generated == observed:
            return True
    return False


def _valid_subarray_size_match(
    actual: Any,
    nums: Any,
    threshold: Any,
) -> bool:
    if (
        isinstance(actual, bool)
        or not isinstance(actual, int)
        or not isinstance(nums, list)
        or isinstance(threshold, bool)
        or not isinstance(threshold, int)
    ):
        return False

    if actual == -1:
        stack: list[int] = []
        for index in range(len(nums) + 1):
            value = nums[index] if index < len(nums) else -1
            while stack and nums[stack[-1]] > value:
                minimum = nums[stack.pop()]
                left_boundary = stack[-1] if stack else -1
                if minimum * (index - left_boundary - 1) > threshold:
                    return False
            stack.append(index)
        return True

    if actual <= 0 or actual > len(nums):
        return False

    candidates: deque[int] = deque()
    for index, value in enumerate(nums):
        while candidates and nums[candidates[-1]] >= value:
            candidates.pop()
        candidates.append(index)
        if candidates[0] <= index - actual:
            candidates.popleft()
        if (
            index + 1 >= actual
            and nums[candidates[0]] * actual > threshold
        ):
            return True
    return False


def _json_object_match(actual: Any, expected: Any) -> bool:
    """Compare JSON objects without coercing numeric-looking property names."""

    def normalize(value: Any) -> Any:
        if isinstance(value, dict):
            return {str(key): normalize(item) for key, item in value.items()}
        if isinstance(value, list):
            return [normalize(item) for item in value]
        return value

    return isinstance(actual, dict) and isinstance(expected, dict) and normalize(actual) == normalize(expected)


def _generated_schedule_match(actual: Any, n: Any) -> bool:
    if not isinstance(n, int) or isinstance(n, bool) or not isinstance(actual, list):
        return False
    if n < 5:
        return actual == []
    if len(actual) != n * (n - 1):
        return False

    matches: list[tuple[int, int]] = []
    for game in actual:
        if (
            not isinstance(game, list)
            or len(game) != 2
            or any(not isinstance(team, int) or isinstance(team, bool) for team in game)
        ):
            return False
        home, away = game
        if not (0 <= home < n and 0 <= away < n) or home == away:
            return False
        matches.append((home, away))

    if len(set(matches)) != n * (n - 1):
        return False
    return all(
        left_home not in right and left_away not in right
        for (left_home, left_away), right in zip(matches, matches[1:])
    )


def _exact_monotone_path_grid_match(
    actual: Any,
    rows: Any,
    columns: Any,
    target_paths: Any,
) -> bool:
    if (
        not isinstance(rows, int)
        or isinstance(rows, bool)
        or not isinstance(columns, int)
        or isinstance(columns, bool)
        or not isinstance(target_paths, int)
        or isinstance(target_paths, bool)
        or rows <= 0
        or columns <= 0
        or target_paths <= 0
        or not isinstance(actual, list)
    ):
        return False

    if actual == []:
        return math.comb(rows + columns - 2, rows - 1) < target_paths

    if (
        len(actual) != rows
        or any(
            not isinstance(row, str)
            or len(row) != columns
            or any(cell not in ".#" for cell in row)
            for row in actual
        )
    ):
        return False

    paths = [0] * columns
    for row in range(rows):
        for column in range(columns):
            if actual[row][column] == "#":
                paths[column] = 0
            elif row == 0 and column == 0:
                paths[column] = 1
            else:
                from_above = paths[column]
                from_left = paths[column - 1] if column else 0
                paths[column] = min(target_paths + 1, from_above + from_left)

    return paths[-1] == target_paths


def _bounded_exact_monotone_path_grid_match(
    actual: Any,
    max_rows: Any,
    max_columns: Any,
    target_paths: Any,
) -> bool:
    if (
        not isinstance(max_rows, int)
        or isinstance(max_rows, bool)
        or not isinstance(max_columns, int)
        or isinstance(max_columns, bool)
        or not isinstance(target_paths, int)
        or isinstance(target_paths, bool)
        or max_rows <= 0
        or max_columns <= 0
        or target_paths <= 0
        or not isinstance(actual, list)
        or not actual
        or not isinstance(actual[0], str)
        or not actual[0]
    ):
        return False

    rows = len(actual)
    columns = len(actual[0])
    if (
        rows > max_rows
        or columns > max_columns
        or any(
            not isinstance(row, str)
            or len(row) != columns
            or any(cell not in ".#" for cell in row)
            for row in actual
        )
    ):
        return False

    paths = [0] * columns
    for row in range(rows):
        for column in range(columns):
            if actual[row][column] == "#":
                paths[column] = 0
            elif row == 0 and column == 0:
                paths[column] = 1
            else:
                from_above = paths[column]
                from_left = paths[column - 1] if column else 0
                paths[column] = min(target_paths + 1, from_above + from_left)

    return paths[-1] == target_paths


def _unique_monotone_path_grid_match(
    actual: Any,
    rows: Any,
    columns: Any,
) -> bool:
    return _exact_monotone_path_grid_match(actual, rows, columns, 1)


def _knights_tour_match(actual: Any, m: int, n: int, r: int, c: int) -> bool:
    if not isinstance(actual, list) or len(actual) != m:
        return False
    pos: dict[int, tuple[int, int]] = {}
    for i, row in enumerate(actual):
        if not isinstance(row, list) or len(row) != n:
            return False
        for j, val in enumerate(row):
            if not isinstance(val, int) or val < 0 or val >= m * n or val in pos:
                return False
            pos[val] = (i, j)
    if len(pos) != m * n:
        return False
    if pos[0] != (r, c):
        return False
    for step in range(m * n - 1):
        r1, c1 = pos[step]
        r2, c2 = pos[step + 1]
        dr, dc = abs(r1 - r2), abs(c1 - c2)
        if not ((dr == 1 and dc == 2) or (dr == 2 and dc == 1)):
            return False
    return True


def _validated_case_matches(case: ValidatedCase, actual: Any, expected: Any) -> bool:
    validator = case.validator or {}
    kind = str(validator.get("kind") or "")
    if kind == "in_place_prefix":
        if not isinstance(actual, dict) or not isinstance(expected, dict):
            return False
        if actual.get("return_value") != expected.get("return_value"):
            return False
        actual_prefix = actual.get("prefix")
        expected_prefix = expected.get("prefix")
        if validator.get("unordered") is True:
            return _unordered_list_matches(actual_prefix, expected_prefix)
        return actual_prefix == expected_prefix
    if kind == "nary_tree":
        return _nary_node_to_fixture(actual) == expected
    if kind == "nary_tree_records":
        return _nary_node_to_records(actual) == expected
    if kind == "nested_integer":
        return _nested_integer_to_fixture(actual) == expected
    if kind == "alien_dictionary_order":
        return _alien_dictionary_order_match(actual, expected, case.input.get("words"))
    if kind == "random_binary_tree_copy":
        if not isinstance(actual, dict):
            return False
        expected_tree = expected.get("tree") if isinstance(expected, dict) else expected
        return actual.get("tree") == expected_tree and actual.get("independent") is True
    if kind == "json_object":
        return _json_object_match(actual, expected)
    if kind == "generated_schedule":
        return _generated_schedule_match(
            actual,
            case.input.get(str(validator.get("n_param") or "n")),
        )
    if kind == "unique_monotone_path_grid":
        return _unique_monotone_path_grid_match(
            actual,
            case.input.get(str(validator.get("rows_param") or "m")),
            case.input.get(str(validator.get("columns_param") or "n")),
        )
    if kind == "exact_monotone_path_grid":
        return _exact_monotone_path_grid_match(
            actual,
            case.input.get(str(validator.get("rows_param") or "m")),
            case.input.get(str(validator.get("columns_param") or "n")),
            case.input.get(str(validator.get("paths_param") or "k")),
        )
    if kind == "bounded_exact_monotone_path_grid":
        return _bounded_exact_monotone_path_grid_match(
            actual,
            validator.get("max_rows"),
            validator.get("max_columns"),
            case.input.get(str(validator.get("paths_param") or "k")),
        )
    if kind == "balanced_bst":
        values_param = str(validator.get("values_param") or "nums")
        values = case.input.get(values_param)
        if validator.get("values_from_tree") is True and isinstance(values, list):
            values = sorted(value for value in values if value is not None)
        return _balanced_bst_matches_values(actual, values)
    if kind == "pre_post_tree":
        return _pre_post_tree_match(
            actual,
            case.input.get(str(validator.get("preorder_param") or "preorder")),
            case.input.get(str(validator.get("postorder_param") or "postorder")),
        )
    if kind == "unordered_list":
        return _unordered_list_matches(actual, expected)
    if kind == "unordered_string":
        return _unordered_string_match(actual, expected)
    if kind == "character_pair_rearrangement":
        return _character_pair_rearrangement_match(
            actual,
            case.input.get(str(validator.get("string_param") or "s")),
            case.input.get(str(validator.get("x_param") or "x")),
            case.input.get(str(validator.get("y_param") or "y")),
        )
    if kind == "unordered_table":
        return _unordered_table_matches(actual, expected)
    if kind == "unordered_nested_list":
        return _unordered_nested_list_matches(actual, expected)
    if kind == "adjacent_path":
        return _adjacent_path_match(
            actual,
            case.input.get(str(validator.get("pairs_param") or "adjacentPairs")),
        )
    if kind == "sequential_grid_path_cover":
        return _sequential_grid_path_cover_match(
            actual,
            expected,
            case.input.get(str(validator.get("grid_param") or "grid")),
            case.input.get(str(validator.get("k_param") or "k")),
        )
    if kind == "modified_graph_edges":
        return _modified_graph_edges_match(
            actual,
            expected,
            case.input.get(str(validator.get("n_param") or "n")),
            case.input.get(str(validator.get("edges_param") or "edges")),
            case.input.get(str(validator.get("source_param") or "source")),
            case.input.get(str(validator.get("destination_param") or "destination")),
            case.input.get(str(validator.get("target_param") or "target")),
        )
    if kind == "valid_pair_arrangement":
        return _valid_pair_arrangement_match(
            actual,
            case.input.get(str(validator.get("pairs_param") or "pairs")),
        )
    if kind == "maximum_sum_subsequence":
        return _maximum_sum_subsequence_match(
            actual,
            case.input.get(str(validator.get("values_param") or "nums")),
            case.input.get(str(validator.get("k_param") or "k")),
        )
    if kind == "recovered_original_array":
        return _recovered_original_array_match(
            actual,
            case.input.get(str(validator.get("values_param") or "nums")),
        )
    if kind == "valid_subarray_size":
        return _valid_subarray_size_match(
            actual,
            case.input.get(str(validator.get("values_param") or "nums")),
            case.input.get(str(validator.get("threshold_param") or "threshold")),
        )
    if kind == "ordered_groups_unordered_items":
        return _ordered_groups_unordered_items_match(actual, expected)
    if kind == "ordered_results_unordered_lists":
        return _ordered_results_unordered_lists_match(actual, expected)
    if kind == "duplicate_subtrees":
        return _duplicate_subtrees_match(actual, expected)
    if kind == "beautiful_arrangement_ii":
        return _beautiful_arrangement_ii_match(
            actual,
            case.input.get(str(validator.get("n_param") or "n")),
            case.input.get(str(validator.get("k_param") or "k")),
        )
    if kind == "beautiful_array":
        return _beautiful_array_match(
            actual,
            case.input.get(str(validator.get("n_param") or "n")),
        )
    if kind == "di_string":
        return _di_string_match(
            actual,
            case.input.get(str(validator.get("string_param") or "s")),
        )
    if kind == "shortest_superstring":
        word_params = validator.get("word_params")
        if isinstance(word_params, list):
            words = [case.input.get(str(param)) for param in word_params]
        else:
            words = case.input.get(str(validator.get("words_param") or "words"))
        return _shortest_superstring_match(
            actual,
            expected,
            words,
        )
    if kind == "shortest_common_supersequence":
        return _shortest_common_supersequence_match(
            actual,
            case.input.get(str(validator.get("left_param") or "str1")),
            case.input.get(str(validator.get("right_param") or "str2")),
        )
    if kind == "stamping_sequence":
        return _stamping_sequence_match(
            actual,
            expected,
            case.input.get(str(validator.get("stamp_param") or "stamp")),
            case.input.get(str(validator.get("target_param") or "target")),
        )
    if kind == "pancake_sort":
        return _pancake_sort_match(
            actual,
            case.input.get(str(validator.get("values_param") or "arr")),
        )
    if kind == "string_without_triples":
        return _string_without_triples_match(
            actual,
            case.input.get(str(validator.get("a_param") or "a")),
            case.input.get(str(validator.get("b_param") or "b")),
        )
    if kind == "longest_happy_string":
        return _longest_happy_string_match(
            actual,
            case.input.get(str(validator.get("a_param") or "a")),
            case.input.get(str(validator.get("b_param") or "b")),
            case.input.get(str(validator.get("c_param") or "c")),
        )
    if kind == "ordered_unordered_groups":
        return _ordered_unordered_groups_match(actual, expected)
    if kind == "circular_doubly_tree":
        return _circular_doubly_tree_match(actual, expected)
    if kind == "circular_sorted_insertion":
        head_param = str(validator.get("head_param") or "head")
        val_param = str(validator.get("value_param") or "insertVal")
        return _circular_sorted_insertion_match(
            actual,
            case.input.get(head_param),
            case.input.get(val_param),
        )
    if kind == "quad_tree":
        return _quad_tree_match(actual, expected)
    if kind == "flattened_multilevel_list":
        return _flattened_multilevel_list_match(actual, expected)
    if kind == "all_one_trace":
        return _all_one_trace_match(actual, case.input.get(str(validator.get("operations_param") or "operations")))
    if kind == "largest_divisible_subset":
        values_param = str(validator.get("values_param") or "nums")
        return _largest_divisible_subset_match(actual, expected, case.input.get(values_param))
    if kind == "k_smallest_pairs":
        return _k_smallest_pairs_match(
            actual,
            case.input.get(str(validator.get("left_param") or "nums1")),
            case.input.get(str(validator.get("right_param") or "nums2")),
            case.input.get(str(validator.get("k_param") or "k")),
        )
    if kind == "phone_directory_trace":
        return _phone_directory_trace_match(
            actual,
            case.input.get(str(validator.get("max_param") or "max_numbers")),
            case.input.get(str(validator.get("operations_param") or "operations")),
        )
    if kind == "randomized_set_trace":
        return _randomized_set_trace_match(
            actual,
            case.input.get(str(validator.get("operations_param") or "operations")),
        )
    if kind == "randomized_collection_trace":
        return _randomized_collection_trace_match(
            actual,
            case.input.get(str(validator.get("operations_param") or "operations")),
        )
    if kind == "linked_list_random_draws":
        return _linked_list_random_draws_match(
            actual,
            case.input.get(str(validator.get("head_param") or "head")),
            case.input.get(str(validator.get("draws_param") or "draws")),
        )
    if kind == "shuffle_array_trace":
        return _shuffle_array_trace_match(
            actual,
            case.input.get(str(validator.get("values_param") or "nums")),
            case.input.get(str(validator.get("operations_param") or "operations")),
        )
    if kind == "random_flip_matrix_trace":
        return _random_flip_matrix_trace_match(
            actual,
            case.input.get(str(validator.get("rows_param") or "m")),
            case.input.get(str(validator.get("cols_param") or "n")),
            case.input.get(str(validator.get("operations_param") or "operations")),
        )
    if kind == "random_pick_indices":
        return _random_pick_indices_match(
            actual,
            case.input.get(str(validator.get("values_param") or "nums")),
            case.input.get(str(validator.get("targets_param") or "targets")),
        )
    if kind == "queue_reconstruction":
        return _queue_reconstruction_match(
            actual,
            case.input.get(str(validator.get("people_param") or "people")),
        )
    if kind == "advantage_shuffle":
        return _advantage_shuffle_match(
            actual,
            case.input.get(str(validator.get("left_param") or "nums1")),
            case.input.get(str(validator.get("right_param") or "nums2")),
        )
    if kind == "parity_partition":
        values_param = str(validator.get("values_param") or "nums")
        return _parity_partition_match(actual, case.input.get(values_param))
    if kind == "indexed_parity":
        values_param = str(validator.get("values_param") or "nums")
        return _indexed_parity_match(actual, case.input.get(values_param))
    if kind == "three_equal_binary_parts":
        values_param = str(validator.get("values_param") or "arr")
        return _three_equal_binary_parts_match(actual, case.input.get(values_param))
    if kind == "three_equal_parts":
        values_param = str(validator.get("values_param") or "arr")
        return _three_equal_parts_match(actual, expected, case.input.get(values_param))
    if kind == "fair_candy_swap":
        return _fair_candy_swap_match(
            actual,
            case.input.get(str(validator.get("alice_param") or "aliceSizes")),
            case.input.get(str(validator.get("bob_param") or "bobSizes")),
        )
    if kind == "minimum_unique_abbreviation":
        return _minimum_unique_abbreviation_match(
            actual,
            expected,
            case.input.get(str(validator.get("target_param") or "target")),
            case.input.get(str(validator.get("dictionary_param") or "dictionary")),
        )
    if kind == "anagram_groups":
        return _anagram_groups_match(actual, expected)
    if kind == "accounts_merge":
        return _accounts_merge_match(actual, expected)
    if kind == "frequency_sorted_string":
        string_param = str(validator.get("string_param") or "s")
        return _frequency_sorted_string_match(actual, case.input.get(string_param))
    if kind == "custom_sorted_string":
        return _custom_sorted_string_match(
            actual,
            case.input.get(str(validator.get("order_param") or "order")),
            case.input.get(str(validator.get("string_param") or "s")),
        )
    if kind == "gray_code":
        bits_param = str(validator.get("bits_param") or "n")
        return _gray_code_match(actual, case.input.get(bits_param))
    if kind == "circular_gray_code":
        bits_param = str(validator.get("bits_param") or "n")
        start_param = str(validator.get("start_param") or "start")
        return _circular_gray_code_match(
            actual,
            case.input.get(bits_param),
            case.input.get(start_param),
        )
    if kind == "de_bruijn_sequence":
        return _de_bruijn_sequence_match(
            actual,
            case.input.get(str(validator.get("n_param") or "n")),
            case.input.get(str(validator.get("k_param") or "k")),
        )
    if kind == "anagram_mapping":
        return _anagram_mapping_match(
            actual,
            case.input.get(str(validator.get("left_param") or "nums1")),
            case.input.get(str(validator.get("right_param") or "nums2")),
        )
    if kind == "sudoku_solution":
        board_param = str(validator.get("board_param") or "board")
        return _sudoku_solution_match(actual, case.input.get(board_param))
    if kind == "distance_order_cells":
        rows_param = str(validator.get("rows_param") or "rows")
        cols_param = str(validator.get("cols_param") or "cols")
        r_param = str(validator.get("r_center_param") or "rCenter")
        c_param = str(validator.get("c_center_param") or "cCenter")
        return _distance_order_cells_match(
            actual,
            case.input.get(rows_param),
            case.input.get(cols_param),
            case.input.get(r_param),
            case.input.get(c_param),
        )
    if kind == "balanced_factor_decomposition":
        return _balanced_factor_decomposition_match(
            actual,
            expected,
            case.input.get(str(validator.get("n_param") or "n")),
            case.input.get(str(validator.get("k_param") or "k")),
        )
    if kind == "absolute_value_sorted":
        values_param = str(validator.get("values_param") or "nums")
        return _absolute_value_sorted_match(actual, case.input.get(values_param))
    if kind == "wiggle_sort":
        values_param = str(validator.get("values_param") or "nums")
        return _wiggle_sort_matches(
            actual,
            case.input.get(values_param),
            strict=bool(validator.get("strict", True)),
        )
    if kind == "not_average_neighbors":
        values_param = str(validator.get("values_param") or "nums")
        return _not_average_neighbors_match(actual, case.input.get(values_param))
    if kind == "distant_barcodes":
        values_param = str(validator.get("values_param") or "barcodes")
        return _distant_barcodes_match(actual, case.input.get(values_param))
    if kind == "maximum_bob_points":
        return _maximum_bob_points_match(
            actual,
            expected,
            case.input.get(str(validator.get("arrows_param") or "numArrows")),
            case.input.get(str(validator.get("alice_param") or "aliceArrows")),
        )
    if kind == "rearranged_k_distance":
        return _rearranged_k_distance_match(
            actual,
            expected,
            case.input.get(str(validator.get("string_param") or "s")),
            case.input.get(str(validator.get("distance_param") or "k")),
        )
    if kind == "reorganized_string":
        return _rearranged_k_distance_match(
            actual,
            expected,
            case.input.get(str(validator.get("string_param") or "s")),
            2,
        )
    if kind == "reformatted_string":
        return _reformatted_string_match(
            actual,
            case.input.get(str(validator.get("string_param") or "s")),
        )
    if kind == "missing_binary_string":
        return _missing_binary_string_match(
            actual,
            case.input.get(str(validator.get("strings_param") or "nums")),
        )
    if kind == "missing_rolls":
        return _missing_rolls_match(
            actual,
            case.input.get(str(validator.get("rolls_param") or "rolls")),
            case.input.get(str(validator.get("mean_param") or "mean")),
            case.input.get(str(validator.get("count_param") or "n")),
        )
    if kind == "subset_sums_reconstruction":
        return _subset_sums_reconstruction_match(
            actual,
            case.input.get(str(validator.get("length_param") or "n")),
            case.input.get(str(validator.get("sums_param") or "sums")),
        )
    if kind == "question_mark_replacement":
        return _question_mark_replacement_match(
            actual,
            case.input.get(str(validator.get("string_param") or "s")),
        )
    if kind == "split_bst":
        return _split_bst_match(actual, expected)
    if kind == "reconstruct_two_row_matrix":
        return _reconstruct_two_row_matrix_match(
            actual,
            case.input.get(str(validator.get("upper_param") or "upper")),
            case.input.get(str(validator.get("lower_param") or "lower")),
            case.input.get(str(validator.get("colsum_param") or "colsum")),
            expected,
        )
    if kind == "matrix_margins":
        return _matrix_margins_match(
            actual,
            case.input.get(str(validator.get("row_sums_param") or "rowSum")),
            case.input.get(str(validator.get("column_sums_param") or "colSum")),
        )
    if kind == "grid_layout":
        return _grid_layout_match(
            actual,
            case.input.get(str(validator.get("n_param") or "n")),
            case.input.get(str(validator.get("edges_param") or "edges")),
        )
    if kind == "last_marked_nodes":
        return _last_marked_nodes_match(
            actual,
            case.input.get(str(validator.get("edges_param") or "edges")),
        )
    if kind == "condition_matrix":
        row_conditions_param = str(
            validator.get("row_conditions_param")
            or ("rowConditions" if "rowConditions" in case.input else "row_conditions")
        )
        column_conditions_param = str(
            validator.get("column_conditions_param")
            or ("colConditions" if "colConditions" in case.input else "col_conditions")
        )
        return _condition_matrix_match(
            actual,
            case.input.get(str(validator.get("k_param") or "k")),
            case.input.get(row_conditions_param),
            case.input.get(column_conditions_param),
        )
    if kind == "group_people":
        values_param = str(validator.get("values_param") or "groupSizes")
        return _group_people_match(actual, case.input.get(values_param))
    if kind == "unique_sum_zero":
        n_param = str(validator.get("n_param") or "n")
        return _unique_sum_zero_match(actual, case.input.get(n_param))
    if kind == "no_zero_sum":
        n_param = str(validator.get("n_param") or "n")
        return _no_zero_sum_match(actual, case.input.get(n_param))
    if kind == "color_red_triangle":
        n_param = str(validator.get("n_param") or "n")
        return _color_red_triangle_match(actual, case.input.get(n_param))
    if kind == "sufficient_team":
        return _sufficient_team_match(
            actual,
            expected,
            case.input.get(str(validator.get("skills_param") or "req_skills")),
            case.input.get(str(validator.get("people_param") or "people")),
        )
    if kind == "vps_split":
        sequence_param = str(validator.get("sequence_param") or "seq")
        return _vps_split_match(actual, case.input.get(sequence_param))
    if kind == "forest_roots":
        return _forest_roots_match(actual, expected)
    if kind == "unique_bsts":
        n_param = str(validator.get("n_param") or "n")
        return _unique_bsts_match(actual, case.input.get(n_param))
    if kind == "next_right_pointers":
        tree_param = str(validator.get("tree_param") or "root")
        return _next_right_pointers_match(actual, case.input.get(tree_param))
    if kind == "float_close":
        return _float_close_match(actual, expected, validator.get("tolerance", 1e-5))
    if kind == "float_list_close":
        return _float_list_close_match(actual, expected, validator.get("tolerance", 1e-5))
    if kind == "float_matrix_close":
        return _float_matrix_close_match(actual, expected, validator.get("tolerance", 1e-5))
    if kind == "avoid_flood":
        values_param = str(validator.get("values_param") or "rains")
        return _avoid_flood_match(actual, expected, case.input.get(values_param))
    if kind == "minimum_subsequence":
        values_param = str(validator.get("values_param") or "nums")
        return _minimum_subsequence_match(actual, case.input.get(values_param))
    if kind == "maximum_even_split":
        final_sum_param = str(validator.get("final_sum_param") or "finalSum")
        return _maximum_even_split_match(
            actual,
            case.input.get(final_sum_param),
        )
    if kind == "minimum_unique_rows_matrix":
        values_param = str(validator.get("values_param") or "nums")
        return _minimum_unique_rows_matrix_match(actual, case.input.get(values_param))
    if kind == "lcp_string":
        lcp_param = str(validator.get("lcp_param") or "lcp")
        return _lcp_string_match(actual, case.input.get(lcp_param))
    if kind == "good_subset_matrix":
        grid_param = str(validator.get("grid_param") or "grid")
        return _good_subset_matrix_match(actual, case.input.get(grid_param), expected)
    if kind == "neither_min_nor_max":
        values_param = str(validator.get("values_param") or "nums")
        return _neither_min_nor_max_match(actual, case.input.get(values_param), expected)
    if kind == "alternating_groups_subsequence":
        return _alternating_groups_subsequence_match(
            actual,
            case.input.get(str(validator.get("words_param") or "words")),
            case.input.get(str(validator.get("groups_param") or "groups")),
            expected,
        )
    if kind == "hamming_alternating_subsequence":
        return _hamming_alternating_subsequence_match(
            actual,
            case.input.get(str(validator.get("words_param") or "words")),
            case.input.get(str(validator.get("groups_param") or "groups")),
            expected,
        )
    if kind == "index_value_pair":
        return _index_value_pair_match(
            actual,
            case.input.get(str(validator.get("values_param") or "nums")),
            case.input.get(str(validator.get("index_param") or "indexDifference")),
            case.input.get(str(validator.get("value_param") or "valueDifference")),
        )
    if kind == "peak_index":
        values_param = str(validator.get("values_param") or "nums")
        return _peak_index_match(actual, case.input.get(values_param))
    if kind == "peak_grid":
        matrix_param = str(validator.get("matrix_param") or "mat")
        return _peak_grid_match(actual, case.input.get(matrix_param))
    if kind == "closest_leaf":
        return _closest_leaf_match(
            actual,
            case.input.get(str(validator.get("tree_param") or "root")),
            case.input.get(str(validator.get("target_param") or "k")),
        )
    if kind == "robot_room_cleaner":
        return _robot_room_cleaner_match(actual, expected)
    if kind == "h2o_groups":
        return _h2o_groups_match(actual)
    if kind == "bounded_blocking_queue":
        return _bounded_blocking_queue_match(actual, expected)
    if kind == "dining_philosophers":
        return _dining_philosophers_match(actual, expected)
    if kind == "crawler_concurrency":
        return _crawler_concurrency_match(actual, expected)
    if kind == "immutable_list_print":
        return _immutable_list_print_match(actual, expected)
    if kind == "traffic_light":
        return _traffic_light_match(actual, expected)
    if kind == "longest_palindromic_substring":
        return _longest_palindromic_substring_match(
            actual,
            expected,
            case.input.get(str(validator.get("string_param") or "s")),
        )
    if kind == "shortest_string_encoding":
        return _shortest_string_encoding_match(
            actual,
            expected,
            case.input.get(str(validator.get("string_param") or "s")),
        )
    if kind == "node_value":
        if actual is None:
            return expected is None
        return getattr(actual, "val", object()) == expected
    if kind == "fibonacci_split":
        digits_param = str(validator.get("digits_param") or "num")
        return _fibonacci_split_match(actual, expected, case.input.get(digits_param))
    if kind == "master_guessed":
        return _master_guessed_match(actual)
    if kind == "majority_index":
        reader_param = str(validator.get("reader_param") or "reader")
        return _majority_index_match(actual, case.input.get(reader_param))
    if kind == "most_similar_path":
        return _most_similar_path_match(
            actual,
            case.input.get(str(validator.get("n_param") or "n")),
            case.input.get(str(validator.get("roads_param") or "roads")),
            case.input.get(str(validator.get("names_param") or "names")),
            case.input.get(str(validator.get("target_param") or "targetPath")),
        )
    if kind == "knights_tour":
        return _knights_tour_match(
            actual,
            int(case.input.get(str(validator.get("m_param") or "m"), 0)),
            int(case.input.get(str(validator.get("n_param") or "n"), 0)),
            int(case.input.get(str(validator.get("r_param") or "r"), 0)),
            int(case.input.get(str(validator.get("c_param") or "c"), 0)),
        )
    if (
        isinstance(case.input, dict)
        and {"m", "n", "r", "c"}.issubset(case.input.keys())
        and isinstance(actual, list)
        and isinstance(expected, list)
        and len(actual) == len(expected) == case.input.get("m")
    ):
        if _knights_tour_match(
            actual,
            int(case.input["m"]),
            int(case.input["n"]),
            int(case.input["r"]),
            int(case.input["c"]),
        ):
            return True
    if actual == expected:
        return True
    if (actual is None and expected == []) or (actual == [] and expected is None):
        return True
    return False


def _prepare_validated_kwargs(
    kwargs: dict[str, Any],
    tree_param_names: list[str] | tuple[str, ...],
    list_node_param_names: list[str] | tuple[str, ...] = (),
    list_node_collection_param_names: list[str] | tuple[str, ...] = (),
    nary_node_param_names: list[str] | tuple[str, ...] = (),
    nary_node_collection_param_names: list[str] | tuple[str, ...] = (),
    random_binary_tree_param_names: list[str] | tuple[str, ...] = (),
    tree_node_target_param_names: list[str] | tuple[str, ...] = (),
    big_array_param_names: list[str] | tuple[str, ...] = (),
) -> dict[str, Any]:
    street_fixture = kwargs.get("street")
    if isinstance(street_fixture, list) and street_fixture:
        kwargs["street"] = _JudgeStreet(street_fixture)
    category_fixture = kwargs.get("categoryHandler")
    if isinstance(category_fixture, list):
        kwargs["categoryHandler"] = _JudgeCategoryHandler(category_fixture)
    for name in big_array_param_names:
        if isinstance(kwargs.get(name), list):
            kwargs[name] = _JudgeBigArray(kwargs[name])
    parent_pair = _parent_tree_pair_from_fixtures(kwargs.get("p"), kwargs.get("q"))
    if parent_pair is not None:
        kwargs["p"], kwargs["q"] = parent_pair
    root_leaf_pair = _parent_tree_root_and_leaf_from_fixtures(
        kwargs.get("root"),
        kwargs.get("leaf"),
    )
    if root_leaf_pair is not None:
        kwargs["root"], kwargs["leaf"] = root_leaf_pair
    root_targets_pair = _tree_root_and_targets_from_fixtures(
        kwargs.get("root"),
        kwargs.get("nodes"),
    )
    if root_targets_pair is not None:
        kwargs["root"], kwargs["nodes"] = root_targets_pair
    original_fixture = kwargs.get("original")
    if (
        isinstance(original_fixture, dict)
        and kwargs.get("cloned") == {"clone_of": "original"}
        and kwargs.get("target") == {"target_of": "original"}
    ):
        original, cloned, target = _cloned_tree_triplet_from_fixture(original_fixture)
        kwargs["original"] = original
        kwargs["cloned"] = cloned
        kwargs["target"] = target
    if "node" in kwargs:
        kwargs["node"] = _parent_tree_node_from_fixture(kwargs["node"])
    robot_fixture = kwargs.get("robot")
    if isinstance(robot_fixture, dict) and "room" in robot_fixture:
        kwargs["robot"] = _JudgeRobot(
            robot_fixture["room"],
            int(robot_fixture.get("row", 0)),
            int(robot_fixture.get("col", 0)),
            int(robot_fixture.get("direction", 0)),
        )
    grid_master_fixture = kwargs.get("master")
    if isinstance(grid_master_fixture, dict) and "grid" in grid_master_fixture:
        mode = str(grid_master_fixture.get("mode") or "unweighted")
        if mode not in {"unweighted", "weighted"}:
            raise ValueError("GridMaster mode must be unweighted or weighted")
        kwargs["master"] = _JudgeGridMaster(
            grid_master_fixture["grid"],
            start=grid_master_fixture.get("start"),
            target=grid_master_fixture.get("target"),
            weighted=mode == "weighted",
        )
    sea_fixture = kwargs.get("sea")
    if isinstance(sea_fixture, dict) and "ships" in sea_fixture:
        kwargs["sea"] = _JudgeSea(
            sea_fixture["ships"],
            int(sea_fixture.get("max_queries", 400)),
        )
        for corner_name in ("topRight", "bottomLeft", "top_right", "bottom_left"):
            corner = kwargs.get(corner_name)
            if isinstance(corner, list) and len(corner) == 2:
                kwargs[corner_name] = _JudgePoint(corner[0], corner[1])
    for matrix_name in ("binary_matrix", "binaryMatrix"):
        matrix_fixture = kwargs.get(matrix_name)
        if isinstance(matrix_fixture, dict) and "matrix" in matrix_fixture:
            kwargs[matrix_name] = _JudgeBinaryMatrix(
                matrix_fixture["matrix"],
                int(matrix_fixture.get("max_queries", 1000)),
            )
    stream_fixture = kwargs.get("stream")
    if isinstance(stream_fixture, dict):
        stream_bits = stream_fixture.get("bits")
        if stream_bits is None and "repeated_bit" in stream_fixture:
            repeated_bit = stream_fixture["repeated_bit"]
            repeat_count = stream_fixture.get("repeat_count")
            suffix = stream_fixture.get("suffix", [])
            if not isinstance(repeat_count, int) or isinstance(repeat_count, bool):
                raise ValueError("infinite stream repeat_count must be an integer")
            if repeat_count < 0 or not isinstance(suffix, list):
                raise ValueError("infinite stream compact fixture is invalid")
            stream_bits = [repeated_bit] * repeat_count + suffix
        if stream_bits is not None:
            max_reads = stream_fixture.get("max_reads")
            kwargs["stream"] = _JudgeInfiniteStream(
                stream_bits,
                None if max_reads is None else int(max_reads),
            )
    font_info_fixture = kwargs.get("fontInfo")
    if isinstance(font_info_fixture, dict) and "heights" in font_info_fixture:
        kwargs["fontInfo"] = _JudgeFontInfo(
            font_info_fixture["heights"],
            font_info_fixture.get("widths"),
            font_info_fixture.get("uniform_widths"),
            int(font_info_fixture.get("max_queries", 100_000)),
        )
    mountain_fixture = kwargs.get("mountainArr")
    if isinstance(mountain_fixture, list):
        kwargs["mountainArr"] = _JudgeMountainArray(mountain_fixture)
    elif isinstance(mountain_fixture, dict) and "values" in mountain_fixture:
        kwargs["mountainArr"] = _JudgeMountainArray(
            mountain_fixture["values"],
            int(mountain_fixture.get("max_queries", 100)),
        )
    html_parser_fixture = kwargs.get("htmlParser")
    if (
        isinstance(html_parser_fixture, dict)
        and "urls" in html_parser_fixture
        and "edges" in html_parser_fixture
    ):
        kwargs["htmlParser"] = _JudgeHtmlParser(
            html_parser_fixture["urls"],
            html_parser_fixture["edges"],
        )
    custom_function_fixture = kwargs.get("customfunction")
    if isinstance(custom_function_fixture, int) and not isinstance(
        custom_function_fixture, bool
    ):
        kwargs["customfunction"] = _JudgeCustomFunction(custom_function_fixture)
    elif (
        isinstance(custom_function_fixture, dict)
        and "function_id" in custom_function_fixture
    ):
        kwargs["customfunction"] = _JudgeCustomFunction(
            custom_function_fixture["function_id"]
        )
    reader_fixture = kwargs.get("reader")
    if isinstance(reader_fixture, dict) and "array" in reader_fixture:
        if reader_fixture.get("api") == "majority":
            max_queries = reader_fixture.get("max_queries")
            kwargs["reader"] = _JudgeMajorityReader(
                reader_fixture["array"],
                None if max_queries is None else int(max_queries),
            )
        else:
            kwargs["reader"] = _JudgeArrayReader(
                reader_fixture["array"],
                int(reader_fixture.get("max_queries", 20)),
            )
    master_fixture = kwargs.get("master")
    if isinstance(master_fixture, dict) and "secret" in master_fixture:
        words = kwargs.get("words")
        kwargs["master"] = _JudgeMaster(
            str(master_fixture["secret"]),
            words if isinstance(words, list) else [],
            int(master_fixture.get("allowed_guesses", 10)),
        )
    for name, fixture in list(kwargs.items()):
        if isinstance(fixture, dict) and set(fixture) == {"immutable_values"}:
            kwargs[name] = _immutable_list_node_from_values(fixture["immutable_values"])
    if "nestedList" in kwargs:
        kwargs["nestedList"] = _nested_integer_list_from_fixture(
            kwargs["nestedList"]
        )
    for name in tree_param_names:
        if name in kwargs:
            fixture = kwargs[name]
            if name in random_binary_tree_param_names:
                kwargs[name] = _random_binary_tree_from_fixture(fixture)
                continue
            if (
                isinstance(fixture, list)
                and fixture
                and all(isinstance(tree, list) for tree in fixture)
            ):
                kwargs[name] = [_tree_from_level_order(tree) for tree in fixture]
            else:
                kwargs[name] = _tree_from_level_order(fixture)
    root = kwargs.get("root")
    for name in tree_node_target_param_names:
        if name in kwargs and not hasattr(kwargs[name], "val"):
            fixture = kwargs[name]
            if isinstance(fixture, dict) and set(fixture) == {"path_from_root"}:
                path = fixture["path_from_root"]
                if not isinstance(path, str) or any(step not in "LR" for step in path):
                    raise ValueError("tree target path must contain only L and R")
                target = root
                for step in path:
                    target = getattr(target, "left" if step == "L" else "right", None)
                    if target is None:
                        raise ValueError("tree target path does not select a node")
                kwargs[name] = target
            else:
                kwargs[name] = _tree_node_with_value(root, fixture)
    for name in ("poly1", "poly2"):
        if name in kwargs:
            kwargs[name] = _poly_node_from_terms(kwargs[name])
    shared_list_names = _prepare_shared_list_nodes(kwargs, list_node_param_names)
    for name in list_node_param_names:
        if name in shared_list_names:
            continue
        if name in kwargs:
            if name in list_node_collection_param_names:
                fixtures = kwargs[name]
                if isinstance(fixtures, list):
                    kwargs[name] = [
                        _list_node_from_values(fixture) for fixture in fixtures
                    ]
            else:
                kwargs[name] = _list_node_from_values(kwargs[name])
    for name in nary_node_param_names:
        if name in kwargs:
            root, nodes, ordered_nodes = _nary_nodes_from_records(kwargs[name])
            if nodes:
                kwargs[name] = (
                    ordered_nodes
                    if name in nary_node_collection_param_names
                    else root
                )
                for target_name in ("p", "q"):
                    target_value = kwargs.get(target_name)
                    if target_value in nodes:
                        kwargs[target_name] = nodes[target_value]
            else:
                kwargs[name] = _nary_node_from_fixture(kwargs[name])
    for name, value in list(kwargs.items()):
        if isinstance(value, dict) and isinstance(value.get("leaf"), bool):
            kwargs[name] = _quad_tree_from_fixture(value)
    return kwargs


def _normalize_validated_value(
    value: Any,
    *,
    returns_tree: bool = False,
    returns_list_node: bool = False,
) -> Any:
    if value is not None and all(
        hasattr(value, attr) for attr in ("coefficient", "power", "next")
    ):
        return _poly_node_to_terms(value)
    if value is not None and hasattr(value, "val") and (hasattr(value, "left") or hasattr(value, "right")):
        return _tree_to_level_order(value)
    if value is not None and hasattr(value, "val") and hasattr(value, "next"):
        return _list_node_to_values(value)
    if returns_tree:
        return _tree_to_level_order(value)
    if returns_list_node:
        return _list_node_to_values(value)
    return value


def _runtime_check_from_times(
    *,
    user_ms: Optional[float],
    reference_ms: Optional[float],
    trials: int,
    n: int,
    seed: Optional[int],
    language: str,
    benchmark_correct: bool = True,
    error_message: str = "",
) -> RuntimeCheck:
    limit_ms = _runtime_limit_ms(reference_ms, language)
    ratio = user_ms / reference_ms if user_ms is not None and reference_ms and reference_ms > 0 else None
    passed = bool(benchmark_correct and user_ms is not None and user_ms <= limit_ms and not error_message)
    if error_message:
        message = error_message
    elif not benchmark_correct:
        message = "Failed the hidden benchmark input."
    elif user_ms is None:
        message = "Runtime benchmark could not measure the user solution."
    elif passed:
        message = f"Runtime OK: {user_ms:.1f} ms <= {limit_ms:.1f} ms."
    else:
        message = f"Runtime too slow: {user_ms:.1f} ms > {limit_ms:.1f} ms."
    return RuntimeCheck(
        checked=True,
        passed=passed,
        user_ms=user_ms,
        reference_ms=reference_ms,
        ratio=ratio,
        limit_ms=limit_ms,
        trials=trials,
        n=n,
        seed=seed,
        message=message,
        benchmark_correct=benchmark_correct,
    )


def _median(values: list[float]) -> Optional[float]:
    if not values:
        return None
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def _timed_traced_call(
    func: Any,
    kwargs: dict[str, Any],
    *,
    step_limit: int = _RUNTIME_STEP_LIMIT,
) -> tuple[Any, float]:
    start = time.perf_counter()
    result, _trace = run_with_trace(
        func,
        kwargs,
        step_limit=step_limit,
        capture=False,
    )
    return result, (time.perf_counter() - start) * 1000.0


def _actual_result(
    result: Any,
    kwargs: dict[str, Any],
    *,
    case: ValidatedCase | None = None,
    returns_in_place: bool = False,
    param_names: list[str] | tuple[str, ...] = (),
    returns_tree: bool = False,
    returns_list_node: bool = False,
) -> Any:
    actual = result
    if returns_in_place and result is None and param_names:
        first_param = param_names[0]
        if first_param in kwargs:
            actual = kwargs[first_param]
    validator = case.validator if case is not None else {}
    validator_kind = str(validator.get("kind") or "")
    if validator_kind == "master_guessed" and result is None:
        return kwargs.get("master")
    if validator_kind == "immutable_list_print" and result is None:
        head_param = str(validator.get("head_param") or "head")
        head = kwargs.get(head_param)
        if hasattr(head, "printed"):
            return head.printed
    if validator_kind == "random_binary_tree_copy":
        root_param = str(validator.get("root_param") or "root")
        return {
            "tree": _random_binary_tree_to_fixture(actual),
            "independent": _node_graphs_are_disjoint(actual, kwargs.get(root_param)),
        }
    if validator_kind in {"nary_tree", "nary_tree_records", "node_value"}:
        return actual
    actual = _normalize_validated_value(
        actual,
        returns_tree=returns_tree,
        returns_list_node=returns_list_node,
    )
    if validator_kind == "in_place_prefix":
        values_param = str(validator.get("values_param") or (param_names[0] if param_names else "nums"))
        values = _normalize_validated_value(kwargs.get(values_param))
        prefix = None
        if (
            isinstance(actual, int)
            and not isinstance(actual, bool)
            and isinstance(values, list)
            and 0 <= actual <= len(values)
        ):
            prefix = values[:actual]
        return {"return_value": actual, "prefix": prefix}
    return actual


def _timed_reference_iterations(
    func: Any,
    kwargs: dict[str, Any],
    iterations: int,
    *,
    case: ValidatedCase | None = None,
    returns_in_place: bool = False,
    param_names: list[str] | tuple[str, ...] = (),
    returns_tree: bool = False,
    returns_list_node: bool = False,
    step_limit: int = _RUNTIME_STEP_LIMIT,
) -> tuple[Any, float]:
    last_result: Any = None
    last_kwargs: dict[str, Any] = kwargs
    elapsed_ms = 0.0
    import copy

    total_iterations = max(1, iterations)
    for index in range(total_iterations):
        call_kwargs = copy.deepcopy(kwargs) if index + 1 < total_iterations else kwargs
        last_result, call_ms = _timed_traced_call(
            func,
            call_kwargs,
            step_limit=step_limit,
        )
        last_kwargs = call_kwargs
        elapsed_ms += call_ms
    return _actual_result(
        last_result,
        last_kwargs,
        case=case,
        returns_in_place=returns_in_place,
        param_names=param_names,
        returns_tree=returns_tree,
        returns_list_node=returns_list_node,
    ), elapsed_ms


def _create_judge_namespace(name: str = "judge", filename: str = "judge.py") -> dict[str, Any]:
    import bisect
    import collections
    from collections import Counter, defaultdict, deque, OrderedDict
    import functools
    from functools import cache, lru_cache, reduce
    import heapq
    import itertools
    try:
        from itertools import pairwise
    except ImportError:
        pairwise = None
    from itertools import accumulate, combinations, combinations_with_replacement, groupby, islice, permutations, product
    import math
    from math import inf
    import operator
    from operator import xor, add, mul, sub, truediv, floordiv, mod, itemgetter, attrgetter
    import random
    import re
    import string
    import sys
    import typing

    ns: dict[str, Any] = {
        "__name__": name,
        "__file__": filename,
        "__package__": None,
        "List": list,
        "Dict": dict,
        "Tuple": tuple,
        "Set": set,
        "Optional": typing.Optional,
        "Union": typing.Union,
        "Any": typing.Any,
        "Callable": typing.Callable,
        "Iterable": typing.Iterable,
        "Iterator": typing.Iterator,
        "Sequence": typing.Sequence,
        "pairwise": pairwise,
        "ListNode": _JudgeListNode,
        "Node": _JudgeNode,
        "Point": _JudgePoint,
        "TreeNode": _JudgeTreeNode,
        "math": math,
        "inf": inf,
        "heapq": heapq,
        "bisect": bisect,
        "bisect_left": bisect.bisect_left,
        "bisect_right": bisect.bisect_right,
        "insort": bisect.insort,
        "insort_left": bisect.insort_left,
        "insort_right": bisect.insort_right,
        "itertools": itertools,
        "accumulate": accumulate,
        "combinations": combinations,
        "combinations_with_replacement": combinations_with_replacement,
        "groupby": groupby,
        "islice": islice,
        "permutations": permutations,
        "product": product,
        "functools": functools,
        "cache": cache,
        "lru_cache": lru_cache,
        "reduce": reduce,
        "collections": collections,
        "Counter": Counter,
        "defaultdict": defaultdict,
        "deque": deque,
        "OrderedDict": OrderedDict,
        "operator": operator,
        "xor": xor,
        "random": random,
        "re": re,
        "string": string,
        "sys": sys,
    }
    for mod_obj in (math, collections, itertools, heapq, bisect, functools, operator, random):
        for k in dir(mod_obj):
            if not k.startswith("_") and k not in ns:
                ns[k] = getattr(mod_obj, k)
    return ns


def _inject_solution_globals(target: Any) -> None:
    if target is None:
        return
    g = getattr(target, "__globals__", None)
    if g is None and hasattr(target, "__init__"):
        g = getattr(target.__init__, "__globals__", None)
    if g is None and hasattr(target, "__class__"):
        g = getattr(target.__class__, "__globals__", None)
    if g is None:
        return
    ns = _create_judge_namespace(str(g.get("__name__") or "judge"), str(g.get("__file__") or "judge.py"))
    for k, v in ns.items():
        if k not in g or g[k] is None:
            g[k] = v


def _instantiate_class(cls: type, kwargs: dict[str, Any], *extra_args: Any) -> Any:
    _inject_solution_globals(cls)
    if extra_args:
        try:
            inst = cls(*extra_args)
            _inject_solution_globals(inst)
            return inst
        except TypeError:
            pass
    import inspect
    try:
        init_sig = inspect.signature(cls.__init__)
        init_params = [p for p in init_sig.parameters.keys() if p != "self"]
        init_kwargs = {p: kwargs[p] for p in init_params if p in kwargs}
        if init_kwargs:
            inst = cls(**init_kwargs)
            _inject_solution_globals(inst)
            return inst
    except Exception:
        pass
    inst = cls()
    _inject_solution_globals(inst)
    return inst


def _execute_class_operations(cls: type, kwargs: dict[str, Any]) -> list[Any] | None:
    _inject_solution_globals(cls)
    if "operations" not in kwargs:
        return None

    ops = kwargs["operations"]
    arguments = kwargs.get("arguments")

    if not isinstance(ops, list) or not ops:
        return None

    if arguments is not None:
        if not isinstance(arguments, list):
            return None
        has_valid = False
        for op in ops:
            if isinstance(op, str) and (op in {"Solution", cls.__name__} or hasattr(cls, op)):
                has_valid = True
            else:
                return None
        if not has_valid:
            return None
    else:
        has_valid = False
        for item in ops:
            if isinstance(item, (list, tuple)) and len(item) > 0 and isinstance(item[0], str):
                op_name = item[0]
                if op_name in {"Solution", cls.__name__} or hasattr(cls, op_name):
                    has_valid = True
                else:
                    return None
            elif isinstance(item, str):
                if item in {"Solution", cls.__name__} or hasattr(cls, item):
                    has_valid = True
                else:
                    return None
            else:
                return None
        if not has_valid:
            return None

    inst = None
    res_list = []

    if arguments is not None:
        for op, arg in zip(ops, arguments):
            if op == "Solution" or op == cls.__name__ or (inst is None and isinstance(op, str) and (op[0].isupper() or op == "Solution")):
                inst = _instantiate_class(cls, kwargs, *arg)
                res_list.append(None)
            else:
                if inst is None:
                    inst = _instantiate_class(cls, kwargs)
                method = getattr(inst, op)
                _inject_solution_globals(method)
                res_list.append(method(*arg))
        return res_list

    if isinstance(ops, list):
        for item in ops:
            if isinstance(item, (list, tuple)) and len(item) > 0:
                op = item[0]
                arg = item[1:]
                if op == "Solution" or op == cls.__name__ or (inst is None and isinstance(op, str) and op[0].isupper()):
                    inst = _instantiate_class(cls, kwargs, *arg)
                else:
                    if inst is None:
                        inst = _instantiate_class(cls, kwargs)
                    method = getattr(inst, op)
                    _inject_solution_globals(method)
                    val = method(*arg)
                    if val is not None:
                        res_list.append(val)
            elif isinstance(item, str):
                if item == "Solution" or item == cls.__name__ or (inst is None and item[0].isupper()):
                    inst = _instantiate_class(cls, kwargs)
                else:
                    if inst is None:
                        inst = _instantiate_class(cls, kwargs)
                    method = getattr(inst, item)
                    _inject_solution_globals(method)
                    val = method()
                    if val is not None:
                        res_list.append(val)
        return res_list

    return None


def _bind_leetcode_solution_runner(namespace: dict[str, Any], challenge: Any = None) -> Any:
    if "solve" in namespace and callable(namespace["solve"]):
        return namespace["solve"]

    cid = getattr(getattr(challenge, "info", None), "id", "") or ""

    if cid == "lc_157":
        def read4_157_runner(**kwargs):
            content = kwargs.get("content", "")
            n = kwargs.get("n", 0)
            file_ptr = [0]
            def mock_read4(buf4: list[str]) -> int:
                count = 0
                while count < 4 and file_ptr[0] < len(content):
                    if count < len(buf4):
                        buf4[count] = content[file_ptr[0]]
                    else:
                        buf4.append(content[file_ptr[0]])
                    count += 1
                    file_ptr[0] += 1
                return count

            sol_cls = namespace.get("Solution")
            if not sol_cls:
                raise NoSolveFunction()
            sol = sol_cls()
            if hasattr(sol.read, "__globals__"):
                sol.read.__globals__["read4"] = mock_read4
            buf = [""] * n
            bytes_read = sol.read(buf, n)
            return "".join(buf[:bytes_read])
        return read4_157_runner

    if cid == "lc_158":
        def read4_158_runner(**kwargs):
            content = kwargs.get("content", "")
            requests = kwargs.get("requests", [])
            file_ptr = [0]
            def mock_read4(buf4: list[str]) -> int:
                count = 0
                while count < 4 and file_ptr[0] < len(content):
                    if count < len(buf4):
                        buf4[count] = content[file_ptr[0]]
                    else:
                        buf4.append(content[file_ptr[0]])
                    count += 1
                    file_ptr[0] += 1
                return count

            sol_cls = namespace.get("Solution")
            if not sol_cls:
                raise NoSolveFunction()
            sol = sol_cls()
            if hasattr(sol.read, "__globals__"):
                sol.read.__globals__["read4"] = mock_read4
            result = []
            for req in requests:
                buf = [""] * req
                bytes_read = sol.read(buf, req)
                result.append("".join(buf[:bytes_read]))
            return result
        return read4_158_runner

    sol_cls = namespace.get("Solution")
    if sol_cls is not None and isinstance(sol_cls, type):
        import inspect
        methods = [
            name for name, func in inspect.getmembers(sol_cls, predicate=inspect.isfunction)
            if not name.startswith("_")
        ]
        if methods:
            method_name = methods[0]
            spec = getattr(challenge, "_spec", None) if challenge else None
            spec_id = getattr(challenge.info, "id", "") if challenge and hasattr(challenge, "info") else ""
            if not spec_id and spec and hasattr(spec, "id"):
                spec_id = spec.id
            if spec_id.startswith("lc_"):
                try:
                    from server.app.challenge_packages import leetcode_package_dir
                    package = leetcode_package_dir(spec_id)
                    if package and (package / "template.py").is_file():
                        tpl = (package / "template.py").read_text(encoding="utf-8")
                        tpl_match = re.search(r"def\s+([A-Za-z0-9_]+)\s*\(self", tpl)
                        if tpl_match and tpl_match.group(1) in methods:
                            method_name = tpl_match.group(1)
                except Exception:
                    pass
            if len(methods) > 1 and spec:
                param_names = list(_get_spec_inputs(spec).keys())
                for m_name in methods:
                    m_obj = getattr(sol_cls, m_name)
                    try:
                        sig = inspect.signature(m_obj)
                        sig_params = [param for param in sig.parameters if param != "self"]
                        if set(sig_params) == set(param_names) or len(sig_params) == len(param_names):
                            method_name = m_name
                            break
                    except Exception:
                        pass

            def solve_runner(*args, **kwargs):
                call_kwargs = dict(kwargs)
                if "operations" not in call_kwargs and len(args) == 1 and isinstance(args[0], list):
                    call_kwargs["operations"] = args[0]
                ops_res = _execute_class_operations(sol_cls, call_kwargs)
                if ops_res is not None:
                    return ops_res

                sol_inst = _instantiate_class(sol_cls, kwargs, *args)
                method = getattr(sol_inst, method_name)
                _inject_solution_globals(method)
                if "queries" in kwargs and isinstance(kwargs["queries"], list):
                    return [
                        method(*q) if isinstance(q, (list, tuple)) else method(q)
                        for q in kwargs["queries"]
                    ]
                try:
                    return method(*args, **kwargs)
                except TypeError:
                    if kwargs and not args:
                        try:
                            return method(*kwargs.values())
                        except Exception:
                            pass
                    raise

            return solve_runner

    if "solve" in namespace and callable(namespace["solve"]):
        return namespace["solve"]

    ns_name = namespace.get("__name__")
    for name, obj in namespace.items():
        if (
            not name.startswith("_")
            and isinstance(obj, type)
            and (getattr(obj, "__module__", None) == ns_name or ns_name is None)
            and name not in dir(__builtins__)
            and name not in {"TreeNode", "ListNode", "Node", "Point", "List", "Dict", "Tuple", "Set", "Optional", "Union", "Any"}
        ):
            custom_cls = obj
            def custom_class_runner(*args, **kwargs):
                call_kwargs = dict(kwargs)
                if "operations" not in call_kwargs and len(args) == 1 and isinstance(args[0], list):
                    call_kwargs["operations"] = args[0]
                ops_res = _execute_class_operations(custom_cls, call_kwargs)
                if ops_res is not None:
                    return ops_res

                import inspect
                methods = [
                    m for m, func in inspect.getmembers(custom_cls, predicate=inspect.isfunction)
                    if not m.startswith("_")
                ]
                if methods:
                    method_name = methods[0]
                    spec = getattr(challenge, "_spec", None) if challenge else None
                    spec_id = getattr(challenge.info, "id", "") if challenge and hasattr(challenge, "info") else ""
                    if not spec_id and spec and hasattr(spec, "id"):
                        spec_id = spec.id
                    if spec_id.startswith("lc_"):
                        try:
                            from server.app.challenge_packages import leetcode_package_dir
                            package = leetcode_package_dir(spec_id)
                            if package and (package / "template.py").is_file():
                                tpl = (package / "template.py").read_text(encoding="utf-8")
                                tpl_match = re.search(r"def\s+([A-Za-z0-9_]+)\s*\(self", tpl)
                                if tpl_match and tpl_match.group(1) in methods:
                                    method_name = tpl_match.group(1)
                        except Exception:
                            pass
                    if len(methods) > 1 and spec:
                        param_names = list(_get_spec_inputs(spec).keys())
                        for m_name in methods:
                            m_obj = getattr(custom_cls, m_name)
                            try:
                                sig = inspect.signature(m_obj)
                                sig_params = [param for param in sig.parameters if param != "self"]
                                if set(sig_params) == set(param_names) or len(sig_params) == len(param_names):
                                    method_name = m_name
                                    break
                            except Exception:
                                pass
                    inst = _instantiate_class(custom_cls, kwargs, *args)
                    method = getattr(inst, method_name)
                    _inject_solution_globals(method)
                    if "queries" in kwargs and isinstance(kwargs["queries"], list):
                        return [
                            method(*q) if isinstance(q, (list, tuple)) else method(q)
                            for q in kwargs["queries"]
                        ]
                    try:
                        return method(*args, **kwargs)
                    except TypeError:
                        if kwargs and not args:
                            try:
                                return method(*kwargs.values())
                            except Exception:
                                pass
                        raise
                raise NoSolveFunction()
            return custom_class_runner

    raise NoSolveFunction()


def _load_python_optimal_solve(challenge: Any) -> tuple[Optional[Any], str]:
    spec = getattr(challenge, "_spec", None)
    if spec is None:
        return None, "No challenge spec is available for Python optimal timing."

    source = load_optimal_source(challenge.info.id, spec, language="python")
    if not source:
        return None, "No Python optimal reference file is available for timing."

    filename = f"{challenge.info.id}_optimal.py"
    namespace = _create_judge_namespace(f"optimal.{challenge.info.id}", filename)
    try:
        exec(  # noqa: S102 - internal optimal solution
            compile(source, filename, "exec", dont_inherit=True),
            namespace,
        )
    except Exception as exc:
        return None, f"Python optimal reference failed to load: {type(exc).__name__}: {exc}"

    try:
        solve_fn = _bind_leetcode_solution_runner(namespace, challenge=challenge)
        return solve_fn, ""
    except Exception as exc:
        return None, f"Python optimal reference failed to bind solve function: {exc}"


def _expected_for_case(
    *,
    reference_solve: Any | None,
    case: ValidatedCase,
    returns_in_place: bool = False,
    param_names: list[str] | tuple[str, ...] = (),
    tree_param_names: list[str] | tuple[str, ...] = (),
    tree_node_target_param_names: list[str] | tuple[str, ...] = (),
    list_node_param_names: list[str] | tuple[str, ...] = (),
    list_node_collection_param_names: list[str] | tuple[str, ...] = (),
    nary_node_param_names: list[str] | tuple[str, ...] = (),
    nary_node_collection_param_names: list[str] | tuple[str, ...] = (),
    random_binary_tree_param_names: list[str] | tuple[str, ...] = (),
    big_array_param_names: list[str] | tuple[str, ...] = (),
    returns_tree: bool = False,
    returns_list_node: bool = False,
) -> tuple[Any, str]:
    if case.expected is not None:
        return _normalize_validated_value(
            case.expected,
            returns_tree=returns_tree,
            returns_list_node=returns_list_node,
        ), ""
    if reference_solve is None:
        return None, "Custom input needs an optimal reference to compute the expected result."
    import copy

    try:
        kwargs = _prepare_validated_kwargs(
            copy.deepcopy(case.input),
            tree_param_names,
            list_node_param_names,
            list_node_collection_param_names,
            nary_node_param_names,
            nary_node_collection_param_names,
            random_binary_tree_param_names,
            tree_node_target_param_names,
            big_array_param_names,
        )
        result = reference_solve(**kwargs)
        return _actual_result(
            result,
            kwargs,
            case=case,
            returns_in_place=returns_in_place,
            param_names=param_names,
            returns_tree=returns_tree,
            returns_list_node=returns_list_node,
        ), ""
    except Exception as exc:
        return None, f"Reference failed on {case.name}: {type(exc).__name__}: {exc}"


def _run_python_solution_on_case(
    *,
    solve_fn: Any,
    reference_solve: Any | None,
    case: ValidatedCase,
    returns_in_place: bool = False,
    param_names: list[str] | tuple[str, ...] = (),
    tree_param_names: list[str] | tuple[str, ...] = (),
    tree_node_target_param_names: list[str] | tuple[str, ...] = (),
    list_node_param_names: list[str] | tuple[str, ...] = (),
    list_node_collection_param_names: list[str] | tuple[str, ...] = (),
    nary_node_param_names: list[str] | tuple[str, ...] = (),
    nary_node_collection_param_names: list[str] | tuple[str, ...] = (),
    random_binary_tree_param_names: list[str] | tuple[str, ...] = (),
    big_array_param_names: list[str] | tuple[str, ...] = (),
    returns_tree: bool = False,
    returns_list_node: bool = False,
    step_limit: int = _STEP_LIMIT,
) -> tuple[RunCaseResult, Any, Any, str, float | None]:
    import copy

    expected, expected_error = _expected_for_case(
        reference_solve=reference_solve,
        case=case,
        returns_in_place=returns_in_place,
        param_names=param_names,
        tree_param_names=tree_param_names,
        tree_node_target_param_names=tree_node_target_param_names,
        list_node_param_names=list_node_param_names,
        list_node_collection_param_names=list_node_collection_param_names,
        nary_node_param_names=nary_node_param_names,
        nary_node_collection_param_names=nary_node_collection_param_names,
        random_binary_tree_param_names=random_binary_tree_param_names,
        big_array_param_names=big_array_param_names,
        returns_tree=returns_tree,
        returns_list_node=returns_list_node,
    )
    if expected_error:
        return (
            RunCaseResult(
                id=case.id,
                name=case.name,
                kind=case.kind,
                correct=False,
                passed=False,
                message=expected_error,
                input_repr=_format_return_value(case.input),
                return_value_repr="",
                expected_repr=None,
                runtime_user_ms=None,
            ),
            None,
            expected,
            expected_error,
            None,
        )

    start = time.perf_counter()
    try:
        call_kwargs = _prepare_validated_kwargs(
            copy.deepcopy(case.input),
            tree_param_names,
            list_node_param_names,
            list_node_collection_param_names,
            nary_node_param_names,
            nary_node_collection_param_names,
            random_binary_tree_param_names,
            tree_node_target_param_names,
            big_array_param_names,
        )
        result, _trace = run_with_trace(
            solve_fn,
            call_kwargs,
            step_limit=(
                max(_RUNTIME_STEP_LIMIT, step_limit)
                if case.kind == "benchmark"
                else step_limit
            ),
            capture=False,
        )
        elapsed_ms = (time.perf_counter() - start) * 1000.0
        actual = _actual_result(
            result,
            call_kwargs,
            case=case,
            returns_in_place=returns_in_place,
            param_names=param_names,
            returns_tree=returns_tree,
            returns_list_node=returns_list_node,
        )
        correct = _validated_case_matches(case, actual, expected)
        message = "" if correct else "Incorrect solution: output did not match the validated expected result."
        return (
            RunCaseResult(
                id=case.id,
                name=case.name,
                kind=case.kind,
                correct=correct,
                passed=correct,
                message=message,
                input_repr=_format_return_value(case.input),
                return_value_repr=_format_return_value(actual),
                expected_repr=_format_return_value(expected),
                runtime_user_ms=elapsed_ms,
            ),
            actual,
            expected,
            message,
            elapsed_ms,
        )
    except ExecutionStepLimitExceeded as exc:
        elapsed_ms = (time.perf_counter() - start) * 1000.0
        return (
            RunCaseResult(
                id=case.id,
                name=case.name,
                kind=case.kind,
                correct=False,
                passed=False,
                message=str(exc),
                input_repr=_format_return_value(case.input),
                return_value_repr="",
                expected_repr=_format_return_value(expected),
                runtime_user_ms=elapsed_ms,
            ),
            None,
            expected,
            str(exc),
            elapsed_ms,
        )
    except Exception as exc:
        elapsed_ms = (time.perf_counter() - start) * 1000.0
        message = f"{type(exc).__name__}: {exc}"
        return (
            RunCaseResult(
                id=case.id,
                name=case.name,
                kind=case.kind,
                correct=False,
                passed=False,
                message=message,
                input_repr=_format_return_value(case.input),
                return_value_repr="",
                expected_repr=_format_return_value(expected),
                runtime_user_ms=elapsed_ms,
            ),
            None,
            expected,
            message,
            elapsed_ms,
        )


def _runtime_check_python_cases(
    *,
    solve_fn: Any,
    reference_solve: Any | None,
    cases: list[ValidatedCase],
    returns_in_place: bool = False,
    param_names: list[str] | tuple[str, ...] = (),
    tree_param_names: list[str] | tuple[str, ...] = (),
    tree_node_target_param_names: list[str] | tuple[str, ...] = (),
    list_node_param_names: list[str] | tuple[str, ...] = (),
    list_node_collection_param_names: list[str] | tuple[str, ...] = (),
    nary_node_param_names: list[str] | tuple[str, ...] = (),
    nary_node_collection_param_names: list[str] | tuple[str, ...] = (),
    random_binary_tree_param_names: list[str] | tuple[str, ...] = (),
    big_array_param_names: list[str] | tuple[str, ...] = (),
    returns_tree: bool = False,
    returns_list_node: bool = False,
    step_limit: int = _RUNTIME_STEP_LIMIT,
) -> RuntimeCheck:
    if reference_solve is None:
        return RuntimeCheck(
            checked=False,
            passed=False,
            n=len(cases),
            message="No Python optimal reference file is available for validated benchmark timing.",
        )
    if not cases:
        return RuntimeCheck(
            checked=False,
            passed=False,
            n=0,
            message="No validated benchmark cases are available.",
        )

    if len(cases) >= 2 and all(case.size is not None for case in cases):
        scaling_samples: list[dict[str, float | int]] = []
        trials = 0
        for case in sorted(cases, key=lambda item: int(item.size or 0)):
            measurement = _runtime_check_python_cases(
                solve_fn=solve_fn,
                reference_solve=reference_solve,
                cases=[case],
                returns_in_place=returns_in_place,
                param_names=param_names,
                tree_param_names=tree_param_names,
                tree_node_target_param_names=tree_node_target_param_names,
                list_node_param_names=list_node_param_names,
                list_node_collection_param_names=list_node_collection_param_names,
                nary_node_param_names=nary_node_param_names,
                nary_node_collection_param_names=nary_node_collection_param_names,
                random_binary_tree_param_names=random_binary_tree_param_names,
                big_array_param_names=big_array_param_names,
                returns_tree=returns_tree,
                returns_list_node=returns_list_node,
                step_limit=step_limit,
            )
            if not measurement.checked or not measurement.benchmark_correct:
                return measurement
            if measurement.user_ms is None or measurement.reference_ms is None or measurement.ratio is None:
                return RuntimeCheck(
                    checked=False,
                    passed=False,
                    n=int(case.size or 0),
                    message=f"Benchmark tier {case.id} did not produce comparable timings.",
                )
            trials = max(trials, measurement.trials)
            scaling_samples.append(
                {
                    "size": int(case.size or 0),
                    "user_ms": measurement.user_ms,
                    "reference_ms": measurement.reference_ms,
                    "ratio": measurement.ratio,
                }
            )
        return _runtime_check_from_scaling(scaling_samples, trials=trials, language="python")

    expected_by_case: dict[str, Any] = {}
    for case in cases:
        expected, expected_error = _expected_for_case(
            reference_solve=reference_solve,
            case=case,
            returns_in_place=returns_in_place,
            param_names=param_names,
            tree_param_names=tree_param_names,
            tree_node_target_param_names=tree_node_target_param_names,
            list_node_param_names=list_node_param_names,
            list_node_collection_param_names=list_node_collection_param_names,
            nary_node_param_names=nary_node_param_names,
            nary_node_collection_param_names=nary_node_collection_param_names,
            random_binary_tree_param_names=random_binary_tree_param_names,
            big_array_param_names=big_array_param_names,
            returns_tree=returns_tree,
            returns_list_node=returns_list_node,
        )
        if expected_error:
            return RuntimeCheck(
                checked=False,
                passed=False,
                n=len(cases),
                message=expected_error,
            )
        expected_by_case[case.id] = expected

    import copy

    def run_cases(func: Any, iterations: int) -> tuple[bool, float, str]:
        total_ms = 0.0
        for case in cases:
            expected = expected_by_case[case.id]
            try:
                result, elapsed_ms = _timed_reference_iterations(
                    func,
                    _prepare_validated_kwargs(
                        copy.deepcopy(case.input),
                        tree_param_names,
                        list_node_param_names,
                        list_node_collection_param_names,
                        nary_node_param_names,
                        nary_node_collection_param_names,
                        random_binary_tree_param_names,
                        tree_node_target_param_names,
                        big_array_param_names,
                    ),
                    iterations,
                    case=case,
                    returns_in_place=returns_in_place,
                    param_names=param_names,
                    returns_tree=returns_tree,
                    returns_list_node=returns_list_node,
                    step_limit=step_limit,
                )
            except Exception as exc:
                return False, total_ms, f"{type(exc).__name__}: {exc}"
            total_ms += elapsed_ms
            if not _validated_case_matches(case, result, expected):
                return False, total_ms, f"Output mismatched the expected result for {case.name}."
        return True, total_ms, ""

    # A short pilot determines one fixed amplification factor shared by both
    # implementations. The displayed values are normalized back to one
    # benchmark-suite execution, never the amplified aggregate.
    reference_ok, pilot_reference_ms, pilot_error = run_cases(reference_solve, 1)
    if not reference_ok:
        return RuntimeCheck(
            checked=False,
            passed=False,
            n=len(cases),
            message=f"Reference benchmark failed: {pilot_error}",
        )
    user_ok, pilot_user_ms, pilot_user_error = run_cases(solve_fn, 1)
    if not user_ok:
        return _runtime_check_from_times(
            user_ms=None,
            reference_ms=pilot_reference_ms,
            trials=0,
            n=len(cases),
            seed=None,
            language="python",
            benchmark_correct="Output mismatched" not in pilot_user_error,
            error_message=f"Benchmark failed: {pilot_user_error}",
        )
    runtime_iterations = _runtime_iterations_for_ms(max(pilot_reference_ms, pilot_user_ms))

    reference_times: list[float] = []
    user_times: list[float] = []
    wall_start = time.perf_counter()
    trial = 0
    while (
        trial < _RUNTIME_MIN_TRIALS
        or (
            sum(reference_times) * runtime_iterations / 1000.0 < _RUNTIME_TARGET_SECONDS
            and trial < _RUNTIME_MAX_TRIALS
            and time.perf_counter() - wall_start < _RUNTIME_MAX_WALL_SECONDS
        )
    ):
        # Alternate the order so interpreter caches, GC pressure, and CPU
        # frequency changes cannot consistently favor the reference or user.
        ordered = (
            (("reference", reference_solve), ("user", solve_fn))
            if trial % 2 == 0
            else (("user", solve_fn), ("reference", reference_solve))
        )
        timings: dict[str, float] = {}
        for label, func in ordered:
            ok, total_ms, error = run_cases(func, runtime_iterations)
            if not ok:
                if label == "reference":
                    return RuntimeCheck(
                        checked=False,
                        passed=False,
                        n=len(cases),
                        message=f"Reference benchmark failed: {error}",
                    )
                return _runtime_check_from_times(
                    user_ms=None,
                    reference_ms=_median(reference_times),
                    trials=trial,
                    n=len(cases),
                    seed=None,
                    language="python",
                    benchmark_correct="Output mismatched" not in error,
                    error_message=f"Benchmark failed: {error}",
                )
            timings[label] = total_ms / runtime_iterations
        reference_times.append(timings["reference"])
        user_times.append(timings["user"])
        trial += 1

    reference_ms = _median(reference_times)
    paired_ratios = [
        user_ms / ref_ms
        for user_ms, ref_ms in zip(user_times, reference_times)
        if ref_ms > 0
    ]
    ratio = _median(paired_ratios)
    user_ms = reference_ms * ratio if reference_ms is not None and ratio is not None else _median(user_times)
    return _runtime_check_from_times(
        user_ms=user_ms,
        reference_ms=reference_ms,
        trials=trial,
        n=len(cases),
        seed=None,
        language="python",
    )


def _runtime_check_from_scaling(
    samples: list[dict[str, float | int]],
    *,
    trials: int,
    language: str,
) -> RuntimeCheck:
    del language
    ordered = sorted(samples, key=lambda sample: int(sample["size"]))
    largest = ordered[-1]
    xs = [math.log(max(1, int(sample["size"]))) for sample in ordered]
    ys = [math.log(max(1e-9, float(sample["ratio"]))) for sample in ordered]
    mean_x = sum(xs) / len(xs)
    mean_y = sum(ys) / len(ys)
    denominator = sum((value - mean_x) ** 2 for value in xs)
    extra_exponent = (
        sum((x_value - mean_x) * (y_value - mean_y) for x_value, y_value in zip(xs, ys)) / denominator
        if denominator > 0
        else float("inf")
    )
    largest_ratio = float(largest["ratio"])
    passed = (
        extra_exponent <= _RUNTIME_SCALING_MAX_EXTRA_EXPONENT
        and largest_ratio <= _RUNTIME_SCALING_MAX_CONSTANT_RATIO
    )
    if passed:
        message = (
            f"Scaling OK: extra growth exponent {extra_exponent:+.2f} <= "
            f"{_RUNTIME_SCALING_MAX_EXTRA_EXPONENT:.2f}; largest runtime ratio {largest_ratio:.2f}x."
        )
    else:
        reasons: list[str] = []
        if extra_exponent > _RUNTIME_SCALING_MAX_EXTRA_EXPONENT:
            reasons.append(
                f"relative growth exponent {extra_exponent:+.2f} exceeds "
                f"{_RUNTIME_SCALING_MAX_EXTRA_EXPONENT:.2f}"
            )
        if largest_ratio > _RUNTIME_SCALING_MAX_CONSTANT_RATIO:
            reasons.append(
                f"largest runtime ratio {largest_ratio:.2f}x exceeds "
                f"{_RUNTIME_SCALING_MAX_CONSTANT_RATIO:.0f}x"
            )
        message = f"Scaling too slow: {'; '.join(reasons)}."
    reference_ms = float(largest["reference_ms"])
    user_ms = float(largest["user_ms"])
    return RuntimeCheck(
        checked=True,
        passed=passed,
        user_ms=user_ms,
        reference_ms=reference_ms,
        ratio=largest_ratio,
        limit_ms=reference_ms * _RUNTIME_SCALING_MAX_CONSTANT_RATIO,
        trials=trials,
        n=int(largest["size"]),
        seed=None,
        message=message,
        benchmark_correct=True,
        scaling_data=ordered,
    )


def _case_counts_toward_verdict(case: ValidatedCase, mode: str) -> bool:
    """Return whether a case controls the submission verdict.

    Custom cases remain fully executed and reported during a real run, but
    they are user-authored diagnostics rather than part of the official judge.
    """

    return mode != "real_test" or case.kind != "custom"


def _verdict_case_results(
    run_cases: list[ValidatedCase],
    case_results: list[RunCaseResult],
    mode: str,
) -> list[RunCaseResult]:
    return [
        case_result
        for case, case_result in zip(run_cases, case_results)
        if _case_counts_toward_verdict(case, mode)
    ]


def _headline_case_result(
    run_cases: list[ValidatedCase],
    case_results: list[RunCaseResult],
    mode: str,
) -> RunCaseResult | None:
    verdict_results = _verdict_case_results(run_cases, case_results, mode)
    return next(
        (case_result for case_result in verdict_results if not case_result.correct),
        verdict_results[0] if verdict_results else None,
    )


def _run_python_validated_cases(
    *,
    challenge: Any,
    solution_path: Path,
    n: int,
    seed: Optional[int],
    mode: str,
    run_cases: list[ValidatedCase],
    benchmark_cases: list[ValidatedCase],
) -> RunResponse:
    try:
        player_filename = str(solution_path)
        player_source = solution_path.read_text(encoding="utf-8")
        namespace = _create_judge_namespace("player_solution", player_filename)
        exec(  # noqa: S102 - player solution is intentionally executed by the local judge
            compile(player_source, player_filename, "exec", dont_inherit=True),
            namespace,
        )
    except SyntaxError as exc:
        raise PlayerSyntaxError(exc) from exc

    try:
        solve_fn = _bind_leetcode_solution_runner(namespace, challenge=challenge)
    except Exception as exc:
        raise PlayerSyntaxError(SyntaxError(f"Could not bind solution entry point: {exc}"))
    reference_solve, reference_error = _load_python_optimal_solve(challenge)
    if reference_solve is None and reference_error:
        log.debug("No optimal reference available for validated cases: %s", reference_error)
    spec = getattr(challenge, "_spec", None)
    returns_in_place = _returns_in_place(str(getattr(spec, "returns", "") or ""), spec=spec)
    returns_tree = _returns_tree(str(getattr(spec, "returns", "") or ""))
    returns_list_node = _returns_list_node(str(getattr(spec, "returns", "") or ""))
    param_names = list(_get_spec_inputs(spec).keys()) if spec else list(getattr(spec, "params", []) or [])
    tree_param_names = _tree_param_names(spec)
    tree_node_target_param_names = _tree_node_target_param_names(spec)
    list_node_param_names = _list_node_param_names(spec)
    list_node_collection_param_names = _list_node_collection_param_names(spec)
    nary_node_param_names = _nary_node_param_names(spec)
    nary_node_collection_param_names = _nary_node_collection_param_names(spec)
    random_binary_tree_param_names = _random_binary_tree_param_names(spec)
    big_array_param_names = _big_array_param_names(spec)

    case_results: list[RunCaseResult] = []
    first_result: Any = None
    first_expected: Any = None
    error_message = ""
    certificate_complete = leetcode_complexity_certificate_status(challenge.info.id).complete
    case_step_limit = _VALIDATED_CASE_STEP_LIMIT_OVERRIDES.get(
        challenge.info.id,
        _RUNTIME_STEP_LIMIT if certificate_complete else _STEP_LIMIT,
    )
    for case in run_cases:
        case_result, result, expected, message, _elapsed_ms = _run_python_solution_on_case(
            solve_fn=solve_fn,
            reference_solve=reference_solve,
            case=case,
            returns_in_place=returns_in_place,
            param_names=param_names,
            tree_param_names=tree_param_names,
            tree_node_target_param_names=tree_node_target_param_names,
            list_node_param_names=list_node_param_names,
            list_node_collection_param_names=list_node_collection_param_names,
            nary_node_param_names=nary_node_param_names,
            nary_node_collection_param_names=nary_node_collection_param_names,
            random_binary_tree_param_names=random_binary_tree_param_names,
            big_array_param_names=big_array_param_names,
            returns_tree=returns_tree,
            returns_list_node=returns_list_node,
            step_limit=case_step_limit,
        )
        case_results.append(case_result)
        if first_result is None and result is not None:
            first_result = result
        if first_expected is None and expected is not None:
            first_expected = expected
        if (
            not case_result.correct
            and _case_counts_toward_verdict(case, mode)
            and not error_message
        ):
            error_message = message or case_result.message

    verdict_results = _verdict_case_results(run_cases, case_results, mode)
    correct = (
        bool(verdict_results)
        and all(case.correct for case in verdict_results)
        and len(case_results) == len(run_cases)
    )
    runtime_check = RuntimeCheck(checked=False, passed=False, message=error_message)
    complexity_check = ComplexityCheck()
    if correct and certificate_complete:
        complexity_check = _complexity_certificate_check(challenge.info.id)
    elif correct and benchmark_cases:
        runtime_check = _runtime_check_python_cases(
            solve_fn=solve_fn,
            reference_solve=reference_solve,
            cases=benchmark_cases,
            returns_in_place=returns_in_place,
            param_names=param_names,
            tree_param_names=tree_param_names,
            tree_node_target_param_names=tree_node_target_param_names,
            list_node_param_names=list_node_param_names,
            list_node_collection_param_names=list_node_collection_param_names,
            nary_node_param_names=nary_node_param_names,
            nary_node_collection_param_names=nary_node_collection_param_names,
            random_binary_tree_param_names=random_binary_tree_param_names,
            big_array_param_names=big_array_param_names,
            returns_tree=returns_tree,
            returns_list_node=returns_list_node,
            step_limit=max(_RUNTIME_STEP_LIMIT, case_step_limit),
        )
    elif correct:
        complexity_check = _complexity_certificate_check(challenge.info.id)

    required_complexity = challenge.info.required_complexity
    within_threshold = (
        runtime_check.passed
        if runtime_check.checked
        else complexity_check.passed
        if complexity_check.checked
        else False
    )
    passed = correct and within_threshold
    message = _build_message(
        error_message=error_message,
        correct=correct,
        within_threshold=within_threshold,
        runtime_check=runtime_check,
        actual_complexity=required_complexity.value,
        required_complexity=required_complexity,
    )
    headline_case = _headline_case_result(run_cases, case_results, mode)

    return RunResponse(
        passed=passed,
        correct=correct,
        within_threshold=within_threshold,
        actual_complexity=required_complexity.value,
        required_complexity=required_complexity.value,
        mode=mode,
        too_efficient=False,
        too_efficient_reason="",
        user_ast_ops=None,
        reference_ast_ops=None,
        reference_ci_low=None,
        reference_ci_high=None,
        reference_coefficient=None,
        scaling_data=[],
        runtime_check=runtime_check.checked,
        runtime_passed=runtime_check.passed if runtime_check.checked else None,
        runtime_user_ms=runtime_check.user_ms,
        runtime_reference_ms=runtime_check.reference_ms,
        runtime_ratio=runtime_check.ratio,
        runtime_limit_ms=runtime_check.limit_ms,
        runtime_trials=runtime_check.trials,
        runtime_message=runtime_check.message,
        benchmark_correct=runtime_check.benchmark_correct,
        runtime_scaling_data=runtime_check.scaling_data,
        complexity_check=complexity_check.checked,
        complexity_passed=complexity_check.passed if complexity_check.checked else None,
        complexity_method=complexity_check.method,
        complexity_message=complexity_check.message,
        message=message,
        return_value_repr=headline_case.return_value_repr if headline_case else "",
        reference_return_value_repr=headline_case.expected_repr if headline_case else _format_return_value(first_expected),
        setup_data_repr={
            key: _format_return_value(value)
            for key, value in (run_cases[0].input if run_cases else {}).items()
        },
        case_results=case_results,
        selected_case_ids=[case.id for case in run_cases],
    )


def _runtime_check_python_function(
    *,
    challenge: Any,
    solution_path: Path,
    n: int,
    seed: Optional[int],
) -> RuntimeCheck:
    challenge_cls = type(challenge)
    bench_n = _benchmark_n(challenge, n)
    bench_seed = seed if seed is not None else 1
    reference_solve, reference_error = _load_python_optimal_solve(challenge)
    if reference_solve is None:
        return RuntimeCheck(
            checked=False,
            passed=False,
            n=bench_n,
            seed=bench_seed,
            message=reference_error,
        )

    try:
        namespace = runpy.run_path(str(solution_path), run_name="player_solution_benchmark")
        solve_fn = _bind_leetcode_solution_runner(namespace, challenge=challenge)
    except Exception as exc:
        return RuntimeCheck(
            checked=True,
            passed=False,
            n=bench_n,
            seed=bench_seed,
            message=f"Benchmark could not load the user solution: {type(exc).__name__}: {exc}",
        )
    if not callable(solve_fn):
        return RuntimeCheck(
            checked=True,
            passed=False,
            n=bench_n,
            seed=bench_seed,
            message="Benchmark could not find a solve() function.",
        )

    reference_times: list[float] = []
    user_times: list[float] = []
    wall_start = time.perf_counter()
    runtime_iterations = 1

    while (
        len(reference_times) < _RUNTIME_MIN_TRIALS
        or (
            sum(reference_times) / 1000.0 < _RUNTIME_TARGET_SECONDS
            and len(reference_times) < _RUNTIME_MAX_TRIALS
            and time.perf_counter() - wall_start < _RUNTIME_MAX_WALL_SECONDS
        )
    ):
        ref_challenge = challenge_cls()
        ref_challenge._n = bench_n
        ref_challenge._seed = bench_seed
        ref_setup = ref_challenge.setup(bench_n, bench_seed)
        try:
            ref_result, ref_ms = _timed_reference_iterations(reference_solve, ref_setup, runtime_iterations)
            suggested_iterations = _runtime_iterations_for_ms(ref_ms / max(1, runtime_iterations))
            if suggested_iterations > runtime_iterations:
                runtime_iterations = suggested_iterations
                ref_result, ref_ms = _timed_reference_iterations(reference_solve, ref_setup, runtime_iterations)
            reference_times.append(ref_ms)
            if not ref_challenge.verify(ref_result):
                return RuntimeCheck(
                    checked=False,
                    passed=False,
                    n=bench_n,
                    seed=bench_seed,
                    message="Python optimal reference failed the hidden benchmark input.",
                )
        except Exception as exc:
            return RuntimeCheck(
                checked=False,
                passed=False,
                n=bench_n,
                seed=bench_seed,
                message=f"Reference benchmark failed: {type(exc).__name__}: {exc}",
            )

        user_challenge = challenge_cls()
        user_challenge._n = bench_n
        user_challenge._seed = bench_seed
        user_setup = user_challenge.setup(bench_n, bench_seed)
        try:
            user_result, user_ms = _timed_reference_iterations(solve_fn, user_setup, runtime_iterations)
            user_times.append(user_ms)
            user_ok = user_challenge.verify(user_result)
        except ExecutionStepLimitExceeded as exc:
            return _runtime_check_from_times(
                user_ms=_runtime_limit_ms(_median(reference_times), "python") + 1.0,
                reference_ms=_median(reference_times),
                trials=len(reference_times),
                n=bench_n,
                seed=bench_seed,
                language="python",
                error_message=str(exc),
            )
        except Exception as exc:
            return _runtime_check_from_times(
                user_ms=None,
                reference_ms=_median(reference_times),
                trials=len(reference_times),
                n=bench_n,
                seed=bench_seed,
                language="python",
                error_message=f"Benchmark crashed: {type(exc).__name__}: {exc}",
            )
        if not user_ok:
            return _runtime_check_from_times(
                user_ms=_median(user_times),
                reference_ms=_median(reference_times),
                trials=len(reference_times),
                n=bench_n,
                seed=bench_seed,
                language="python",
                benchmark_correct=False,
            )

    return _runtime_check_from_times(
        user_ms=_median(user_times),
        reference_ms=_median(reference_times),
        trials=len(reference_times),
        n=bench_n,
        seed=bench_seed,
        language="python",
    )


def _runtime_check_external_function(
    *,
    challenge: Any,
    source: str,
    language: str,
    n: int,
    seed: Optional[int],
) -> RuntimeCheck:
    challenge_cls = type(challenge)
    bench_n = _benchmark_n(challenge, n)
    bench_seed = seed if seed is not None else 1

    bench_challenge = challenge_cls()
    bench_challenge._n = bench_n
    bench_challenge._seed = bench_seed
    setup_data = bench_challenge.setup(bench_n, bench_seed)
    spec = getattr(bench_challenge, "_spec", None)
    param_names = list(getattr(spec, "params", []) or setup_data.keys())
    param_hints = dict(getattr(spec, "inputs", {}) or {})
    returns_hint = str(getattr(spec, "returns", "") or "")
    in_place = _returns_in_place(returns_hint)
    if spec is None:
        return RuntimeCheck(
            checked=False,
            n=bench_n,
            seed=bench_seed,
            message="No challenge spec is available for same-language timing.",
        )

    reference_source = load_optimal_source(
        bench_challenge.info.id,
        spec,
        language=language,
    )
    if not reference_source:
        return RuntimeCheck(
            checked=False,
            passed=False,
            n=bench_n,
            seed=bench_seed,
            message=f"No {language} optimal reference is available for timing.",
        )

    input_json = json.dumps(setup_data)
    reference_result = run_function_program(
        language=language,
        source=reference_source,
        input_json=input_json,
        param_names=param_names,
        param_hints=param_hints,
        returns_hint=returns_hint,
        timeout_seconds=_RUNTIME_EXTERNAL_TIMEOUT_SECONDS,
        measure_runtime=True,
    )
    if reference_result.error_message:
        return RuntimeCheck(
            checked=False,
            n=bench_n,
            seed=bench_seed,
            message=f"Same-language reference benchmark failed: {reference_result.error_message}",
        )
    reference_ms = reference_result.runtime_ms
    if reference_ms is None:
        return RuntimeCheck(
            checked=False,
            n=bench_n,
            seed=bench_seed,
            message="Same-language reference did not report internal runtime.",
        )
    try:
        ref_raw_result = _last_non_empty_line(reference_result.stdout)
        ref_result = json.loads(ref_raw_result) if ref_raw_result else None
        ref_result = _restore_external_json_value(ref_result)
        bench_challenge.verify(ref_result)
    except Exception as exc:
        return RuntimeCheck(
            checked=False,
            n=bench_n,
            seed=bench_seed,
            message=f"Same-language reference produced an invalid result: {type(exc).__name__}: {exc}",
        )

    runtime_iterations = _runtime_iterations_for_ms(reference_ms) if language == "javascript" and not in_place else 1
    if runtime_iterations > 1:
        reference_result = run_function_program(
            language=language,
            source=reference_source,
            input_json=input_json,
            param_names=param_names,
            param_hints=param_hints,
            returns_hint=returns_hint,
            timeout_seconds=_RUNTIME_EXTERNAL_TIMEOUT_SECONDS,
            measure_runtime=True,
            runtime_iterations=runtime_iterations,
        )
        if reference_result.error_message:
            return RuntimeCheck(
                checked=False,
                n=bench_n,
                seed=bench_seed,
                message=f"Same-language reference benchmark failed: {reference_result.error_message}",
            )
        reference_ms = reference_result.runtime_ms
        if reference_ms is None:
            return RuntimeCheck(
                checked=False,
                n=bench_n,
                seed=bench_seed,
                message="Same-language reference did not report internal runtime.",
            )

    external_result = run_function_program(
        language=language,
        source=source,
        input_json=input_json,
        param_names=param_names,
        param_hints=param_hints,
        returns_hint=returns_hint,
        timeout_seconds=_RUNTIME_EXTERNAL_TIMEOUT_SECONDS,
        measure_runtime=True,
        runtime_iterations=runtime_iterations,
    )
    user_ms = external_result.runtime_ms
    if external_result.error_message:
        return _runtime_check_from_times(
            user_ms=user_ms,
            reference_ms=reference_ms,
            trials=1,
            n=bench_n,
            seed=bench_seed,
            language=language,
            error_message=external_result.error_message,
        )
    if user_ms is None:
        return _runtime_check_from_times(
            user_ms=None,
            reference_ms=reference_ms,
            trials=1,
            n=bench_n,
            seed=bench_seed,
            language=language,
            error_message="Benchmark did not report internal runtime.",
        )

    raw_result = _last_non_empty_line(external_result.stdout)
    try:
        result = json.loads(raw_result) if raw_result else None
        result = _restore_external_json_value(result)
        benchmark_correct = bench_challenge.verify(result)
    except Exception:
        benchmark_correct = False

    return _runtime_check_from_times(
        user_ms=user_ms,
        reference_ms=reference_ms,
        trials=1,
        n=bench_n,
        seed=bench_seed,
        language=language,
        benchmark_correct=benchmark_correct,
    )


class ChallengeNotFound(Exception):
    """The challenge_id is not in the registry."""

    def __init__(self, challenge_id: str):
        self.challenge_id = challenge_id
        super().__init__(f"Challenge '{challenge_id}' not found")


class NTooLarge(Exception):
    """The requested n exceeds the challenge's max_n."""

    def __init__(self, requested: int, maximum: int):
        self.requested = requested
        self.maximum = maximum
        super().__init__(f"n={requested} exceeds max_n={maximum} for this challenge")


class PlayerSyntaxError(Exception):
    """The player's source failed to parse (SyntaxError during compile)."""

    def __init__(self, exc: SyntaxError):
        self.exc = exc
        super().__init__(f"SyntaxError: {exc.msg} (line {exc.lineno}, offset {exc.offset})")


class NoSolveFunction(Exception):
    """The player's source compiled but did not define a top-level `def solve`."""

    def __init__(self):
        super().__init__("Player source must define a top-level `def solve(**kwargs)`")


class UnsupportedLanguageExecution(Exception):
    """The requested language is not wired for this challenge shape yet."""

    def __init__(self, language: str, challenge_id: str):
        self.language = language
        self.challenge_id = challenge_id
        super().__init__(
            f"{language} execution is not wired for challenge '{challenge_id}'."
        )


# ----------------------------------------------------------------------------
# The main entry point.
# ----------------------------------------------------------------------------


def run_player_code(
    challenge_id: str,
    source: str,
    n: int = 16,
    seed: Optional[int] = None,
    mode: str = "practice",
    execution_path: Optional[str] = None,
    language: str = "python",
    run_cases: Optional[list[ValidatedCase]] = None,
    benchmark_cases: Optional[list[ValidatedCase]] = None,
) -> RunResponse:
    """Run a player's source against a challenge and return the structured result.

    Parameters
    ----------
    challenge_id:
        Must be a key in :data:`CHALLENGE_REGISTRY`.
    source:
        Full Python source. Must define ``def solve(**kwargs)``.
    n:
        Legacy synthetic input size. Ignored when validated cases are passed.
    seed:
        Legacy synthetic RNG seed. Ignored when validated cases are passed.
    mode:
        Echoed back in the response. "practice" or "real_test".
    execution_path:
        Optional workspace path to execute from. When provided,
        ``runpy.run_path`` runs this exact path instead of a
        tempfile copy, so debugpy breakpoints in the player's
        the active ``user_solutions/python_vN.py`` hit normally. Used by direct debug
        entry points such as ``tools/run_solution.py``; the
        FastAPI route (which receives only the source text from
        the renderer) leaves this ``None`` and gets the temp-file
        behaviour.

    Returns
    -------
    :class:`RunResponse`
        All the data the frontend needs: the pass/fail verdict, selected
        case results, compact return-value representation, and calibrated
        runtime numbers for the Complexity tab.

    Raises
    ------
    ChallengeNotFound, NTooLarge, PlayerSyntaxError, NoSolveFunction
        Translated to 404 / 422 / 422 / 400 by the route layer.
    """
    language_id = normalize_language(language)

    # --- 1. Resolve challenge ---
    challenge_cls = CHALLENGE_REGISTRY.get(challenge_id)
    if challenge_cls is None:
        raise ChallengeNotFound(challenge_id)
    challenge = challenge_cls()
    spec = getattr(challenge, "_spec", None)
    reference_metadata = getattr(spec, "reference_metadata", {}) or {}
    special_category = str(reference_metadata.get("category") or "").lower()
    if run_cases is None and n > challenge.max_n:
        raise NTooLarge(n, challenge.max_n)

    # --- 2. Stage the source. By default we write it to a fresh
    #        temp dir so the tracer sees a unique ``co_filename``
    #        per run (avoids cache collisions between concurrent
    #        runs of the same challenge). When ``execution_path``
    #        is given by a direct debug entry point, we skip the
    #        temp file and run from that exact path so debugpy hits
    #        breakpoints in the player's open editor file.
    # NOTE: No source wrapping / AST rewriting is performed here. The
    # player source is exec'd verbatim via ``runpy.run_path``. The
    # engine's tracking proxies (TrackedList, TrackedGrid, ...) were
    # removed in v0.8.5; the player's input is now a plain list /
    # dict / set. What the user sees in the editor is exactly what
    # runs.
    tmpdir: Path | None = None
    if execution_path is not None:
        # Caller (typically tools/run_solution.py) wants the source
        # to execute from the workspace path so debugpy breakpoints
        # in the open editor file hit. ``runpy.run_path`` reads the
        # file from disk; we don't write to it.
        solution_path = Path(execution_path)
        if not solution_path.is_file():
            raise PlayerSyntaxError(
                SyntaxError(
                    f"Solution file not found on disk: {solution_path}",
                    (str(solution_path), 0, 0, ""),
                )
            )
    else:
        tmpdir = Path(tempfile.mkdtemp(prefix="coden-run-"))
        solution_path = tmpdir / f"solution.{language_extension(language_id)}"
        solution_path.write_text(source, encoding="utf-8")

    try:
        if run_cases is not None and special_category in {"concurrency", "database", "pandas", "shell"}:
            return _run_special_environment_cases(
                challenge=challenge,
                source=source,
                mode=mode,
                category=special_category,
                run_cases=run_cases,
            )
        if run_cases is not None and language_id != "python":
            return _run_external_validated_cases(
                challenge=challenge,
                source=source,
                mode=mode,
                language=language_id,
                run_cases=run_cases,
                benchmark_cases=benchmark_cases if benchmark_cases is not None else run_cases,
            )

        if language_id != "python":
            return _run_external_function_player(
                challenge=challenge,
                source=source,
                n=n,
                seed=seed,
                mode=mode,
                language=language_id,
            )

        if run_cases is not None:
            return _run_python_validated_cases(
                challenge=challenge,
                solution_path=solution_path,
                n=n,
                seed=seed,
                mode=mode,
                run_cases=run_cases,
                benchmark_cases=benchmark_cases if benchmark_cases is not None else run_cases,
            )

        # --- 3. Exec the source in a fresh namespace ---
        try:
            namespace = runpy.run_path(str(solution_path), run_name="player_solution")
        except SyntaxError as exc:
            raise PlayerSyntaxError(exc) from exc

        try:
            solve_fn = _bind_leetcode_solution_runner(namespace, challenge=challenge)
        except Exception:
            raise NoSolveFunction()

        # --- 4. Set per-run instance state on the challenge ---
        challenge._n = n
        challenge._seed = seed

        # --- 5. Setup the challenge (returns plain lists / dicts) ---
        setup_data = challenge.setup(n, seed)

        # Capture pristine setup data representation before user solve mutates it in-place.
        setup_data_repr = {
            k: _format_return_value(v) for k, v in setup_data.items()
        }

        # Deep-copy setup data for the reference solve before the player's
        # code (which might perform in-place mutations) executes.
        import copy
        reference_return_value_repr: Optional[str] = None
        reference_solve, reference_error = _load_python_optimal_solve(challenge)
        if reference_solve is not None:
            try:
                ref_setup_data = copy.deepcopy(setup_data)
                ref_result = reference_solve(**ref_setup_data)
                reference_return_value_repr = _format_return_value(ref_result)
            except Exception as exc:
                log.warning("Failed to run optimal reference solve: %s", exc)
        elif reference_error:
            log.debug("No optimal reference value available: %s", reference_error)

        # --- 6. Run the player's solve() under the tracer ---
        error_message = ""
        result: Any = None
        # Initialize trace to an empty trace so the post-run
        # handling (serialization, message construction) can
        # always read ``trace.frames`` even if run_with_trace
        # raises before assigning. The empty trace carries no
        # frames, so the visualizer just shows "no trace".
        trace = ExecutionTrace()
        try:
            result, trace = run_with_trace(
                solve_fn,
                setup_data,
                step_limit=_STEP_LIMIT,
            )
        except ExecutionStepLimitExceeded as exc:
            error_message = str(exc)
        except Exception as exc:
            # Player code crashed. Surface a friendly message; the
            # trace is whatever was captured before the crash.
            error_message = f"{type(exc).__name__}: {exc}"

        # --- 7. Verify correctness (if the run didn't already fail) ---
        correct = False
        if not error_message:
            try:
                correct = challenge.verify(result)
            except Exception as exc:
                error_message = f"Could not verify: {type(exc).__name__}: {exc}"
                correct = False

        # --- 8. Runtime benchmark against the optimal reference ---
        runtime_check = RuntimeCheck(checked=False, passed=False, message=error_message)
        if correct:
            runtime_check = _runtime_check_python_function(
                challenge=challenge,
                solution_path=solution_path,
                n=n,
                seed=seed,
            )

        # --- 9. Static source heuristics (not the verdict gate) ---
        # We count ops by walking the AST of BOTH the user's
        # source and the reference's source. The result is a
        # deterministic integer per (source, n) pair. No
        # dynamic counter, no proxies â€” what the user sees
        # in the editor is exactly what gets counted.
        user_ast_ops: Optional[int] = None
        spec = getattr(challenge, "_spec", None)
        reference_source = (spec.source if spec is not None else None) or ""
        reference_ast_ops: Optional[int] = None

        # --- 10. Derive the verdict from the runtime check ---
        required_complexity = challenge.info.required_complexity

        # --- 9a. Compute tolerance band around reference's AST ops ---
        # The user's AST count should land within this band
        # to be considered "as efficient as the reference".
        #   low  = floor(Î¼ * 0.90)
        #   high = ceil (Î¼ * 1.05)
        # Below the band: likely a cheat. Above the band:
        # correct but slower than optimal. The band is the
        # "as good as the canonical solution" range.
        reference_ci_low: Optional[int] = None
        reference_ci_high: Optional[int] = None

        within_threshold = runtime_check.passed if runtime_check.checked else False

        actual_complexity = required_complexity.value
        passed = correct and within_threshold

        # --- 11. Too-efficient check (targeted hardcoding/private-state scan) ---
        # If the user's AST count is < 30% of the
        # reference's AST count, they probably skipped work
        # (or hardcoded an answer). The check is purely
        # structural â€” no runtime data needed.
        too_efficient = False
        too_efficient_reason = ""

        # --- 12. Compute reference coefficient ---
        reference_coefficient: Optional[float] = None
        if False and reference_ast_ops is not None and reference_ast_ops > 0:
            from engine.counter import get_complexity_factor
            ref_factor = get_complexity_factor(n, required_complexity)
            reference_coefficient = (reference_ast_ops - 10) / ref_factor if ref_factor > 0 else 0.0
            reference_coefficient = max(0.0, reference_coefficient)

        message = _build_message(
            error_message=error_message,
            correct=correct,
            within_threshold=within_threshold,
            user_ast_ops=user_ast_ops,
            actual_complexity=actual_complexity,
            required_complexity=required_complexity,
            runtime_check=runtime_check,
            too_efficient=too_efficient,
            too_efficient_reason=too_efficient_reason,
        )

        # --- 12. Render the return value as a compact string. ---
        # The trace's ``return_value`` is what the tracer captured
        # for the top-level ``solve()`` call; if the tracer didn't
        # run (e.g. ``solve`` wasn't defined), fall back to the
        # raw return. Cap at _RETURN_VALUE_CAP so a 10,000-element
        # list doesn't blow up the response.
        return_value_repr = _format_return_value(result)

        scaling_data = []

        return RunResponse(
            passed=passed,
            correct=correct,
            within_threshold=within_threshold,
            actual_complexity=actual_complexity,
            required_complexity=required_complexity.value,
            mode=mode,
            too_efficient=too_efficient,
            too_efficient_reason=too_efficient_reason,
            user_ast_ops=user_ast_ops,
            reference_ast_ops=reference_ast_ops,
            reference_ci_low=reference_ci_low,
            reference_ci_high=reference_ci_high,
            reference_coefficient=reference_coefficient,
            scaling_data=scaling_data,
            runtime_check=runtime_check.checked,
            runtime_passed=runtime_check.passed if runtime_check.checked else None,
            runtime_user_ms=runtime_check.user_ms,
            runtime_reference_ms=runtime_check.reference_ms,
            runtime_ratio=runtime_check.ratio,
            runtime_limit_ms=runtime_check.limit_ms,
            runtime_trials=runtime_check.trials,
            runtime_message=runtime_check.message,
            benchmark_correct=runtime_check.benchmark_correct,
            runtime_scaling_data=runtime_check.scaling_data,
            message=message,
            return_value_repr=return_value_repr,
            reference_return_value_repr=reference_return_value_repr,
            setup_data_repr=setup_data_repr,
        )
    finally:
        # Always clean up the temp dir, even on exception. Skip
        # when we ran from an explicit ``execution_path`` (no
        # temp dir was created).
        if tmpdir is not None:
            shutil.rmtree(tmpdir, ignore_errors=True)


def _runtime_check_database_cases(
    *,
    challenge: Any,
    source: str,
    cases: list[ValidatedCase],
) -> RuntimeCheck:
    if len(cases) < 2 or any(case.size is None or case.size <= 0 for case in cases):
        return RuntimeCheck(
            checked=False,
            passed=False,
            message="Database scaling requires at least two positive-size benchmark tiers.",
        )

    spec = getattr(challenge, "_spec", None)
    if spec is None:
        return RuntimeCheck(checked=False, passed=False, message="No challenge spec is available for SQL timing.")
    reference_source = load_optimal_source(challenge.info.id, spec, language="sql")
    if not reference_source:
        return RuntimeCheck(
            checked=False,
            passed=False,
            message="No SQL optimal reference is available for timing.",
        )

    samples: list[dict[str, float | int]] = []
    trials = _RUNTIME_MAX_TRIALS
    for case in sorted(cases, key=lambda item: int(item.size or 0)):
        reference_times: list[float] = []
        user_times: list[float] = []
        for trial in range(trials):
            ordered_sources = (
                (("reference", reference_source), ("user", source))
                if trial % 2 == 0
                else (("user", source), ("reference", reference_source))
            )
            timings: dict[str, float] = {}
            for label, candidate_source in ordered_sources:
                result = run_special_environment(
                    category="database",
                    source=candidate_source,
                    input_data=case.input,
                    timeout_seconds=max(0.1, (case.timeout_ms or 8000) / 1000.0),
                )
                if not result.ok:
                    return RuntimeCheck(
                        checked=False,
                        passed=False,
                        n=int(case.size or 0),
                        message=f"{label.title()} SQL benchmark failed: {result.error_message}",
                    )
                if case.expected is not None and not _validated_case_matches(case, result.value, case.expected):
                    if label == "reference":
                        return RuntimeCheck(
                            checked=False,
                            passed=False,
                            n=int(case.size or 0),
                            trials=trial,
                            message=f"Reference SQL benchmark output mismatched on {case.id}.",
                        )
                    return RuntimeCheck(
                        checked=True,
                        passed=False,
                        n=int(case.size or 0),
                        trials=trial,
                        message=f"User SQL benchmark output mismatched on {case.id}.",
                        benchmark_correct=False,
                    )
                timings[label] = float(result.runtime_ms or 0.0)
            reference_times.append(timings["reference"])
            user_times.append(timings["user"])

        reference_ms = _median(reference_times)
        paired_ratios = [
            user_ms / ref_ms
            for user_ms, ref_ms in zip(user_times, reference_times)
            if ref_ms > 0
        ]
        ratio = _median(paired_ratios)
        if reference_ms is None or ratio is None:
            return RuntimeCheck(
                checked=False,
                passed=False,
                n=int(case.size or 0),
                message=f"SQL benchmark tier {case.id} did not produce comparable timings.",
            )
        samples.append(
            {
                "size": int(case.size or 0),
                "reference_ms": reference_ms,
                "user_ms": reference_ms * ratio,
                "ratio": ratio,
            }
        )

    return _runtime_check_from_scaling(samples, trials=trials, language="sql")


def _runtime_check_concurrency_cases(
    *,
    challenge: Any,
    source: str,
    cases: list[ValidatedCase],
) -> RuntimeCheck:
    if len(cases) < 2 or any(case.size is None or case.size <= 0 for case in cases):
        return RuntimeCheck(
            checked=False,
            passed=False,
            message="Concurrency scaling requires at least two positive-size benchmark tiers.",
        )
    spec = getattr(challenge, "_spec", None)
    if spec is None:
        return RuntimeCheck(checked=False, passed=False, message="No challenge spec is available for timing.")
    reference_source = load_optimal_source(challenge.info.id, spec, language="python")
    if not reference_source:
        return RuntimeCheck(
            checked=False,
            passed=False,
            message="No Python concurrency reference is available for timing.",
        )

    samples: list[dict[str, float | int]] = []
    trials = 3
    for case in sorted(cases, key=lambda item: int(item.size or 0)):
        reference_times: list[float] = []
        user_times: list[float] = []
        for trial in range(trials):
            ordered_sources = (
                (("reference", reference_source), ("user", source))
                if trial % 2 == 0
                else (("user", source), ("reference", reference_source))
            )
            timings: dict[str, float] = {}
            for label, candidate_source in ordered_sources:
                result = run_special_environment(
                    category="concurrency",
                    source=candidate_source,
                    input_data=case.input,
                    challenge_id=challenge.info.id,
                    timeout_seconds=max(0.1, (case.timeout_ms or 8000) / 1000.0),
                )
                if not result.ok:
                    return RuntimeCheck(
                        checked=False,
                        passed=False,
                        n=int(case.size or 0),
                        message=f"{label.title()} concurrency benchmark failed: {result.error_message}",
                    )
                if case.expected is not None and not _validated_case_matches(case, result.value, case.expected):
                    if label == "reference":
                        return RuntimeCheck(
                            checked=False,
                            passed=False,
                            n=int(case.size or 0),
                            trials=trial,
                            message=f"Reference concurrency output mismatched on {case.id}.",
                        )
                    return RuntimeCheck(
                        checked=True,
                        passed=False,
                        n=int(case.size or 0),
                        trials=trial,
                        message=f"User concurrency output mismatched on {case.id}.",
                        benchmark_correct=False,
                    )
                timings[label] = float(result.runtime_ms or 0.0)
            reference_times.append(timings["reference"])
            user_times.append(timings["user"])
        reference_ms = _median(reference_times)
        user_ms = _median(user_times)
        if reference_ms is None or user_ms is None or reference_ms <= 0:
            return RuntimeCheck(
                checked=False,
                passed=False,
                n=int(case.size or 0),
                message=f"Concurrency benchmark tier {case.id} did not produce comparable timings.",
            )
        samples.append(
            {
                "size": int(case.size or 0),
                "reference_ms": reference_ms,
                "user_ms": user_ms,
                "ratio": user_ms / reference_ms,
            }
        )
    return _runtime_check_from_scaling(samples, trials=trials, language="python")


def _run_special_environment_cases(
    *,
    challenge: Any,
    source: str,
    mode: str,
    category: str,
    run_cases: list[ValidatedCase],
) -> RunResponse:
    case_results: list[RunCaseResult] = []
    first_value: Any = None
    first_error = ""
    for case in run_cases:
        result = run_special_environment(
            category=category,
            source=source,
            input_data=case.input,
            challenge_id=challenge.info.id,
            timeout_seconds=max(0.1, (case.timeout_ms or 8000) / 1000.0),
        )
        if first_value is None:
            first_value = result.value
        expected_available = case.expected is not None
        correct = result.ok and (
            not expected_available or _validated_case_matches(case, result.value, case.expected)
        )
        message = result.error_message
        if result.ok and expected_available and not correct:
            message = "Output did not match the expected result."
        if result.ok and not expected_available:
            message = "Run completed. Add an expected value to turn this fixture into a judged case."
        if (
            not correct
            and _case_counts_toward_verdict(case, mode)
            and not first_error
        ):
            first_error = message
        case_results.append(
            RunCaseResult(
                id=case.id,
                name=case.name,
                kind=case.kind,
                correct=correct,
                passed=correct,
                message=message,
                input_repr=_format_return_value(case.input),
                return_value_repr=_format_return_value(result.value) if result.ok else "",
                expected_repr=_format_return_value(case.expected) if expected_available else None,
                runtime_user_ms=result.runtime_ms,
            )
        )
    verdict_results = _verdict_case_results(run_cases, case_results, mode)
    correct = (
        bool(verdict_results)
        and all(case.correct for case in verdict_results)
        and len(case_results) == len(run_cases)
    )
    environment_label = {
        "concurrency": "Concurrency",
        "database": "SQL",
        "pandas": "Pandas",
        "shell": "Bash",
    }.get(category, category)
    benchmark_cases = [case for case in run_cases if case.kind == "benchmark"]
    runtime_check = RuntimeCheck(checked=False, passed=False)
    complexity_check = ComplexityCheck()
    if correct and category == "database" and benchmark_cases:
        runtime_check = _runtime_check_database_cases(
            challenge=challenge,
            source=source,
            cases=benchmark_cases,
        )
    if correct and category == "concurrency" and benchmark_cases:
        runtime_check = _runtime_check_concurrency_cases(
            challenge=challenge,
            source=source,
            cases=benchmark_cases,
        )
    if correct and not benchmark_cases:
        complexity_check = _complexity_certificate_check(challenge.info.id)
    within_threshold = correct and (
        runtime_check.passed
        if runtime_check.checked
        else complexity_check.passed
        if complexity_check.checked
        else True
    )
    passed = correct and within_threshold
    if first_error:
        message = first_error
    elif runtime_check.checked:
        message = runtime_check.message
    elif complexity_check.checked:
        message = complexity_check.message
    else:
        message = f"{environment_label} run completed successfully."
    required = challenge.info.required_complexity.value
    return RunResponse(
        passed=passed,
        correct=correct,
        within_threshold=within_threshold,
        actual_complexity=required,
        required_complexity=required,
        mode=mode,
        message=message,
        return_value_repr=_format_return_value(first_value),
        reference_return_value_repr=(
            _format_return_value(run_cases[0].expected)
            if run_cases and run_cases[0].expected is not None else None
        ),
        setup_data_repr={key: _format_return_value(value) for key, value in run_cases[0].input.items()},
        case_results=case_results,
        selected_case_ids=[case.id for case in run_cases],
        runtime_check=runtime_check.checked,
        runtime_passed=runtime_check.passed if runtime_check.checked else None,
        runtime_user_ms=(
            runtime_check.user_ms
            if runtime_check.checked
            else (case_results[0].runtime_user_ms if case_results else None)
        ),
        runtime_reference_ms=runtime_check.reference_ms,
        runtime_ratio=runtime_check.ratio,
        runtime_limit_ms=runtime_check.limit_ms,
        runtime_trials=runtime_check.trials,
        runtime_message=(
            runtime_check.message
            if runtime_check.checked
            else "Source-native playground run; no benchmark tier was selected."
        ),
        benchmark_correct=runtime_check.benchmark_correct,
        runtime_scaling_data=runtime_check.scaling_data,
        complexity_check=complexity_check.checked,
        complexity_passed=complexity_check.passed if complexity_check.checked else None,
        complexity_method=complexity_check.method,
        complexity_message=complexity_check.message,
    )


def _run_external_function_player(
    *,
    challenge: Any,
    source: str,
    n: int,
    seed: Optional[int],
    mode: str,
    language: str,
) -> RunResponse:
    challenge._n = n
    challenge._seed = seed
    setup_data = challenge.setup(n, seed)
    setup_data_repr = {k: _format_return_value(v) for k, v in setup_data.items()}

    import copy

    reference_return_value_repr: Optional[str] = None
    if hasattr(challenge, "_reference_solve"):
        try:
            ref_setup_data = copy.deepcopy(setup_data)
            ref_result = challenge._reference_solve(**ref_setup_data)
            reference_return_value_repr = _format_return_value(ref_result)
        except Exception as exc:
            log.warning("Failed to run reference solve: %s", exc)

    spec = getattr(challenge, "_spec", None)
    param_names = list(getattr(spec, "params", []) or setup_data.keys())
    param_hints = dict(getattr(spec, "inputs", {}) or {})
    returns_hint = str(getattr(spec, "returns", "") or "")
    input_json = json.dumps(setup_data)

    external_result = run_function_program(
        language=language,
        source=source,
        input_json=input_json,
        param_names=param_names,
        param_hints=param_hints,
        returns_hint=returns_hint,
    )
    error_message = external_result.error_message
    raw_result = _last_non_empty_line(external_result.stdout)
    result: Any = None
    if not error_message:
        try:
            result = json.loads(raw_result) if raw_result else None
            result = _restore_external_json_value(result)
        except json.JSONDecodeError as exc:
            error_message = f"Could not parse program result as JSON: {exc}"
            result = raw_result

    correct = False
    if not error_message:
        try:
            correct = challenge.verify(result)
        except Exception as exc:
            error_message = f"Could not verify: {type(exc).__name__}: {exc}"
            correct = False

    runtime_check = RuntimeCheck(checked=False, passed=False, message=error_message)
    if correct:
        runtime_check = _runtime_check_external_function(
            challenge=challenge,
            source=source,
            language=language,
            n=n,
            seed=seed,
        )

    user_ast_ops: Optional[int] = None
    reference_source = (getattr(spec, "source", "") if spec is not None else "") or ""
    del reference_source
    reference_ast_ops: Optional[int] = None
    reference_ci_low: Optional[int] = None
    reference_ci_high: Optional[int] = None

    required_complexity = challenge.info.required_complexity
    within_threshold = runtime_check.passed if runtime_check.checked else False

    actual_complexity = required_complexity.value
    passed = correct and within_threshold

    too_efficient = False
    too_efficient_reason = ""

    reference_coefficient: Optional[float] = None
    if False and reference_ast_ops is not None and reference_ast_ops > 0:
        from engine.counter import get_complexity_factor

        ref_factor = get_complexity_factor(n, required_complexity)
        reference_coefficient = (reference_ast_ops - 10) / ref_factor if ref_factor > 0 else 0.0
        reference_coefficient = max(0.0, reference_coefficient)

    message = _build_message(
        error_message=error_message,
        correct=correct,
        within_threshold=within_threshold,
        user_ast_ops=user_ast_ops,
        actual_complexity=actual_complexity,
        required_complexity=required_complexity,
        runtime_check=runtime_check,
        too_efficient=too_efficient,
        too_efficient_reason=too_efficient_reason,
    )

    return RunResponse(
        passed=passed,
        correct=correct,
        within_threshold=within_threshold,
        actual_complexity=actual_complexity,
        required_complexity=required_complexity.value,
        mode=mode,
        too_efficient=too_efficient,
        too_efficient_reason=too_efficient_reason,
        user_ast_ops=user_ast_ops,
        reference_ast_ops=reference_ast_ops,
        reference_ci_low=reference_ci_low,
        reference_ci_high=reference_ci_high,
        reference_coefficient=reference_coefficient,
        scaling_data=[],
        runtime_check=runtime_check.checked,
        runtime_passed=runtime_check.passed if runtime_check.checked else None,
        runtime_user_ms=runtime_check.user_ms,
        runtime_reference_ms=runtime_check.reference_ms,
        runtime_ratio=runtime_check.ratio,
        runtime_limit_ms=runtime_check.limit_ms,
        runtime_trials=runtime_check.trials,
        runtime_message=runtime_check.message,
        benchmark_correct=runtime_check.benchmark_correct,
        runtime_scaling_data=runtime_check.scaling_data,
        message=message,
        return_value_repr=_format_return_value(result),
        reference_return_value_repr=reference_return_value_repr,
        setup_data_repr=setup_data_repr,
    )


def _run_external_validated_cases(
    *,
    challenge: Any,
    source: str,
    mode: str,
    language: str,
    run_cases: list[ValidatedCase],
    benchmark_cases: list[ValidatedCase],
) -> RunResponse:
    spec = getattr(challenge, "_spec", None)
    param_names = list(getattr(spec, "params", []) or [])
    param_hints = dict(getattr(spec, "inputs", {}) or {})
    returns_hint = str(getattr(spec, "returns", "") or "")
    returns_in_place = _returns_in_place(returns_hint)
    returns_tree = _returns_tree(returns_hint)
    returns_list_node = _returns_list_node(returns_hint)
    reference_solve, reference_error = _load_python_optimal_solve(challenge)
    if reference_solve is None and reference_error:
        log.debug("No Python optimal reference available for external validated cases: %s", reference_error)

    case_results: list[RunCaseResult] = []
    first_result: Any = None
    first_expected: Any = None
    error_message = ""
    for case in run_cases:
        case_result, result, expected, message, _elapsed_ms = _run_external_solution_on_case(
            source=source,
            language=language,
            reference_solve=reference_solve,
            case=case,
            param_names=param_names,
            param_hints=param_hints,
            returns_hint=returns_hint,
            returns_in_place=returns_in_place,
            returns_tree=returns_tree,
            returns_list_node=returns_list_node,
        )
        case_results.append(case_result)
        if first_result is None and result is not None:
            first_result = result
        if first_expected is None and expected is not None:
            first_expected = expected
        if (
            not case_result.correct
            and _case_counts_toward_verdict(case, mode)
            and not error_message
        ):
            error_message = message or case_result.message

    verdict_results = _verdict_case_results(run_cases, case_results, mode)
    correct = (
        bool(verdict_results)
        and all(case.correct for case in verdict_results)
        and len(case_results) == len(run_cases)
    )
    runtime_check = RuntimeCheck(checked=False, passed=False, message=error_message)
    complexity_check = ComplexityCheck()
    if correct and benchmark_cases:
        runtime_check = _runtime_check_external_cases(
            challenge=challenge,
            source=source,
            language=language,
            cases=benchmark_cases,
            reference_solve=reference_solve,
            param_names=param_names,
            param_hints=param_hints,
            returns_hint=returns_hint,
            returns_in_place=returns_in_place,
            returns_tree=returns_tree,
            returns_list_node=returns_list_node,
        )
    elif correct:
        complexity_check = _complexity_certificate_check(challenge.info.id)

    required_complexity = challenge.info.required_complexity
    within_threshold = (
        runtime_check.passed
        if runtime_check.checked
        else complexity_check.passed
        if complexity_check.checked
        else False
    )
    passed = correct and within_threshold
    message = _build_message(
        error_message=error_message,
        correct=correct,
        within_threshold=within_threshold,
        runtime_check=runtime_check,
        actual_complexity=required_complexity.value,
        required_complexity=required_complexity,
    )
    headline_case = _headline_case_result(run_cases, case_results, mode)

    return RunResponse(
        passed=passed,
        correct=correct,
        within_threshold=within_threshold,
        actual_complexity=required_complexity.value,
        required_complexity=required_complexity.value,
        mode=mode,
        too_efficient=False,
        too_efficient_reason="",
        user_ast_ops=None,
        reference_ast_ops=None,
        reference_ci_low=None,
        reference_ci_high=None,
        reference_coefficient=None,
        scaling_data=[],
        runtime_check=runtime_check.checked,
        runtime_passed=runtime_check.passed if runtime_check.checked else None,
        runtime_user_ms=runtime_check.user_ms,
        runtime_reference_ms=runtime_check.reference_ms,
        runtime_ratio=runtime_check.ratio,
        runtime_limit_ms=runtime_check.limit_ms,
        runtime_trials=runtime_check.trials,
        runtime_message=runtime_check.message,
        benchmark_correct=runtime_check.benchmark_correct,
        runtime_scaling_data=runtime_check.scaling_data,
        complexity_check=complexity_check.checked,
        complexity_passed=complexity_check.passed if complexity_check.checked else None,
        complexity_method=complexity_check.method,
        complexity_message=complexity_check.message,
        message=message,
        return_value_repr=headline_case.return_value_repr if headline_case else _format_return_value(first_result),
        reference_return_value_repr=headline_case.expected_repr if headline_case else _format_return_value(first_expected),
        setup_data_repr={
            key: _format_return_value(value)
            for key, value in (run_cases[0].input if run_cases else {}).items()
        },
        case_results=case_results,
        selected_case_ids=[case.id for case in run_cases],
    )


def _run_external_solution_on_case(
    *,
    source: str,
    language: str,
    reference_solve: Any | None,
    case: ValidatedCase,
    param_names: list[str] | tuple[str, ...],
    param_hints: dict[str, str],
    returns_hint: str,
    returns_in_place: bool = False,
    returns_tree: bool = False,
    returns_list_node: bool = False,
) -> tuple[RunCaseResult, Any, Any, str, float | None]:
    expected, expected_error = _expected_for_case(
        reference_solve=reference_solve,
        case=case,
        returns_in_place=returns_in_place,
        param_names=param_names,
        returns_tree=returns_tree,
        returns_list_node=returns_list_node,
    )
    if expected_error:
        return (
            RunCaseResult(
                id=case.id,
                name=case.name,
                kind=case.kind,
                correct=False,
                passed=False,
                message=expected_error,
                input_repr=_format_return_value(case.input),
                return_value_repr="",
                expected_repr=None,
                runtime_user_ms=None,
            ),
            None,
            expected,
            expected_error,
            None,
        )

    external_result = run_function_program(
        language=language,
        source=source,
        input_json=json.dumps(case.input),
        param_names=list(param_names),
        param_hints=param_hints,
        returns_hint=returns_hint,
    )
    if external_result.error_message:
        return (
            RunCaseResult(
                id=case.id,
                name=case.name,
                kind=case.kind,
                correct=False,
                passed=False,
                message=external_result.error_message,
                input_repr=_format_return_value(case.input),
                return_value_repr="",
                expected_repr=_format_return_value(expected),
                runtime_user_ms=external_result.runtime_ms,
            ),
            None,
            expected,
            external_result.error_message,
            external_result.runtime_ms,
        )

    raw_result = _last_non_empty_line(external_result.stdout)
    try:
        actual = json.loads(raw_result) if raw_result else None
        actual = _restore_external_json_value(actual)
        actual = _normalize_validated_value(
            actual,
            returns_tree=returns_tree,
            returns_list_node=returns_list_node,
        )
    except json.JSONDecodeError as exc:
        message = f"Could not parse program result as JSON: {exc}"
        return (
            RunCaseResult(
                id=case.id,
                name=case.name,
                kind=case.kind,
                correct=False,
                passed=False,
                message=message,
                input_repr=_format_return_value(case.input),
                return_value_repr=raw_result,
                expected_repr=_format_return_value(expected),
                runtime_user_ms=external_result.runtime_ms,
            ),
            raw_result,
            expected,
            message,
            external_result.runtime_ms,
        )

    correct = _validated_case_matches(case, actual, expected)
    message = "" if correct else "Incorrect solution: output did not match the validated expected result."
    return (
        RunCaseResult(
            id=case.id,
            name=case.name,
            kind=case.kind,
            correct=correct,
            passed=correct,
            message=message,
            input_repr=_format_return_value(case.input),
            return_value_repr=_format_return_value(actual),
            expected_repr=_format_return_value(expected),
            runtime_user_ms=external_result.runtime_ms,
        ),
        actual,
        expected,
        message,
        external_result.runtime_ms,
    )


def _runtime_check_external_cases(
    *,
    challenge: Any,
    source: str,
    language: str,
    cases: list[ValidatedCase],
    reference_solve: Any | None,
    param_names: list[str] | tuple[str, ...],
    param_hints: dict[str, str],
    returns_hint: str,
    returns_in_place: bool = False,
    returns_tree: bool = False,
    returns_list_node: bool = False,
) -> RuntimeCheck:
    spec = getattr(challenge, "_spec", None)
    if spec is None:
        return RuntimeCheck(
            checked=False,
            n=len(cases),
            message="No challenge spec is available for same-language timing.",
        )
    if not cases:
        return RuntimeCheck(
            checked=False,
            passed=False,
            n=0,
            message="No validated benchmark cases are available.",
        )

    if len(cases) >= 2 and all(case.size is not None for case in cases):
        scaling_samples: list[dict[str, float | int]] = []
        trials = 0
        for case in sorted(cases, key=lambda item: int(item.size or 0)):
            measurement = _runtime_check_external_cases(
                challenge=challenge,
                source=source,
                language=language,
                cases=[case],
                reference_solve=reference_solve,
                param_names=param_names,
                param_hints=param_hints,
                returns_hint=returns_hint,
                returns_in_place=returns_in_place,
                returns_tree=returns_tree,
                returns_list_node=returns_list_node,
            )
            if not measurement.checked or not measurement.benchmark_correct:
                return measurement
            if measurement.user_ms is None or measurement.reference_ms is None or measurement.ratio is None:
                return RuntimeCheck(
                    checked=False,
                    passed=False,
                    n=int(case.size or 0),
                    message=f"Benchmark tier {case.id} did not produce comparable timings.",
                )
            trials = max(trials, measurement.trials)
            scaling_samples.append(
                {
                    "size": int(case.size or 0),
                    "user_ms": measurement.user_ms,
                    "reference_ms": measurement.reference_ms,
                    "ratio": measurement.ratio,
                }
            )
        return _runtime_check_from_scaling(scaling_samples, trials=trials, language=language)

    reference_source = load_optimal_source(
        challenge.info.id,
        spec,
        language=language,
    )
    if not reference_source:
        return RuntimeCheck(
            checked=False,
            passed=False,
            n=len(cases),
            message=f"No {language} optimal reference is available for timing.",
        )

    expected_by_case: dict[str, Any] = {}
    for case in cases:
        expected, expected_error = _expected_for_case(
            reference_solve=reference_solve,
            case=case,
            returns_in_place=returns_in_place,
            param_names=param_names,
            returns_tree=returns_tree,
            returns_list_node=returns_list_node,
        )
        if expected_error:
            return RuntimeCheck(
                checked=False,
                passed=False,
                n=len(cases),
                message=expected_error,
            )
        expected_by_case[case.id] = expected

    reference_total = 0.0
    user_total = 0.0
    for case in cases:
        input_json = json.dumps(case.input)
        reference_result = run_function_program(
            language=language,
            source=reference_source,
            input_json=input_json,
            param_names=list(param_names),
            param_hints=param_hints,
            returns_hint=returns_hint,
            timeout_seconds=_RUNTIME_EXTERNAL_TIMEOUT_SECONDS,
            measure_runtime=True,
        )
        if reference_result.error_message:
            return RuntimeCheck(
                checked=False,
                n=len(cases),
                message=f"Same-language reference benchmark failed on {case.name}: {reference_result.error_message}",
            )
        reference_ms = reference_result.runtime_ms
        if reference_ms is None:
            return RuntimeCheck(
                checked=False,
                n=len(cases),
                message="Same-language reference did not report internal runtime.",
            )

        runtime_iterations = _runtime_iterations_for_ms(reference_ms) if language == "javascript" and not returns_in_place else 1
        if runtime_iterations > 1:
            reference_result = run_function_program(
                language=language,
                source=reference_source,
                input_json=input_json,
                param_names=list(param_names),
                param_hints=param_hints,
                returns_hint=returns_hint,
                timeout_seconds=_RUNTIME_EXTERNAL_TIMEOUT_SECONDS,
                measure_runtime=True,
                runtime_iterations=runtime_iterations,
            )
            if reference_result.error_message:
                return RuntimeCheck(
                    checked=False,
                    n=len(cases),
                    message=f"Same-language reference benchmark failed on {case.name}: {reference_result.error_message}",
                )
            reference_ms = reference_result.runtime_ms
            if reference_ms is None:
                return RuntimeCheck(
                    checked=False,
                    n=len(cases),
                    message="Same-language reference did not report internal runtime.",
                )

        raw_reference = _last_non_empty_line(reference_result.stdout)
        try:
            reference_value = json.loads(raw_reference) if raw_reference else None
            reference_value = _restore_external_json_value(reference_value)
            reference_value = _normalize_validated_value(
                reference_value,
                returns_tree=returns_tree,
                returns_list_node=returns_list_node,
            )
        except Exception as exc:
            return RuntimeCheck(
                checked=False,
                n=len(cases),
                message=f"Same-language reference produced invalid JSON on {case.name}: {type(exc).__name__}: {exc}",
            )
        expected = expected_by_case[case.id]
        if not _validated_case_matches(case, reference_value, expected):
            return RuntimeCheck(
                checked=False,
                n=len(cases),
                message=f"Same-language reference output mismatched the expected result for {case.name}.",
            )
        reference_total += reference_ms

        external_result = run_function_program(
            language=language,
            source=source,
            input_json=input_json,
            param_names=list(param_names),
            param_hints=param_hints,
            returns_hint=returns_hint,
            timeout_seconds=_RUNTIME_EXTERNAL_TIMEOUT_SECONDS,
            measure_runtime=True,
            runtime_iterations=runtime_iterations,
        )
        user_ms = external_result.runtime_ms
        if external_result.error_message:
            return _runtime_check_from_times(
                user_ms=user_ms,
                reference_ms=reference_total,
                trials=len(cases),
                n=len(cases),
                seed=None,
                language=language,
                error_message=external_result.error_message,
            )
        if user_ms is None:
            return _runtime_check_from_times(
                user_ms=None,
                reference_ms=reference_total,
                trials=len(cases),
                n=len(cases),
                seed=None,
                language=language,
                error_message="Benchmark did not report internal runtime.",
            )

        raw_result = _last_non_empty_line(external_result.stdout)
        try:
            result = json.loads(raw_result) if raw_result else None
            result = _restore_external_json_value(result)
            result = _normalize_validated_value(
                result,
                returns_tree=returns_tree,
                returns_list_node=returns_list_node,
            )
            benchmark_correct = _validated_case_matches(case, result, expected)
        except Exception:
            benchmark_correct = False
        user_total += user_ms
        if not benchmark_correct:
            return _runtime_check_from_times(
                user_ms=user_total,
                reference_ms=reference_total,
                trials=len(cases),
                n=len(cases),
                seed=None,
                language=language,
                benchmark_correct=False,
            )

    return _runtime_check_from_times(
        user_ms=user_total,
        reference_ms=reference_total,
        trials=len(cases),
        n=len(cases),
        seed=None,
        language=language,
    )


def _last_non_empty_line(text: str) -> str:
    for line in reversed(text.splitlines()):
        if line.strip():
            return line.strip()
    return ""


def _restore_external_json_value(value: Any) -> Any:
    """Restore Python verifier shapes after C-family JSON round-trips."""
    if isinstance(value, list):
        return [_restore_external_json_value(item) for item in value]
    if isinstance(value, dict):
        return {
            _restore_external_json_key(key): _restore_external_json_value(item)
            for key, item in value.items()
        }
    return value


def _restore_external_json_key(key: Any) -> Any:
    if isinstance(key, str) and re.fullmatch(r"-?(?:0|[1-9]\d*)", key):
        try:
            return int(key)
        except ValueError:
            return key
    return key


def _build_message(
    error_message: str,
    correct: bool,
    within_threshold: bool,
    runtime_check: RuntimeCheck,
    user_ast_ops: Optional[int] = None,
    actual_complexity: Any = None,
    required_complexity: Any = None,
    too_efficient: bool = False,
    too_efficient_reason: str = "",
) -> str:
    """Build the pass/fail message the web StatusBanner shows.

    The user-facing verdict is tied to correctness and the calibrated runtime
    comparison against the optimal reference. Static-op values are ignored.
    """
    del user_ast_ops, actual_complexity
    if too_efficient:
        return (
            f"Solution rejected: {too_efficient_reason}"
            if too_efficient_reason
            else "Solution rejected: too efficient (suspicious pattern)."
        )
    if error_message:
        return error_message
    if not correct:
        return "Incorrect solution!"
    if not within_threshold:
        return runtime_check.message or "Correct, but no optimal runtime benchmark is available."
    if runtime_check.checked and runtime_check.message:
        return f"Passed! {runtime_check.message}"
    required_label = getattr(required_complexity, "value", str(required_complexity or "unknown"))
    return f"Passed! Required complexity: {required_label}"


# Cap on the rendered return value. A 10,000-element list at
# ~5 chars per element would be 50 KB; we cap well below that so
# the response stays small and the UI can show it without
# horizontal scrolling.
_RETURN_VALUE_CAP = 500


def format_compact_json(value: Any, indent: int = 2) -> str:
    """Recursively format JSON, keeping 1D arrays/lists horizontal.

    If a list contains only primitive values, it is formatted as a single line
    via json.dumps. Nested structures (like grids and dictionaries) are split
    across lines and indented recursively.
    """
    import json

    def is_primitive(val: Any) -> bool:
        return isinstance(val, (int, float, str, bool, type(None)))

    def is_1d_list(val: Any) -> bool:
        if not isinstance(val, list):
            return False
        return all(is_primitive(item) for item in val)

    if is_1d_list(value):
        return json.dumps(value)

    if isinstance(value, list):
        parts = []
        for item in value:
            item_str = format_compact_json(item, indent)
            indented = "\n".join(" " * indent + line for line in item_str.splitlines())
            parts.append(indented)
        return "[\n" + ",\n".join(parts) + "\n]"

    if isinstance(value, dict):
        parts = []
        for k, v in value.items():
            k_str = json.dumps(k)
            v_str = format_compact_json(v, indent)
            lines = v_str.splitlines()
            if len(lines) == 1:
                parts.append(" " * indent + f"{k_str}: {lines[0]}")
            else:
                first = " " * indent + f"{k_str}: {lines[0]}"
                rest = "\n".join(" " * indent + line for line in lines[1:])
                parts.append(first + "\n" + rest)
        return "{\n" + ",\n".join(parts) + "\n}"

    return json.dumps(value)


def _format_return_value(value: Any) -> str:
    """Render the return value of ``solve()`` as a compact string.

    Goes through :func:`trace_codec.to_json_safe` so lists /
    tuples / sets / dicts render sensibly (Python ``repr()`` would
    produce a single-line blob that's unreadable for nested
    structures). Capped at :data:`_RETURN_VALUE_CAP` characters
    with a trailing ellipsis when truncated.
    """
    try:
        safe = to_json_safe(value)
        text = format_compact_json(safe, indent=2)
    except Exception:
        text = repr(value)
    if len(text) > _RETURN_VALUE_CAP:
        text = text[:_RETURN_VALUE_CAP] + "â€¦"
    return text
