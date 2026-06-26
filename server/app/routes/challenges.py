"""``GET /api/challenges`` and ``GET /api/challenges/{id}``.

Lists the registered challenges and returns the full detail (params,
samples, starter source) for one. Built once at import time from
:data:`challenges.registry.CHALLENGE_REGISTRY` and cached as a
module-level list so the request is a constant-time dict lookup.
"""
from __future__ import annotations

import json
import urllib.error
import urllib.request

from fastapi import APIRouter, HTTPException

from challenges.registry import CHALLENGE_REGISTRY
from code_n.solutions import _solution_template
from server.app.optimal_sources import load_optimal_source
from server.app.challenge_sets import challenge_set_id, challenge_set_label, normalize_algorithm_set
from server.app.schemas import (
    ChallengeDetail,
    ChallengeSummary,
    ParamDoc,
    Sample,
)


router = APIRouter()

_LEETCODE_QUESTION_CACHE: dict[str, dict[str, str]] = {}


def _spec_to_summary(challenge_id: str, challenge) -> ChallengeSummary:
    from server.app.leetcode_mapping import LEETCODE_MAPPING
    lc = LEETCODE_MAPPING.get(challenge_id, {})
    
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
            unlocked=True,
            leetcode_title=lc.get("title", ""),
            leetcode_slug=lc.get("slug", ""),
            leetcode_url=lc.get("url", ""),
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
        unlocked=True,
        leetcode_title=lc.get("title", ""),
        leetcode_slug=lc.get("slug", ""),
        leetcode_url=lc.get("url", ""),
    )


@router.get("/leetcode/questions/{title_slug}")
def get_leetcode_question(title_slug: str) -> dict[str, str]:
    """Fetch LeetCode's public frontend problem id for one title slug.

    The local registry stores stable LeetCode URLs. The numeric id is
    owned by LeetCode, so we resolve it from their public GraphQL API
    and cache it for the current server process.
    """
    if title_slug in _LEETCODE_QUESTION_CACHE:
        return _LEETCODE_QUESTION_CACHE[title_slug]

    body = json.dumps({
        "query": (
            "query questionTitle($titleSlug: String!) { "
            "question(titleSlug: $titleSlug) { questionFrontendId title titleSlug } "
            "}"
        ),
        "variables": {"titleSlug": title_slug},
    }).encode("utf-8")
    request = urllib.request.Request(
        "https://leetcode.com/graphql",
        data=body,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0",
            "Referer": f"https://leetcode.com/problems/{title_slug}/",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=8) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise HTTPException(status_code=502, detail=f"LeetCode lookup failed: {exc}") from exc

    question = (payload.get("data") or {}).get("question")
    if not question:
        raise HTTPException(status_code=404, detail=f"LeetCode question '{title_slug}' not found")

    result = {
        "frontend_id": str(question.get("questionFrontendId") or ""),
        "title": str(question.get("title") or ""),
        "slug": str(question.get("titleSlug") or title_slug),
    }
    _LEETCODE_QUESTION_CACHE[title_slug] = result
    return result


def get_unlocked_challenges(progress, all_challenges) -> set[str]:
    active_set = normalize_algorithm_set(progress.active_set)
    if active_set != "neetcode":
        return {c.info.id for c in all_challenges}
        
    completed = set(progress.completed)
    
    # Helper to normalise category names
    def normalise_cat(cat: str) -> str:
        cat = cat.lower()
        if cat == 'trees':
            return 'tree'
        if cat == 'backtracking':
            return 'recursion'
        if cat == 'hash':
            return 'hashing'
        return cat

    # 1. Group challenges by normalised category in insertion order
    cat_challenges = {}
    for c in all_challenges:
        cid = c.info.id
        if not cid.startswith("nc_"):
            continue
        cat = normalise_cat(c.info.category) if c.info.category else ""
        cat_challenges.setdefault(cat, []).append(cid)

    # 2. Determine unlocked challenges sequentially within each category
    unlocked_challenges = set()
    for cat, cids in cat_challenges.items():
        if cids:
            unlocked_challenges.add(cids[0])
            for i in range(1, len(cids)):
                # Unlocked only if the previous problem in the category is completed
                prev_cid = cids[i - 1]
                if prev_cid in completed:
                    unlocked_challenges.add(cids[i])
            
    return unlocked_challenges


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
    complexity_notes = getattr(spec, "complexity_notes", {}) or {}

    optimal_source = load_optimal_source(spec.id, spec)

    return ChallengeDetail(
        **summary.model_dump(),
        params=params,
        samples=samples,
        starter_source=starter_source,
        optimal_source=optimal_source,
        complexity_notes=complexity_notes,
    )


@router.get("/challenges")
def list_challenges() -> list[ChallengeSummary]:
    """List all challenges. Order matches registry insertion order."""
    from server.app import progress_store
    progress = progress_store.load()
    active_set = normalize_algorithm_set(progress.active_set)
    
    all_challenges = [cls() for cls in CHALLENGE_REGISTRY.values()]
    unlocked_set = get_unlocked_challenges(progress, all_challenges)
    
    summaries = []
    for c in all_challenges:
        if challenge_set_id(c.info.id) != active_set:
            continue
        summary = _spec_to_summary(c.info.id, c)
        summary.unlocked = c.info.id in unlocked_set
        summaries.append(summary)
    return summaries


@router.get("/challenges/{challenge_id}")
def get_challenge_detail(challenge_id: str) -> ChallengeDetail:
    """Full detail (params, samples, starter source) for one challenge."""
    from server.app import progress_store
    progress = progress_store.load()
    active_set = normalize_algorithm_set(progress.active_set)
    
    cls = CHALLENGE_REGISTRY.get(challenge_id)
    if cls is None:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found")
        
    c = cls()
    all_challenges = [cls() for cls in CHALLENGE_REGISTRY.values()]
    unlocked_set = get_unlocked_challenges(progress, all_challenges)
    
    challenge_set = challenge_set_id(challenge_id)
    if challenge_set != active_set:
        raise HTTPException(
            status_code=404,
            detail=f"Challenge '{challenge_id}' is not in the {challenge_set_label(active_set)} set."
        )

    if active_set == "neetcode":
        if not challenge_id.startswith("nc_"):
            raise HTTPException(
                status_code=404,
                detail=f"Challenge '{challenge_id}' is not in the NeetCode 250 set."
            )
        if challenge_id not in unlocked_set:
            raise HTTPException(
                status_code=403,
                detail="Challenge is locked. Complete parent challenges first."
            )
        
    return _spec_to_detail(c)
