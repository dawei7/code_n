"""Sync official LeetCode Quests as views over canonical problem packages.

The public Quest catalog exposes each quest's ordered units, levels, and
favorite problem lists.  This tool records only that hierarchy and problem
ordering; canonical problem content remains exclusively under
``dsa/leetcode``.  Quest quizzes are intentionally excluded because they are
not canonical LeetCode problems.
"""

from __future__ import annotations

import argparse
import json
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
INDEX_PATH = LEETCODE_ROOT / "index.json"
SUBSETS_PATH = LEETCODE_ROOT / "subsets.json"
MANIFEST_PATH = LEETCODE_ROOT / "_meta" / "leetcode-quest-subsets.json"
GRAPHQL_URL = "https://leetcode.com/graphql/"

QUEST_DEFINITIONS = (
    {
        "slug": "data-structures-and-algorithms-quest",
        "source_url": "https://leetcode.com/quest/data-structures-and-algorithms-quest/",
    },
    {
        "slug": "database-quest",
        "source_url": "https://leetcode.com/quest/database-quest/",
    },
    {
        "slug": "system-and-software-design-quest",
        "source_url": "https://leetcode.com/quest/system-and-software-design-quest/",
    },
    {
        "slug": "maths-quest",
        "source_url": "https://leetcode.com/quest/maths-quest/",
    },
    {
        "slug": "2026-spring-sprint",
        "source_url": "https://leetcode.com/quest/2026-spring-sprint/",
    },
)

QUEST_DETAIL_QUERY = """query questDetail($questSlug: String!) {
  questDetail(questSlug: $questSlug) {
    id
    name
    slug
  }
  questUnits(questSlug: $questSlug) {
    id
    name
    totalLevelNum
    sections {
      main
      levels {
        id
        name
        isPremium
        favoriteSlug
        favoriteQuestionNum
        entryQuestionSlug
      }
    }
  }
}"""


def _request_graphql(
    query: str,
    variables: dict[str, Any],
    *,
    referer: str,
) -> dict[str, Any]:
    body = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    request = urllib.request.Request(
        GRAPHQL_URL,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Referer": referer,
            "User-Agent": "Mozilla/5.0 (compatible; cOde(n) LeetCode Quest sync)",
        },
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        payload = json.loads(response.read().decode("utf-8"))
    errors = payload.get("errors")
    if errors:
        raise RuntimeError(f"LeetCode Quest query failed: {errors}")
    data = payload.get("data")
    if not isinstance(data, dict):
        raise RuntimeError("LeetCode Quest query returned no data")
    return data


def _canonical_questions_by_slug() -> dict[str, dict[str, Any]]:
    payload = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    return {
        str(question.get("slug") or "").casefold(): question
        for question in payload.get("questions", [])
        if isinstance(question, dict) and question.get("slug")
    }


