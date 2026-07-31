"""Audit alignment between app-local and Accepted LeetCode Optimal sources.

Remote acceptance proves that the platform-native source is correct for
LeetCode.  It does not prove that the separately maintained app-local source
uses the same implementation.  This audit therefore recognizes only
structural evidence that can be checked locally and sends every other pair to
an explicit review queue.

The audit never edits either source.  In particular, a verified native source
remains immutable until a proposed replacement has independently received an
Accepted verdict.
"""

from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.languages import app_solution_filename  # noqa: E402


LEETCODE_ROOT = ROOT / "dsa" / "leetcode"
JSON_REPORT_PATH = LEETCODE_ROOT / "_reports" / "optimal_solution_alignment.json"
MARKDOWN_REPORT_PATH = LEETCODE_ROOT / "_reports" / "optimal_solution_alignment.md"
REVIEW_FILE_NAME = "alignment_review.json"

PYTHON_LANGUAGES = {"python", "python3"}
REVIEW_CLASSIFICATIONS = {
    "app_execution_adapter",
    "judge_environment",
    "platform_signature",
    "source_native_data_model",
    "sql_dialect",
}
REQUIRED_REVIEW_ASSERTIONS = {
    "same_algorithm",
    "same_data_flow",
    "same_helper_logic",
    "complexity_matches",
    "naming_consistent_where_interfaces_permit",
    "difference_is_unavoidable",
}


@dataclass(frozen=True)
class AlignmentEntry:
    frontend_id: int
    challenge_id: str
    package: str
    language: str
    status: str
    method: str
    detail: str
    app_source: str
    native_source: str
    app_sha256: str
    native_sha256: str
    review: str | None
    classifications: tuple[str, ...]


class _EraseTypeSyntax(ast.NodeTransformer):
    """Remove type-only differences while preserving executable structure."""

    @staticmethod
    def _without_docstring(body: list[ast.stmt]) -> list[ast.stmt]:
        if (
            body
            and isinstance(body[0], ast.Expr)
            and isinstance(body[0].value, ast.Constant)
            and isinstance(body[0].value.value, str)
        ):
            return body[1:]
        return body

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        node = self.generic_visit(node)
        node.returns = None
        node.type_comment = None
        node.body = self._without_docstring(node.body)
        for argument in (
            *node.args.posonlyargs,
            *node.args.args,
            *node.args.kwonlyargs,
        ):
            argument.annotation = None
            argument.type_comment = None
        if node.args.vararg is not None:
            node.args.vararg.annotation = None
            node.args.vararg.type_comment = None
        if node.args.kwarg is not None:
            node.args.kwarg.annotation = None
            node.args.kwarg.type_comment = None
        return node

    def visit_AsyncFunctionDef(
        self, node: ast.AsyncFunctionDef
    ) -> ast.AsyncFunctionDef:
        node = self.generic_visit(node)
        node.returns = None
        node.type_comment = None
        node.body = self._without_docstring(node.body)
        for argument in (
            *node.args.posonlyargs,
            *node.args.args,
            *node.args.kwonlyargs,
        ):
            argument.annotation = None
            argument.type_comment = None
        if node.args.vararg is not None:
            node.args.vararg.annotation = None
            node.args.vararg.type_comment = None
        if node.args.kwarg is not None:
            node.args.kwarg.annotation = None
            node.args.kwarg.type_comment = None
        return node

    def visit_ClassDef(self, node: ast.ClassDef) -> ast.ClassDef:
        node = self.generic_visit(node)
        node.body = self._without_docstring(node.body)
        return node

    def visit_AnnAssign(self, node: ast.AnnAssign) -> ast.stmt | None:
        node = self.generic_visit(node)
        if node.value is None:
            return None
        return ast.copy_location(
            ast.Assign(targets=[node.target], value=node.value),
            node,
        )


def _canonical(node: ast.AST | list[ast.stmt]) -> str:
    copied: ast.AST
    if isinstance(node, list):
        copied = ast.Module(body=copy.deepcopy(node), type_ignores=[])
    else:
        copied = copy.deepcopy(node)
    transformed = _EraseTypeSyntax().visit(copied)
    ast.fix_missing_locations(transformed)
    return ast.dump(transformed, include_attributes=False)


