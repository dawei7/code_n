"""The engine runner — runs a player's solution against a challenge.

This is the single point of integration between the FastAPI server
and the Python engine. It is the only file that:

* exec()'s player code
* calls into the engine's :class:`code_n.challenge.Challenge`
* runs the player's ``solve()`` under a tracer (the tracer
  enforces a step limit that catches infinite loops)
* converts the AST-based op count + the verifier's verdict
  into the Pydantic response model in :mod:`server.app.schemas`

Design notes
------------

**One temp file per run.** The engine's tracer uses
``func.__code__.co_filename`` to filter frames to the player's
file. A real file gives each run a unique filename (so two
concurrent runs with the same source don't collide). The
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

**The trace is internal-only.** The per-step trace frames
are no longer shipped to the frontend (the player debugs in
VSCode). The engine still uses the tracer for the step
limit; the trace exists only as a local variable in
``run_player_code`` and is discarded after the run.
"""
from __future__ import annotations

import logging
import runpy
import shutil
import tempfile
from pathlib import Path
from typing import Any, Optional

from challenges.registry import CHALLENGE_REGISTRY
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

from .ast_ops import count_ops as ast_count_ops
from .schemas import RunResponse
from .too_efficient import check as check_too_efficient
from .trace_codec import to_json_safe


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
    execution_path: Optional[str] = None,
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
    execution_path:
        Optional workspace path to execute from. When provided,
        ``runpy.run_path`` runs this exact path instead of a
        tempfile copy, so debugpy breakpoints in the player's
        ``solutions/<id>.py`` hit normally. Used by the VSCode
        F5 entry point (``tools/run_solution.py``); the FastAPI
        route (which receives only the source text from the
        renderer) leaves this ``None`` and gets the temp-file
        behaviour.

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

    # --- 2. Stage the source. By default we write it to a fresh
    #        temp dir so the tracer sees a unique ``co_filename``
    #        per run (avoids cache collisions between concurrent
    #        runs of the same challenge). When ``execution_path``
    #        is given (VSCode debug entry point) we skip the temp
    #        file and run from that exact path so debugpy hits
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

        # Capture pristine setup data representation before user solve mutates it in-place.
        setup_data_repr = {
            k: _format_return_value(v) for k, v in setup_data.items()
        }

        # Deep-copy setup data for the reference solve before the player's
        # code (which might perform in-place mutations) executes.
        import copy
        reference_return_value_repr: Optional[str] = None
        if hasattr(challenge, "_reference_solve"):
            try:
                ref_setup_data = copy.deepcopy(setup_data)
                ref_result = challenge._reference_solve(**ref_setup_data)
                reference_return_value_repr = _format_return_value(ref_result)
            except Exception as exc:
                log.warning(f"Failed to run reference solve: {exc}")

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

        # --- 9a. Compute tolerance band around reference's AST ops ---
        # The user's AST count should land within this band
        # to be considered "as efficient as the reference".
        #   low  = floor(μ * 0.90)
        #   high = ceil (μ * 1.05)
        # Below the band: likely a cheat. Above the band:
        # correct but slower than optimal. The band is the
        # "as good as the canonical solution" range.
        reference_ci_low: Optional[int] = None
        reference_ci_high: Optional[int] = None
        if reference_ast_ops is not None and reference_ast_ops > 0:
            import math
            reference_ci_low = int(math.floor(reference_ast_ops * 0.90))
            reference_ci_high = int(math.ceil(reference_ast_ops * 1.05))

        # Check if the required complexity is fulfilled. If the user's solution
        # falls within the tolerance band (<= reference_ci_high), it is automatically
        # considered efficient enough. Otherwise, fallback to the hardcoded budget limit.
        if reference_ci_high is not None:
            within_threshold = user_ast_ops <= reference_ci_high
        else:
            budget = limit_for(n, required_complexity)
            within_threshold = user_ast_ops <= budget

        # Classify complexity dynamically using the reference's coefficient if available
        actual_complexity = classify_ast_ops(
            user_ast_ops,
            n,
            reference_ast_ops=reference_ast_ops,
            required_complexity=required_complexity,
        )
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

        # --- 11a. Compute reference coefficient ---
        reference_coefficient: Optional[float] = None
        if reference_ast_ops is not None and reference_ast_ops > 0:
            from code_n.counter import get_complexity_factor
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
            reference_coefficient=reference_coefficient,
            scaling_data=scaling_data,
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
        text = text[:_RETURN_VALUE_CAP] + "…"
    return text
