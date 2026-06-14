"""The engine runner — runs a player's solution against a challenge.

This is the single point of integration between the FastAPI server
and the Python engine. It is the only file that:

* exec()'s player code
* calls into the engine's :class:`code_n.challenge.Challenge`
* converts engine types (:class:`OpRecord`, :class:`TraceFrame`,
  :class:`OpStats`, :class:`ComplexityClass`) into the Pydantic
  response models in :mod:`server.app.schemas`

Design notes
------------

**Why we bypass** ``Challenge.run()`` **for the trace.** The engine's
``Challenge.run`` only captures an :class:`ExecutionTrace` when there
are no tracked inputs in the setup data (sorting challenges use
``TrackedList`` as the player's input, which triggers the
``result = solve_fn(**setup_data)`` fast path and skips the tracer).
The web visualizer needs the trace to step through, so this module
mirrors the engine's orchestration but always calls
:func:`run_with_trace` with ``count_lines=False``. The counter state,
operation limit, fingerprint check, and message construction are all
reproduced from :mod:`code_n.challenge` to keep behavior identical.

**Why one temp file per run.** The engine's tracer uses
``func.__code__.co_filename`` to filter frames to the player's
file. A real file gives each run a unique filename (so two
concurrent runs with the same source don't collide) and lets the
breakpoint loader work against an actual on-disk file. The temp
file is cleaned up in a ``finally`` block.

**Concurrency caveat.** :func:`code_n.counter.get_counter` is
module-level state. The engine is designed for a single process
running one challenge at a time, and the desktop app is single-user,
so concurrent ``Run`` requests would trample each other's counter.
For the MVP, the frontend sends one request at a time; the
follow-up is to thread-localize the counter or move runs into a
``ProcessPoolExecutor``.
"""
from __future__ import annotations

import logging
import os
import runpy
import shutil
import tempfile
import traceback
from pathlib import Path
from typing import Any, Optional

from challenges.registry import CHALLENGE_REGISTRY, get_challenge
from code_n.challenge import (
    Challenge,
    OperationLimitExceeded,
    check_fingerprint,
)
from code_n.counter import (
    ComplexityClass,
    OpStats,
    get_counter,
    reset_counter,
)
from code_n.execution_trace import (
    ExecutionStepLimitExceeded,
    ExecutionTrace,
    run_with_trace,
)
from code_n.tracked import TrackedGrid, TrackedList

from .config import MAX_TRACE_FRAMES
from .schemas import (
    OpRecordOut,
    RunResponse,
    StatsOut,
    TraceFrameOut,
)
from .trace_codec import serialize_frame, serialize_op


log = logging.getLogger(__name__)


# ----------------------------------------------------------------------------
# Custom exception types raised by this module. The FastAPI routes
# translate them to HTTP responses via try/except (see run.py).
# ----------------------------------------------------------------------------


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


# ----------------------------------------------------------------------------
# The main entry point.
# ----------------------------------------------------------------------------


