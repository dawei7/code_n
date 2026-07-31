"""Regression checks for direct app/native solution adapters."""

from __future__ import annotations

import ast
import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEETCODE_ROOT = ROOT / "dsa" / "leetcode"


class _StoredNames(ast.NodeVisitor):
    def __init__(self) -> None:
        self.names: list[str] = []
        self._seen: set[str] = set()

    def visit_Name(self, node: ast.Name) -> None:
        if isinstance(node.ctx, (ast.Store, ast.Del)) and node.id not in self._seen:
            self._seen.add(node.id)
            self.names.append(node.id)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        return

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        return

    def visit_Lambda(self, node: ast.Lambda) -> None:
        return

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        return


class _ScopeRenamer(ast.NodeTransformer):
    def __init__(self, names: dict[str, str]) -> None:
        self.names = names

    def visit_Name(self, node: ast.Name) -> ast.Name:
        if node.id in self.names:
            node.id = self.names[node.id]
        return node

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        return node

    def visit_AsyncFunctionDef(
        self, node: ast.AsyncFunctionDef
    ) -> ast.AsyncFunctionDef:
        return node

    def visit_Lambda(self, node: ast.Lambda) -> ast.Lambda:
        return node

    def visit_ClassDef(self, node: ast.ClassDef) -> ast.ClassDef:
        return node


def _arguments(function: ast.FunctionDef | ast.AsyncFunctionDef) -> list[str]:
    positional = [*function.args.posonlyargs, *function.args.args]
    names = [argument.arg for argument in positional if argument.arg not in {"self", "cls"}]
    names.extend(argument.arg for argument in function.args.kwonlyargs)
    if function.args.vararg is not None:
        names.append(function.args.vararg.arg)
    if function.args.kwarg is not None:
        names.append(function.args.kwarg.arg)
    return names


def _body_dump(
    function: ast.FunctionDef | ast.AsyncFunctionDef,
    *,
    normalize_locals: bool,
) -> str:
    body = copy.deepcopy(function.body)
    if (
        body
        and isinstance(body[0], ast.Expr)
        and isinstance(body[0].value, ast.Constant)
        and isinstance(body[0].value.value, str)
    ):
        body = body[1:]

    names = {name: f"_argument_{index}" for index, name in enumerate(_arguments(function))}
    if normalize_locals:
        stored = _StoredNames()
        for statement in function.body:
            stored.visit(statement)
        local_index = 0
        for name in stored.names:
            if name not in names:
                names[name] = f"_local_{local_index}"
                local_index += 1

    renamer = _ScopeRenamer(names)
    normalized = [renamer.visit(statement) for statement in body]
    module = ast.Module(body=normalized, type_ignores=[])
    return ast.dump(module, include_attributes=False)


def _app_function(tree: ast.Module) -> ast.FunctionDef | ast.AsyncFunctionDef | None:
    candidates = [
        node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == "solve"
    ]
    return candidates[0] if len(candidates) == 1 else None


def _native_functions(
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


def test_alpha_equivalent_direct_adapters_preserve_native_local_names() -> None:
    divergent: list[str] = []
    for package in sorted(LEETCODE_ROOT.iterdir()):
        manifest_path = package / "variants" / "optimal" / "submission.json"
        app_path = manifest_path.parent / "solutions" / "python.py"
        if not manifest_path.is_file() or not app_path.is_file():
            continue
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("status") != "verified" or manifest.get("language") not in {
            "python",
            "python3",
        }:
            continue
        native_path = manifest_path.parent / str(manifest["source"])
        app = _app_function(ast.parse(app_path.read_text(encoding="utf-8")))
        natives = _native_functions(ast.parse(native_path.read_text(encoding="utf-8")))
        if app is None or not natives:
            continue

        app_parameter_body = _body_dump(app, normalize_locals=False)
        if any(
            app_parameter_body == _body_dump(native, normalize_locals=False)
            for native in natives
        ):
            continue
        app_alpha_body = _body_dump(app, normalize_locals=True)
        if any(
            app_alpha_body == _body_dump(native, normalize_locals=True)
            for native in natives
        ):
            divergent.append(package.name)

    assert not divergent, (
        "Direct app/native adapters differ only in local identifier names: "
        + ", ".join(divergent)
    )
