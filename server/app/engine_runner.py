"""The engine runner — runs a player's solution against a challenge.

This is the single point of integration between the FastAPI server
and the Python engine. It is the only file that:

* exec()'s player code
* calls into the engine's :class:`code_n.challenge.Challenge`
* runs the player's ``solve()`` under a tracer (for the
  visualizer step player)
* converts the AST-based op count + the verifier's verdict
  into the Pydantic response model in :mod:`server.app.schemas`

Design notes
------------

**One temp file per run.** The engine's tracer uses
``func.__code__.co_filename`` to filter frames to the player's
file. A real file gives each run a unique filename (so two
concurrent runs with the same source don't collide) and lets
the breakpoint loader work against an actual on-disk file. The
temp file is cleaned up in a ``finally`` block.

**No source wrapping.** The player source is exec'd verbatim
via ``runpy.run_path``. The runtime op counter (and its
``TrackedList`` / ``TrackedGrid`` wrappers) was removed in
v0.8.5. The player's input is now a plain list / dict / set;
the AST-based op counter in :mod:`server.app.ast_ops` is the
single source of truth for the "how many ops does your code
do?" question.

**Verdict is AST-based.** ``passed`` is ``correct AND
user_ast_ops <= limit_for(n, required_complexity)`` —
``within_threshold`` is a pure comparison of two integers.
``actual_complexity`` is the smallest ``ComplexityClass``
whose budget still fits the user's AST op count at ``n``
(see :func:`code_n.counter.classify_ast_ops`). The complexity
heuristic has no runtime dependency.

**Step limit is a safety cap.** The tracer raises
``ExecutionStepLimitExceeded`` after a fixed number of Python
line events (100,000) to catch infinite loops. The cap is
independent of the complexity budget — a single ``for i in
range(10**9):`` would trip the cap, but a correct but
sloppy O(n²) solution that just barely exceeds the budget
would still be evaluated end-to-end.
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
from code_n.challenge import Challenge
from code_n.counter import (
    ComplexityClass,
    classify_ast_ops,
    limit_for,
)
from code_n.execution_trace import (
    ExecutionStepLimitExceeded,
    ExecutionTrace,
    run_with_trace,
)

from .ai_report import build as build_ai_report
from .ast_ops import count_ops as ast_count_ops
from .config import MAX_TRACE_FRAMES
from .schemas import RunResponse, TraceFrameOut
from .too_efficient import check as check_too_efficient
from .trace_codec import serialize_frame


log = logging.getLogger(__name__)


# Safety cap on Python line events. Independent of the
# complexity budget — purely an infinite-loop guard. 100,000
# events is plenty for any correct algorithm up to the max
# input size; an infinite loop is caught quickly.
_STEP_LIMIT = 100_000


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
    mode: str = "practice",
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
        Optional RNG seed for reproducible inputs. The route layer
        picks a fresh seed when ``mode="real_test"``.
    mode:
        Echoed back in the response. "practice" or "real_test".

    Returns
    -------
    :class:`RunResponse`
        All the data the frontend needs: the pass/fail verdict
        (derived from the AST op count), the trace for the
        visualizer, and the ±5% tolerance band numbers for the
        Complexity tab.

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
    #        filter to this exact file.
    #
    # NOTE: No source wrapping / AST rewriting is performed here. The
    # player source is exec'd verbatim via ``runpy.run_path``. The
    # engine's tracking proxies (TrackedList, TrackedGrid, ...) were
    # removed in v0.8.5; the player's input is now a plain list /
    # dict / set. What the user sees in the editor is exactly what
    # runs.
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

        # --- 5. Setup the challenge (returns plain lists / dicts) ---
        setup_data = challenge.setup(n, seed)

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

        # --- 8. AST-based op counts (the SINGLE op metric) ---
        # We count ops by walking the AST of BOTH the user's
        # source and the reference's source. The result is a
        # deterministic integer per (source, n) pair. No
        # dynamic counter, no proxies — what the user sees
        # in the editor is exactly what gets counted.
        user_ast_ops = ast_count_ops(source, n)
        spec = getattr(challenge, "_spec", None)
        reference_source = (spec.source if spec is not None else None) or ""
        reference_ast_ops = (
            ast_count_ops(reference_source, n) if reference_source else None
        )

        # --- 9. Derive the verdict from the AST op count ---
        required_complexity = challenge.info.required_complexity
        budget = limit_for(n, required_complexity)
        within_threshold = user_ast_ops <= budget
        # "as efficient as the smallest class whose budget
        # still fits your op count"
        actual_complexity = classify_ast_ops(user_ast_ops, n)
        passed = correct and within_threshold

        # --- 10. Too-efficient check (AST + ratio vs reference) ---
        # If the user's AST count is < 30% of the
        # reference's AST count, they probably skipped work
        # (or hardcoded an answer). The check is purely
        # structural — no runtime data needed.
        too_efficient = False
        too_efficient_reason = ""
        if correct:
            te_result = check_too_efficient(
                user_source=source,
                user_ops=user_ast_ops,
                reference_ops=reference_ast_ops,
            )
            if te_result.flagged:
                too_efficient = True
                too_efficient_reason = te_result.message
                passed = False

        # --- 11. ±5% tolerance band around the reference's AST ops ---
        # The user's AST op count should land within this band
        # to be considered "as efficient as the reference".
        #   low  = floor(μ * 0.95)
        #   high = ceil (μ * 1.05)
        # Below the band: likely a cheat. Above the band:
        # correct but slower than optimal. The band is the
        # "as good as the canonical solution" range.
        reference_ci_low: Optional[int] = None
        reference_ci_high: Optional[int] = None
        if reference_ast_ops is not None and reference_ast_ops > 0:
            import math
            reference_ci_low = int(math.floor(reference_ast_ops * 0.95))
            reference_ci_high = int(math.ceil(reference_ast_ops * 1.05))

        message = _build_message(
            error_message=error_message,
            correct=correct,
            within_threshold=within_threshold,
            user_ast_ops=user_ast_ops,
            actual_complexity=actual_complexity,
            required_complexity=required_complexity,
            too_efficient=too_efficient,
            too_efficient_reason=too_efficient_reason,
        )

        # --- 12. Serialize the trace. Downsample if huge. ---
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
            actual_complexity=actual_complexity.value,
            required_complexity=required_complexity.value,
            n=n,
            seed=seed,
            mode=mode,
            too_efficient=too_efficient,
            too_efficient_reason=too_efficient_reason,
            user_ast_ops=user_ast_ops,
            reference_ast_ops=reference_ast_ops,
            reference_ci_low=reference_ci_low,
            reference_ci_high=reference_ci_high,
            message=message,
            trace=[TraceFrameOut(**f) for f in trace_serialized],
            return_value_repr=str(trace.return_value or repr(result)),
            truncated=truncated,
            ai_report=build_ai_report(
                challenge_id=challenge_id,
                challenge_name=challenge.info.name,
                category=challenge.info.category,
                description=challenge.info.description,
                required_complexity=required_complexity.value,
                n=n,
                seed=seed,
                user_source=source,
                passed=passed,
                correct=correct,
                within_threshold=within_threshold,
                actual_complexity=actual_complexity.value,
                message=message,
                ops_total=user_ast_ops,
                too_efficient=too_efficient,
                too_efficient_reason=too_efficient_reason,
                trace_frames=trace.frames,
                user_ast_ops=user_ast_ops,
                reference_ast_ops=reference_ast_ops,
                reference_ci_low=reference_ci_low,
                reference_ci_high=reference_ci_high,
            ).to_dict(),
        )
    finally:
        # Always clean up the temp dir, even on exception.
        shutil.rmtree(tmpdir, ignore_errors=True)


def _build_message(
    error_message: str,
    correct: bool,
    within_threshold: bool,
    user_ast_ops: int,
    actual_complexity: ComplexityClass,
    required_complexity: ComplexityClass,
    too_efficient: bool = False,
    too_efficient_reason: str = "",
) -> str:
    """Build the pass/fail message the web StatusBanner shows.

    The message references the AST op count (``user_ast_ops``)
    — the single source of truth for "how many ops does your
    code do?". When ``too_efficient`` is true, the run is
    shown as not correct with a short explanation (the user
    can fix and retry).
    """
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
        return (
            f"Correct, but too slow! "
            f"Used {user_ast_ops} ops (complexity: {actual_complexity.value}), "
            f"need {required_complexity.value}"
        )
    return f"Passed! {user_ast_ops} ops (complexity: {actual_complexity.value})"
