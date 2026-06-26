"""Import free LeetCode metadata and scaffold local reference docs.

The importer intentionally does not copy LeetCode problem statements,
editorials, or solution text. It stores stable metadata and creates
original-writeup placeholders that can be filled in locally.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DATASET_ROOT = REPO_ROOT / "docs" / "algorithms" / "leetcode"
INDEX_PATH = DATASET_ROOT / "index.json"
TEMPLATE_PATH = DATASET_ROOT / "_template.md"

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
      freqBar
      frontendQuestionId: questionFrontendId
      isFavor
      isPaidOnly
      status
      title
      titleSlug
      topicTags {
        name
        slug
      }
    }
  }
}
"""


def slugify(value: str) -> str:
    text = value.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def request_graphql(query: str, variables: dict[str, Any]) -> dict[str, Any]:
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    request = urllib.request.Request(
        GRAPHQL_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 cOde(n) metadata importer",
            "Referer": "https://leetcode.com/problemset/",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"LeetCode metadata request failed: HTTP {exc.code}: {detail}") from exc

    data = json.loads(body)
    if data.get("errors"):
        raise RuntimeError(f"LeetCode metadata request failed: {data['errors']}")
    return data["data"]


def fetch_free_questions(page_size: int = 100) -> list[dict[str, Any]]:
    skip = 0
    questions: list[dict[str, Any]] = []
    total = None

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
        for question in page["questions"]:
            if question.get("isPaidOnly"):
                continue
            questions.append(normalize_question(question))
        skip += page_size

    questions.sort(key=sort_key)
    return questions


def sort_key(question: dict[str, Any]) -> tuple[int, str]:
    frontend_id = str(question.get("frontend_id") or "")
    return (int(frontend_id) if frontend_id.isdigit() else 10**9, question["slug"])


def normalize_question(question: dict[str, Any]) -> dict[str, Any]:
    tags = [
        {"name": tag["name"], "slug": tag["slug"]}
        for tag in question.get("topicTags", [])
    ]
    slug = question["titleSlug"]
    return {
        "frontend_id": question.get("frontendQuestionId"),
        "title": question["title"],
        "slug": slug,
        "difficulty": question.get("difficulty"),
        "acceptance_rate": question.get("acRate"),
        "paid_only": bool(question.get("isPaidOnly")),
        "topics": tags,
        "url": f"https://leetcode.com/problems/{slug}/",
    }


def topic_dir(question: dict[str, Any]) -> Path:
    topics = question.get("topics") or []
    if not topics:
        return DATASET_ROOT / "uncategorized"
    return DATASET_ROOT / slugify(topics[0]["slug"])


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


def scaffold_docs(questions: list[dict[str, Any]], limit: int | None = None) -> int:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    created = 0
    for question in questions[:limit]:
        directory = topic_dir(question)
        directory.mkdir(parents=True, exist_ok=True)
        frontend_id = question.get("frontend_id") or "unknown"
        path = directory / f"{frontend_id}_{question['slug']}.md"
        if path.exists():
            continue
        path.write_text(render_doc(question, template), encoding="utf-8")
        created += 1
    return created


def write_index(questions: list[dict[str, Any]]) -> None:
    DATASET_ROOT.mkdir(parents=True, exist_ok=True)
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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--page-size", type=int, default=100)
    parser.add_argument("--no-scaffold", action="store_true")
    parser.add_argument("--scaffold-limit", type=int, default=None)
    args = parser.parse_args(argv)

    questions = fetch_free_questions(page_size=args.page_size)
    write_index(questions)
    created = 0 if args.no_scaffold else scaffold_docs(questions, args.scaffold_limit)
    print(f"Wrote {INDEX_PATH.relative_to(REPO_ROOT)} with {len(questions)} free problems.")
    if not args.no_scaffold:
        print(f"Created {created} new LeetCode reference scaffold(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