class _NormalizeEntryRecursion(ast.NodeTransformer):
    """Erase the app ``solve`` versus native ``self.method`` recursion wrapper."""

    def __init__(self, entry_name: str) -> None:
        self.entry_name = entry_name

    def visit_Name(self, node: ast.Name) -> ast.AST:
        if isinstance(node.ctx, ast.Load) and node.id == self.entry_name:
            return ast.copy_location(ast.Name(id="__entry__", ctx=node.ctx), node)
        return node

    def visit_Attribute(self, node: ast.Attribute) -> ast.AST:
        node = self.generic_visit(node)
        if (
            isinstance(node.ctx, ast.Load)
            and node.attr == self.entry_name
            and isinstance(node.value, ast.Name)
            and node.value.id == "self"
        ):
            return ast.copy_location(ast.Name(id="__entry__", ctx=node.ctx), node)
        return node


def _function_body(function: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    body = ast.Module(body=copy.deepcopy(function.body), type_ignores=[])
    normalized = _NormalizeEntryRecursion(function.name).visit(body)
    ast.fix_missing_locations(normalized)
    return _canonical(_EraseTypeSyntax._without_docstring(normalized.body))


def _app_solve(tree: ast.Module) -> ast.FunctionDef | ast.AsyncFunctionDef | None:
    matches = [
        node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name == "solve"
    ]
    return matches[0] if len(matches) == 1 else None


def _native_public_functions(
    tree: ast.Module,
) -> list[ast.FunctionDef | ast.AsyncFunctionDef]:
    methods: list[ast.FunctionDef | ast.AsyncFunctionDef] = []
    functions: list[ast.FunctionDef | ast.AsyncFunctionDef] = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == "Solution":
            methods.extend(
                child
                for child in node.body
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef))
                and not child.name.startswith("_")
            )
        elif (
            isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and not node.name.startswith("_")
        ):
            functions.append(node)
    return methods or functions


def _top_level_definitions(tree: ast.Module) -> dict[str, ast.AST]:
    return {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
    }


def _loaded_names(node: ast.AST) -> set[str]:
    return {
        child.id
        for child in ast.walk(node)
        if isinstance(child, ast.Name) and isinstance(child.ctx, ast.Load)
    }


