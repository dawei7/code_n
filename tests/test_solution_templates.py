"""Canonical LeetCode solution-template tests."""
from __future__ import annotations

import re

from challenges.registry import get_challenge
from engine import solutions


def test_all_registered_challenges_have_explicit_templates() -> None:
    registered = set(__import__("challenges.registry", fromlist=["list_challenges"]).list_challenges())
    assert registered == set(solutions._CHALLENGE_TEMPLATES)


def test_python_templates_are_clean_and_explicit() -> None:
    for challenge_id, info in solutions._CHALLENGE_TEMPLATES.items():
        assert challenge_id.startswith("lc_")
        assert all(re.match(r"^[a-z_][a-z0-9_]*$", param) for param in info["params"])
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
