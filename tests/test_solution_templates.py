"""Canonical LeetCode solution-template tests."""
from __future__ import annotations

import ast
import json
import keyword
import re
import symtable
import warnings

from challenges.registry import get_challenge
from engine import solutions
from server.app.challenge_packages import (
    leetcode_cases_path,
    leetcode_metadata_path,
    leetcode_solution_path,
)


def test_all_registered_challenges_have_explicit_templates() -> None:
    registered = set(__import__("challenges.registry", fromlist=["list_challenges"]).list_challenges())
    assert registered == set(solutions._CHALLENGE_TEMPLATES)


def test_python_templates_are_clean_and_explicit() -> None:
    for challenge_id, info in solutions._CHALLENGE_TEMPLATES.items():
        assert challenge_id.startswith("lc_")
        assert all(
            param.isidentifier() and not keyword.iskeyword(param)
            for param in info["params"]
        )
        template = solutions._solution_template(
            challenge_id,
            f"{challenge_id}: {challenge_id.title()}",
            "test description",
        )
        signature = "def solve(" + ", ".join(info["params"]) + "):"
        assert signature in template
        assert template.startswith('\"\"\"\nDescription\n-----------\n')
        assert "return None" in template
        assert "```" not in template
        with warnings.catch_warnings():
            warnings.simplefilter("error", SyntaxWarning)
            compile(template, f"{challenge_id}_template.py", "exec")
        assert get_challenge(challenge_id) is not None


def test_marked_judge_models_are_copied_into_python_templates() -> None:
    for challenge_id, info in solutions._CHALLENGE_TEMPLATES.items():
        solution_path = leetcode_solution_path(challenge_id, "python")
        if solution_path is None or not solution_path.is_file():
            continue
        source = solution_path.read_text(encoding="utf-8")
        source_tree = ast.parse(source)
        expected_models = {
            node.name
            for node in source_tree.body
            if isinstance(node, ast.ClassDef)
            and (ast.get_docstring(node, clean=False) or "").startswith(
                "Local equivalent of "
            )
        }
        if not expected_models:
            continue

        template = solutions._solution_template(
            challenge_id,
            f"{challenge_id}: starter model regression",
            "test description",
        )
        template_tree = ast.parse(template)
        actual_models = {
            node.name for node in template_tree.body if isinstance(node, ast.ClassDef)
        }
        assert expected_models <= actual_models, challenge_id


def test_source_native_judge_models_are_explicit_in_app_solutions() -> None:
    judge_models = {
        "TreeNode",
        "ListNode",
        "PolyNode",
        "RopeTreeNode",
        "Street",
        "CategoryHandler",
        "BigArray",
        "Node",
        "NodeCopy",
        "Point",
        "NestedInteger",
        "Employee",
        "Interval",
        "ArrayReader",
        "Master",
        "MountainArray",
        "HtmlParser",
        "CustomFunction",
        "Sea",
        "BinaryMatrix",
        "GridMaster",
    }
    for challenge_id in solutions._CHALLENGE_TEMPLATES:
        solution_path = leetcode_solution_path(challenge_id, "python")
        if solution_path is None or not solution_path.is_file():
            continue
        native_paths = sorted(solution_path.parent.glob("leetcode_python*.py"))
        if not native_paths:
            continue

        native_source = native_paths[0].read_text(encoding="utf-8")
        native_tree = ast.parse(native_source)
        native_defined_models = {
            node.name
            for node in ast.walk(native_tree)
            if isinstance(node, ast.ClassDef) and node.name in judge_models
        }
        expected_models = {
            model
            for model in judge_models - native_defined_models
            if re.search(rf"\b{model}\b", native_source)
        }
        if not expected_models:
            continue

        source_tree = ast.parse(solution_path.read_text(encoding="utf-8"))
        marked_models = {
            node.name
            for node in source_tree.body
            if isinstance(node, ast.ClassDef)
            and (ast.get_docstring(node, clean=False) or "").startswith(
                "Local equivalent of "
            )
        }
        assert expected_models <= marked_models, challenge_id


def test_app_references_do_not_depend_on_injected_judge_model_names() -> None:
    model_names = {
        "TreeNode",
        "ListNode",
        "PolyNode",
        "RopeTreeNode",
        "Street",
        "CategoryHandler",
        "BigArray",
        "Node",
        "NodeCopy",
        "Point",
        "NestedInteger",
        "Employee",
        "Interval",
        "ArrayReader",
        "Master",
        "MountainArray",
        "HtmlParser",
        "CustomFunction",
        "Sea",
        "BinaryMatrix",
        "GridMaster",
    }

    def unresolved_global_models(table: symtable.SymbolTable) -> set[str]:
        unresolved: set[str] = set()
        for name in model_names & set(table.get_identifiers()):
            symbol = table.lookup(name)
            if symbol.is_referenced() and symbol.is_global():
                unresolved.add(name)
        for child in table.get_children():
            unresolved.update(unresolved_global_models(child))
        return unresolved

    for challenge_id in solutions._CHALLENGE_TEMPLATES:
        solution_path = leetcode_solution_path(challenge_id, "python")
        if solution_path is None or not solution_path.is_file():
            continue
        source = solution_path.read_text(encoding="utf-8")
        module_table = symtable.symtable(source, str(solution_path), "exec")
        module_bindings = {
            name
            for name in model_names & set(module_table.get_identifiers())
            if module_table.lookup(name).is_assigned()
            or module_table.lookup(name).is_imported()
        }
        unresolved = unresolved_global_models(module_table) - module_bindings
        assert not unresolved, f"{challenge_id}: undefined {sorted(unresolved)}"


