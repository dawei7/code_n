"""Refresh mutable LeetCode metrics stored in every canonical problem package.

The command joins three data sources by numeric LeetCode frontend id:

* LeetCode's authenticated GraphQL problem list for official difficulty,
  acceptance rate, and the Premium 0-100 ``frequency`` value.
* the local ZeroTrac snapshot for real contest Elo ratings;
* the local legacy-contest membership snapshot used to calibrate estimated Elo.

Real ZeroTrac ratings remain sparse and authoritative.  ``estimated_elo_rating``
is written only for problems without a real rating.  The estimate uses official
difficulty and acceptance percentile, with non-overlapping difficulty bands.

The updater writes ``frequency``, ``elo_rating``, and
``estimated_elo_rating`` to every ``metadata.json`` and mirrors them in
``dsa/leetcode/index.json``. It validates the complete download before writing
anything and rejects unauthenticated all-zero Frequency responses.
"""

from __future__ import annotations

import argparse
import bisect
import json
import math
import os
import sys
import tempfile
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
INDEX_PATH = LEETCODE_ROOT / "index.json"
RATINGS_PATH = LEETCODE_ROOT / "_meta" / "zerotrac-ratings.json"
REPORT_PATH = LEETCODE_ROOT / "_meta" / "leetcode-metrics.json"
COOKIE_PATH = LEETCODE_ROOT / "_local" / ".leetcode_cookie"
GRAPHQL_URL = "https://leetcode.com/graphql"
USER_AGENT = "Mozilla/5.0 cOde(n) mutable metadata sync"
MODEL_VERSION = "difficulty-acceptance-v1"

DIFFICULTIES = ("Easy", "Medium", "Hard")
BASE_QUANTILE = 1 / 3
MINIMUM_QUANTILE = 0.10
MAXIMUM_QUANTILE = 0.75
TIER_GAP = 20.0
PERCENTILE_FLOOR = 0.05
PERCENTILE_CEILING = 0.95

ACCOUNT_QUERY = """
query globalData {
  userStatus {
    isSignedIn
    isPremium
    username
  }
}
"""

METRICS_QUERY = """
query problemsetQuestionList(
  $categorySlug: String,
  $limit: Int,
  $skip: Int,
  $filters: QuestionListFilterInput
) {
  problemsetQuestionList: questionList(
    categorySlug: $categorySlug,
    limit: $limit,
    skip: $skip,
    filters: $filters
  ) {
    total: totalNum
    questions: data {
      frontendQuestionId: questionFrontendId
      title
      titleSlug
      difficulty
      acRate
      frequency
    }
  }
}
"""


@dataclass
class EstimateModel:
    difficulty: str
    real_minimum: float
    real_maximum: float
    base: float
    minimum: float
    maximum: float
    calibration_offset: float = 0.0
    real_rating_count: int = 0
    acceptance_count: int = 0


def _atomic_write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as stream:
            json.dump(payload, stream, indent=2, ensure_ascii=False)
            stream.write("\n")
        os.replace(temporary_path, path)
    finally:
        temporary_path.unlink(missing_ok=True)


