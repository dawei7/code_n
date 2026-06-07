"""Pydantic schemas for the cOde(n) HTTP API.

All request and response bodies are defined here so the route modules
stay focused on wiring. Pydantic v2 syntax (``BaseModel`` + type
hints); ``model_dump`` produces the JSON-serialisable dict.

Naming convention: outbound models end in ``Out`` (or are themselves
``*Response`` / ``*Summary`` / ``*Detail``); inbound models are
``*Request`` / ``*Update`` / ``*Put``.
"""
from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field


# ----------------------------------------------------------------------------
# Challenges
# ----------------------------------------------------------------------------


class ParamDoc(BaseModel):
    """One named parameter of the player's ``solve()`` function."""

    name: str
    doc: str
    type_hint: str


class Sample(BaseModel):
    """One input/output example shown in the Explore view."""

    input_repr: str
    output_repr: str


class ChallengeSummary(BaseModel):
    """Card data for the challenge list in the left rail."""

    id: str
    name: str
    category: str
    difficulty: int
    required_complexity: str
    description: str
    hint: str = ""
    source_url: str = ""
    parents: list[str] = Field(default_factory=list)
    children: list[str] = Field(default_factory=list)
    max_n: int


class ChallengeDetail(ChallengeSummary):
    """Full data for the challenge view, including the editor's starter code."""

    params: list[ParamDoc]
    samples: list[Sample]
    starter_source: str
    optimal_source: str
    # Per-algorithm complexity notes (best/average/worst/space/
    # stable/in_place) for the scientific complexity panel.
    # Empty dict → hide the panel for this algorithm.
    complexity_notes: dict[str, str] = {}  # The Solve button writes this verbatim.


# ----------------------------------------------------------------------------
# Run
# ----------------------------------------------------------------------------


class RunRequest(BaseModel):
    """Body for ``POST /api/challenges/{id}/run``.

    The player types code in the editor; the server writes it to a
    temp file, imports it, and runs it against the engine.
    """

    source: str = Field(
        ...,
        description="Full Python source; must define `def solve(**kwargs)`",
    )
    n: int = Field(16, ge=2, le=100)
    seed: Optional[int] = None


class OpRecordOut(BaseModel):
    """One row of the engine's operation log."""

    op_type: str  # OpType.value: "compare" | "swap" | "read" | "write" | "call"
    detail: str


class TraceFrameOut(BaseModel):
    """One frame of the execution trace, captured at a Python line event.

    ``locals`` is a JSON-safe snapshot of the player's frame locals at
    that line. ``source_line`` is the actual source text (looked up
    server-side from ``source_file:line_no``) so the frontend can show
    "the statement that just ran" in the LocalsPanel header.
    """

    op_index: int
    line_no: int
    event: str  # "call" | "line" | "return"
    locals: dict[str, Any]
    return_value: str
    breakpoint: bool
    source_file: str
    source_line: str = ""


class StatsOut(BaseModel):
    """Aggregate operation counts for the run."""

    comparisons: int = 0
    swaps: int = 0
    reads: int = 0
    writes: int = 0
    calls: int = 0
    total: int = 0


class RunResponse(BaseModel):
    """The full result of a single run.

    ``ops_log`` and ``trace`` are the two timelines the visualizer
    steps through. The frontend maps them to the same step index:
    ``step N`` shows ``trace[N]`` for the locals and ``ops_log[N]``
    for the highlighted cells.
    """

    passed: bool
    correct: bool
    within_threshold: bool
    algorithm_match: bool
    algorithm_reason: str
    actual_complexity: str
    required_complexity: str
    n: int
    message: str
    stats: StatsOut
    ops_log: list[OpRecordOut]
    trace: list[TraceFrameOut]
    return_value_repr: str
    truncated: bool = False  # True if the trace was downsampled for size.


# ----------------------------------------------------------------------------
# Progress
# ----------------------------------------------------------------------------


class LevelRecordOut(BaseModel):
    challenge_id: str
    best_ops: int
    complexity_achieved: str
    attempts: int


class ProgressOut(BaseModel):
    player_name: str
    completed: list[str]
    last_status: dict[str, str]
    records: dict[str, LevelRecordOut]


class ProgressUpdate(BaseModel):
    """Body for ``PUT /api/progress``.

    Exactly one of ``mark`` / ``fail`` / ``reset`` should be set.
    ``player_name`` is a write-through for the player's display name.
    """

    player_name: Optional[str] = None
    mark: Optional[dict] = None  # {"challenge_id": str, "ops": int, "complexity": str}
    fail: Optional[str] = None  # challenge_id
    reset: bool = False


# ----------------------------------------------------------------------------
# Solutions
# ----------------------------------------------------------------------------


class SolutionGet(BaseModel):
    challenge_id: str
    source: str
    exists: bool


class SolutionPut(BaseModel):
    source: str
