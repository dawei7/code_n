"""Separate bundled Competitive source files into displayable implementations.

The imported Competitive corpus keeps every implementation for a problem in a
single canonical source file. Python files commonly express alternatives as
separate ``Solution*`` classes; a smaller set uses numbered entry methods such
as ``twoSum`` and ``twoSum2`` in one class. The UI needs those alternatives as
independent read-only panels without rewriting thousands of canonical files.
"""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass


_NUMBERED_METHOD_RE = re.compile(r"^(.*?)(\d+)$")


@dataclass(frozen=True)
class _SourceRange:
    start: int
    end: int


def _attached_comment_start(
    lines: list[str],
    node: ast.AST,
    *,
    lower_bound: int,
) -> int:
    """Include the blank/comment heading immediately above one definition."""

    start = max(int(getattr(node, "lineno", 1)) - 1, lower_bound)
    while start > lower_bound:
        previous = lines[start - 1].strip()
        if previous and not previous.startswith("#"):
            break
        start -= 1
    return start


def _definition_range(
    lines: list[str],
    node: ast.AST,
    *,
    lower_bound: int,
) -> _SourceRange:
    return _SourceRange(
        start=_attached_comment_start(lines, node, lower_bound=lower_bound),
        end=int(getattr(node, "end_lineno", getattr(node, "lineno", 1))),
    )


def _without_ranges(source_lines: list[str], ranges: list[_SourceRange]) -> str:
    remaining = list(source_lines)
    for item in sorted(ranges, key=lambda value: value.start, reverse=True):
        del remaining[item.start:item.end]
    return "".join(remaining).strip() + "\n"


def _solution_classes(tree: ast.Module) -> list[ast.ClassDef]:
    return [
        node
        for node in tree.body
        if isinstance(node, ast.ClassDef) and node.name.startswith("Solution")
    ]


def _numbered_entry_methods(solution_class: ast.ClassDef) -> list[ast.FunctionDef | ast.AsyncFunctionDef]:
    methods = [
        node
        for node in solution_class.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and not node.name.startswith("_")
    ]
    if not methods:
        return []

    first_name = methods[0].name
    first_match = _NUMBERED_METHOD_RE.fullmatch(first_name)
    base_name = first_match.group(1) if first_match else first_name
    alternatives = [
        method
        for method in methods
        if method.name == base_name
        or (
            (match := _NUMBERED_METHOD_RE.fullmatch(method.name)) is not None
            and match.group(1) == base_name
        )
    ]
    return alternatives if len(alternatives) > 1 else []


def _method_ranges(
    lines: list[str],
    solution_class: ast.ClassDef,
    methods: list[ast.FunctionDef | ast.AsyncFunctionDef],
) -> dict[int, _SourceRange]:
    ranges: dict[int, _SourceRange] = {}
    previous_end = int(solution_class.lineno)
    method_ids = {id(method) for method in methods}
    for node in solution_class.body:
        if id(node) in method_ids:
            ranges[id(node)] = _definition_range(
                lines,
                node,
                lower_bound=previous_end,
            )
        previous_end = int(getattr(node, "end_lineno", getattr(node, "lineno", previous_end)))
    return ranges


def split_competitive_python_source(source: str) -> list[str]:
    """Return one complete display source for each recognizable implementation.

    Unparseable or structurally unusual files remain a single implementation.
    When alternatives are found, imports, module-level helpers, and unrelated
    support declarations are retained in every returned source.
    """

    try:
        tree = ast.parse(source)
    except (SyntaxError, ValueError):
        return [source]

    classes = _solution_classes(tree)
    if not classes:
        return [source]

    lines = source.splitlines(keepends=True)
    class_ranges: dict[int, _SourceRange] = {}
    previous_end = 0
    for solution_class in classes:
        class_ranges[id(solution_class)] = _definition_range(
            lines,
            solution_class,
            lower_bound=previous_end,
        )
        previous_end = int(solution_class.end_lineno or solution_class.lineno)

    implementations: list[str] = []
    for selected_class in classes:
        other_class_ranges = [
            item
            for class_id, item in class_ranges.items()
            if class_id != id(selected_class)
        ]
        entry_methods = _numbered_entry_methods(selected_class)
        if not entry_methods:
            implementations.append(_without_ranges(lines, other_class_ranges))
            continue

        method_ranges = _method_ranges(lines, selected_class, entry_methods)
        for selected_method in entry_methods:
            removed_methods = [
                item
                for method_id, item in method_ranges.items()
                if method_id != id(selected_method)
            ]
            implementations.append(
                _without_ranges(lines, [*other_class_ranges, *removed_methods])
            )

    return implementations or [source]


def split_competitive_solution_source(source: str, language: str) -> list[str]:
    """Split a Competitive source when its language has safe structure rules."""

    if language == "python":
        return split_competitive_python_source(source)
    return [source]