def _load_json_object(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Cannot read JSON object {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise RuntimeError(f"Expected a JSON object in {path}")
    return payload


def load_index_questions() -> list[dict[str, Any]]:
    payload = _load_json_object(INDEX_PATH)
    questions = payload.get("questions")
    if not isinstance(questions, list) or not questions:
        raise RuntimeError(f"{INDEX_PATH} has no canonical question list")
    normalized: list[dict[str, Any]] = []
    seen: set[str] = set()
    for raw_question in questions:
        if not isinstance(raw_question, dict):
            raise RuntimeError(f"{INDEX_PATH} contains a non-object question")
        frontend_id = str(raw_question.get("frontend_id") or "")
        slug = str(raw_question.get("slug") or "")
        if not frontend_id or not slug:
            raise RuntimeError(f"Canonical question is missing identity: {raw_question!r}")
        if frontend_id in seen:
            raise RuntimeError(f"Duplicate canonical frontend id: {frontend_id}")
        seen.add(frontend_id)
        normalized.append(dict(raw_question))
    return normalized


def load_rating_metadata() -> tuple[dict[str, float], set[str], dict[str, Any]]:
    payload = _load_json_object(RATINGS_PATH)
    raw_ratings = payload.get("ratings")
    if not isinstance(raw_ratings, dict):
        raise RuntimeError(f"{RATINGS_PATH} has no ratings mapping")
    ratings = {
        str(frontend_id): float(rating)
        for frontend_id, rating in raw_ratings.items()
        if isinstance(rating, (int, float)) and math.isfinite(float(rating))
    }
    legacy_payload = payload.get("legacy_acceptance_estimate")
    raw_legacy = (
        legacy_payload.get("contest_by_frontend_id")
        if isinstance(legacy_payload, dict)
        else None
    )
    legacy_ids = {
        str(frontend_id)
        for frontend_id, contest_number in (raw_legacy or {}).items()
        if isinstance(contest_number, int) and 1 <= contest_number <= 62
    }
    return ratings, legacy_ids, payload


def quantile(sorted_values: list[float], position: float) -> float:
    if not sorted_values:
        raise ValueError("Cannot calculate a quantile of an empty sequence")
    index = (len(sorted_values) - 1) * max(0.0, min(1.0, position))
    lower = math.floor(index)
    upper = math.ceil(index)
    if lower == upper:
        return sorted_values[lower]
    fraction = index - lower
    return sorted_values[lower] + (sorted_values[upper] - sorted_values[lower]) * fraction


def acceptance_percentile(value: float, sorted_values: list[float]) -> float | None:
    if not sorted_values:
        return None
    first = bisect.bisect_left(sorted_values, value)
    last = bisect.bisect_right(sorted_values, value) - 1
    mid_rank = (first + max(first, last)) / 2
    return 0.5 if len(sorted_values) == 1 else mid_rank / (len(sorted_values) - 1)


def estimated_elo_from_acceptance(
    model: EstimateModel,
    percentile: float | None,
    calibration_offset: float | None = None,
) -> float:
    if percentile is None:
        return model.base
    robust_percentile = max(
        PERCENTILE_FLOOR,
        min(PERCENTILE_CEILING, percentile),
    )
    if robust_percentile >= 0.5:
        fraction = (robust_percentile - 0.5) / 0.5
        estimate = model.base - (model.base - model.minimum) * fraction
    else:
        fraction = (0.5 - robust_percentile) / 0.5
        estimate = model.base + (model.maximum - model.base) * fraction
    offset = model.calibration_offset if calibration_offset is None else calibration_offset
    return max(model.minimum, min(model.maximum, estimate + offset))


def _calibration_offset(
    model: EstimateModel,
    percentiles: list[float | None],
) -> float:
    if not percentiles or all(percentile is None for percentile in percentiles):
        return 0.0
    lower = model.minimum - model.maximum
    upper = model.maximum - model.minimum
    for _ in range(48):
        candidate = (lower + upper) / 2
        average = sum(
            estimated_elo_from_acceptance(model, percentile, candidate)
            for percentile in percentiles
        ) / len(percentiles)
        if average < model.base:
            lower = candidate
        else:
            upper = candidate
    return (lower + upper) / 2


def calculate_estimated_elos(
    questions: Iterable[dict[str, Any]],
    ratings: dict[str, float],
    legacy_ids: set[str],
) -> tuple[dict[str, float], dict[str, EstimateModel]]:
    question_list = list(questions)
    ratings_by_difficulty = {difficulty: [] for difficulty in DIFFICULTIES}
    acceptance_by_difficulty = {difficulty: [] for difficulty in DIFFICULTIES}

    for question in question_list:
        frontend_id = str(question.get("frontend_id") or "")
        difficulty = str(question.get("difficulty") or "")
        if difficulty not in ratings_by_difficulty:
            continue
        rating = ratings.get(frontend_id)
        if rating is not None:
            ratings_by_difficulty[difficulty].append(rating)
        acceptance = question.get("acceptance_rate")
        if isinstance(acceptance, (int, float)) and math.isfinite(float(acceptance)):
            acceptance_by_difficulty[difficulty].append(float(acceptance))

    for values in ratings_by_difficulty.values():
        values.sort()
    for values in acceptance_by_difficulty.values():
        values.sort()

    models: dict[str, EstimateModel] = {}
    for difficulty in DIFFICULTIES:
        real_values = ratings_by_difficulty[difficulty]
        if not real_values:
            raise RuntimeError(f"No real ZeroTrac ratings are available for {difficulty}")
        acceptance_values = acceptance_by_difficulty[difficulty]
        models[difficulty] = EstimateModel(
            difficulty=difficulty,
            real_minimum=real_values[0],
            real_maximum=real_values[-1],
            base=quantile(real_values, BASE_QUANTILE),
            minimum=quantile(real_values, MINIMUM_QUANTILE),
            maximum=quantile(real_values, MAXIMUM_QUANTILE),
            real_rating_count=len(real_values),
            acceptance_count=len(acceptance_values),
        )

    for easier_name, harder_name in zip(DIFFICULTIES, DIFFICULTIES[1:]):
        easier = models[easier_name]
        harder = models[harder_name]
        if easier.maximum >= harder.minimum:
            midpoint = (easier.base + harder.base) / 2
            easier.maximum = min(easier.maximum, midpoint - TIER_GAP / 2)
            harder.minimum = max(harder.minimum, midpoint + TIER_GAP / 2)
        if easier.maximum >= harder.minimum:
            raise RuntimeError(
                f"Estimated Elo bands overlap: {easier_name} {easier.maximum} "
                f">= {harder_name} {harder.minimum}"
            )

    for model in models.values():
        model.minimum = max(model.real_minimum, min(model.base, model.minimum))
        model.maximum = min(model.real_maximum, max(model.base, model.maximum))

    for difficulty in DIFFICULTIES:
        model = models[difficulty]
        acceptance_values = acceptance_by_difficulty[difficulty]
        legacy_percentiles: list[float | None] = []
        for question in question_list:
            frontend_id = str(question.get("frontend_id") or "")
            if (
                frontend_id not in legacy_ids
                or frontend_id in ratings
                or str(question.get("difficulty") or "") != difficulty
            ):
                continue
            acceptance = question.get("acceptance_rate")
            percentile = (
                acceptance_percentile(float(acceptance), acceptance_values)
                if isinstance(acceptance, (int, float)) and math.isfinite(float(acceptance))
                else None
            )
            legacy_percentiles.append(percentile)
        model.calibration_offset = _calibration_offset(model, legacy_percentiles)

    estimates: dict[str, float] = {}
    for question in question_list:
        frontend_id = str(question.get("frontend_id") or "")
        if not frontend_id or frontend_id in ratings:
            continue
        difficulty = str(question.get("difficulty") or "")
        model = models.get(difficulty)
        if model is None:
            continue
        acceptance = question.get("acceptance_rate")
        percentile = (
            acceptance_percentile(
                float(acceptance),
                acceptance_by_difficulty[difficulty],
            )
            if isinstance(acceptance, (int, float)) and math.isfinite(float(acceptance))
            else None
        )
        estimates[frontend_id] = estimated_elo_from_acceptance(model, percentile)
    return estimates, models


def _cookie_header(cookie_path: Path) -> str:
    explicit = os.environ.get("LEETCODE_COOKIE", "").strip()
    if explicit:
        return explicit
    session = os.environ.get("LEETCODE_SESSION", "").strip()
    csrf = (
        os.environ.get("LEETCODE_CSRFTOKEN", "").strip()
        or os.environ.get("LEETCODE_CSRF_TOKEN", "").strip()
    )
    clearance = os.environ.get("LEETCODE_CF_CLEARANCE", "").strip()
    if session and csrf:
        parts = [f"LEETCODE_SESSION={session}", f"csrftoken={csrf}"]
        if clearance:
            parts.append(f"cf_clearance={clearance}")
        return "; ".join(parts)
    if cookie_path.is_file():
        return cookie_path.read_text(encoding="utf-8").strip()
    return ""


def _request_graphql(
    query: str,
    variables: dict[str, Any],
    *,
    cookie: str,
) -> dict[str, Any]:
    body = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "User-Agent": USER_AGENT,
        "Referer": "https://leetcode.com/problemset/",
    }
    if cookie:
        headers["Cookie"] = cookie
    request = urllib.request.Request(
        GRAPHQL_URL,
        data=body,
        headers=headers,
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"LeetCode metrics request failed: {exc}") from exc
    if payload.get("errors"):
        raise RuntimeError(f"LeetCode metrics request failed: {payload['errors']}")
    data = payload.get("data")
    if not isinstance(data, dict):
        raise RuntimeError("LeetCode metrics response has no data object")
    return data


def fetch_leetcode_metrics(
    *,
    cookie_path: Path = COOKIE_PATH,
    page_size: int = 100,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    cookie = _cookie_header(cookie_path)
    if not cookie:
        raise RuntimeError(
            "LeetCode Frequency requires an authenticated Premium session. "
            "Set LEETCODE_SESSION and LEETCODE_CSRFTOKEN, or refresh "
            f"{cookie_path}."
        )
    status_data = _request_graphql(ACCOUNT_QUERY, {}, cookie=cookie)
    status = status_data.get("userStatus")
    if not isinstance(status, dict) or not status.get("isSignedIn"):
        raise RuntimeError(
            "The saved LeetCode session is expired or invalid. Refresh "
            f"{cookie_path}; no metadata was changed."
        )
    if not status.get("isPremium"):
        raise RuntimeError(
            "LeetCode Frequency is a Premium field. The authenticated account "
            "is not Premium; no metadata was changed."
        )

    questions: list[dict[str, Any]] = []
    skip = 0
    total: int | None = None
    while total is None or skip < total:
        data = _request_graphql(
            METRICS_QUERY,
            {
                "categorySlug": "",
                "limit": page_size,
                "skip": skip,
                "filters": {},
            },
            cookie=cookie,
        )
        page = data.get("problemsetQuestionList")
        if not isinstance(page, dict):
            raise RuntimeError("LeetCode metrics response has no question list")
        total = int(page.get("total") or 0)
        raw_questions = page.get("questions")
        if not isinstance(raw_questions, list) or not raw_questions:
            break
        for raw_question in raw_questions:
            if not isinstance(raw_question, dict):
                raise RuntimeError("LeetCode metrics response contains a non-object question")
            frequency = raw_question.get("frequency")
            if (
                not isinstance(frequency, (int, float))
                or not math.isfinite(float(frequency))
                or not 0 <= float(frequency) <= 100
            ):
                raise RuntimeError(
                    "LeetCode returned a missing or invalid Frequency value for "
                    f"{raw_question.get('titleSlug')!r}"
                )
            questions.append({
                "frontend_id": str(raw_question.get("frontendQuestionId") or ""),
                "title": str(raw_question.get("title") or ""),
                "slug": str(raw_question.get("titleSlug") or ""),
                "difficulty": str(raw_question.get("difficulty") or ""),
                "acceptance_rate": raw_question.get("acRate"),
                "frequency": float(frequency),
            })
        skip += len(raw_questions)

    if total is None or len(questions) != total:
        raise RuntimeError(
            f"Incomplete LeetCode Frequency download: received {len(questions)} of {total}"
        )
    if not questions or max(float(question["frequency"]) for question in questions) <= 0:
        raise RuntimeError(
            "LeetCode returned only zero Frequency values. This usually means "
            "the session lost Premium access; no metadata was changed."
        )
    return questions, {
        "username": str(status.get("username") or ""),
        "is_premium": True,
        "question_count": len(questions),
    }


def load_metrics_snapshot(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict) and isinstance(payload.get("stat_status_pairs"), list):
        raw_pairs = payload["stat_status_pairs"]
        expected_total = payload.get("num_total")
        if isinstance(expected_total, int) and len(raw_pairs) != expected_total:
            raise RuntimeError(
                "Incomplete LeetCode REST snapshot: "
                f"received {len(raw_pairs)} of {expected_total}"
            )

        raw_frequencies: list[float] = []
        for raw_pair in raw_pairs:
            frequency = raw_pair.get("frequency") if isinstance(raw_pair, dict) else None
            if (
                not isinstance(frequency, (int, float))
                or not math.isfinite(float(frequency))
                or float(frequency) < 0
            ):
                raise RuntimeError(f"Invalid REST snapshot Frequency: {frequency!r}")
            raw_frequencies.append(float(frequency))
        maximum_frequency = max(raw_frequencies, default=0.0)
        if maximum_frequency <= 0:
            raise RuntimeError(
                "LeetCode REST snapshot contains only zero Frequency values. "
                "The signed-in account may not have Premium access."
            )

        difficulty_names = {1: "Easy", 2: "Medium", 3: "Hard"}
        questions: list[dict[str, Any]] = []
        for raw_pair, raw_frequency in zip(raw_pairs, raw_frequencies, strict=True):
            stat = raw_pair.get("stat")
            if not isinstance(stat, dict):
                raise RuntimeError("REST snapshot contains a question without stat metadata")
            total_accepted = stat.get("total_acs")
            total_submitted = stat.get("total_submitted")
            acceptance_rate = None
            if (
                isinstance(total_accepted, (int, float))
                and isinstance(total_submitted, (int, float))
                and float(total_submitted) > 0
            ):
                acceptance_rate = 100 * float(total_accepted) / float(total_submitted)
            difficulty = raw_pair.get("difficulty")
            difficulty_level = (
                difficulty.get("level") if isinstance(difficulty, dict) else None
            )
            questions.append({
                "frontend_id": str(stat.get("frontend_question_id") or ""),
                "title": str(stat.get("question__title") or ""),
                "slug": str(stat.get("question__title_slug") or ""),
                "difficulty": difficulty_names.get(difficulty_level, ""),
                "acceptance_rate": acceptance_rate,
                # The REST endpoint exposes the raw prominence score. LeetCode's
                # problem-list tooltip displays it relative to the corpus maximum.
                "frequency": round(100 * raw_frequency / maximum_frequency, 1),
            })
        return questions

    if isinstance(payload, dict):
        raw_questions = payload.get("questions")
    else:
        raw_questions = payload
    if not isinstance(raw_questions, list):
        raise RuntimeError("Metrics snapshot must be a question array or contain a questions array")
    questions: list[dict[str, Any]] = []
    for raw_question in raw_questions:
        if not isinstance(raw_question, dict):
            raise RuntimeError("Metrics snapshot contains a non-object question")
        frequency = raw_question.get("frequency")
        if (
            not isinstance(frequency, (int, float))
            or not math.isfinite(float(frequency))
            or not 0 <= float(frequency) <= 100
        ):
            raise RuntimeError(f"Invalid snapshot Frequency: {frequency!r}")
        questions.append({
            "frontend_id": str(
                raw_question.get("frontend_id")
                or raw_question.get("frontendQuestionId")
                or raw_question.get("questionFrontendId")
                or ""
            ),
            "title": str(raw_question.get("title") or ""),
            "slug": str(raw_question.get("slug") or raw_question.get("titleSlug") or ""),
            "difficulty": str(raw_question.get("difficulty") or ""),
            "acceptance_rate": (
                raw_question.get("acceptance_rate")
                if "acceptance_rate" in raw_question
                else raw_question.get("acRate")
            ),
            "frequency": float(frequency),
        })
    return questions


def _join_current_metrics(
    canonical_questions: list[dict[str, Any]],
    upstream_questions: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    upstream_by_id: dict[str, dict[str, Any]] = {}
    for question in upstream_questions:
        frontend_id = str(question.get("frontend_id") or "")
        if not frontend_id:
            raise RuntimeError(f"Upstream question is missing a frontend id: {question!r}")
        if frontend_id in upstream_by_id:
            raise RuntimeError(f"Duplicate upstream frontend id: {frontend_id}")
        upstream_by_id[frontend_id] = question

    joined: list[dict[str, Any]] = []
    missing: list[str] = []
    for canonical in canonical_questions:
        frontend_id = str(canonical["frontend_id"])
        upstream = upstream_by_id.get(frontend_id)
        if upstream is None:
            missing.append(frontend_id)
            continue
        canonical_slug = str(canonical.get("slug") or "")
        upstream_slug = str(upstream.get("slug") or canonical_slug)
        if upstream_slug != canonical_slug:
            raise RuntimeError(
                f"LeetCode identity mismatch for {frontend_id}: "
                f"{upstream_slug!r} != {canonical_slug!r}"
            )
        merged = dict(canonical)
        merged["difficulty"] = str(upstream.get("difficulty") or canonical.get("difficulty") or "")
        acceptance = upstream.get("acceptance_rate")
        if isinstance(acceptance, (int, float)) and math.isfinite(float(acceptance)):
            merged["acceptance_rate"] = float(acceptance)
        merged["frequency"] = upstream.get("frequency")
        joined.append(merged)
    if missing:
        preview = ", ".join(missing[:10])
        raise RuntimeError(
            f"LeetCode metrics download is missing {len(missing)} canonical ids: {preview}"
        )
    return joined


def _with_metric_fields(
    payload: dict[str, Any],
    *,
    frequency: float | None,
    elo_rating: float | None,
    estimated_elo_rating: float | None,
    difficulty: str,
    acceptance_rate: float | None,
) -> dict[str, Any]:
    updates = {
        "difficulty": difficulty,
        "acceptance_rate": acceptance_rate,
        "frequency": frequency,
        "elo_rating": elo_rating,
        "estimated_elo_rating": estimated_elo_rating,
    }
    result: dict[str, Any] = {}
    inserted = False
    for key, value in payload.items():
        if key in updates:
            if key == "difficulty":
                result["difficulty"] = updates["difficulty"]
            elif key == "acceptance_rate":
                result["acceptance_rate"] = updates["acceptance_rate"]
                result["frequency"] = updates["frequency"]
                result["elo_rating"] = updates["elo_rating"]
                result["estimated_elo_rating"] = updates["estimated_elo_rating"]
                inserted = True
            continue
        result[key] = value
    if "difficulty" not in result:
        result["difficulty"] = updates["difficulty"]
    if not inserted:
        result["acceptance_rate"] = updates["acceptance_rate"]
        result["frequency"] = updates["frequency"]
        result["elo_rating"] = updates["elo_rating"]
        result["estimated_elo_rating"] = updates["estimated_elo_rating"]
    return result


def metadata_paths_by_frontend_id() -> dict[str, Path]:
    result: dict[str, Path] = {}
    for path in LEETCODE_ROOT.glob("*/metadata.json"):
        prefix, separator, _slug = path.parent.name.partition("_")
        if not separator or not prefix.isdigit() or len(prefix) < 4:
            continue
        payload = _load_json_object(path)
        frontend_id = str(payload.get("frontend_id") or "")
        if not frontend_id:
            raise RuntimeError(f"Package metadata has no frontend id: {path}")
        if frontend_id in result:
            raise RuntimeError(
                f"Duplicate package frontend id {frontend_id}: {result[frontend_id]} and {path}"
            )
        result[frontend_id] = path
    return result


def update_metrics(
    *,
    upstream_questions: list[dict[str, Any]] | None,
    refresh_frequency: bool,
    dry_run: bool,
) -> dict[str, Any]:
    index_payload = _load_json_object(INDEX_PATH)
    canonical_questions = load_index_questions()
    ratings, legacy_ids, rating_payload = load_rating_metadata()

    if refresh_frequency:
        if upstream_questions is None:
            raise ValueError("upstream_questions is required when refresh_frequency is true")
        questions = _join_current_metrics(canonical_questions, upstream_questions)
    else:
        questions = [dict(question) for question in canonical_questions]
        for question in questions:
            question.setdefault("frequency", None)

    estimates, models = calculate_estimated_elos(questions, ratings, legacy_ids)
    package_paths = metadata_paths_by_frontend_id()
    canonical_ids = {str(question["frontend_id"]) for question in questions}
    missing_packages = sorted(canonical_ids - set(package_paths), key=lambda value: int(value))
    if missing_packages:
        preview = ", ".join(missing_packages[:10])
        raise RuntimeError(
            f"{len(missing_packages)} canonical questions have no package metadata: {preview}"
        )

    updated_questions: list[dict[str, Any]] = []
    package_writes: list[tuple[Path, dict[str, Any]]] = []
    changed_packages = 0
    for question in questions:
        frontend_id = str(question["frontend_id"])
        frequency = question.get("frequency")
        if frequency is None:
            normalized_frequency = None
        elif (
            isinstance(frequency, (int, float))
            and math.isfinite(float(frequency))
            and 0 <= float(frequency) <= 100
        ):
            normalized_frequency = float(frequency)
        else:
            raise RuntimeError(
                f"Stored Frequency for frontend id {frontend_id} is invalid: {frequency!r}"
            )
        estimate = estimates.get(frontend_id)
        normalized_estimate = round(estimate, 6) if estimate is not None else None
        real_rating = ratings.get(frontend_id)
        if (real_rating is None) == (normalized_estimate is None):
            raise RuntimeError(
                f"Frontend id {frontend_id} must have exactly one real or estimated Elo value"
            )
        acceptance = question.get("acceptance_rate")
        normalized_acceptance = (
            float(acceptance)
            if isinstance(acceptance, (int, float)) and math.isfinite(float(acceptance))
            else None
        )
        difficulty = str(question.get("difficulty") or "")

        updated_question = _with_metric_fields(
            question,
            frequency=normalized_frequency,
            elo_rating=real_rating,
            estimated_elo_rating=normalized_estimate,
            difficulty=difficulty,
            acceptance_rate=normalized_acceptance,
        )
        updated_questions.append(updated_question)

        path = package_paths[frontend_id]
        package = _load_json_object(path)
        if str(package.get("slug") or "") != str(question.get("slug") or ""):
            raise RuntimeError(
                f"Package identity mismatch for {frontend_id}: "
                f"{package.get('slug')!r} != {question.get('slug')!r}"
            )
        updated_package = _with_metric_fields(
            package,
            frequency=normalized_frequency,
            elo_rating=real_rating,
            estimated_elo_rating=normalized_estimate,
            difficulty=difficulty,
            acceptance_rate=normalized_acceptance,
        )
        if updated_package != package:
            changed_packages += 1
            package_writes.append((path, updated_package))

    updated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    report = {
        "updated_at": updated_at,
        "model_version": MODEL_VERSION,
        "frequency_refreshed": refresh_frequency,
        "canonical_problem_count": len(updated_questions),
        "frequency_count": sum(
            isinstance(question.get("frequency"), (int, float))
            for question in updated_questions
        ),
        "real_elo_count": sum(
            str(question["frontend_id"]) in ratings
            for question in updated_questions
        ),
        "estimated_elo_count": len(estimates),
        "changed_metadata_files": changed_packages,
        "zerotrac_revision": str(rating_payload.get("upstream_revision") or ""),
        "zerotrac_updated_at": str(rating_payload.get("upstream_updated_at") or ""),
        "estimate_model": {
            difficulty: {
                key: round(value, 6) if isinstance(value, float) else value
                for key, value in asdict(model).items()
            }
            for difficulty, model in models.items()
        },
    }

    if not dry_run:
        for path, payload in package_writes:
            _atomic_write_json(path, payload)
        updated_index = dict(index_payload)
        updated_index["questions"] = updated_questions
        updated_index["count"] = len(updated_questions)
        _atomic_write_json(INDEX_PATH, updated_index)
        _atomic_write_json(REPORT_PATH, report)
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--offline",
        action="store_true",
        help=(
            "Recompute estimated Elo from the current local index and preserve "
            "stored Frequency values; no LeetCode request is made."
        ),
    )
    parser.add_argument(
        "--snapshot",
        type=Path,
        help="Use a reviewed LeetCode metrics JSON snapshot instead of the live API.",
    )
    parser.add_argument(
        "--cookie-path",
        type=Path,
        default=COOKIE_PATH,
        help="Cookie-header file used for authenticated LeetCode Frequency.",
    )
    parser.add_argument("--page-size", type=int, default=100)
    parser.add_argument(
        "--refresh-zerotrac",
        action="store_true",
        help="Refresh the real ZeroTrac snapshot before recalculating estimates.",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    if args.offline and args.snapshot:
        parser.error("--offline and --snapshot cannot be combined")
    if args.refresh_zerotrac and args.dry_run:
        parser.error("--refresh-zerotrac cannot be combined with --dry-run")

    account: dict[str, Any] = {}
    upstream_questions: list[dict[str, Any]] | None = None
    refresh_frequency = not args.offline
    if args.snapshot:
        upstream_questions = load_metrics_snapshot(args.snapshot)
        account = {"source": str(args.snapshot)}
    elif refresh_frequency:
        upstream_questions, account = fetch_leetcode_metrics(
            cookie_path=args.cookie_path,
            page_size=args.page_size,
        )

    # Authenticate and validate the complete LeetCode Frequency download
    # before allowing the optional ZeroTrac refresh to write its snapshot.
    if refresh_frequency and upstream_questions is not None:
        _join_current_metrics(load_index_questions(), upstream_questions)
    if args.refresh_zerotrac:
        from tools.sync_zerotrac_ratings import sync as sync_zerotrac

        sync_zerotrac()

    report = update_metrics(
        upstream_questions=upstream_questions,
        refresh_frequency=refresh_frequency,
        dry_run=args.dry_run,
    )
    if account:
        report["leetcode_account"] = account
    action = "Would update" if args.dry_run else "Updated"
    print(
        f"{action} {report['canonical_problem_count']} problems: "
        f"{report['frequency_count']} Frequency values, "
        f"{report['real_elo_count']} real Elo ratings, and "
        f"{report['estimated_elo_count']} estimated Elo values "
        f"({report['changed_metadata_files']} package files changed)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
