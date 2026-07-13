"""``GET /api/challenges`` and ``GET /api/challenges/{id}``.

Lists the canonical challenge corpus and returns the full detail (params,
samples, starter source) for one. The complete summary list is built once at
application startup. Algorithm-set selectors are client-side views over this
same list, so switching views never requires another challenge request.
"""
from __future__ import annotations

import json
import urllib.error
import urllib.request
from functools import lru_cache

from fastapi import APIRouter, HTTPException

from challenges.registry import CHALLENGE_REGISTRY
from engine.solutions import _solution_template
from engine.languages import FUNCTION_LANGUAGES
from engine.special_environments import category_is_runnable
from server.app.optimal_sources import load_optimal_sources_by_language
from server.app.validated_cases import visible_cases
from server.app.challenge_sets import (
    external_subset_memberships_for,
    normalize_algorithm_set,
)
from server.app.challenge_packages import leetcode_submission_manifest_path
from server.app.schemas import (
    ChallengeDetail,
    ChallengeSummary,
    ParamDoc,
    Sample,
    TestCaseSummary,
)


router = APIRouter()

_LEETCODE_QUESTION_CACHE: dict[str, dict[str, str]] = {}


def _normalize_neetcode_category(category: str) -> str:
    cleaned = category.replace("neetcode_", "").replace("_", " ").strip()
    replacements = {
        "dp1": "1-D Dynamic Programming",
        "dp2": "2-D Dynamic Programming",
        "bit": "Bit Manipulation",
        "heap": "Heap / Priority Queue",
        "linked list": "Linked List",
        "binary search": "Binary Search",
        "advanced graphs": "Advanced Graphs",
    }
    return replacements.get(cleaned, cleaned.title())


def _custom_starter_sources(reference_metadata: dict) -> dict[str, str]:
    sources = reference_metadata.get("starter_sources")
    if not isinstance(sources, dict):
        return {}
    return {
        str(language): str(source)
        for language, source in sources.items()
        if isinstance(language, str) and isinstance(source, str)
    }


def _starter_source_for(spec, language: str = "python") -> str:
    reference_metadata = getattr(spec, "reference_metadata", {}) or {}
    custom_sources = _custom_starter_sources(reference_metadata)
    if language in custom_sources:
        return custom_sources[language]
    return _solution_template(
        spec.id,
        heading=f"{spec.id}: {spec.name}",
        description=spec.description,
        language=language,
    )


def _submission_summary(challenge_id: str) -> tuple[str, str, bool]:
    path = leetcode_submission_manifest_path(challenge_id)
    if path is None or not path.is_file():
        return "missing", "", False
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return "missing", "", False
    if not isinstance(payload, dict):
        return "missing", "", False
    return (
        str(payload.get("status") or "missing"),
        str(payload.get("language") or ""),
        bool(payload.get("paid_only", False)),
    )