def _level_records() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    quests: list[dict[str, Any]] = []
    levels: list[dict[str, Any]] = []
    for quest_order, definition in enumerate(QUEST_DEFINITIONS, start=1):
        data = _request_graphql(
            QUEST_DETAIL_QUERY,
            {"questSlug": definition["slug"]},
            referer=definition["source_url"],
        )
        detail = data.get("questDetail")
        units = data.get("questUnits")
        if not isinstance(detail, dict) or not isinstance(units, list):
            raise RuntimeError(f"Quest '{definition['slug']}' is unavailable")

        quest_slug = str(detail.get("slug") or definition["slug"])
        quest_name = str(detail.get("name") or quest_slug)
        level_order = 0
        for unit_order, unit in enumerate(units, start=1):
            if not isinstance(unit, dict):
                continue
            unit_name = str(unit.get("name") or f"Unit {unit_order}")
            sections = unit.get("sections") if isinstance(unit.get("sections"), list) else []
            for section_order, section in enumerate(sections, start=1):
                if not isinstance(section, dict):
                    continue
                section_levels = (
                    section.get("levels")
                    if isinstance(section.get("levels"), list)
                    else []
                )
                for branch_order, level in enumerate(section_levels, start=1):
                    if not isinstance(level, dict):
                        continue
                    favorite_slug = str(level.get("favoriteSlug") or "")
                    if not favorite_slug:
                        raise RuntimeError(
                            f"Quest level '{quest_name} / {unit_name} / {level.get('name')}' "
                            "has no problem-list slug"
                        )
                    level_order += 1
                    levels.append(
                        {
                            "quest_slug": quest_slug,
                            "quest_name": quest_name,
                            "quest_order": quest_order,
                            "source_url": definition["source_url"],
                            "unit_id": str(unit.get("id") or ""),
                            "unit_name": unit_name,
                            "unit_order": unit_order,
                            "section_order": section_order,
                            "main_level_id": str(section.get("main") or ""),
                            "level_id": str(level.get("id") or ""),
                            "level_name": str(level.get("name") or f"Level {level_order}"),
                            "level_order": level_order,
                            "branch_order": branch_order,
                            "favorite_slug": favorite_slug,
                            "source_question_count": int(level.get("favoriteQuestionNum") or 0),
                            "entry_question_slug": str(level.get("entryQuestionSlug") or ""),
                            "premium_only": bool(level.get("isPremium")),
                        }
                    )

        quests.append(
            {
                "id": str(detail.get("id") or ""),
                "slug": quest_slug,
                "name": quest_name,
                "order": quest_order,
                "source_url": definition["source_url"],
                "unit_count": len(units),
                "level_count": level_order,
            }
        )
    return quests, levels


def _chunks(items: list[dict[str, Any]], size: int) -> Iterable[list[dict[str, Any]]]:
    for start in range(0, len(items), size):
        yield items[start : start + size]


