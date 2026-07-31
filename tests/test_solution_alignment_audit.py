"""Focused tests for the app/native Optimal alignment audit."""

import hashlib
import json
from pathlib import Path

import pytest

from tools.audit_leetcode_solution_alignment import (
    _python_alignment,
    _review_alignment,
)


def test_direct_python_alignment_ignores_type_only_syntax() -> None:
    app = """
def helper(values: list[int]) -> int:
    total: int = 0
    for value in values:
        total += value
    return total

def solve(values: list[int]) -> int:
    return helper(values)
"""
    native = """
from typing import List

def helper(values: List[int]) -> int:
    total = 0
    for value in values:
        total += value
    return total

class Solution:
    def total(self, values: List[int]) -> int:
        return helper(values)
"""

    assert _python_alignment(app, native) == (
        "structurally_aligned",
        "direct_python_body",
    )


def test_direct_python_alignment_ignores_native_method_docstring() -> None:
    app = """
def solve(root, k):
    return root.val[k - 1]
"""
    native = '''
class Solution:
    def getKthCharacter(self, root, k):
        """LeetCode type hint for a judge-provided RopeTreeNode."""
        return root.val[k - 1]
'''

    assert _python_alignment(app, native) == (
        "structurally_aligned",
        "direct_python_body",
    )


def test_direct_python_alignment_follows_helper_implementations() -> None:
    app = """
def helper(value):
    return value + 1

def solve(value):
    return helper(value)
"""
    native = """
def helper(value):
    return value - 1

class Solution:
    def transform(self, value):
        return helper(value)
"""

    status, _detail = _python_alignment(app, native)
    assert status == "review_required"


def test_direct_python_alignment_allows_explicit_data_only_judge_model() -> None:
    app = '''
class TreeNode:
    """Local equivalent of the binary-tree node supplied by LeetCode's judge."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(value):
    return TreeNode(value)
'''
    native = """
class Solution:
    def build(self, value):
        return TreeNode(value)
"""

    assert _python_alignment(app, native) == (
        "structurally_aligned",
        "direct_python_body",
    )


def test_direct_python_alignment_normalizes_recursive_entry_wrapper() -> None:
    app = """
def solve(root):
    if root is None:
        return 0
    return 1 + solve(root.left) + solve(root.right)
"""
    native = """
class Solution:
    def countNodes(self, root):
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
"""

    assert _python_alignment(app, native) == (
        "structurally_aligned",
        "direct_python_body",
    )


def test_algorithm_class_cannot_masquerade_as_judge_model() -> None:
    app = '''
class TreeNode:
    """Local equivalent of the binary-tree node supplied by LeetCode's judge."""

    def __init__(self, val=0):
        self.val = val

    def transform(self):
        return self.val + 1

def solve(value):
    return TreeNode(value)
'''
    native = """
class Solution:
    def build(self, value):
        return TreeNode(value)
"""

    status, _detail = _python_alignment(app, native)
    assert status == "review_required"


def test_design_class_alignment_ignores_app_dispatcher() -> None:
    app = """
class Counter:
    def __init__(self):
        self.value: int = 0

    def increment(self) -> int:
        self.value += 1
        return self.value

def solve(operations):
    counter = Counter()
    return [counter.increment() for _ in operations]
"""
    native = """
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value
"""

    assert _python_alignment(app, native) == (
        "structurally_aligned",
        "python_class_surface",
    )


def test_algebraically_rewritten_code_requires_review() -> None:
    app = """
def solve(left, right):
    first = (left + right) * 0.5
    second = (left - right) * -0.5j
    return first * second
"""
    native = """
class Solution:
    def combine(self, left, right):
        return -0.25j * (left + right) * (left - right)
"""

    status, _detail = _python_alignment(app, native)
    assert status == "review_required"


def _sha256(source: str) -> str:
    return hashlib.sha256(source.encode("utf-8")).hexdigest()


def test_review_must_bind_every_alignment_artifact(tmp_path: Path) -> None:
    package = tmp_path / "0002_example"
    branch = package / "variants" / "optimal"
    solutions = branch / "solutions"
    solutions.mkdir(parents=True)
    app_path = solutions / "solve.py"
    native_path = solutions / "leetcode.py"
    app_source = "def solve(values):\n    return values\n"
    native_source = "class Solution:\n    def run(self, head):\n        return head\n"
    app_path.write_text(app_source, encoding="utf-8")
    native_path.write_text(native_source, encoding="utf-8")
    variants_source = "{}\n"
    approach_source = "## General\n\n## Complexity detail\n\n## Alternatives and edge cases\n"
    (package / "solution_variants.json").write_text(
        variants_source, encoding="utf-8"
    )
    (branch / "approach.md").write_text(approach_source, encoding="utf-8")
    review = {
        "schema_version": 1,
        "status": "reviewed",
        "app_source": "solutions/solve.py",
        "native_source": "solutions/leetcode.py",
        "hashes": {
            "app_sha256": _sha256(app_source),
            "native_sha256": _sha256(native_source),
            "solution_variants_sha256": _sha256(variants_source),
            "approach_sha256": _sha256(approach_source),
        },
        "classifications": ["source_native_data_model"],
        "assertions": {
            "same_algorithm": True,
            "same_data_flow": True,
            "same_helper_logic": True,
            "complexity_matches": True,
            "naming_consistent_where_interfaces_permit": True,
            "difference_is_unavoidable": True,
        },
        "differences": [
            {
                "aspect": "input representation",
                "native": "linked nodes",
                "app": "serialized values",
                "rationale": "The app harness uses JSON values.",
            }
        ],
    }
    review_path = branch / "alignment_review.json"
    review_path.write_text(json.dumps(review), encoding="utf-8")

    assert _review_alignment(
        package=package,
        app_path=app_path,
        native_path=native_path,
        app_source=app_source,
        native_source=native_source,
    ) == (review_path, ("source_native_data_model",))

    review["hashes"]["app_sha256"] = "0" * 64
    review_path.write_text(json.dumps(review), encoding="utf-8")
    with pytest.raises(ValueError, match="stale or invalid app_sha256"):
        _review_alignment(
            package=package,
            app_path=app_path,
            native_path=native_path,
            app_source=app_source,
            native_source=native_source,
        )
