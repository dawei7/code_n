"""Canonical LeetCode solution-template tests."""
from __future__ import annotations

import ast
import json
import keyword

from challenges.registry import get_challenge
from engine import solutions
from server.app.challenge_packages import leetcode_cases_path, leetcode_solution_path


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
        compile(template, f"{challenge_id}_template.py", "exec")
        assert get_challenge(challenge_id) is not None


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
        assert info["params"] == list(first_input), challenge_id


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