def _is_explicit_judge_model(node: ast.AST) -> bool:
    """Recognize a visible, data-only app equivalent of a judge model."""

    if isinstance(node, ast.ClassDef) and node.name == "GridMaster":
        if node.bases or node.keywords or node.decorator_list:
            return False
        if not (ast.get_docstring(node, clean=False) or "").startswith(
            "Local equivalent of "
        ):
            return False
        methods = {
            child.name: child
            for child in node.body
            if isinstance(child, ast.FunctionDef)
        }
        return set(methods) == {"canMove", "move", "isTarget"}

    if isinstance(node, ast.ClassDef) and node.name == "Street":
        if node.bases or node.keywords or node.decorator_list:
            return False
        if not (ast.get_docstring(node, clean=False) or "").startswith(
            "Local equivalent of "
        ):
            return False
        methods = {
            child.name: child
            for child in node.body
            if isinstance(child, ast.FunctionDef)
        }
        return set(methods) in (
            {"__init__", "openDoor", "closeDoor", "isDoorOpen", "moveRight", "moveLeft"},
            {"__init__", "closeDoor", "isDoorOpen", "moveRight"},
        )

    if isinstance(node, ast.ClassDef) and node.name == "CategoryHandler":
        if node.bases or node.keywords or node.decorator_list:
            return False
        if not (ast.get_docstring(node, clean=False) or "").startswith(
            "Local equivalent of "
        ):
            return False
        methods = {
            child.name: child
            for child in node.body
            if isinstance(child, ast.FunctionDef)
        }
        return set(methods) == {"__init__", "haveSameCategory"}

    if isinstance(node, ast.ClassDef) and node.name == "BigArray":
        if node.bases or node.keywords or node.decorator_list:
            return False
        if not (ast.get_docstring(node, clean=False) or "").startswith(
            "Local equivalent of "
        ):
            return False
        methods = {
            child.name: child
            for child in node.body
            if isinstance(child, ast.FunctionDef)
        }
        return set(methods) == {"__init__", "size", "at"}

    if isinstance(node, ast.ClassDef) and node.name == "BinaryMatrix":
        if node.bases or node.keywords or node.decorator_list:
            return False
        if not (ast.get_docstring(node, clean=False) or "").startswith(
            "Local equivalent of "
        ):
            return False
        methods = {
            child.name: child
            for child in node.body
            if isinstance(child, ast.FunctionDef)
        }
        if set(methods) != {"__init__", "get", "dimensions"}:
            return False
        initializer = methods["__init__"]
        return all(
            not isinstance(child, ast.Attribute)
            or not isinstance(child.ctx, ast.Store)
            or (
                isinstance(child.value, ast.Name)
                and child.value.id == "self"
                and child.attr == "matrix"
            )
            for child in ast.walk(initializer)
        )

    if isinstance(node, ast.ClassDef) and node.name == "Sea":
        if node.bases or node.keywords or node.decorator_list:
            return False
        if not (ast.get_docstring(node, clean=False) or "").startswith(
            "Local equivalent of "
        ):
            return False
        methods = [
            child
            for child in node.body
            if isinstance(child, ast.FunctionDef)
        ]
        return (
            len(methods) == 1
            and methods[0].name == "hasShips"
            and not methods[0].decorator_list
        )

    if isinstance(node, ast.ClassDef) and node.name == "CustomFunction":
        if node.bases or node.keywords or node.decorator_list:
            return False
        if not (ast.get_docstring(node, clean=False) or "").startswith(
            "Local equivalent of "
        ):
            return False
        methods = {
            child.name: child
            for child in node.body
            if isinstance(child, ast.FunctionDef)
        }
        if set(methods) != {"__init__", "f"}:
            return False
        initializer = methods["__init__"]
        return all(
            not isinstance(child, ast.Attribute)
            or not isinstance(child.ctx, ast.Store)
            or (
                isinstance(child.value, ast.Name)
                and child.value.id == "self"
                and child.attr == "function_id"
            )
            for child in ast.walk(initializer)
        )

    if isinstance(node, ast.ClassDef) and node.name == "HtmlParser":
        if node.bases or node.keywords or node.decorator_list:
            return False
        if not (ast.get_docstring(node, clean=False) or "").startswith(
            "Local equivalent of "
        ):
            return False
        methods = {
            child.name: child
            for child in node.body
            if isinstance(child, ast.FunctionDef)
        }
        if set(methods) != {"__init__", "getUrls"}:
            return False
        initializer = methods["__init__"]
        return all(
            not isinstance(child, ast.Attribute)
            or not isinstance(child.ctx, ast.Store)
            or (
                isinstance(child.value, ast.Name)
                and child.value.id == "self"
                and child.attr == "outgoing"
            )
            for child in ast.walk(initializer)
        )

    if isinstance(node, ast.ClassDef) and node.name == "MountainArray":
        if node.bases or node.keywords or node.decorator_list:
            return False
        if not (ast.get_docstring(node, clean=False) or "").startswith(
            "Local equivalent of "
        ):
            return False
        methods = {
            child.name: child
            for child in node.body
            if isinstance(child, ast.FunctionDef)
        }
        if set(methods) != {"__init__", "get", "length"}:
            return False
        initializer = methods["__init__"]
        return all(
            not isinstance(child, ast.Attribute)
            or not isinstance(child.ctx, ast.Store)
            or (
                isinstance(child.value, ast.Name)
                and child.value.id == "self"
                and child.attr == "values"
            )
            for child in ast.walk(initializer)
        )

    if isinstance(node, ast.ClassDef) and node.name == "Master":
        if node.bases or node.keywords or node.decorator_list:
            return False
        if not (ast.get_docstring(node, clean=False) or "").startswith(
            "Local equivalent of "
        ):
            return False
        methods = [
            child
            for child in node.body
            if isinstance(child, ast.FunctionDef)
        ]
        return (
            len(methods) == 1
            and methods[0].name == "guess"
            and not methods[0].decorator_list
        )

    if isinstance(node, ast.ClassDef) and node.name == "ArrayReader":
        if node.bases or node.keywords or node.decorator_list:
            return False
        if not (ast.get_docstring(node, clean=False) or "").startswith(
            "Local equivalent of "
        ):
            return False
        methods = {
            child.name: child
            for child in node.body
            if isinstance(child, ast.FunctionDef)
        }
        if set(methods) != {"__init__", "get", "compareSub", "length", "query"}:
            return False
        initializer = methods["__init__"]
        return all(
            not isinstance(child, ast.Attribute)
            or not isinstance(child.ctx, ast.Store)
            or (
                isinstance(child.value, ast.Name)
                and child.value.id == "self"
                and child.attr == "values"
            )
            for child in ast.walk(initializer)
        )

    if isinstance(node, ast.ClassDef) and node.name == "NestedInteger":
        if node.bases or node.keywords or node.decorator_list:
            return False
        if not (ast.get_docstring(node, clean=False) or "").startswith(
            "Local equivalent of "
        ):
            return False
        methods = {
            child.name: child
            for child in node.body
            if isinstance(child, ast.FunctionDef)
        }
        if set(methods) != {
            "__init__",
            "isInteger",
            "add",
            "setInteger",
            "getInteger",
            "getList",
        }:
            return False
        allowed_attributes = {"_integer", "_list"}
        initializer = methods["__init__"]
        for child in ast.walk(initializer):
            if (
                isinstance(child, ast.Attribute)
                and isinstance(child.ctx, ast.Store)
                and (
                    not isinstance(child.value, ast.Name)
                    or child.value.id != "self"
                    or child.attr not in allowed_attributes
                )
            ):
                return False
        return True

    allowed_attributes = {
        "TreeNode": {"val", "left", "right", "next", "parent"},
        "ListNode": {"val", "next", "prev"},
        "PolyNode": {"coefficient", "power", "next"},
        "RopeTreeNode": {"len", "val", "left", "right"},
        "Node": {
            "val",
            "isLeaf",
            "left",
            "right",
            "topLeft",
            "topRight",
            "bottomLeft",
            "bottomRight",
            "next",
            "prev",
            "child",
            "parent",
            "random",
            "neighbors",
            "children",
        },
        "NodeCopy": {"val", "left", "right", "random"},
        "Point": {"x", "y"},
        "Employee": {"id", "importance", "subordinates"},
        "Interval": {"start", "end"},
    }
    if not isinstance(node, ast.ClassDef) or node.name not in allowed_attributes:
        return False
    if node.bases or node.keywords or node.decorator_list:
        return False
    if not (ast.get_docstring(node, clean=False) or "").startswith(
        "Local equivalent of "
    ):
        return False
    body = node.body[1:] if ast.get_docstring(node, clean=False) is not None else node.body
    if len(body) != 1 or not isinstance(body[0], ast.FunctionDef):
        return False
    initializer = body[0]
    if initializer.name != "__init__" or initializer.decorator_list:
        return False
    for statement in initializer.body:
        if not isinstance(statement, (ast.Assign, ast.AnnAssign)):
            return False
        targets = statement.targets if isinstance(statement, ast.Assign) else [statement.target]
        for target in targets:
            if not (
                isinstance(target, ast.Attribute)
                and isinstance(target.value, ast.Name)
                and target.value.id == "self"
                and target.attr in allowed_attributes[node.name]
            ):
                return False
    return True


