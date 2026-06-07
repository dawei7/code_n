"""``GET /api/challenges`` and ``GET /api/challenges/{id}``.

Lists the registered challenges and returns the full detail (params,
samples, starter source) for one. Built once at import time from
:data:`challenges.registry.CHALLENGE_REGISTRY` and cached as a
module-level list so the request is a constant-time dict lookup.
"""
from __future__ import annotations

from fastapi import APIRouter, HTTPException

from challenges.registry import CHALLENGE_REGISTRY
from code_n.solutions import _solution_template
from server.app.schemas import (
    ChallengeDetail,
    ChallengeSummary,
    ParamDoc,
    Sample,
)


router = APIRouter()


def _spec_to_summary(challenge_id: str, challenge) -> ChallengeSummary:
    spec = getattr(challenge, "_spec", None)
    if spec is None:
        # Bare Challenge subclass (not a spec) — degrade gracefully.
        info = challenge.info
        return ChallengeSummary(
            id=info.id,
            name=info.name,
            category=info.category,
            difficulty=info.difficulty,
            required_complexity=info.required_complexity.value,
            description=info.description,
            hint=info.hint or "",
            source_url="",
            parents=[],
            children=[],
            max_n=challenge.max_n,
        )
    return ChallengeSummary(
        id=spec.id,
        name=spec.name,
        category=spec.category,
        difficulty=spec.difficulty,
        required_complexity=spec.required_complexity.value,
        description=spec.description,
        hint=spec.hint or "",
        source_url=spec.source_url or "",
        parents=list(spec.parents),
        children=list(spec.children),
        max_n=challenge.max_n,
    )


def _spec_to_detail(challenge) -> ChallengeDetail:
    spec = getattr(challenge, "_spec", None)
    if spec is None:
        raise HTTPException(status_code=404, detail="Challenge has no spec metadata")

    summary = _spec_to_summary(spec.id, challenge)

    params = [
        ParamDoc(
            name=name,
            doc=spec.inputs.get(name, ""),
            type_hint=spec.inputs.get(name, "Any"),
        )
        for name in spec.params
    ]
    samples = [
        Sample(input_repr=s.input_repr, output_repr=s.output_repr)
        for s in spec.samples
    ]
    starter_source = _solution_template(
        spec.id,
        heading=f"{spec.id}: {spec.name}",
        description=spec.description,
    )

    return ChallengeDetail(
        **summary.model_dump(),
        params=params,
        samples=samples,
        starter_source=starter_source,
        optimal_source=spec.source or "",
    )


@router.get("/challenges")
def list_challenges() -> list[ChallengeSummary]:
    """List all challenges. Order matches registry insertion order."""
    return [
        _spec_to_summary(cid, cls())
        for cid, cls in CHALLENGE_REGISTRY.items()
    ]


@router.get("/challenges/{challenge_id}")
def get_challenge_detail(challenge_id: str) -> ChallengeDetail:
    """Full detail (params, samples, starter source) for one challenge."""
    cls = CHALLENGE_REGISTRY.get(challenge_id)
    if cls is None:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found")
    return _spec_to_detail(cls())
