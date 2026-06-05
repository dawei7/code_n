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

import random
import traceback
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Callable, Optional

from .grid import Grid, CellType
from .counter import (
    OperationCounter, OpRecord, get_counter, reset_counter,
    ComplexityClass, OpStats, OperationLimitExceeded
)
from .renderer import Renderer
from .tracked import TrackedList, TrackedGrid, TrackedQueue, TrackedStack, TrackedSet
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
        self.renderer = Renderer()
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

    def visualize_setup(self):
        """Show the initial state on the grid."""
        if self.grid:
            self.renderer.display(self.grid, title=self.info.name)

    def visualize_result(self, counter: OperationCounter):
        """Show the final state with stats."""
        if self.grid:
            self.renderer.display(
                self.grid,
                title=self.info.name,
                counter=counter,
                n=self._n,
                threshold=self.info.required_complexity
            )

    def run(self, solve_fn: Callable, n: int = 16,
            seed: Optional[int] = None, animate: bool = True,
            pygame: bool = False,
            pygame_speed: Optional[str] = None) -> ChallengeResult:
        """Execute the challenge with the player's solution function."""
        self._n = n
        self._seed = seed

        reset_counter()
        counter = get_counter()
        operation_limit = counter.limit_for(n, self.info.required_complexity)
        progress_window = None
        if pygame:
            from .pygame_renderer import ComputationProgressWindow

            progress_window = ComputationProgressWindow(
                self.info.name,
                self.info.description,
                operation_limit,
            )

        # Setup
        if progress_window:
            progress_window.update("Preparing challenge", 0, operation_limit, force=True)
        setup_data = self.setup(n, seed)

        # Show initial state
        if animate:
            self.visualize_setup()
            input("\nPress Enter to run your solution...")

        # Run player's solution
        trace = ExecutionTrace()
        error_message = ""
        result = None
        step_limit = max(10_000, operation_limit * 25)
        counter.set_operation_limit(operation_limit, self.info.required_complexity)
        if progress_window:
            progress_interval = max(1, operation_limit // 250)
            progress_window.update("Running your solution", 0, operation_limit, force=True)
            counter.set_progress_callback(
                lambda total, limit: progress_window.update("Running your solution", total, limit),
                interval=progress_interval,
            )
        try:
            count_lines = not _has_tracked_inputs(setup_data)
            if pygame:
                result, trace = run_with_trace(
                    solve_fn,
                    setup_data,
                    counter,
                    count_lines=count_lines,
                    step_limit=step_limit,
                    step_callback=(
                        lambda steps: progress_window.update(
                            f"Running your solution ({steps} Python steps)",
                            counter.total_ops,
                            operation_limit,
                        )
                        if progress_window
                        else None
                    ),
                    step_interval=max(500, step_limit // 250),
                )
            elif count_lines:
                result, trace = run_with_trace(solve_fn, setup_data, counter, count_lines=True)
            else:
                result = solve_fn(**setup_data)
        except OperationLimitExceeded as exc:
            error_message = str(exc)
            trace.return_value = error_message
        except ExecutionStepLimitExceeded as exc:
            error_message = str(exc)
            trace.return_value = error_message
        except Exception as exc:
            if not pygame:
                raise
            error_message = f"Your solution crashed: {type(exc).__name__}: {exc}"
            trace.return_value = "\n".join(traceback.format_exception_only(type(exc), exc)).strip()
        finally:
            counter.clear_operation_limit()
            counter.clear_progress_callback()
            if progress_window:
                progress_window.update("Preparing replay", counter.total_ops, operation_limit, force=True)
                progress_window.close()

        # Verify correctness
        if error_message:
            correct = False
        else:
            try:
                was_counting = counter.enabled
                counter.enabled = False
                correct = self.verify(result)
            except Exception as exc:
                if not pygame:
                    raise
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
        # it never affects `passed`, only `algorithm_match` and a hint
        # appended to the result message. The point is to teach the
        # player which specific algorithm they used when several
        # algorithms of the same O-class could solve the problem.
        algorithm_match, algorithm_reason = check_fingerprint(
            counter.ops_log, self.info.expected_operations,
        )

        # Build message
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

        # Show result
        if animate:
            self.visualize_result(counter)

        if pygame:
            from .pygame_renderer import PygameRenderer, VisualRunResult

            # Some challenges (greedy problems, dynamic-programming
            # problems on flat lists, anything not 2D) don't have a
            # 2D grid to visualize. The Pygame renderer still needs
            # *some* grid object to lay out its result window, so
            # substitute a 1x1 placeholder when one wasn't set up.
            # The challenge's own setup() should also set a
            # representative grid for pedagogical value; this is a
            # safety net so a missing grid never silently swallows a
            # run.
            if self.grid is None:
                from .grid import CellType as _CellType, Grid as _Grid
                placeholder = _Grid(1, 1)
                placeholder.set(0, 0, _CellType.VALUE, value="?")
                grid_for_renderer = placeholder
            else:
                grid_for_renderer = self.grid

            visual_result = VisualRunResult(
                passed=passed,
                message=message,
                stats=stats,
                actual_complexity=actual_complexity,
                required_complexity=self.info.required_complexity,
                n=n,
                description=self.info.description,
                return_value=trace.return_value or repr(result),
                trace_frames=trace.frames,
            )
            PygameRenderer(speed=pygame_speed).play(
                grid=grid_for_renderer,
                operations=counter.ops_log,
                title=self.info.name,
                result=visual_result,
            )

        if animate or pygame:
            print(f"\n{message}")

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
            message=message
        )


def _has_tracked_inputs(setup_data: dict[str, Any]) -> bool:
    tracked_types = (TrackedList, TrackedGrid, TrackedQueue, TrackedStack, TrackedSet)
    return any(isinstance(value, tracked_types) for value in setup_data.values())
