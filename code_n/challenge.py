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
    ComplexityClass, OpStats
)
from .renderer import Renderer
from .tracked import TrackedList, TrackedGrid, TrackedQueue, TrackedStack, TrackedSet
from .execution_trace import ExecutionTrace, run_with_trace


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

    def __init__(self):
        self.grid: Optional[Grid] = None
        self.renderer = Renderer()
        self._n: int = 0
        self._seed: Optional[int] = None

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

        # Setup
        reset_counter()
        setup_data = self.setup(n, seed)

        # Show initial state
        if animate:
            self.visualize_setup()
            input("\nPress Enter to run your solution...")

        # Run player's solution
        counter = get_counter()
        trace = ExecutionTrace()
        error_message = ""
        result = None
        try:
            if pygame:
                result, trace = run_with_trace(solve_fn, setup_data, counter)
            else:
                result = solve_fn(**setup_data)
        except Exception as exc:
            if not pygame:
                raise
            error_message = f"Your solution crashed: {type(exc).__name__}: {exc}"
            trace.return_value = "\n".join(traceback.format_exception_only(type(exc), exc)).strip()

        # Verify correctness
        if error_message:
            correct = False
        else:
            try:
                correct = self.verify(result)
            except Exception as exc:
                if not pygame:
                    raise
                correct = False
                error_message = f"Could not verify your result: {type(exc).__name__}: {exc}"
                trace.return_value = repr(result)
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
