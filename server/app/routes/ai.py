"""``POST /api/ai/hint`` — local Ollama hint for a recent run.

The client sends the AI report (the same one it already has from
``RunResponse.ai_report``) along with the challenge id. The
server:

  1. Looks up the canonical optimal source server-side (the
     client never has access to it). This is the only place
     the optimal source ever leaves the server.
  2. Builds a prompt that includes the user's code, the test
     result, the complexity comparison, the locals at failure,
     and the optimal source. The prompt has a strong
     "DO NOT include the solution" instruction.
  3. POSTs to the local Ollama instance at
     ``http://localhost:11434/api/generate`` with
     ``model="qwen2.5-coder:7b"`` (the hardcoded default).
  4. Post-processes the response: any line that appears in
     the optimal source is stripped, plus any line that looks
     like a code line (def, return, if, for, while, import,
     or anything inside a ``````` block).
  5. Returns ``{hint, model, latency_ms}``. If Ollama is
     unreachable (URLError, connection refused, timeout), the
     endpoint returns a server-generated fallback hint built
     from the static ``algorithm_hint`` (the OperationConstraint
     fingerprint reason), so the user always gets *something*.

The endpoint is intentionally small: no streaming, no chat
history, no embeddings. Just "ask the local LLM for one short
hint about the last run".
"""
from __future__ import annotations

import json
import logging
import time
import urllib.error
import urllib.request
from typing import Any, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from challenges.registry import CHALLENGE_REGISTRY


log = logging.getLogger(__name__)


router = APIRouter()


# ---- Defaults (env-overridable for power users) ----
DEFAULT_OLLAMA_URL = "http://localhost:11434"
DEFAULT_MODEL = "qwen2.5-coder:7b"
OLLAMA_TIMEOUT_SECONDS = 30.0

import os
_OLLAMA_URL = os.environ.get("CODEN_OLLAMA_URL", DEFAULT_OLLAMA_URL)
_MODEL = os.environ.get("CODEN_OLLAMA_MODEL", DEFAULT_MODEL)


# ---- Request schema ----


class HintRequest(BaseModel):
    """Body for ``POST /api/ai/hint``.

    The client posts the AI report it received from the run
    endpoint. We re-validate it on the server (Pydantic does
    this implicitly via :class:`dict`).
    """

    report: dict[str, Any] = Field(
        ...,
        description="The AI report from the run (RunResponse.ai_report).",
    )


class HintResponse(BaseModel):
    hint: str
    model: str
    latency_ms: int
    fallback: bool = False
    fallback_reason: str = ""


# ---- Prompt construction ----


_PROMPT_TEMPLATE = """You are a coding tutor helping a student debug a Python algorithm.

The student is solving: {name} ({challenge_id}, category: {category})
Required complexity: {required_complexity}

Problem:
{description}

Student's code:
```python
{user_source}
```

Test setup: n={n}, seed={seed}
Result: {result_summary}
Message: {message}
Op count: {ops_total} (classified: {actual_complexity}, required: {required_complexity})

Locals at the last execution frame:
{locals_block}

Reference solution (DO NOT include this in your response, do not paraphrase it, do not hint at specific lines):
```python
{optimal_source}
```

Give ONE short hint (1-2 sentences, no code) about what the student might be doing wrong or how to improve. Do NOT include code, the optimal solution, or the full answer. Hints only."""


def _build_prompt(report: dict[str, Any], optimal_source: str) -> str:
    """Format the prompt template with the report + optimal source."""
    test = report.get("test", {})
    result = report.get("result", {})

    if result.get("passed"):
        result_summary = "PASSED"
    elif result.get("too_efficient"):
        result_summary = "REJECTED (too efficient: possible hardcoded or skipping work)"
    elif not result.get("correct"):
        result_summary = "FAILED (wrong output)"
    elif not result.get("within_threshold"):
        result_summary = "TOO SLOW (correct but over the complexity budget)"
    else:
        result_summary = f"FAILED: {result.get('message', '')}"

    locals_block = _format_locals(report.get("locals_at_failure"))

    return _PROMPT_TEMPLATE.format(
        challenge_id=report.get("challenge_id", "?"),
        name=report.get("challenge_name", "?"),
        category=report.get("category", "?"),
        required_complexity=report.get("required_complexity", "?"),
        description=(report.get("description", "") or "(no description)"),
        user_source=(report.get("user_source", "") or "(empty)"),
        n=test.get("n", "?"),
        seed=test.get("seed", "?"),
        result_summary=result_summary,
        message=result.get("message", ""),
        ops_total=result.get("ops_total", 0),
        actual_complexity=result.get("actual_complexity", "?"),
        locals_block=locals_block,
        optimal_source=optimal_source,
    )


def _format_locals(locals_at_failure: Optional[dict]) -> str:
    if not locals_at_failure:
        return "(no locals captured — likely a syntax error)"
    try:
        return json.dumps(locals_at_failure, indent=2)[:2000]
    except (TypeError, ValueError):
        return "(could not serialize locals)"


# ---- Response post-processing ----


