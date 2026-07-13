"""Sync AlgoMaster practice lists as views over canonical LeetCode packages.

The AlgoMaster page exposes all four lists in its server-rendered Next.js
payload. This tool records only list membership and pattern ordering; problem
content continues to come exclusively from ``dsa/leetcode``.
"""

from __future__ import annotations

import argparse
import json
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
INDEX_PATH = LEETCODE_ROOT / "index.json"
SUBSETS_PATH = LEETCODE_ROOT / "subsets.json"
MANIFEST_PATH = LEETCODE_ROOT / "_meta" / "algomaster-subsets.json"
SOURCE_URL = "https://algomaster.io/practice/dsa-patterns"
LIST_DEFINITIONS = (
    {
        "source_key": "am_600",
        "slug": "am-600",
        "name": "AlgoMaster 600",
        "duration": "6+ months",
        "description": "600 curated LeetCode problems for 6+ months of preparation.",
    },
    {
        "source_key": "am_300",
        "slug": "am-300",
        "name": "AlgoMaster 300",
        "duration": "3+ months",
        "description": "300 curated LeetCode problems for 3+ months of preparation.",
    },
    {
        "source_key": "am_150",
        "slug": "am-150",
        "name": "AlgoMaster 150",
        "duration": "1-3 months",
        "description": "150 curated LeetCode problems for 1-3 months of preparation.",
    },
    {
        "source_key": "am_75",
        "slug": "am-75",
        "name": "AlgoMaster 75",
        "duration": "less than 1 month",
        "description": "75 curated LeetCode problems for less than 1 month of preparation.",
    },
)
EXPECTED_COUNTS = {definition["source_key"]: int(definition["slug"].removeprefix("am-")) for definition in LIST_DEFINITIONS}


class _ScriptCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._in_script = False
        self._buffer: list[str] = []
        self.scripts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "script":
            self._in_script = True
            self._buffer = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._in_script:
            self.scripts.append("".join(self._buffer))
            self._in_script = False

    def handle_data(self, data: str) -> None:
        if self._in_script:
            self._buffer.append(data)


