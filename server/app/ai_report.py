"""Build the structured AI report shipped in every RunResponse.

The report is the input to the local Ollama hint endpoint AND the
content of the AI Report tab in the UI. It contains:

  * Challenge meta (id, name, category, description, required complexity)
  * Test input summary (n, seed, a short repr of the input)
  * User source (verbatim)
  * Result (passed, message, op counts, classified complexity,
    within_threshold, too_efficient + reason)
  * Locals at failure: the last trace frame's locals, if any

What the report does NOT contain: the optimal source. The
reference is only added to the LLM prompt server-side (in
``routes/ai.py``), so it never reaches the client and can never
leak through the AI tab. The LLM response is post-processed to
strip code before it's returned to the user.

The report is JSON-serialisable: sets are converted to lists,
TrackedList / TrackedGrid are unwrapped via the engine codec,
and the rest is plain dicts / str / int / float / bool.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Optional

from .trace_codec import to_json_safe


# Cap on the description we ship. The full description can be
# long; the LLM only needs the first ~400 chars to anchor on the
# problem.
_DESCRIPTION_CAP = 400

# Cap on the user source we ship. The full source is in the
# file already; 4KB is plenty for the LLM to see what the user
# is doing.
_SOURCE_CAP = 4096

# Cap on the locals-at-failure dict (after serialization). For
# huge data structures (a 50-element BFS frontier, etc.) we don't
# want to blow up the prompt.
_LOCALS_CAP_BYTES = 4096


@dataclass
class AiReport:
    """The structured report built by :func:`build`.

    Fields use Python-friendly names (snake_case). The Pydantic
    response model in ``schemas.py`` aliases them to the wire
    format (``aiReport`` etc).
    """

    challenge_id: str
    challenge_name: str
    category: str
    description: str
    required_complexity: str
    test: dict[str, Any]
    user_source: str
    result: dict[str, Any]
    locals_at_failure: Optional[dict[str, Any]] = None
    # Optional: an algorithm hint from the OperationConstraint
    # fingerprint (when present and the algorithm match failed).
    # Useful for the fallback hint when Ollama is down.
    algorithm_hint: str = ""
    # AST-derived op counts (the "scientific" metric, computed
    # statically by walking the source's AST). Used by the
    # Complexity tab and the LLM hint prompt.
    user_ast_ops: Optional[int] = None
    reference_ast_ops: Optional[int] = None
    reference_ci_low: Optional[int] = None
    reference_ci_high: Optional[int] = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "challenge_id": self.challenge_id,
            "challenge_name": self.challenge_name,
            "category": self.category,
            "description": self.description,
            "required_complexity": self.required_complexity,
            "test": self.test,
            "user_source": self.user_source,
            "result": self.result,
            "locals_at_failure": self.locals_at_failure,
            "algorithm_hint": self.algorithm_hint,
            "user_ast_ops": self.user_ast_ops,
            "reference_ast_ops": self.reference_ast_ops,
            "reference_ci_low": self.reference_ci_low,
            "reference_ci_high": self.reference_ci_high,
        }


def build(
    *,
    challenge_id: str,
    challenge_name: str,
    category: str,
    description: str,
    required_complexity: str,
    n: int,
    seed: Optional[int],
    user_source: str,
    passed: bool,
    correct: bool,
    within_threshold: bool,
    actual_complexity: str,
    message: str,
    ops_total: int,
    ops_breakdown: dict[str, int],
    too_efficient: bool,
    too_efficient_reason: str,
    trace_frames: list[Any],
    algorithm_hint: str = "",
    user_ast_ops: Optional[int] = None,
    reference_ast_ops: Optional[int] = None,
    reference_ci_low: Optional[int] = None,
    reference_ci_high: Optional[int] = None,
) -> AiReport:
    """Build the report from the run's raw state.

    Parameters
    ----------
    challenge_id, challenge_name, category, description, required_complexity:
        From the AlgorithmSpec. Description is truncated.
    n, seed:
        The actual values the run used (echoed back to the
        frontend in real_test mode).
    user_source:
        The source the player submitted.
    passed, correct, within_threshold, actual_complexity, message:
        From the RunResponse verdict.
    ops_total, ops_breakdown:
        ``{"comparisons": N, "swaps": N, ...}`` for the run.
    too_efficient, too_efficient_reason:
        From the too_efficient check.
    trace_frames:
        The list of TraceFrame objects from ``ExecutionTrace.frames``.
        The report picks the last frame as the "locals at failure"
        snapshot. If the list is empty (e.g. syntax error before
        execution started), ``locals_at_failure`` is None.
    algorithm_hint:
        The static ``algorithm_reason`` from the OperationConstraint
        fingerprint check, when present. Used as a fallback hint
        when Ollama is down.
    reference_ops, reference_ci_low, reference_ci_high:
        Deterministic ±5% tolerance band around the reference's
        op count. Forwarded to the LLM so it can reason about
        the user's efficiency.
    """
    # --- test summary ---
    test_summary: dict[str, Any] = {
        "n": n,
        "seed": seed,
    }

    # --- result ---
    result: dict[str, Any] = {
        "passed": passed,
        "correct": correct,
        "within_threshold": within_threshold,
        "actual_complexity": actual_complexity,
        "message": message,
        "ops_total": ops_total,
        "ops_breakdown": ops_breakdown,
        "too_efficient": too_efficient,
        "too_efficient_reason": too_efficient_reason,
    }

    # --- locals at failure ---
    locals_at_failure: Optional[dict[str, Any]] = None
    if trace_frames:
        # The last frame is the most useful snapshot — by the
        # time the run errored out (or returned), the frame
        # locals are the state the player left things in.
        # For runs that errored, this is the frame right before
        # the exception. For runs that completed, this is the
        # final frame.
        last = trace_frames[-1]
        frame_dict = {
            "line_no": int(getattr(last, "line_no", 0)),
            "event": str(getattr(last, "event", "")),
            "locals": to_json_safe(getattr(last, "locals", {})),
            "return_value": str(getattr(last, "return_value", "") or ""),
        }
        # Cap the locals size to keep prompts small.
        try:
            dumped = json.dumps(frame_dict)
            if len(dumped) <= _LOCALS_CAP_BYTES:
                locals_at_failure = frame_dict
            else:
                # Keep the frame metadata but truncate the locals.
                frame_dict["locals"] = {
                    "_truncated": True,
                    "_reason": f"locals were {len(dumped)} bytes, capped at {_LOCALS_CAP_BYTES}",
                }
                locals_at_failure = frame_dict
        except (TypeError, ValueError):
            locals_at_failure = {
                "line_no": int(getattr(last, "line_no", 0)),
                "event": str(getattr(last, "event", "")),
                "locals": {"_error": "could not serialize"},
            }

    return AiReport(
        challenge_id=challenge_id,
        challenge_name=challenge_name,
        category=category,
        description=(description or "")[:_DESCRIPTION_CAP],
        required_complexity=required_complexity,
        test=test_summary,
        user_source=(user_source or "")[:_SOURCE_CAP],
        result=result,
        locals_at_failure=locals_at_failure,
        algorithm_hint=algorithm_hint,
    )