def _referenced_definitions_match(
    app_entry: ast.AST,
    native_entry: ast.AST,
    app_definitions: dict[str, ast.AST],
    native_definitions: dict[str, ast.AST],
) -> bool:
    """Compare same-name helpers reachable from two matching entry points."""
    entry_names = {
        str(getattr(app_entry, "name", "")),
        str(getattr(native_entry, "name", "")),
    }
    pending = list(
        (_loaded_names(app_entry) | _loaded_names(native_entry)) - entry_names
    )
    checked: set[str] = set()
    while pending:
        name = pending.pop()
        if name in checked:
            continue
        checked.add(name)
        app_definition = app_definitions.get(name)
        native_definition = native_definitions.get(name)
        if app_definition is None and native_definition is None:
            continue
        if native_definition is None and _is_explicit_judge_model(app_definition):
            continue
        if app_definition is None or native_definition is None:
            return False
        if _canonical(app_definition) != _canonical(native_definition):
            return False
        pending.extend(
            _loaded_names(app_definition) | _loaded_names(native_definition)
        )
    return True


def _matching_native_classes(
    app_tree: ast.Module,
    native_tree: ast.Module,
) -> bool:
    app_classes = {
        node.name: node for node in app_tree.body if isinstance(node, ast.ClassDef)
    }
    native_classes = [
        node for node in native_tree.body if isinstance(node, ast.ClassDef)
    ]
    if not native_classes:
        return False
    app_definitions = _top_level_definitions(app_tree)
    native_definitions = _top_level_definitions(native_tree)
    for native_class in native_classes:
        app_class = app_classes.get(native_class.name)
        if app_class is None or _canonical(app_class) != _canonical(native_class):
            return False
        if not _referenced_definitions_match(
            app_class,
            native_class,
            app_definitions,
            native_definitions,
        ):
            return False
    return True


