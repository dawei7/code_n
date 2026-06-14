"""Challenge definition and execution framework.

Each challenge defines:
- A grid setup (the visual problem)
- Input data generation
- A complexity threshold (max allowed O-class)
- A verification function (did the player solve it correctly?)
- Optionally, an "algorithm fingerprint" that nudges the player
  toward using a specific technique (e.g. BFS, bubble sort) when
  several algorithms of the same complexity could solve the problem.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Callable, Optional

from .grid import Grid
from .counter import (
    OpRecord, get_counter, reset_counter,
    ComplexityClass, OpStats, OperationLimitExceeded,
)
from .tracked import TrackedList, TrackedGrid
from .execution_trace import ExecutionStepLimitExceeded, ExecutionTrace, run_with_trace


# Relation keywords for OperationConstraint.
OP_AT_LEAST = "at_least"
OP_AT_MOST = "at_most"
OP_EXACTLY = "exactly"


@dataclass(frozen=True)
class OperationConstraint:
    """One rule for the algorithm fingerprint.

    Each op recorded by the engine has a human-readable detail string
    (e.g. ``"list[3] = 42"``, ``"queue.enqueue(7)"``, ``"list[3]<->list[7]"``).
    The constraint counts ops whose detail contains ``needle`` and
    asserts that the count satisfies ``relation`` against ``count``:

    * ``OP_AT_LEAST`` — the count must be ``>= count``
    * ``OP_AT_MOST``  — the count must be ``<= count``
    * ``OP_EXACTLY``  — the count must be ``== count``

    Common needles:
      * ``"<->"`` — any swap (list or grid)
      * ``"queue.enqueue"`` / ``"queue.dequeue"`` — BFS queue ops
      * ``"stack.push"`` / ``"stack.pop"`` — DFS stack ops
      * ``"list.append("`` — list append
      * ``"line "`` — Python source-line CALL entries (recursion)
    """

    needle: str
    relation: str
    count: int


def check_fingerprint(
    ops_log: list[OpRecord],
    constraints: list[OperationConstraint],
) -> tuple[bool, str]:
    """Return ``(matched, reason)`` for a list of constraints.

    ``matched`` is True iff every constraint holds. ``reason`` is a
    human-readable summary of which constraints failed and why; it
    is empty when ``matched`` is True.

    This is an *advisory* check: the player's solution can still pass
    (correct + within the complexity budget) even if the fingerprint
    fails. The point is to surface a teaching hint, not to punish.
    """
    if not constraints:
        return True, ""
    # Count each op against the FIRST constraint whose needle it
    # matches. This avoids one op double-counting for two overlapping
    # needles (e.g. "<->" + "list[") both matching a swap op).
    counts: dict[OperationConstraint, int] = {c: 0 for c in constraints}
    for op in ops_log:
        detail = op.detail or ""
        for c in constraints:
            if c.needle in detail:
                counts[c] += 1
                break
    failures: list[str] = []
    for c in constraints:
        actual = counts[c]
        if c.relation == OP_AT_LEAST and actual < c.count:
            failures.append(f"expected at least {c.count} '{c.needle}' ops, saw {actual}")
        elif c.relation == OP_AT_MOST and actual > c.count:
            failures.append(f"expected at most {c.count} '{c.needle}' ops, saw {actual}")
        elif c.relation == OP_EXACTLY and actual != c.count:
            failures.append(f"expected exactly {c.count} '{c.needle}' ops, saw {actual}")
    if failures:
        return False, "; ".join(failures)
    return True, ""


@dataclass
class ChallengeResult:
    passed: bool
    correct: bool
    within_threshold: bool
    algorithm_match: bool
    algorithm_reason: str
    stats: OpStats
    actual_complexity: ComplexityClass
    required_complexity: ComplexityClass
    n: int
    message: str = ""


@dataclass
class ChallengeInfo:
    id: str
    name: str
    description: str
    category: str
    difficulty: int  # 1-10
    required_complexity: ComplexityClass
    hint: str = ""
    # Optional list of rules that the player's op log must satisfy
    # for the "algorithm hint" to come back clean. See
    # OperationConstraint above for the supported needles.
    expected_operations: list[OperationConstraint] = field(default_factory=list)


class Challenge(ABC):
    """Base class for all challenges."""

    # Default maximum input size. The runner clamps --n to this and the
    # engine sizes the visualizer around it. 1D challenges use this;
    # 2D challenges (BFS/DFS grids) override to MAX_2D_N below because
    # a 50x50 grid is too dense to be useful even at the smallest zoom.
    MAX_N = 50
    MAX_2D_N = 35

    def __init__(self):
        self.grid: Optional[Grid] = None
        self._n: int = 0
        self._seed: Optional[int] = None

    @property
    def max_n(self) -> int:
        """Maximum n this challenge accepts.

        Defaults to MAX_N (1D / single-array). 2D grid challenges
        override to MAX_2D_N so the visualization stays viewable.
        """
        return self.MAX_N

    @property
    @abstractmethod
    def info(self) -> ChallengeInfo:
        """Return challenge metadata."""
        ...

    @abstractmethod
    def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
        """Set up the challenge and return the data the player will work with.

        Returns a dict of named arguments that will be passed to the player's solve function.
        """
        ...

    @abstractmethod
    def verify(self, result: Any) -> bool:
        """Verify the player's solution is correct."""
        ...

    def run(self, solve_fn: Callable, n: int = 16,
            seed: Optional[int] = None, animate: bool = False) -> ChallengeResult:
        """Execute the challenge with the player's solution function.

        This is the engine-internal path used by the unit tests. It
        does pure setup → solve → verify → classify → message
        bookkeeping and returns a :class:`ChallengeResult`. It has
        no I/O (no ``input()`` prompt, no ``print()``, no
        visualization, no side effects beyond the global
        :class:`OperationCounter`).

        The ``animate`` parameter is retained for backward
        compatibility with the test suite (which passes
        ``animate=False``) but is otherwise a no-op: visualization
        was always a no-op anyway because the legacy Pygame
        renderer modules were removed.

        The server uses its own trace pipeline in
        :mod:`server.app.engine_runner` and never calls this.
        """
        self._n = n
        self._seed = seed

        reset_counter()
        counter = get_counter()
        operation_limit = counter.limit_for(n, self.info.required_complexity)

        # Setup
        setup_data = self.setup(n, seed)

        # Run player's solution under trace capture so the resulting
        # ChallengeResult carries the frame timeline (even though
        # no test currently inspects it; the server uses its own).
        trace = ExecutionTrace()
        error_message = ""
        result = None
        counter.set_operation_limit(operation_limit, self.info.required_complexity)
        try:
            count_lines = not _has_tracked_inputs(setup_data)
            if count_lines:
                result, trace = run_with_trace(
                    solve_fn, setup_data, counter, count_lines=True,
                )
            else:
                result = solve_fn(**setup_data)
        except OperationLimitExceeded as exc:
            error_message = str(exc)
            trace.return_value = error_message
        except ExecutionStepLimitExceeded as exc:
            error_message = str(exc)
            trace.return_value = error_message
        finally:
            counter.clear_operation_limit()

        # Verify correctness. The verifier runs with the counter
        # disabled so its own reads don't inflate the op budget.
        if error_message:
            correct = False
        else:
            try:
                was_counting = counter.enabled
                counter.enabled = False
                correct = self.verify(result)
            except Exception as exc:
                correct = False
                error_message = f"Could not verify your result: {type(exc).__name__}: {exc}"
                trace.return_value = repr(result)
            finally:
                counter.enabled = was_counting

        stats = counter.stats
        actual_complexity = counter.classify(n)
        within_threshold = counter.meets_threshold(n, self.info.required_complexity)
        passed = correct and within_threshold

        # Algorithm fingerprint check. The fingerprint is advisory:
        # it never affects ``passed``, only ``algorithm_match`` and
        # a hint appended to the result message. The point is to
        # teach the player which specific algorithm they used when
        # several algorithms of the same O-class could solve the
        # problem.
        algorithm_match, algorithm_reason = check_fingerprint(
            counter.ops_log, self.info.expected_operations,
        )

        # Build the pass/fail message. The server's
        # ``build_message()`` helper in engine_runner.py mirrors
        # this logic for the HTTP path; keep the two in sync.
        if error_message:
            message = error_message
        elif not correct:
            message = "Incorrect solution!"
        elif not within_threshold:
            message = (
                f"Correct, but too slow! "
                f"Used {stats.total} ops (complexity: {actual_complexity.value}), "
                f"need {self.info.required_complexity.value}"
            )
        else:
            message = (
                f"Passed! {stats.total} ops "
                f"(complexity: {actual_complexity.value})"
            )
            if not algorithm_match and algorithm_reason:
                message += f"\nAlgorithm hint: {algorithm_reason}"

        return ChallengeResult(
            passed=passed,
            correct=correct,
            within_threshold=within_threshold,
            algorithm_match=algorithm_match,
            algorithm_reason=algorithm_reason,
            stats=stats,
            actual_complexity=actual_complexity,
            required_complexity=self.info.required_complexity,
            n=n,
            message=message,
        )


def _has_tracked_inputs(setup_data: dict[str, Any]) -> bool:
    tracked_types = (TrackedList, TrackedGrid)
    return any(isinstance(value, tracked_types) for value in setup_data.values())