def run_player_code(
    challenge_id: str,
    source: str,
    n: int = 16,
    seed: Optional[int] = None,
) -> RunResponse:
    """Run a player's source against a challenge and return the structured result.

    Parameters
    ----------
    challenge_id:
        Must be a key in :data:`CHALLENGE_REGISTRY`.
    source:
        Full Python source. Must define ``def solve(**kwargs)``.
    n:
        Input size. Clamped against ``challenge.max_n`` by the route layer.
    seed:
        Optional RNG seed for reproducible inputs.

    Returns
    -------
    :class:`RunResponse`
        All the data the frontend needs: the pass/fail verdict, the
        stats, the full op log, and the per-line execution trace.

    Raises
    ------
    ChallengeNotFound, NTooLarge, PlayerSyntaxError, NoSolveFunction
        Translated to 404 / 422 / 422 / 400 by the route layer.
    """
    # --- 1. Resolve challenge ---
    challenge_cls = CHALLENGE_REGISTRY.get(challenge_id)
    if challenge_cls is None:
        raise ChallengeNotFound(challenge_id)
    challenge = challenge_cls()
    if n > challenge.max_n:
        raise NTooLarge(n, challenge.max_n)

    # --- 2. Stage the source in a temp dir so the engine's tracer can
    #        filter to this exact file. ---
    tmpdir = Path(tempfile.mkdtemp(prefix="coden-run-"))
    solution_path = tmpdir / "solution.py"
    solution_path.write_text(source, encoding="utf-8")

    try:
        # --- 3. Exec the source in a fresh namespace ---
        try:
            namespace = runpy.run_path(str(solution_path), run_name="player_solution")
        except SyntaxError as exc:
            raise PlayerSyntaxError(exc) from exc

        if "solve" not in namespace:
            raise NoSolveFunction()
        solve_fn = namespace["solve"]

        # --- 4. Set per-run instance state on the challenge ---
        challenge._n = n
        challenge._seed = seed

        # --- 5. Reset the (module-level) counter for this run ---
        reset_counter()
        counter = get_counter()
        required_complexity = challenge.info.required_complexity
        operation_limit = counter.limit_for(n, required_complexity)
        counter.set_operation_limit(operation_limit, required_complexity)
        # The engine's Challenge.run uses `max(10_000, operation_limit * 25)`
        # as the Python line-event cap. Mirror that.
        step_limit = max(10_000, operation_limit * 25)

        # --- 6. Setup the challenge (this also sets challenge.grid, etc.) ---
        setup_data = challenge.setup(n, seed)

        # --- 7. Run the player's solve() under the tracer ---
        trace = ExecutionTrace()
        error_message = ""
        result: Any = None
        try:
            # count_lines=False: don't count each Python line as a
            # CALL op (that's for line-step debugging). The trace
            # itself is captured regardless of this flag.
            result, trace = run_with_trace(
                solve_fn,
                setup_data,
                counter,
                count_lines=False,
                step_limit=step_limit,
            )
        except OperationLimitExceeded as exc:
            error_message = str(exc)
        except ExecutionStepLimitExceeded as exc:
            error_message = str(exc)
        except Exception as exc:
            # Player code crashed. Surface a friendly message; the
            # trace is whatever was captured before the crash.
            error_message = f"{type(exc).__name__}: {exc}"

        # --- 8. Verify correctness (if the run didn't already fail) ---
        correct = False
        if not error_message:
            try:
                # The verify() function reads the result, which might
                # be a TrackedList. Disable counting so the verify
                # read doesn't pollute the stats.
                was_counting = counter.enabled
                counter.enabled = False
                correct = challenge.verify(result)
            except Exception as exc:
                error_message = f"Could not verify: {type(exc).__name__}: {exc}"
                correct = False
            finally:
                counter.enabled = was_counting

        # --- 9. Build the structured result ---
        stats = counter.stats
        actual_complexity = counter.classify(n)
        within_threshold = counter.meets_threshold(n, required_complexity)
        passed = correct and within_threshold
        algorithm_match, algorithm_reason = check_fingerprint(
            counter.ops_log, challenge.info.expected_operations
        )

        message = _build_message(
            error_message=error_message,
            correct=correct,
            within_threshold=within_threshold,
            stats=stats,
            actual_complexity=actual_complexity,
            required_complexity=required_complexity,
            algorithm_match=algorithm_match,
            algorithm_reason=algorithm_reason,
        )

        # --- 10. Serialize the trace + ops log. Downsample if huge. ---
        ops_serialized = [serialize_op(op) for op in counter.ops_log]
        trace_serialized = [serialize_frame(f) for f in trace.frames]
        truncated = False
        if len(trace_serialized) > MAX_TRACE_FRAMES:
            # Keep every Nth frame + the first + last so the visualizer
            # can still see the start and end states. For MVP we just
            # truncate; the follow-up is to downsample more cleverly.
            step = max(1, len(trace_serialized) // MAX_TRACE_FRAMES)
            trace_serialized = trace_serialized[::step]
            truncated = True

        return RunResponse(
            passed=passed,
            correct=correct,
            within_threshold=within_threshold,
            algorithm_match=algorithm_match,
            algorithm_reason=algorithm_reason,
            actual_complexity=actual_complexity.value,
            required_complexity=required_complexity.value,
            n=n,
            message=message,
            stats=StatsOut(
                comparisons=stats.comparisons,
                swaps=stats.swaps,
                reads=stats.reads,
                writes=stats.writes,
                calls=stats.calls,
                total=stats.total,
            ),
            ops_log=[OpRecordOut(**op) for op in ops_serialized],
            trace=[TraceFrameOut(**f) for f in trace_serialized],
            return_value_repr=str(trace.return_value or repr(result)),
            truncated=truncated,
        )
    finally:
        # Always clean up the temp dir, even on exception.
        shutil.rmtree(tmpdir, ignore_errors=True)


def _build_message(
    error_message: str,
    correct: bool,
    within_threshold: bool,
    stats: OpStats,
    actual_complexity: ComplexityClass,
    required_complexity: ComplexityClass,
    algorithm_match: bool,
    algorithm_reason: str,
) -> str:
    """Build the same pass/fail message the engine's Challenge.run prints.

    The web StatusBanner shows it in the UI.
    """
    if error_message:
        return error_message
    if not correct:
        return "Incorrect solution!"
    if not within_threshold:
        return (
            f"Correct, but too slow! "
            f"Used {stats.total} ops (complexity: {actual_complexity.value}), "
            f"need {required_complexity.value}"
        )
    msg = f"Passed! {stats.total} ops (complexity: {actual_complexity.value})"
    if not algorithm_match and algorithm_reason:
        msg += f"\nAlgorithm hint: {algorithm_reason}"
    return msg