def _download_source() -> str:
    request = urllib.request.Request(
        f"{SOURCE_URL}?tab=am-600",
        headers={
            "Accept": "text/html,application/xhtml+xml",
            "User-Agent": "Mozilla/5.0 (compatible; cOde(n) subset sync)",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def _find_pattern_lists(node: Any) -> list[list[dict[str, Any]]]:
    found: list[list[dict[str, Any]]] = []
    if isinstance(node, dict):
        patterns = node.get("patterns")
        if isinstance(patterns, list) and all(isinstance(pattern, dict) for pattern in patterns):
            found.append(patterns)
        for value in node.values():
            found.extend(_find_pattern_lists(value))
    elif isinstance(node, list):
        for value in node:
            found.extend(_find_pattern_lists(value))
    return found


def _extract_patterns(html: str) -> list[dict[str, Any]]:
    collector = _ScriptCollector()
    collector.feed(html)
    candidates: list[list[dict[str, Any]]] = []
    prefix = "self.__next_f.push("
    for script in collector.scripts:
        if "practice_problems" not in script or not script.startswith(prefix) or not script.endswith(")"):
            continue
        pushed = json.loads(script[len(prefix) : -1])
        if not isinstance(pushed, list) or len(pushed) < 2 or not isinstance(pushed[1], str):
            continue
        _, separator, serialized = pushed[1].partition(":")
        if not separator:
            continue
        candidates.extend(_find_pattern_lists(json.loads(serialized)))
    if not candidates:
        raise RuntimeError("AlgoMaster pattern data was not found in the server-rendered page")
    return max(candidates, key=lambda patterns: sum(len(pattern.get("problems") or []) for pattern in patterns))


def _canonical_questions_by_slug() -> dict[str, dict[str, Any]]:
    payload = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    return {
        str(question.get("slug") or "").casefold(): question
        for question in payload.get("questions", [])
        if isinstance(question, dict) and question.get("slug")
    }


def _build_manifest(patterns: list[dict[str, Any]]) -> tuple[dict[str, Any], list[tuple[str, str, str]]]:
    canonical_by_slug = _canonical_questions_by_slug()
    source_to_slug = {definition["source_key"]: definition["slug"] for definition in LIST_DEFINITIONS}
    records: list[dict[str, Any]] = []
    count_by_source_key = dict.fromkeys(source_to_slug, 0)
    source_id_mismatches: list[tuple[str, str, str]] = []
    seen_slugs: set[str] = set()
    global_order = 0

    for pattern_order, pattern in enumerate(patterns, start=1):
        pattern_name = str(pattern.get("name") or "Uncategorized")
        problems = pattern.get("problems") if isinstance(pattern.get("problems"), list) else []
        for pattern_problem_order, problem in enumerate(problems, start=1):
            if not isinstance(problem, dict):
                continue
            source_slug = str(problem.get("external_link") or "").strip()
            canonical = canonical_by_slug.get(source_slug.casefold())
            if canonical is None:
                raise RuntimeError(f"AlgoMaster problem '{source_slug}' is missing from dsa/leetcode/index.json")
            canonical_slug = str(canonical["slug"])
            if canonical_slug in seen_slugs:
                raise RuntimeError(f"AlgoMaster contains duplicate LeetCode slug '{canonical_slug}'")
            seen_slugs.add(canonical_slug)
            global_order += 1

            source_frontend_id = str(problem.get("id") or "")
            canonical_frontend_id = str(canonical["frontend_id"])
            if source_frontend_id != canonical_frontend_id:
                source_id_mismatches.append((source_frontend_id, canonical_slug, canonical_frontend_id))

            raw_lists = problem.get("lists") if isinstance(problem.get("lists"), list) else []
            list_slugs: list[str] = []
            for source_key in source_to_slug:
                if source_key in raw_lists:
                    count_by_source_key[source_key] += 1
                    list_slugs.append(source_to_slug[source_key])
            if not list_slugs:
                raise RuntimeError(f"AlgoMaster problem '{source_slug}' has no recognized list membership")

            records.append(
                {
                    "challenge_id": f"lc_{canonical_frontend_id}",
                    "leetcode_slug": canonical_slug,
                    "source_frontend_id": source_frontend_id,
                    "pattern": pattern_name,
                    "pattern_order": pattern_order,
                    "pattern_problem_order": pattern_problem_order,
                    "order": global_order,
                    "lists": list_slugs,
                }
            )

    if count_by_source_key != EXPECTED_COUNTS:
        raise RuntimeError(f"Unexpected AlgoMaster list counts: {count_by_source_key}; expected {EXPECTED_COUNTS}")

    list_definitions = []
    for order, definition in enumerate(LIST_DEFINITIONS, start=1):
        item = {key: value for key, value in definition.items() if key != "source_key"}
        item.update(
            {
                "order": order,
                "count": EXPECTED_COUNTS[definition["source_key"]],
                "source_url": f"{SOURCE_URL}?tab={definition['slug']}",
            }
        )
        list_definitions.append(item)

    return (
        {
            "schema_version": 1,
            "provider": "AlgoMaster",
            "source_url": SOURCE_URL,
            "problem_count": len(records),
            "lists": list_definitions,
            "problems": records,
        },
        source_id_mismatches,
    )


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _merge_subset_catalog(manifest: dict[str, Any]) -> None:
    payload = json.loads(SUBSETS_PATH.read_text(encoding="utf-8")) if SUBSETS_PATH.is_file() else {"subsets": []}
    subsets = [
        subset
        for subset in payload.get("subsets", [])
        if isinstance(subset, dict)
        and str(subset.get("provider") or "").casefold() != "algomaster"
        and not str(subset.get("id") or "").startswith("external:algomaster_")
    ]
    problems = manifest["problems"]
    for definition in manifest["lists"]:
        slug = str(definition["slug"])
        challenge_ids = [problem["challenge_id"] for problem in problems if slug in problem["lists"]]
        subsets.append(
            {
                "id": f"external:algomaster_{slug.replace('-', '_')}",
                "kind": "external",
                "provider": "algomaster",
                "slug": f"algomaster_{slug.replace('-', '_')}",
                "name": definition["name"],
                "challenge_ids": challenge_ids,
                "count": len(challenge_ids),
                "source_url": definition["source_url"],
                "description": definition["description"],
                "duration": definition["duration"],
            }
        )
    payload["source"] = "local LeetCode package and subset metadata"
    payload["count"] = len(subsets)
    payload["subsets"] = subsets
    _write_json(SUBSETS_PATH, payload)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    patterns = _extract_patterns(_download_source())
    manifest, source_id_mismatches = _build_manifest(patterns)
    _write_json(MANIFEST_PATH, manifest)
    _merge_subset_catalog(manifest)
    print(
        json.dumps(
            {
                "manifest": str(MANIFEST_PATH.relative_to(REPO_ROOT)).replace("\\", "/"),
                "problem_count": manifest["problem_count"],
                "list_counts": {item["slug"]: item["count"] for item in manifest["lists"]},
                "source_id_mismatches": source_id_mismatches,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
