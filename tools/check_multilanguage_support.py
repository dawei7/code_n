"""Audit generated multi-language challenge support.

This verifier is intentionally chunkable because the full registry is large.
Use it to prove starter generation, function harness generation, and setup
value-shape inference across slices of the challenge registry.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from challenges.registry import CHALLENGE_REGISTRY  # noqa: E402
from engine.solutions import (  # noqa: E402
    _CPP_KEYWORDS,
    _CSHARP_KEYWORDS,
    _GO_KEYWORDS,
    _JAVASCRIPT_KEYWORDS,
    _JAVA_KEYWORDS,
    _KOTLIN_KEYWORDS,
    _solution_template,
)
from server.app.challenge_sets import is_challenge_in_set  # noqa: E402
from server.app.external_programs import (  # noqa: E402
    _cpp_function_harness,
    _csharp_function_harness,
    _go_function_harness,
    _javascript_function_harness,
    _java_function_harness,
    _kotlin_function_harness,
    _value_kind,
)


STARTER_LANGUAGES = ("cpp", "java", "csharp", "javascript", "go", "kotlin")
HARNESS_BUILDERS = {
    "cpp": _cpp_function_harness,
    "java": _java_function_harness,
    "csharp": _csharp_function_harness,
    "javascript": _javascript_function_harness,
    "go": _go_function_harness,
    "kotlin": _kotlin_function_harness,
}


def main() -> int:
    args = _parse_args()
    requested_sets = {item.strip() for item in args.sets.split(",") if item.strip()}
    selected = [
        (cid, cls)
        for cid, cls in CHALLENGE_REGISTRY.items()
        if any(is_challenge_in_set(cid, requested_set) for requested_set in requested_sets)
    ]
    end = None if args.limit is None else args.offset + args.limit
    selected = selected[args.offset:end]

    errors: list[tuple[Any, ...]] = []
    unknown_values: list[tuple[str, str, str, str]] = []
    kind_counts: Counter[str] = Counter()
    checked = 0
    function_checked = 0

    for cid, cls in selected:
        challenge = cls()
        spec = getattr(challenge, "_spec", None)
        if spec is None:
            continue
        checked += 1
        for language in STARTER_LANGUAGES:
            try:
                starter = _solution_template(
                    spec.id,
                    heading=f"{spec.id}: {spec.name}",
                    description=spec.description,
                    language=language,
                )
                _check_starter_shape(cid, language, starter, errors)
            except Exception as exc:
                errors.append((cid, language, "starter", type(exc).__name__, str(exc)))

        if args.starters_only:
            continue

        function_checked += 1
        n = min(args.n, getattr(challenge, "max_n", args.n))
        try:
            challenge._n = n
            challenge._seed = args.seed
            values = challenge.setup(n, args.seed)
        except Exception as exc:
            errors.append((cid, "setup", "setup", type(exc).__name__, str(exc)))
            continue

        for name, value in values.items():
            kind = _value_kind(value)
            kind_counts[str(kind)] += 1
            if kind is None:
                unknown_values.append((cid, name, type(value).__name__, repr(value)[:160]))

        params = list(getattr(spec, "params", []) or values.keys())
        hints = dict(getattr(spec, "inputs", {}) or {})
        returns = str(getattr(spec, "returns", "") or "")
        for language, builder in HARNESS_BUILDERS.items():
            try:
                builder(params, hints, returns, param_values=values)
            except Exception as exc:
                errors.append((cid, language, "harness", type(exc).__name__, str(exc)))

    report = {
        "sets": sorted(requested_sets),
        "offset": args.offset,
        "limit": args.limit,
        "selected": len(selected),
        "checked": checked,
        "function_checked": function_checked,
        "error_count": len(errors),
        "errors": errors[: args.show],
        "unknown_value_count": len(unknown_values),
        "unknown_values": unknown_values[: args.show],
        "kind_counts": kind_counts.most_common(),
    }
    print(json.dumps(report, indent=2))
    return 1 if errors or unknown_values else 0


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sets",
        default="leetcode",
        help="Comma-separated LeetCode views to audit: leetcode, neetcode.",
    )
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--n", type=int, default=8)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--show", type=int, default=50)
    parser.add_argument("--starters-only", action="store_true")
    return parser.parse_args()


def _check_starter_shape(
    challenge_id: str,
    language: str,
    starter: str,
    errors: list[tuple[Any, ...]],
) -> None:
    if language != "go" and "Solution" not in starter:
        errors.append((challenge_id, language, "missing_solution_class"))
        return

    method = "Solve" if language == "csharp" else "solve"
    params = _signature_parameter_names(starter, method, language)
    if params is None:
        errors.append((challenge_id, language, "missing_solution_method", method))
        return

    keywords = {
        "cpp": _CPP_KEYWORDS,
        "java": _JAVA_KEYWORDS,
        "csharp": _CSHARP_KEYWORDS,
        "javascript": _JAVASCRIPT_KEYWORDS,
        "go": _GO_KEYWORDS,
        "kotlin": _KOTLIN_KEYWORDS,
    }[language]
    for name in params:
        if not re.fullmatch(r"@?[A-Za-z_][A-Za-z0-9_]*", name):
            errors.append((challenge_id, language, "invalid_parameter_identifier", name))
        if language == "csharp":
            if name in keywords:
                errors.append((challenge_id, language, "unescaped_keyword_parameter", name))
        elif name in keywords:
            errors.append((challenge_id, language, "keyword_parameter", name))


def _signature_parameter_names(starter: str, method: str, language: str) -> list[str] | None:
    match = re.search(rf"\b{re.escape(method)}\s*\(", starter)
    if match is None:
        return None
    open_paren = starter.find("(", match.start())
    close_paren = _matching(starter, open_paren, "(", ")")
    if close_paren < 0:
        return None
    raw_params = starter[open_paren + 1:close_paren].strip()
    if not raw_params:
        return []
    names: list[str] = []
    for param in _split_top_level_commas(raw_params):
        text = param.strip()
        if not text:
            continue
        if language == "javascript":
            names.append(text)
            continue
        if language == "go":
            names.append(text.split()[0])
            continue
        if language == "kotlin":
            names.append(text.split(":", 1)[0].strip())
            continue
        pieces = text.split()
        if not pieces:
            continue
        names.append(pieces[-1].lstrip("&*"))
    return names


def _split_top_level_commas(text: str) -> list[str]:
    parts: list[str] = []
    current: list[str] = []
    angle_depth = 0
    paren_depth = 0
    for ch in text:
        if ch == "<":
            angle_depth += 1
        elif ch == ">":
            angle_depth = max(0, angle_depth - 1)
        elif ch == "(":
            paren_depth += 1
        elif ch == ")":
            paren_depth = max(0, paren_depth - 1)
        if ch == "," and angle_depth == 0 and paren_depth == 0:
            parts.append("".join(current))
            current = []
            continue
        current.append(ch)
    if current:
        parts.append("".join(current))
    return parts


def _matching(text: str, start: int, open_char: str, close_char: str) -> int:
    depth = 0
    for index in range(start, len(text)):
        ch = text[index]
        if ch == open_char:
            depth += 1
        elif ch == close_char:
            depth -= 1
            if depth == 0:
                return index
    return -1


if __name__ == "__main__":
    sys.exit(main())