def test_unique_bst_starter_defines_executable_tree_node() -> None:
    template = solutions._solution_template(
        "lc_95",
        "lc_95: Unique Binary Search Trees II",
        "Generate all structurally unique binary search trees.",
    )
    namespace: dict[str, object] = {}
    exec(template, namespace)
    tree_node = namespace["TreeNode"]
    root = tree_node(2, tree_node(1), tree_node(3))
    assert (root.val, root.left.val, root.right.val) == (2, 1, 3)


def test_document_input_parser_ignores_constraint_bullets() -> None:
    from challenges.algorithms.leetcode import _inputs

    text = """
### Function Contract
**Inputs**

Let $n$ be the array length.

- `arr`: the integer array.
- Every value lies in the supported range.
- Values need not be distinct.

**Return value**
Return a boolean.
"""

    assert _inputs(text) == [("arr", "the integer array.")]


def test_templates_match_app_local_solve_signatures() -> None:
    for challenge_id, info in solutions._CHALLENGE_TEMPLATES.items():
        solution_path = leetcode_solution_path(challenge_id, "python")
        if solution_path is None or not solution_path.is_file():
            continue
        tree = ast.parse(solution_path.read_text(encoding="utf-8"))
        solve = next(
            (
                node
                for node in tree.body
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                and node.name == "solve"
            ),
            None,
        )
        if solve is None:
            continue
        expected = [
            arg.arg
            for arg in (*solve.args.posonlyargs, *solve.args.args)
        ]
        assert info["params"] == expected, challenge_id


def test_templates_match_authored_case_inputs() -> None:
    for challenge_id, info in solutions._CHALLENGE_TEMPLATES.items():
        cases_path = leetcode_cases_path(challenge_id)
        if cases_path is None or not cases_path.is_file():
            continue
        payload = json.loads(cases_path.read_text(encoding="utf-8"))
        first_input = next(
            (
                case.get("input")
                for case in payload.get("cases", [])
                if isinstance(case, dict) and isinstance(case.get("input"), dict)
            ),
            None,
        )
        if first_input is None or list(first_input) == ["args"]:
            continue
        table_inputs = first_input.get("tables")
        metadata_path = leetcode_metadata_path(challenge_id)
        metadata = (
            json.loads(metadata_path.read_text(encoding="utf-8"))
            if metadata_path is not None and metadata_path.is_file()
            else {}
        )
        case_params = (
            list(table_inputs)
            if metadata.get("category") == "pandas"
            and list(first_input) == ["tables"]
            and isinstance(table_inputs, dict)
            else list(first_input)
        )
        assert info["params"] == case_params, challenge_id


def test_arithmetic_progression_template_has_only_arr() -> None:
    template = solutions._solution_template(
        "lc_1502",
        "Can Make Arithmetic Progression From Sequence",
        "Test description.",
    )
    assert "def solve(arr):" in template
    assert "def solve(arr, every, values):" not in template


def test_two_sum_templates_cover_all_function_languages() -> None:
    expected_fragments = {
        "python": "def solve(nums, target):",
        "cpp": "vector<int> solve(vector<int> nums, int target)",
        "java": "List<Integer> solve(List<Integer> nums, int target)",
        "csharp": "List<int> Solve(List<int> nums, int target)",
        "javascript": "solve(nums, target)",
        "go": "func solve(nums []int, target int) []int",
        "kotlin": "fun solve(nums: MutableList<Int>, target: Int): MutableList<Int>",
    }
    for language, fragment in expected_fragments.items():
        template = solutions._solution_template("lc_1", "lc_1: Two Sum", "Two Sum.", language)
        assert fragment in template


def test_special_environment_starters_remain_native() -> None:
    sql = solutions._solution_template("lc_175", "Combine Two Tables", "SQL task.", "sql")
    pandas = solutions._solution_template("lc_2877", "Create a DataFrame", "Pandas task.", "python")
    bash = solutions._solution_template("lc_193", "Valid Phone Numbers", "Shell task.", "bash")
    assert "SELECT" in sql.upper()
    assert "def solve(" in pandas
    assert "#!/" in bash or "grep" in bash
