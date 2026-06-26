"""Tests for the per-challenge solution templates.

Every challenge's auto-generated starter file must:
  * have EXPLICIT parameter names (no `**kwargs`)
  * show the function signature as `def solve(arg1, arg2, ...):`
  * use a clean triple-quoted header with underlined section titles

These properties were added after the user reported the
`**kwargs` template was misleading. The check is purely textual
on the generated template; we don't write the file to disk.
"""
from __future__ import annotations

import re

from code_n import solutions
from challenges.registry import get_challenge


def test_all_registered_challenges_have_explicit_templates():
    registered = set(__import__("challenges.registry", fromlist=["list_challenges"]).list_challenges())
    templated = set(solutions._CHALLENGE_TEMPLATES.keys())
    missing = registered - templated
    assert not missing, f"Missing explicit templates for: {sorted(missing)}"


def test_no_template_uses_kwargs():
    for cid, info in solutions._CHALLENGE_TEMPLATES.items():
        params = info["params"]
        assert "**kwargs" not in params, f"{cid} still uses **kwargs"
        assert all(re.match(r"^[a-z_][a-z0-9_]*$", p) for p in params), (
            f"{cid} has invalid parameter names: {params}"
        )


def test_template_signature_matches_param_list():
    for cid, info in solutions._CHALLENGE_TEMPLATES.items():
        template = solutions._solution_template(
            cid, f"{cid}: {cid.title()}", "test description",
        )
        expected_sig = "def solve(" + ", ".join(info["params"]) + "):"
        assert expected_sig in template, f"{cid} template missing signature: {expected_sig}"


def test_template_docstring_is_uncluttered():
    for cid, info in solutions._CHALLENGE_TEMPLATES.items():
        template = solutions._solution_template(
            cid, f"{cid}: {cid.title()}", "test description",
        )
        assert template.startswith('"""\nDescription\n-----------\n')
        assert "test description" in template
        assert "\nExamples\n--------\n" in template
        assert "1. Description" not in template
        assert "2. Examples" not in template
        assert "Inputs passed to solve():" not in template
        assert "\nGoal:\n" not in template
        assert "##" not in template
        assert "```" not in template
        assert "GeeksforGeeks Reference" not in template
        for name in info["params"]:
            assert f"    {name}:" not in template, (
                f"{cid} template still includes input metadata for '{name}'"
            )


def test_neetcode_template_uses_three_examples_from_docs():
    template = solutions._solution_template(
        "nc_1",
        "nc_1: Concatenation of Array",
        "Given an integer array `nums` of length `n`, return the concatenation of `nums` with itself.\n\n"
        "## Example\n```\nInput: nums = [1, 2, 1]\nOutput: [1, 2, 1, 1, 2, 1]\n```\n\n"
        "## GeeksforGeeks Reference\n"
        "[Python list concatenation](https://www.geeksforgeeks.org/python-list-operations/)",
    )
    assert "Given an integer array nums of length n" in template
    assert template.count("Example ") == 3
    assert "Input:  nums = [1, 2, 1]" in template
    assert "Output: [1, 2, 1, 1, 2, 1]" in template
    assert "## Example" not in template
    assert "GeeksforGeeks Reference" not in template


def test_template_starts_with_solve_call():
    """Every starter file must be valid Python with an explicit solve() stub."""
    for cid in solutions._CHALLENGE_TEMPLATES:
        template = solutions._solution_template(
            cid, f"{cid}: {cid.title()}", "test description",
        )
        assert "def solve(" in template
        assert "return None" in template
        ch = get_challenge(cid)
        if ch is not None:
            compile(template, f"{cid}_template.py", "exec")