def _python_alignment(app_source: str, native_source: str) -> tuple[str, str]:
    try:
        app_tree = ast.parse(app_source)
        native_tree = ast.parse(native_source)
    except SyntaxError as exc:
        return "review_required", f"Python syntax error prevents alignment: {exc}"

    app = _app_solve(app_tree)
    app_definitions = _top_level_definitions(app_tree)
    native_definitions = _top_level_definitions(native_tree)
    if app is not None:
        app_body = _function_body(app)
        for native in _native_public_functions(native_tree):
            if app_body != _function_body(native):
                continue
            if _referenced_definitions_match(
                app,
                native,
                app_definitions,
                native_definitions,
            ):
                return (
                    "structurally_aligned",
                    "direct_python_body",
                )

    if _matching_native_classes(app_tree, native_tree):
        return "structurally_aligned", "python_class_surface"

    return (
        "review_required",
        "Python entry body or referenced implementation differs",
    )


def _normalized_text(source: str) -> str:
    return source.replace("\r\n", "\n").strip()


def _text_alignment(
    *, language: str, app_source: str, native_source: str
) -> tuple[str, str]:
    app = _normalized_text(app_source)
    native = _normalized_text(native_source)
    if language == "javascript":
        if native and native in app:
            return "structurally_aligned", "native_javascript_embedded"
        return "review_required", "JavaScript implementation text differs"
    if language == "mysql":
        if app.rstrip(";").rstrip() == native.rstrip(";").rstrip():
            return "structurally_aligned", "exact_sql_query"
        return "review_required", "MySQL and app-local SQL query text differs"
    if language == "bash":
        if app == native:
            return "structurally_aligned", "exact_bash_source"
        return "review_required", "Bash source text differs"
    return "review_required", f"Unsupported alignment language: {language}"


