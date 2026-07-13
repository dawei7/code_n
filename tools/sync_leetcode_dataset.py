"""Sync canonical LeetCode metadata into ``dsa/leetcode`` packages.

The sync stores metadata only. It does not copy LeetCode problem statements,
editorials, or solution text. Existing local docs, cases, benchmarks, and
solutions are preserved.

Use ``--company-tags`` to enrich packages with company tags. That mode
is intentionally separate because it needs per-question metadata and is slower.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
INDEX_PATH = LEETCODE_ROOT / "index.json"
SUBSETS_PATH = LEETCODE_ROOT / "subsets.json"
TEMPLATE_PATH = LEETCODE_ROOT / "_template.md"
COOKIE_PATH = LEETCODE_ROOT / "_local" / ".leetcode_cookie"
REPORT_PATH = LEETCODE_ROOT / "_reports" / "sync_report.json"
GRAPHQL_URL = "https://leetcode.com/graphql"


PROBLEMSET_QUERY = """
query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList: questionList(
    categorySlug: $categorySlug
    limit: $limit
    skip: $skip
    filters: $filters
  ) {
    total: totalNum
    questions: data {
      acRate
      difficulty
      frontendQuestionId: questionFrontendId
      title
      titleSlug
      categoryTitle
      topicTags {
        name
        slug
      }
    }
  }
}
"""

STUDY_PLAN_CATALOGS_QUERY = """
query GetStudyPlanCatalogs {
  studyPlanV2Catalogs {
    name
    recommendedStudyPlans
    slug
  }
}
"""

STUDY_PLANS_BY_CATALOG_QUERY = """
query GetStudyPlanByCatalog($catalogSlug: String!, $offset: Int!, $limit: Int!) {
  studyPlansV2ByCatalog(catalogSlug: $catalogSlug, offset: $offset, limit: $limit) {
    hasMore
    total
    studyPlans {
      slug
      questionNum
      premiumOnly
      onGoing
      name
      highlight
      cover
    }
  }
}
"""

STUDY_PLAN_DETAIL_QUERY = """
query studyPlanDetail($slug: String!) {
  studyPlanV2Detail(planSlug: $slug) {
    slug
    name
    highlight
    description
    premiumOnly
    questionNum
    defaultLanguage
    relatedStudyPlans {
      name
      slug
      premiumOnly
    }
    planSubGroups {
      slug
      name
      premiumOnly
      questionNum
      questions {
        titleSlug
        title
        questionFrontendId
        paidOnly
        id
        difficulty
        topicTags {
          slug
          name
        }
      }
    }
  }
}
"""


def slugify(value: str) -> str:
    text = value.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "unknown"


def package_dir(question: dict[str, Any]) -> Path:
    return LEETCODE_ROOT / f"{question['frontend_id']}_{slugify(question['slug'])}"


def cookie_header() -> str:
    if COOKIE_PATH.is_file():
        return COOKIE_PATH.read_text(encoding="utf-8").strip()
    return ""


def request_graphql(query: str, variables: dict[str, Any], *, referer: str = "https://leetcode.com/problemset/") -> dict[str, Any]:
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 cOde(n) metadata sync",
        "Referer": referer,
    }
    cookie = cookie_header()
    if cookie:
        headers["Cookie"] = cookie
    request = urllib.request.Request(GRAPHQL_URL, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"LeetCode metadata request failed: HTTP {exc.code}: {detail}") from exc

    data = json.loads(body)
    if data.get("errors"):
        raise RuntimeError(f"LeetCode metadata request failed: {data['errors']}")
    return data["data"]


def fetch_questions(page_size: int = 100) -> list[dict[str, Any]]:
    skip = 0
    total: int | None = None
    questions: list[dict[str, Any]] = []
    while total is None or skip < total:
        data = request_graphql(
            PROBLEMSET_QUERY,
            {
                "categorySlug": "",
                "skip": skip,
                "limit": page_size,
                "filters": {},
            },
        )
        page = data["problemsetQuestionList"]
        total = int(page["total"])
        raw_questions = list(page["questions"])
        if not raw_questions:
            break
        questions.extend(normalize_question(question) for question in raw_questions)
        skip += len(raw_questions)
    questions.sort(key=sort_key)
    return questions


def sort_key(question: dict[str, Any]) -> tuple[int, str]:
    frontend_id = str(question.get("frontend_id") or "")
    return (int(frontend_id) if frontend_id.isdigit() else 10**9, str(question.get("slug") or ""))


def category_slug(category_title: str) -> str:
    return slugify(category_title or "uncategorized")


def supported_languages_for_category(category_title: str) -> list[str]:
    slug = category_slug(category_title)
    if slug == "algorithms":
        return ["python", "cpp", "java", "csharp", "javascript", "go", "kotlin"]
    if slug == "database":
        return ["sql"]
    if slug == "javascript":
        return ["javascript"]
    if slug == "pandas":
        return ["python"]
    if slug == "shell":
        return ["bash"]
    if slug == "concurrency":
        return []
    return []


def primary_language_for_category(category_title: str) -> str:
    languages = supported_languages_for_category(category_title)
    return languages[0] if languages else ""


def normalize_question(question: dict[str, Any]) -> dict[str, Any]:
    slug = str(question["titleSlug"])
    category_title = str(question.get("categoryTitle") or "Algorithms")
    topics = [
        {"name": str(tag.get("name") or ""), "slug": str(tag.get("slug") or "")}
        for tag in question.get("topicTags", [])
        if tag.get("slug")
    ]
    languages = supported_languages_for_category(category_title)
    return {
        "frontend_id": str(question.get("frontendQuestionId") or ""),
        "title": str(question["title"]),
        "slug": slug,
        "difficulty": str(question.get("difficulty") or ""),
        "acceptance_rate": question.get("acRate"),
        "category": category_slug(category_title),
        "category_title": category_title,
        "topics": topics,
        "url": f"https://leetcode.com/problems/{slug}/",
        "supported_languages": languages,
        "primary_language": primary_language_for_category(category_title),
        "runnable_in_coden": category_slug(category_title) in {"algorithms", "database", "pandas", "shell"},
    }


def metadata_for_question(question: dict[str, Any]) -> dict[str, Any]:
    topic_slugs = [tag["slug"] for tag in question["topics"]]
    subsets = ["leetcode_all", f"leetcode_category:{question['category']}"]
    subsets.extend(f"leetcode_topic:{slug}" for slug in topic_slugs)
    tags = ["leetcode", f"category:{question['category']}"]
    tags.extend(f"topic:{slug}" for slug in topic_slugs)
    tags.extend(f"language:{language}" for language in question["supported_languages"])
    return {
        "challenge_id": f"lc_{question['frontend_id']}",
        "source": "leetcode",
        "frontend_id": question["frontend_id"],
        "slug": question["slug"],
        "title": question["title"],
        "difficulty": question["difficulty"],
        "acceptance_rate": question["acceptance_rate"],
        "category": question["category"],
        "category_title": question["category_title"],
        "topics": question["topics"],
        "url": question["url"],
        "supported_languages": question["supported_languages"],
        "primary_language": question["primary_language"],
        "runnable_in_coden": question["runnable_in_coden"],
        "subsets": sorted(set(subsets)),
        "tags": sorted(set(tags)),
    }


def render_doc(question: dict[str, Any], template: str) -> str:
    topics = ", ".join(tag["name"] for tag in question.get("topics", [])) or "Uncategorized"
    return template.format(
        title=question["title"],
        frontend_id=question.get("frontend_id") or "unknown",
        difficulty=question.get("difficulty") or "unknown",
        topics=topics,
        slug=question["slug"],
        url=question["url"],
    )


def write_package(question: dict[str, Any], metadata: dict[str, Any], *, scaffold_docs: bool) -> str:
    directory = package_dir(question)
    directory.mkdir(parents=True, exist_ok=True)
    metadata_path = directory / "metadata.json"
    existing = {}
    if metadata_path.is_file():
        try:
            existing = json.loads(metadata_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            existing = {}
    if isinstance(existing.get("company_tags"), list):
        metadata["company_tags"] = existing["company_tags"]
    if isinstance(existing.get("company_tag_stats"), dict):
        metadata["company_tag_stats"] = existing["company_tag_stats"]
    if isinstance(existing.get("study_plans"), list):
        metadata["study_plans"] = existing["study_plans"]
    if isinstance(existing.get("neetcode_subsets"), list):
        metadata["neetcode_subsets"] = existing["neetcode_subsets"]
        neetcode_subset_tokens = {
            f"neetcode:{membership.get('subset_slug')}"
            for membership in existing["neetcode_subsets"]
            if isinstance(membership, dict) and membership.get("subset_slug")
        }
        neetcode_tag_tokens = {
            f"subset:neetcode:{membership.get('subset_slug')}"
            for membership in existing["neetcode_subsets"]
            if isinstance(membership, dict) and membership.get("subset_slug")
        }
        metadata["subsets"] = sorted(set(metadata.get("subsets", [])) | neetcode_subset_tokens)
        metadata["tags"] = sorted(set(metadata.get("tags", [])) | neetcode_tag_tokens)
        if any(
            isinstance(membership, dict) and membership.get("subset_slug") == "neetcode250"
            for membership in existing["neetcode_subsets"]
        ):
            metadata["subsets"] = sorted(set(metadata["subsets"]) | {"neetcode_250"})
            metadata["tags"] = sorted(set(metadata["tags"]) | {"subset:neetcode_250"})
    metadata_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    doc_path = directory / "doc.md"
    if scaffold_docs and not doc_path.exists():
        template = TEMPLATE_PATH.read_text(encoding="utf-8")
        doc_path.write_text(render_doc(question, template), encoding="utf-8")
        return "created"
    return "preserved" if doc_path.exists() else "missing"


def write_index(questions: list[dict[str, Any]]) -> None:
    INDEX_PATH.write_text(
        json.dumps(
            {
                "source": "https://leetcode.com/problemset/",
                "license_note": (
                    "Metadata only. Do not copy LeetCode problem statements, "
                    "editorials, or solution text into this dataset."
                ),
                "count": len(questions),
                "questions": questions,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )


def subset_record(kind: str, slug: str, name: str, challenge_ids: list[str], *, preserve_order: bool = False) -> dict[str, Any]:
    unique_ids = list(dict.fromkeys(challenge_ids))
    if not preserve_order:
        unique_ids = sorted(
            unique_ids,
            key=lambda cid: int(cid.removeprefix("lc_")) if cid.removeprefix("lc_").isdigit() else 10**9,
        )
    return {
        "id": f"{kind}:{slug}" if kind != "leetcode" else slug,
        "kind": kind,
        "slug": slug,
        "name": name,
        "challenge_ids": unique_ids,
        "count": len(unique_ids),
    }


def write_subsets(questions: list[dict[str, Any]]) -> None:
    category_members: dict[str, list[str]] = defaultdict(list)
    category_names: dict[str, str] = {}
    topic_members: dict[str, list[str]] = defaultdict(list)
    topic_names: dict[str, str] = {}
    language_members: dict[str, list[str]] = defaultdict(list)
    all_members: list[str] = []
    for question in questions:
        challenge_id = f"lc_{question['frontend_id']}"
        all_members.append(challenge_id)
        category_members[question["category"]].append(challenge_id)
        category_names[question["category"]] = question["category_title"]
        for topic in question["topics"]:
            topic_members[topic["slug"]].append(challenge_id)
            topic_names[topic["slug"]] = topic["name"]
        for language in question["supported_languages"]:
            language_members[language].append(challenge_id)

    subsets = [subset_record("leetcode", "leetcode_all", "All LeetCode Problems", all_members)]
    subsets.extend(
        subset_record("category", slug, category_names.get(slug, slug), members)
        for slug, members in sorted(category_members.items())
    )
    subsets.extend(
        subset_record("topic", slug, topic_names.get(slug, slug), members)
        for slug, members in sorted(topic_members.items())
    )
    subsets.extend(
        subset_record("language", slug, slug, members)
        for slug, members in sorted(language_members.items())
    )
    if SUBSETS_PATH.is_file():
        try:
            existing_payload = json.loads(SUBSETS_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            existing_payload = {}
        preserved_kinds = {"company", "study_plan", "study_plan_section", "neetcode", "external"}
        existing_ids = {str(subset.get("id")) for subset in subsets if isinstance(subset, dict)}
        for subset in existing_payload.get("subsets", []):
            if not isinstance(subset, dict):
                continue
            if str(subset.get("kind")) not in preserved_kinds:
                continue
            if str(subset.get("id")) in existing_ids:
                continue
            subsets.append(subset)

    SUBSETS_PATH.write_text(
        json.dumps(
            {
                "source": "local LeetCode package and subset metadata",
                "count": len(subsets),
                "subsets": subsets,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )


def sync_problemset(args: argparse.Namespace) -> dict[str, Any]:
    LEETCODE_ROOT.mkdir(parents=True, exist_ok=True)
    questions = fetch_questions(page_size=args.page_size)
    doc_statuses = Counter()
    for question in questions:
        metadata = metadata_for_question(question)
        doc_statuses[write_package(question, metadata, scaffold_docs=not args.no_scaffold)] += 1
    write_index(questions)
    write_subsets(questions)
    categories = Counter(question["category"] for question in questions)
    report = {
        "mode": "problemset",
        "total": len(questions),
        "categories": dict(sorted(categories.items())),
        "doc_statuses": dict(sorted(doc_statuses.items())),
        "subsets_path": str(SUBSETS_PATH.relative_to(REPO_ROOT)).replace("\\", "/"),
    }
    write_report(report)
    return report


def company_query(slugs: list[str]) -> str:
    fields = []
    for index, slug in enumerate(slugs):
        alias = f"q{index}"
        fields.append(
            f'{alias}: question(titleSlug: "{slug}") {{ '
            "titleSlug companyTags { name slug } companyTagStats }"
        )
    return "query companyTagsBatch { " + " ".join(fields) + " }"


def load_questions_from_index() -> list[dict[str, Any]]:
    payload = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    return list(payload["questions"])


def enrich_company_tags(args: argparse.Namespace) -> dict[str, Any]:
    questions = load_questions_from_index()
    if args.company_limit is not None:
        questions = questions[: args.company_limit]
    updated = 0
    company_members: dict[str, list[str]] = defaultdict(list)
    company_names: dict[str, str] = {}
    errors: list[str] = []

    for start in range(0, len(questions), args.company_batch_size):
        batch = questions[start : start + args.company_batch_size]
        slugs = [str(question["slug"]) for question in batch]
        try:
            data = request_graphql(company_query(slugs), {}, referer="https://leetcode.com/problemset/")
        except Exception as exc:
            errors.append(f"batch {start}: {exc}")
            if args.keep_going:
                continue
            raise
        for index, question in enumerate(batch):
            payload = data.get(f"q{index}") or {}
            tags = [
                {"name": str(tag.get("name") or ""), "slug": str(tag.get("slug") or "")}
                for tag in payload.get("companyTags") or []
                if tag.get("slug")
            ]
            stats = {}
            raw_stats = payload.get("companyTagStats")
            if isinstance(raw_stats, str) and raw_stats:
                try:
                    stats = json.loads(raw_stats)
                except json.JSONDecodeError:
                    stats = {}
            metadata_path = package_dir(question) / "metadata.json"
            if not metadata_path.is_file():
                continue
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            metadata["company_tags"] = tags
            metadata["company_tag_stats"] = stats
            subsets = set(metadata.get("subsets") or [])
            tag_values = set(metadata.get("tags") or [])
            for tag in tags:
                subsets.add(f"leetcode_company:{tag['slug']}")
                tag_values.add(f"company:{tag['slug']}")
                company_members[tag["slug"]].append(metadata["challenge_id"])
                company_names[tag["slug"]] = tag["name"]
            metadata["subsets"] = sorted(subsets)
            metadata["tags"] = sorted(tag_values)
            metadata_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            updated += 1
        if args.company_delay:
            time.sleep(args.company_delay)

    merge_company_subsets(company_members, company_names)
    report = {
        "mode": "company_tags",
        "requested": len(questions),
        "updated": updated,
        "company_count": len(company_members),
        "errors": errors,
    }
    write_report(report)
    return report


def merge_company_subsets(company_members: dict[str, list[str]], company_names: dict[str, str]) -> None:
    if not company_members:
        return
    payload = json.loads(SUBSETS_PATH.read_text(encoding="utf-8")) if SUBSETS_PATH.is_file() else {"subsets": []}
    existing = {
        str(subset.get("id")): subset
        for subset in payload.get("subsets", [])
        if isinstance(subset, dict)
    }
    for slug, members in company_members.items():
        record = subset_record("company", slug, company_names.get(slug, slug), sorted(set(members)))
        existing[record["id"]] = record
    subsets = sorted(existing.values(), key=lambda item: (str(item.get("kind")), str(item.get("name"))))
    payload["count"] = len(subsets)
    payload["subsets"] = subsets
    SUBSETS_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def fetch_study_plan_summaries(args: argparse.Namespace) -> list[dict[str, Any]]:
    requested_slugs = [slugify(slug) for slug in (args.study_plan_slug or []) if slug]
    if requested_slugs:
        return [{"slug": slug, "name": slug, "catalog_slug": "manual"} for slug in requested_slugs]

    catalogs_payload = request_graphql(
        STUDY_PLAN_CATALOGS_QUERY,
        {},
        referer="https://leetcode.com/studyplan/",
    )
    catalogs = [
        catalog
        for catalog in catalogs_payload.get("studyPlanV2Catalogs", [])
        if isinstance(catalog, dict) and catalog.get("slug")
    ]
    summaries: list[dict[str, Any]] = []
    seen: set[str] = set()
    for catalog in catalogs:
        offset = 0
        while True:
            payload = request_graphql(
                STUDY_PLANS_BY_CATALOG_QUERY,
                {
                    "catalogSlug": catalog["slug"],
                    "offset": offset,
                    "limit": args.study_plan_page_size,
                },
                referer="https://leetcode.com/studyplan/",
            )
            page = payload.get("studyPlansV2ByCatalog") or {}
            plans = [
                plan
                for plan in page.get("studyPlans", [])
                if isinstance(plan, dict) and plan.get("slug")
            ]
            for plan in plans:
                slug = str(plan["slug"])
                if slug in seen:
                    continue
                seen.add(slug)
                summaries.append({
                    **plan,
                    "catalog_slug": str(catalog.get("slug") or ""),
                    "catalog_name": str(catalog.get("name") or ""),
                })
            offset += len(plans)
            if not page.get("hasMore") or not plans:
                break
            if args.study_plan_delay:
                time.sleep(args.study_plan_delay)
    if args.study_plan_limit is not None:
        summaries = summaries[: args.study_plan_limit]
    return summaries


def fetch_study_plan_detail(slug: str) -> dict[str, Any]:
    payload = request_graphql(
        STUDY_PLAN_DETAIL_QUERY,
        {"slug": slug},
        referer=f"https://leetcode.com/studyplan/{slug}/",
    )
    detail = payload.get("studyPlanV2Detail")
    if not isinstance(detail, dict) or not detail.get("slug"):
        raise RuntimeError(f"LeetCode study plan '{slug}' was not found")
    return detail


def metadata_paths_by_slug() -> dict[str, Path]:
    result: dict[str, Path] = {}
    for question in load_questions_from_index():
        slug = str(question.get("slug") or "")
        if not slug:
            continue
        path = package_dir(question) / "metadata.json"
        if path.is_file():
            result[slug] = path
    return result


def _belongs_to_study_plan_token(value: str, synced_slugs: set[str]) -> bool:
    for slug in synced_slugs:
        if value == f"leetcode_studyplan:{slug}" or value.startswith(f"leetcode_studyplan:{slug}:"):
            return True
        if value == f"study_plan:{slug}" or value.startswith(f"study_plan_section:{slug}:"):
            return True
    return False


def prune_study_plan_memberships(synced_slugs: set[str]) -> None:
    if not synced_slugs:
        return
    for metadata_path in LEETCODE_ROOT.glob("*/metadata.json"):
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        changed = False
        memberships = metadata.get("study_plans") if isinstance(metadata.get("study_plans"), list) else []
        kept_memberships = [
            membership
            for membership in memberships
            if not (
                isinstance(membership, dict)
                and str(membership.get("plan_slug") or membership.get("slug") or "") in synced_slugs
            )
        ]
        if len(kept_memberships) != len(memberships):
            metadata["study_plans"] = kept_memberships
            changed = True

        for field in ("subsets", "tags"):
            values = metadata.get(field) if isinstance(metadata.get(field), list) else []
            kept_values = [
                value
                for value in values
                if not (isinstance(value, str) and _belongs_to_study_plan_token(value, synced_slugs))
            ]
            if len(kept_values) != len(values):
                metadata[field] = kept_values
                changed = True

        if changed:
            metadata_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def merge_study_plan_subsets(records: list[dict[str, Any]], synced_slugs: set[str]) -> None:
    payload = json.loads(SUBSETS_PATH.read_text(encoding="utf-8")) if SUBSETS_PATH.is_file() else {"subsets": []}
    existing: dict[str, dict[str, Any]] = {}
    for subset in payload.get("subsets", []):
        if not isinstance(subset, dict):
            continue
        kind = str(subset.get("kind") or "")
        slug = str(subset.get("slug") or "")
        if kind == "study_plan" and slug in synced_slugs:
            continue
        if kind == "study_plan_section" and slug.split(":", 1)[0] in synced_slugs:
            continue
        existing[str(subset.get("id"))] = subset
    for record in records:
        existing[str(record.get("id"))] = record

    kind_order = {
        "leetcode": 0,
        "category": 1,
        "topic": 2,
        "language": 3,
        "company": 4,
        "study_plan": 5,
        "study_plan_section": 6,
        "external": 7,
    }
    subsets = sorted(
        existing.values(),
        key=lambda item: (
            kind_order.get(str(item.get("kind") or ""), 99),
            str(item.get("name") or ""),
            str(item.get("slug") or ""),
        ),
    )
    payload["count"] = len(subsets)
    payload["subsets"] = subsets
    SUBSETS_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def sync_study_plans(args: argparse.Namespace) -> dict[str, Any]:
    summaries = fetch_study_plan_summaries(args)
    synced_slugs = {str(summary.get("slug") or "") for summary in summaries if summary.get("slug")}
    prune_study_plan_memberships(synced_slugs)
    paths_by_slug = metadata_paths_by_slug()
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    updated_paths: set[str] = set()
    plan_count = 0
    section_count = 0
    membership_count = 0

    for summary in summaries:
        plan_slug = str(summary.get("slug") or "")
        if not plan_slug:
            continue
        try:
            detail = fetch_study_plan_detail(plan_slug)
        except Exception as exc:
            errors.append(f"{plan_slug}: {exc}")
            if args.keep_going:
                continue
            raise

        plan_slug = str(detail.get("slug") or plan_slug)
        plan_name = str(detail.get("name") or summary.get("name") or plan_slug)
        catalog_slug = str(summary.get("catalog_slug") or "")
        catalog_name = str(summary.get("catalog_name") or "")
        plan_members: list[str] = []
        section_records: list[dict[str, Any]] = []
        global_order = 0
        plan_count += 1

        for section_index, section in enumerate(detail.get("planSubGroups") or [], start=1):
            if not isinstance(section, dict):
                continue
            section_slug = str(section.get("slug") or f"section-{section_index}")
            section_name = str(section.get("name") or section_slug)
            section_members: list[str] = []
            section_count += 1
            questions = section.get("questions") if isinstance(section.get("questions"), list) else []

            for problem_index, problem in enumerate(questions, start=1):
                if not isinstance(problem, dict):
                    continue
                title_slug = str(problem.get("titleSlug") or "")
                metadata_path = paths_by_slug.get(title_slug)
                if metadata_path is None:
                    errors.append(f"{plan_slug}/{section_slug}: missing local package for {title_slug}")
                    continue
                try:
                    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError) as exc:
                    errors.append(f"{plan_slug}/{section_slug}: cannot read {metadata_path}: {exc}")
                    continue

                global_order += 1
                challenge_id = str(metadata.get("challenge_id") or f"lc_{problem.get('questionFrontendId')}")
                membership = {
                    "plan_slug": plan_slug,
                    "plan_name": plan_name,
                    "section_slug": section_slug,
                    "section_name": section_name,
                    "path": [section_name],
                    "order": global_order,
                    "section_order": section_index,
                    "problem_order": problem_index,
                    "catalog_slug": catalog_slug,
                    "catalog_name": catalog_name,
                    "premium_only": bool(detail.get("premiumOnly")),
                    "section_premium_only": bool(section.get("premiumOnly")),
                    "paid_only": bool(problem.get("paidOnly")),
                    "source_url": f"https://leetcode.com/studyplan/{plan_slug}/",
                }
                metadata.setdefault("study_plans", [])
                metadata["study_plans"].append(membership)
                subsets = set(metadata.get("subsets") if isinstance(metadata.get("subsets"), list) else [])
                tags = set(metadata.get("tags") if isinstance(metadata.get("tags"), list) else [])
                subsets.add(f"leetcode_studyplan:{plan_slug}")
                subsets.add(f"leetcode_studyplan:{plan_slug}:{section_slug}")
                tags.add(f"study_plan:{plan_slug}")
                tags.add(f"study_plan_section:{plan_slug}:{section_slug}")
                metadata["subsets"] = sorted(subsets)
                metadata["tags"] = sorted(tags)
                metadata_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
                updated_paths.add(str(metadata_path))
                membership_count += 1
                plan_members.append(challenge_id)
                section_members.append(challenge_id)

            section_record = subset_record(
                "study_plan_section",
                f"{plan_slug}:{section_slug}",
                f"{plan_name} / {section_name}",
                section_members,
                preserve_order=True,
            )
            section_record.update({
                "plan_slug": plan_slug,
                "plan_name": plan_name,
                "section_slug": section_slug,
                "section_name": section_name,
                "path": [plan_name, section_name],
                "career_mode": True,
                "source_url": f"https://leetcode.com/studyplan/{plan_slug}/",
            })
            section_records.append(section_record)

        plan_record = subset_record("study_plan", plan_slug, plan_name, plan_members, preserve_order=True)
        plan_record.update({
            "catalog_slug": catalog_slug,
            "catalog_name": catalog_name,
            "career_mode": True,
            "source_url": f"https://leetcode.com/studyplan/{plan_slug}/",
            "highlight": str(detail.get("highlight") or summary.get("highlight") or ""),
            "premium_only": bool(detail.get("premiumOnly")),
            "section_count": len(section_records),
        })
        records.append(plan_record)
        records.extend(section_records)

        if args.study_plan_delay:
            time.sleep(args.study_plan_delay)

    merge_study_plan_subsets(records, synced_slugs)
    report = {
        "mode": "study_plans",
        "requested": len(summaries),
        "synced_plans": plan_count,
        "synced_sections": section_count,
        "memberships": membership_count,
        "updated_metadata_files": len(updated_paths),
        "errors": errors,
    }
    write_report(report)
    return report


def write_report(report: dict[str, Any]) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--page-size", type=int, default=100)
    parser.add_argument("--no-scaffold", action="store_true")
    parser.add_argument("--company-tags", action="store_true", help="Enrich existing packages with company tags.")
    parser.add_argument("--company-batch-size", type=int, default=20)
    parser.add_argument("--company-delay", type=float, default=0.05)
    parser.add_argument("--company-limit", type=int, default=None)
    parser.add_argument("--study-plans", action="store_true", help="Sync official LeetCode study-plan membership.")
    parser.add_argument("--study-plan-slug", action="append", default=[], help="Sync one study-plan slug; repeat to sync several. Defaults to all catalog plans.")
    parser.add_argument("--study-plan-page-size", type=int, default=100)
    parser.add_argument("--study-plan-delay", type=float, default=0.05)
    parser.add_argument("--study-plan-limit", type=int, default=None)
    parser.add_argument("--keep-going", action="store_true")
    args = parser.parse_args(argv)

    if args.study_plans:
        report = sync_study_plans(args)
    elif args.company_tags:
        report = enrich_company_tags(args)
    else:
        report = sync_problemset(args)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if not report.get("errors") else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
