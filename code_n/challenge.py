"""Challenge definition and execution framework.

Each challenge defines:
- A grid setup (the visual problem)
- Input data generation
- A complexity threshold (max allowed O-class)
- A verification function (did the player solve it correctly?)
"""

import random
import traceback
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Callable, Optional

from .grid import Grid, CellType
from .counter import (
    OperationCounter, get_counter, reset_counter,
    ComplexityClass, OpStats, OperationLimitExceeded
)
from .renderer import Renderer
from .tracked import TrackedList, TrackedGrid, TrackedQueue, TrackedStack, TrackedSet
from .execution_trace import ExecutionStepLimitExceeded, ExecutionTrace, run_with_trace


@dataclass
class ChallengeResult:
    passed: bool
    correct: bool
    within_threshold: bool
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

        # Show result
        if animate:
            self.visualize_result(counter)

        if pygame and self.grid:
            from .pygame_renderer import PygameRenderer, VisualRunResult

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
                grid=self.grid,
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
            stats=stats,
            actual_complexity=actual_complexity,
            required_complexity=self.info.required_complexity,
            n=n,
            message=message
        )


def _has_tracked_inputs(setup_data: dict[str, Any]) -> bool:
    tracked_types = (TrackedList, TrackedGrid, TrackedQueue, TrackedStack, TrackedSet)
    return any(isinstance(value, tracked_types) for value in setup_data.values())
