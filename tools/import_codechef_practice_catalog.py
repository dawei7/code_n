"""Import only CodeChef's official "Difficulty rating wise" practice paths."""
from __future__ import annotations

import json
import math
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = REPO_ROOT / "docs" / "algorithms" / "codechef" / "index.json"
FULL_CATALOG_PATH = REPO_ROOT / "docs" / "algorithms" / "codechef" / "catalog.json"
CATALOG_URL = "https://www.codechef.com/api/practice/catalog"
SYLLABUS_URL = "https://www.codechef.com/api/{mode}/syllabus/{slug}"
PROBLEMS_URL = "https://www.codechef.com/api/list/problems"
ROADMAP_URL = "https://www.codechef.com/api/roadmap/syllabus/{slug}"
VISIBLE_ROADMAPS = (
    ("become-5-star", "Become 5 star"),
    ("data-structures-and-algorithms", "Data Structures and Algorithms"),
)
PAGE_SIZE = 5_000
EXCLUDED_VISIBLE_CODES = {
    # Course reading/checkpoint pages rather than normal CodeChef coding tasks.
    "MATDEF",
    "MATMCQ1",
    "MATTYPES",
    # No accepted Python/PyPy baseline is exposed and generated Python
    # submissions repeatedly TLE on the full CodeChef judge.
    "PTREE",
}


def fetch_json(url: str, attempts: int = 4) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "Referer": "https://www.codechef.com/practice#difficulty-rating-wise",
            "User-Agent": "cOde(n) CodeChef difficulty-path importer/1.0",
        },
    )
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                payload = json.load(response)
            if payload.get("status") != "success":
                raise RuntimeError(payload.get("message", "CodeChef API error"))
            return payload
        except (OSError, ValueError, RuntimeError):
            if attempt + 1 == attempts:
                raise
            time.sleep(2 ** attempt)
    raise AssertionError("unreachable")


VISIBLE_PATH_GROUPS = (
    ("Difficulty rating wise", "difficulty-rating-wise"),
)

# The complete difficulty ladder is displayed inside Become 5 Star rather than
# as a competing top-level path. Each course maps to its corresponding milestone.
DIFFICULTY_MILESTONES = {
    1: (1, "become_1_star"),
    2: (1, "become_1_star"),
    3: (2, "become_2_star"),
    4: (2, "become_2_star"),
    5: (3, "become_3_star"),
    6: (4, "become_4_star"),
    7: (5, "become_5_star"),
}


def visible_course_groups(
    catalog: dict[str, Any],
) -> list[tuple[str, str, list[dict[str, Any]]]]:
    result = []
    for display_name, group_slug in VISIBLE_PATH_GROUPS:
        section = next(
            (item.get(display_name) for item in catalog.get("practice_paths", []) if display_name in item),
            None,
        )
        path = (section or {}).get(group_slug)
        if not path:
            raise RuntimeError(f"CodeChef catalog has no {display_name} section")
        result.append((display_name, group_slug, list(path.get("courses", {}).values())))
    return result


def fetch_full_catalog() -> list[dict[str, Any]]:
    """Fetch the full public catalog for internal metadata lookup only."""
    def page(number: int) -> dict[str, Any]:
        query = urllib.parse.urlencode({
            "page": number,
            "limit": PAGE_SIZE,
            "sort_by": "difficulty_rating",
            "sort_order": "asc",
            "start_rating": -1,
            "end_rating": 10_000,
            "topic": "",
            "tags": "",
            "group": "all",
            "problemType": "rated",
        })
        return fetch_json(f"{PROBLEMS_URL}?{query}")

    first = page(0)
    rows = list(first.get("data", []))
    for number in range(1, math.ceil(int(first["count"]) / PAGE_SIZE)):
        rows.extend(page(number).get("data", []))
    return rows