def _strip_code_blocks(text: str, optimal_source: str) -> str:
    """Strip anything that smells like a code block or the
    optimal solution from the LLM response.

    Three layers of defense:

      1. Remove any line that appears verbatim in the optimal
         source (catches "leaked" code from prompt instructions
         the model ignored).
      2. Remove any line that starts with a Python keyword
         (``def``, ``return``, ``if``, ``for``, ``while``,
         ``import``) — catches the model writing a small code
         snippet even without a ``````` block.
      3. Remove any block of text wrapped in ``````` (catches
         the model using markdown code blocks).

    Whatever remains is the prose hint.
    """
    optimal_lines = {line.strip() for line in optimal_source.splitlines() if line.strip()}

    # Layer 1 + 2: filter line-by-line
    out_lines: list[str] = []
    in_code_block = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        if not stripped:
            out_lines.append(line)
            continue
        if stripped in optimal_lines:
            continue
        # Python keyword check
        first_word = stripped.split(maxsplit=1)[0]
        if first_word in {"def", "return", "if", "elif", "else:", "for", "while", "import", "from", "class", "try:", "except", "with", "lambda", "yield", "raise", "pass"}:
            # Allow short English sentences that happen to start
            # with "if", "for", etc. (e.g. "If you want to…").
            # A line is treated as code if it ends with `:`, has
            # `=`, has balanced parens, has `[` or `]` (subscript
            # or list literal), or starts the line directly with
            # the keyword (no introductory phrase).
            stripped_after = stripped[len(first_word):].lstrip()
            if (
                stripped.endswith(":")
                or "=" in stripped
                or (("(" in stripped) and (")" in stripped))
                or ("[" in stripped) or ("]" in stripped)
                # The line is just the keyword + something (no
                # "you" / "this" / "we" prefixing it).
                or stripped_after.split(maxsplit=1)[0:1] == stripped_after.split(maxsplit=1)[0:1]
                and first_word in {"return", "def", "import", "from", "raise", "pass", "yield"}
            ):
                continue
        out_lines.append(line)

    return "\n".join(out_lines).strip()


# ---- Endpoint ----


@router.post("/ai/hint")
def get_hint(body: HintRequest) -> HintResponse:
    """Ask local Ollama for one hint about the most recent run.

    Falls back to a server-generated hint when Ollama is down
    (returns ``fallback=True`` so the UI can label it).
    """
    report = body.report
    challenge_id = report.get("challenge_id")
    if not challenge_id:
        raise HTTPException(status_code=400, detail="report.challenge_id is required")

    # Look up the optimal source server-side. The client never
    # has access to it; this is the only place it leaves the
    # server.
    challenge_cls = CHALLENGE_REGISTRY.get(challenge_id)
    if challenge_cls is None:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found")
    spec = getattr(challenge_cls(), "_spec", None)
    if spec is None or not getattr(spec, "source", None):
        raise HTTPException(
            status_code=500,
            detail=f"Challenge '{challenge_id}' has no spec source",
        )
    optimal_source = spec.source

    # Try Ollama.
    prompt = _build_prompt(report, optimal_source)
    start = time.monotonic()
    try:
        raw = _call_ollama(prompt)
        latency_ms = int((time.monotonic() - start) * 1000)
        cleaned = _strip_code_blocks(raw, optimal_source)
        if not cleaned:
            # The LLM returned only code that we stripped;
            # fall back so the user gets *something*.
            return _fallback(report, reason="ollama_response_was_only_code")
        return HintResponse(hint=cleaned, model=_MODEL, latency_ms=latency_ms)
    except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
        log.info("Ollama unreachable: %s; serving fallback hint", e)
        return _fallback(report, reason=f"ollama_unreachable: {type(e).__name__}")
    except Exception as e:
        # Any other failure (JSON parse, HTTP error, etc.) →
        # fallback. We never want to 500 the user on an AI
        # failure; the fallback hint is at least as good as a
        # broken page.
        log.warning("Ollama call failed: %s", e)
        return _fallback(report, reason=f"ollama_error: {type(e).__name__}")


def _call_ollama(prompt: str) -> str:
    """POST the prompt to Ollama and return the raw response text.

    Raises on connection failure / HTTP error / JSON parse
    failure (caller catches and falls back).
    """
    payload = {
        "model": _MODEL,
        "prompt": prompt,
        "stream": False,
    }
    req = urllib.request.Request(
        f"{_OLLAMA_URL}/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=OLLAMA_TIMEOUT_SECONDS) as resp:
        raw = resp.read().decode("utf-8")
    body = json.loads(raw)
    return body.get("response", "")


def _fallback(report: dict[str, Any], reason: str) -> HintResponse:
    """Build a server-generated hint from the static fields in
    the report. Used when Ollama is down or returns junk."""
    result = report.get("result", {})
    static_hint = report.get("algorithm_hint", "") or ""
    parts: list[str] = []

    if result.get("too_efficient"):
        parts.append(
            "Your solution looks too efficient — the op count is well below the "
            "reference's, which often means a hardcoded answer or reading private "
            "state. Re-run with a fresh approach that does the actual work."
        )
    elif not result.get("passed"):
        if not result.get("correct"):
            parts.append("The output doesn't match the expected result yet.")
        elif not result.get("within_threshold"):
            parts.append(
                f"The output is correct, but the algorithm is too slow "
                f"({result.get('actual_complexity')} vs required "
                f"{report.get('required_complexity', '?')})."
            )
        if static_hint:
            parts.append(static_hint)

    if not parts:
        parts.append("No specific hint available — review the locals at the last frame and the message above.")

    return HintResponse(
        hint=" ".join(parts),
        model="fallback",
        latency_ms=0,
        fallback=True,
        fallback_reason=reason,
    )