def _fetch_problem_lists(levels: list[dict[str, Any]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for batch in _chunks(levels, 20):
        variable_defs: list[str] = []
        fields: list[str] = []
        variables: dict[str, str] = {}
        for index, level in enumerate(batch):
            variable = f"slug{index}"
            alias = f"list{index}"
            variable_defs.append(f"${variable}: String!")
            variables[variable] = str(level["favorite_slug"])
            fields.append(
                f"""{alias}: favoriteQuestionList(
  favoriteSlug: ${variable}
  sortBy: {{sortField: CUSTOM, sortOrder: ASCENDING}}
  version: \"v2\"
) {{ questions {{ titleSlug }} }}"""
            )
        query = "query questListQuestionOrder(" + ", ".join(variable_defs) + ") {\n"
        query += "\n".join(fields) + "\n}"
        data = _request_graphql(
            query,
            variables,
            referer=str(batch[0]["source_url"]),
        )
        for index, level in enumerate(batch):
            payload = data.get(f"list{index}")
            questions = payload.get("questions") if isinstance(payload, dict) else None
            if not isinstance(questions, list):
                raise RuntimeError(
                    f"Problem list '{level['favorite_slug']}' returned no questions"
                )
            slugs = [
                str(question.get("titleSlug") or "")
                for question in questions
                if isinstance(question, dict) and question.get("titleSlug")
            ]
            expected = int(level["source_question_count"])
            if expected and len(slugs) != expected:
                raise RuntimeError(
                    f"Problem list '{level['favorite_slug']}' returned {len(slugs)} "
                    f"questions; expected {expected}"
                )
            result[str(level["favorite_slug"])] = slugs
    return result


def _build_manifest() -> dict[str, Any]:
    canonical_by_slug = _canonical_questions_by_slug()
    quests, levels = _level_records()
    problems_by_list = _fetch_problem_lists(levels)
    memberships: list[dict[str, Any]] = []
    quest_problem_order: dict[str, int] = defaultdict(int)

    for level in levels:
        favorite_slug = str(level["favorite_slug"])
        problem_slugs = problems_by_list[favorite_slug]
        challenge_ids: list[str] = []
        for problem_order, source_slug in enumerate(problem_slugs, start=1):
            canonical = canonical_by_slug.get(source_slug.casefold())
            if canonical is None:
                raise RuntimeError(
                    f"Quest problem '{source_slug}' is missing from dsa/leetcode/index.json"
                )
            canonical_slug = str(canonical["slug"])
            challenge_id = f"lc_{canonical['frontend_id']}"
            challenge_ids.append(challenge_id)
            quest_slug = str(level["quest_slug"])
            quest_problem_order[quest_slug] += 1
            memberships.append(
                {
                    "challenge_id": challenge_id,
                    "leetcode_slug": canonical_slug,
                    "quest_slug": quest_slug,
                    "quest_name": level["quest_name"],
                    "quest_order": level["quest_order"],
                    "unit_name": level["unit_name"],
                    "unit_order": level["unit_order"],
                    "level_name": level["level_name"],
                    "level_order": level["level_order"],
                    "favorite_slug": favorite_slug,
                    "problem_order": problem_order,
                    "order": quest_problem_order[quest_slug],
                    "source_url": level["source_url"],
                }
            )
        level["challenge_ids"] = challenge_ids
        level["count"] = len(challenge_ids)

    for quest in quests:
        ordered_unique = list(
            dict.fromkeys(
                membership["challenge_id"]
                for membership in memberships
                if membership["quest_slug"] == quest["slug"]
            )
        )
        quest["challenge_ids"] = ordered_unique
        quest["count"] = len(ordered_unique)
        quest["membership_count"] = sum(
            1 for membership in memberships if membership["quest_slug"] == quest["slug"]
        )

    return {
        "schema_version": 1,
        "provider": "LeetCode",
        "kind": "quest",
        "source_url": "https://leetcode.com/quest/",
        "quest_count": len(quests),
        "problem_count": len({item["challenge_id"] for item in memberships}),
        "membership_count": len(memberships),
        "quests": quests,
        "levels": levels,
        "problems": memberships,
    }


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _merge_subset_catalog(manifest: dict[str, Any]) -> None:
    payload = (
        json.loads(SUBSETS_PATH.read_text(encoding="utf-8"))
        if SUBSETS_PATH.is_file()
        else {"subsets": []}
    )
    subsets = [
        subset
        for subset in payload.get("subsets", [])
        if isinstance(subset, dict)
        and str(subset.get("provider") or "").casefold() != "leetcode_quest"
        and not str(subset.get("id") or "").startswith("external:leetcode_quest_")
    ]
    for quest in manifest["quests"]:
        slug = str(quest["slug"])
        subsets.append(
            {
                "id": f"external:leetcode_quest_{slug.replace('-', '_')}",
                "kind": "external",
                "provider": "leetcode_quest",
                "slug": f"leetcode_quest_{slug.replace('-', '_')}",
                "name": quest["name"],
                "challenge_ids": quest["challenge_ids"],
                "count": quest["count"],
                "source_url": quest["source_url"],
                "description": f"Official {quest['name']} problems in Quest order.",
            }
        )
    payload["source"] = "local LeetCode package and subset metadata"
    payload["count"] = len(subsets)
    payload["subsets"] = subsets
    _write_json(SUBSETS_PATH, payload)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    manifest = _build_manifest()
    _write_json(MANIFEST_PATH, manifest)
    _merge_subset_catalog(manifest)
    print(
        json.dumps(
            {
                "manifest": str(MANIFEST_PATH.relative_to(REPO_ROOT)).replace("\\", "/"),
                "quest_counts": {
                    quest["slug"]: quest["count"] for quest in manifest["quests"]
                },
                "level_counts": {
                    quest["slug"]: quest["level_count"] for quest in manifest["quests"]
                },
                "problem_count": manifest["problem_count"],
                "membership_count": manifest["membership_count"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