def _spec_to_summary(challenge_id: str, challenge) -> ChallengeSummary:
    spec = getattr(challenge, "_spec", None)
    if spec is None:
        # Bare Challenge subclass (not a spec) — degrade gracefully.
        info = challenge.info
        return ChallengeSummary(
            id=info.id,
            name=info.name,
            category=info.category,
            categories=[info.category],
            difficulty_label="",
            elo_rating=None,
            difficulty_estimate=None,
            acceptance_rate=None,
            required_complexity=info.required_complexity.value,
            description=info.description,
            hint=info.hint or "",
            source_url="",
            parents=[],
            children=[],
            max_n=challenge.max_n,
            unlocked=True,
            leetcode_title="",
            leetcode_slug="",
            leetcode_url="",
        )
    reference_metadata = getattr(spec, "reference_metadata", {}) or {}
    lc_slug = str(reference_metadata.get("slug") or "")
    external_subsets = external_subset_memberships_for(spec.id) if lc_slug else []
    leetcode_title = spec.name
    leetcode_slug = lc_slug
    leetcode_url = str(spec.source_url or "")
    submission_status, submission_language, submission_paid_only = _submission_summary(spec.id)
    return ChallengeSummary(
        id=spec.id,
        name=spec.name,
        category=spec.category,
        categories=spec.categories or [spec.category],
        difficulty_label=spec.difficulty_label,
        elo_rating=spec.elo_rating,
        difficulty_estimate=spec.difficulty_estimate,
        acceptance_rate=spec.acceptance_rate,
        required_complexity=spec.required_complexity.value,
        description=spec.description,
        hint=spec.hint or "",
        source_url=spec.source_url or "",
        parents=list(spec.parents),
        children=list(spec.children),
        max_n=challenge.max_n,
        unlocked=True,
        leetcode_title=leetcode_title,
        leetcode_slug=leetcode_slug,
        leetcode_url=leetcode_url,
        leetcode_category=str(reference_metadata.get("category") or ""),
        leetcode_category_title=str(reference_metadata.get("category_title") or ""),
        leetcode_frontend_id=str(reference_metadata.get("frontend_id") or spec.id.removeprefix("lc_")),
        leetcode_topics=[
            dict(topic)
            for topic in reference_metadata.get("topics", [])
            if isinstance(topic, dict)
        ],
        leetcode_subsets=[
            str(subset)
            for subset in reference_metadata.get("subsets", [])
            if isinstance(subset, str)
        ],
        leetcode_tags=[
            str(tag)
            for tag in reference_metadata.get("tags", [])
            if isinstance(tag, str)
        ],
        leetcode_company_tags=[
            dict(company)
            for company in reference_metadata.get("company_tags", [])
            if isinstance(company, dict)
        ],
        leetcode_study_plans=[
            dict(study_plan)
            for study_plan in reference_metadata.get("study_plans", [])
            if isinstance(study_plan, dict)
        ],
        leetcode_external_subsets=external_subsets,
        supported_languages=[
            str(language)
            for language in reference_metadata.get("supported_languages", [])
            if isinstance(language, str)
        ],
        runnable_in_coden=category_is_runnable(reference_metadata),
        leetcode_submission_status=submission_status,
        leetcode_submission_language=submission_language,
        leetcode_submission_paid_only=submission_paid_only,
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
    if active_set not in {"neetcode", "leetcode_studyplan"}:
        return {c.info.id for c in all_challenges}
        
    completed = set(progress.completed)
    sequences: dict[str, list[tuple[int, str]]] = {}

    if active_set == "neetcode":
        neetcode_memberships = {
            challenge.info.id: [
                membership
                for membership in external_subset_memberships_for(challenge.info.id)
                if str(membership.get("kind") or "") == "neetcode"
            ]
            for challenge in all_challenges
        }
        for challenge_id, memberships in neetcode_memberships.items():
            for membership in memberships:
                path = membership.get("path") if isinstance(membership.get("path"), list) else []
                key = "/".join([str(membership.get("subset_slug") or "neetcode"), *(str(part) for part in path)])
                order = int(membership.get("order", 0) or 0)
                sequences.setdefault(key, []).append((order, challenge_id))

    if active_set == "leetcode_studyplan":
        for challenge in all_challenges:
            cid = challenge.info.id
            spec = getattr(challenge, "_spec", None)
            metadata = getattr(spec, "reference_metadata", {}) or {}
            study_plans = metadata.get("study_plans") if isinstance(metadata.get("study_plans"), list) else []
            for membership in study_plans:
                if not isinstance(membership, dict):
                    continue
                plan_slug = str(membership.get("plan_slug") or membership.get("slug") or "study-plan")
                path = membership.get("path") if isinstance(membership.get("path"), list) else []
                key = "/".join([plan_slug, *(str(part) for part in path)])
                order = int(membership.get("order", membership.get("problem_order", 0)) or 0)
                sequences.setdefault(key, []).append((order, cid))

    if not sequences:
        return {c.info.id for c in all_challenges}

    unlocked_challenges: set[str] = set()
    for ordered_members in sequences.values():
        cids = [
            cid
            for _, cid in sorted(ordered_members, key=lambda item: (item[0], item[1]))
        ]
        if not cids:
            continue
        unlocked_challenges.add(cids[0])
        for index in range(1, len(cids)):
            if cids[index - 1] in completed:
                unlocked_challenges.add(cids[index])
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
    test_cases = [
        TestCaseSummary(**case)
        for case in visible_cases(spec.id)
    ]
    reference_metadata = getattr(spec, "reference_metadata", {}) or {}
    runnable_in_coden = category_is_runnable(reference_metadata)
    supported_languages = set(reference_metadata.get("supported_languages") or [])
    starter_source = _starter_source_for(spec, "python")
    starter_sources = _custom_starter_sources(reference_metadata)
    if runnable_in_coden:
        starter_sources = {
            **starter_sources,
            **{
            language: _solution_template(
                spec.id,
                heading=f"{spec.id}: {spec.name}",
                description=spec.description,
                language=language,
            )
            for language in FUNCTION_LANGUAGES
            if not supported_languages or language in supported_languages
            },
        }
    complexity_notes = getattr(spec, "complexity_notes", {}) or {}

    optimal_sources = load_optimal_sources_by_language(spec.id, spec)
    optimal_source = optimal_sources.get("python", "")

    return ChallengeDetail(
        **summary.model_dump(),
        params=params,
        samples=samples,
        test_cases=test_cases,
        starter_source=starter_source,
        starter_sources=starter_sources,
        optimal_source=optimal_source,
        optimal_sources=optimal_sources,
        complexity_notes=complexity_notes,
    )


@router.get("/challenges")
def list_challenges() -> list[ChallengeSummary]:
    """Return the preloaded canonical corpus in registry insertion order."""
    return list(_cached_challenge_summaries())


@lru_cache(maxsize=1)
def _cached_challenge_summaries() -> tuple[ChallengeSummary, ...]:
    """Build immutable summary metadata once for every client-side view."""
    return tuple(
        _spec_to_summary(challenge_id, challenge_cls())
        for challenge_id, challenge_cls in CHALLENGE_REGISTRY.items()
    )


def warm_challenge_summaries() -> int:
    """Preload the full corpus before the desktop window is shown."""
    return len(_cached_challenge_summaries())


@router.get("/challenges/{challenge_id}")
def get_challenge_detail(challenge_id: str) -> ChallengeDetail:
    """Full canonical detail for one challenge, independent of its UI view."""
    cls = CHALLENGE_REGISTRY.get(challenge_id)
    if cls is None:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found")
    return _spec_to_detail(cls())