def _sha256(source: str) -> str:
    canonical = source.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _review_alignment(
    *,
    package: Path,
    app_path: Path,
    native_path: Path,
    app_source: str,
    native_source: str,
) -> tuple[Path, tuple[str, ...]] | None:
    review_path = package / "variants" / "optimal" / REVIEW_FILE_NAME
    if not review_path.is_file():
        return None

    review = json.loads(review_path.read_text(encoding="utf-8"))
    prefix = f"{package.name}/variants/optimal/{REVIEW_FILE_NAME}"
    if review.get("schema_version") != 1 or review.get("status") != "reviewed":
        raise ValueError(f"{prefix}: expected schema_version 1 and reviewed status")

    expected_paths = {
        "app_source": app_path.relative_to(review_path.parent).as_posix(),
        "native_source": native_path.relative_to(review_path.parent).as_posix(),
    }
    for field, expected in expected_paths.items():
        if review.get(field) != expected:
            raise ValueError(f"{prefix}: {field} must be {expected!r}")

    variants_path = package / "solution_variants.json"
    approach_path = review_path.parent / "approach.md"
    expected_hashes = {
        "app_sha256": _sha256(app_source),
        "native_sha256": _sha256(native_source),
        "solution_variants_sha256": _sha256(
            variants_path.read_text(encoding="utf-8")
        ),
        "approach_sha256": _sha256(approach_path.read_text(encoding="utf-8")),
    }
    hashes = review.get("hashes")
    if not isinstance(hashes, dict):
        raise ValueError(f"{prefix}: hashes must be an object")
    for field, expected in expected_hashes.items():
        if hashes.get(field) != expected:
            raise ValueError(f"{prefix}: stale or invalid {field}")

    classifications_value = review.get("classifications")
    if not isinstance(classifications_value, list) or not classifications_value:
        raise ValueError(f"{prefix}: classifications must be a non-empty array")
    classifications = tuple(classifications_value)
    if (
        len(set(classifications)) != len(classifications)
        or set(classifications) - REVIEW_CLASSIFICATIONS
    ):
        raise ValueError(f"{prefix}: invalid or duplicate classification")

    assertions = review.get("assertions")
    if not isinstance(assertions, dict) or set(assertions) != REQUIRED_REVIEW_ASSERTIONS:
        raise ValueError(f"{prefix}: assertions must contain the exact required keys")
    if any(assertions[key] is not True for key in REQUIRED_REVIEW_ASSERTIONS):
        raise ValueError(f"{prefix}: every alignment assertion must be true")

    differences = review.get("differences")
    if not isinstance(differences, list) or not differences:
        raise ValueError(f"{prefix}: differences must be a non-empty array")
    required_difference_fields = {"aspect", "native", "app", "rationale"}
    for index, difference in enumerate(differences):
        if not isinstance(difference, dict) or set(difference) != required_difference_fields:
            raise ValueError(f"{prefix}: difference {index} has invalid fields")
        if any(
            not isinstance(difference[field], str) or not difference[field].strip()
            for field in required_difference_fields
        ):
            raise ValueError(f"{prefix}: difference {index} contains blank evidence")
    return review_path, classifications


def _entry(package: Path) -> AlignmentEntry:
    metadata = json.loads((package / "metadata.json").read_text(encoding="utf-8"))
    manifest_path = package / "variants" / "optimal" / "submission.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("status") != "verified":
        raise ValueError(f"{package.name}: Optimal submission is not verified")
    language = str(manifest.get("language") or "")
    try:
        app_name = app_solution_filename(language)
    except ValueError:
        raise ValueError(f"{package.name}: unsupported submission language {language!r}")
    app_path = manifest_path.parent / "solutions" / app_name
    native_path = manifest_path.parent / str(manifest.get("source") or "")
    app_source = app_path.read_text(encoding="utf-8")
    native_source = native_path.read_text(encoding="utf-8")
    if language in PYTHON_LANGUAGES:
        status, method = _python_alignment(app_source, native_source)
    else:
        status, method = _text_alignment(
            language=language,
            app_source=app_source,
            native_source=native_source,
        )
    review = _review_alignment(
        package=package,
        app_path=app_path,
        native_path=native_path,
        app_source=app_source,
        native_source=native_source,
    )
    if review is not None:
        if status == "structurally_aligned":
            raise ValueError(
                f"{package.name}: remove stale {REVIEW_FILE_NAME}; sources now align"
            )
        review_path, classifications = review
        status = "reviewed_difference"
        method = "hash_bound_review"
        detail = ", ".join(classifications)
    else:
        review_path = None
        classifications = ()
        detail = (
            "Executable structure matches after type-only syntax is removed."
            if status == "structurally_aligned"
            else method
        )
    return AlignmentEntry(
        frontend_id=int(metadata["frontend_id"]),
        challenge_id=str(metadata["challenge_id"]),
        package=_relative(package),
        language=language,
        status=status,
        method=(
            method
            if status in {"structurally_aligned", "reviewed_difference"}
            else "manual_review"
        ),
        detail=detail,
        app_source=_relative(app_path),
        native_source=_relative(native_path),
        app_sha256=_sha256(app_source),
        native_sha256=_sha256(native_source),
        review=_relative(review_path) if review_path is not None else None,
        classifications=classifications,
    )