def category_name(group_slug: str, order: int, course: dict[str, Any]) -> str:
    slug = str(course["slug"]).replace("-", "_")
    group = group_slug.replace("-", "_")
    return f"codechef_{group}__{order:02d}_{slug}"


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def difficulty_level(raw_rating: Any) -> int:
    try:
        rating = int(raw_rating)
    except (TypeError, ValueError):
        return 1
    if rating < 0:
        return 1
    return min(10, max(1, (rating - 300) // 250 + 1))


def extract_questions(
    course: dict[str, Any],
    group_name: str,
    group_slug: str,
    order: int,
    old_by_code: dict[str, dict[str, Any]],
    syllabus_mode: str = "practice",
) -> list[dict[str, Any]]:
    syllabus = fetch_json(SYLLABUS_URL.format(mode=syllabus_mode, slug=course["slug"]))
    result: list[dict[str, Any]] = []
    course_category = category_name(group_slug, order, course)
    for module_order, module in enumerate(syllabus.get("modules", []), start=1):
        if group_slug == "star-wise-paths":
            lesson = slugify(str(module.get("name") or f"Lesson {module_order}"))
            category = f"{course_category}___{module_order:02d}_{lesson}"
        else:
            category = course_category
        for submodule in module.get("submodules", []):
            contest_code = str(submodule.get("contest_code") or "")
            for problem in submodule.get("problems_with_status", []):
                code = str(problem["code"])
                if code in EXCLUDED_VISIBLE_CODES:
                    continue
                rating = int(problem.get("difficulty_rating") or -1)
                old = old_by_code.get(code, {})
                item = {
                    "code": code,
                    "name": str(problem.get("name") or code),
                    "url": (
                        f"https://www.codechef.com/{syllabus_mode}/course/{course['slug']}/"
                        f"{contest_code}/problems/{code}"
                    ),
                    "difficulty": str(course.get("title") or course.get("name")),
                    "difficulty_level": difficulty_level(rating),
                    "difficulty_rating": rating,
                    "difficulty_type": str(problem.get("difficulty_type") or ""),
                    "category": category,
                    "path_slug": str(course["slug"]),
                    "path_group": group_name,
                    "lesson": str(module.get("name") or ""),
                    "lesson_order": module_order,
                    "path_level": str(course.get("level") or ""),
                    "contest_code": contest_code,
                    "categories": [category],
                }
                # Retain useful public statistics gathered by an earlier run.
                for key in (
                    "total_submissions", "successful_submissions",
                    "distinct_successful_submissions",
                    "partially_successful_submissions", "recently_added",
                ):
                    if key in old:
                        item[key] = old[key]
                result.append(item)
    return result


def import_catalog() -> tuple[int, list[tuple[str, int]]]:
    full_catalog = fetch_full_catalog()
    old_by_code = {str(item["code"]): item for item in full_catalog}
    FULL_CATALOG_PATH.write_text(
        json.dumps({
            "source": "CodeChef public practice catalog",
            "url": "https://www.codechef.com/practice",
            "total_problems": len(old_by_code),
            "questions": full_catalog,
        }, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    course_groups = visible_course_groups(fetch_json(CATALOG_URL))

    questions_by_code: dict[str, dict[str, Any]] = {}
    summaries: list[dict[str, Any]] = []
    counts: list[tuple[str, int]] = []
    absorbed_course_slugs: set[str] = set()
    for group_name, group_slug, courses in course_groups:
        for order, course in enumerate(courses, start=1):
            absorbed_course_slugs.add(str(course.get("slug") or ""))
            questions = extract_questions(
                course, group_name, group_slug, order, old_by_code,
            )
            milestone_order, milestone_slug = DIFFICULTY_MILESTONES[order]
            absorbed_category = (
                f"codechef_become_5_star__{milestone_order:02d}_{milestone_slug}"
                f"___{order:02d}_{slugify(str(course['title']))}"
                "____01_difficulty_rating_practice"
            )
            for item in questions:
                item["category"] = absorbed_category
                item["categories"] = [absorbed_category]
                item["path_group"] = "Become 5 star"
            counts.append((f"Become 5 star / {course['title']}", len(questions)))
            for item in questions:
                previous = questions_by_code.get(item["code"])
                if previous is None:
                    questions_by_code[item["code"]] = item
                else:
                    previous["categories"] = list(dict.fromkeys(
                        [*previous.get("categories", []), *item.get("categories", [])]
                    ))
            summaries.append({
                "group": "Become 5 star",
                "group_slug": "become-5-star",
                "order": order,
                "slug": course["slug"],
                "name": course["name"],
                "title": course["title"],
                "path_level": course["level"],
                "description": course["description"],
                "problem_count": len(questions),
            })

    for roadmap_slug, roadmap_name in VISIBLE_ROADMAPS:
        roadmap = fetch_json(ROADMAP_URL.format(slug=roadmap_slug))
        group_key = roadmap_slug.replace("-", "_")
        for section_order, section in enumerate(roadmap.get("sections", []), start=1):
            section_name = str(section.get("sectionName") or f"Section {section_order}")
            section_slug = slugify(section_name)
            for path_order, path in enumerate(section.get("paths", []), start=1):
                if (
                    roadmap_slug == "become-5-star"
                    and str(path.get("pathSlug") or "") in absorbed_course_slugs
                ):
                    continue
                course = {
                    "slug": path["pathSlug"],
                    "name": path["pathName"],
                    "title": path["pathName"],
                    "level": "Roadmap",
                    "description": path.get("pathDescription") or "",
                }
                syllabus_mode = "practice" if path.get("isPracticePath") else "learn"
                questions = extract_questions(
                    course,
                    roadmap_name,
                    roadmap_slug,
                    path_order,
                    old_by_code,
                    syllabus_mode=syllabus_mode,
                )
                category = (
                    f"codechef_{group_key}__{section_order:02d}_{section_slug}"
                    f"___{path_order:02d}_{slugify(str(path['pathName']))}"
                )
                for item in questions:
                    item_category = category
                    if roadmap_slug == "become-5-star":
                        item_category += (
                            f"____{int(item.get('lesson_order', 0)):02d}_"
                            f"{slugify(str(item.get('lesson') or 'Problems'))}"
                        )
                    item["category"] = item_category
                    item["categories"] = [item_category]
                    item["path_group"] = roadmap_name
                    previous = questions_by_code.get(item["code"])
                    if previous is None:
                        questions_by_code[item["code"]] = item
                    else:
                        previous["categories"] = list(dict.fromkeys(
                            [*previous.get("categories", []), item_category]
                        ))
                counts.append((
                    f"{roadmap_name} / {section_name} / {path['pathName']}",
                    len(questions),
                ))
                summaries.append({
                    "group": roadmap_name,
                    "group_slug": roadmap_slug,
                    "section": section_name,
                    "order": path_order,
                    "slug": path["pathSlug"],
                    "name": path["pathName"],
                    "title": path["pathName"],
                    "path_level": "Roadmap",
                    "description": path.get("pathDescription") or "",
                    "problem_count": len(questions),
                })

    output = {
        "source": "CodeChef curated practice paths and roadmaps",
        "url": "https://www.codechef.com/practice",
        "total_problems": len(questions_by_code),
        "visible_paths": summaries,
        "questions": sorted(
            questions_by_code.values(),
            key=lambda item: (item["difficulty_level"], item["difficulty_rating"], item["code"]),
        ),
    }
    INDEX_PATH.write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return len(questions_by_code), counts


def main() -> None:
    total, counts = import_catalog()
    print(f"CodeChef difficulty index: {total} unique problems")
    for name, count in counts:
        print(f"  {name}: {count}")


if __name__ == "__main__":
    main()