def build_report(root: Path = LEETCODE_ROOT) -> dict[str, Any]:
    packages = sorted(root.glob("[0-9][0-9][0-9][0-9]_*"))
    frontend_ids = [
        int(json.loads((package / "metadata.json").read_text(encoding="utf-8"))["frontend_id"])
        for package in packages
    ]
    if frontend_ids != list(range(1, 4006)):
        raise ValueError("Canonical package scope must be the complete ID range 1..4005")
    entries = [_entry(package) for package in packages]
    status_counts = Counter(entry.status for entry in entries)
    language_counts = Counter(entry.language for entry in entries)
    method_counts = Counter(entry.method for entry in entries)
    first_review = next(
        (entry for entry in entries if entry.status == "review_required"),
        None,
    )
    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "scope": (
            "All canonical Optimal app/native source pairs through frontend ID 4005. "
            "Structural alignment is local evidence, not a substitute for remote acceptance."
        ),
        "counts": {
            "packages": len(entries),
            "structurally_aligned": status_counts["structurally_aligned"],
            "reviewed_difference": status_counts["reviewed_difference"],
            "review_required": status_counts["review_required"],
            "languages": dict(sorted(language_counts.items())),
            "methods": dict(sorted(method_counts.items())),
        },
        "first_review_required": (
            {
                "frontend_id": first_review.frontend_id,
                "challenge_id": first_review.challenge_id,
                "package": first_review.package,
            }
            if first_review is not None
            else None
        ),
        "entries": [asdict(entry) for entry in entries],
    }


def _write_markdown(report: dict[str, Any], path: Path) -> None:
    counts = report["counts"]
    lines = [
        "# Optimal Solution Alignment",
        "",
        f"Generated: {report['generated_at']}",
        "",
        str(report["scope"]),
        "",
        "## Summary",
        "",
        "| Metric | Count |",
        "| --- | ---: |",
        f"| Packages | {counts['packages']} |",
        f"| Structurally aligned | {counts['structurally_aligned']} |",
        f"| Reviewed unavoidable difference | {counts['reviewed_difference']} |",
        f"| Review required | {counts['review_required']} |",
        "",
        "Structural alignment compares executable Python bodies and their referenced "
        "same-name helpers after removing type-only syntax. Design classes, exact SQL "
        "and Bash sources, and verbatim embedded JavaScript submissions have separate "
        "structural checks. Every other pair remains unreviewed; equivalent outputs or "
        "matching complexity labels do not silently promote it. A structurally different "
        "pair clears the queue only through a current hash-bound review of a permitted, "
        "unavoidable adapter or dialect difference.",
        "",
        "## Review queue",
        "",
        "| ID | Challenge | Language | Reason |",
        "| ---: | --- | --- | --- |",
    ]
    review_entries = [
        entry for entry in report["entries"] if entry["status"] == "review_required"
    ]
    for entry in review_entries:
        lines.append(
            f"| {entry['frontend_id']} | `{entry['challenge_id']}` | "
            f"{entry['language']} | {entry['detail']} |"
        )
    if not review_entries:
        lines.append("| - | None | - | - |")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=JSON_REPORT_PATH)
    parser.add_argument("--markdown", type=Path, default=MARKDOWN_REPORT_PATH)
    parser.add_argument("--no-write", action="store_true")
    parser.add_argument(
        "--allow-review-required",
        action="store_true",
        help="Return success while the explicit review queue is non-empty.",
    )
    args = parser.parse_args()

    report = build_report()
    if not args.no_write:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(
            json.dumps(report, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        _write_markdown(report, args.markdown)
    print(json.dumps(report["counts"], indent=2))
    if report["first_review_required"] is not None:
        print(
            "First review required: "
            + json.dumps(report["first_review_required"], ensure_ascii=False)
        )
    if not args.no_write:
        print(f"Wrote {_relative(args.json)} and {_relative(args.markdown)}.")
    return int(
        bool(report["counts"]["review_required"])
        and not args.allow_review_required
    )


if __name__ == "__main__":
    sys.exit(main())
