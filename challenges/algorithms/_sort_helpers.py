"""Shared helpers for the sorting-algorithm challenges.

Centralises the ``is_sorted_result`` check so every sort
challenge uses identical acceptance semantics: the player may
either mutate the input in place (``return None``) or return a
new sorted sequence. Both are accepted.
"""

from __future__ import annotations

from typing import Any

from code_n.tracked import TrackedList, unwrap_tracked


def is_sorted_result(result: Any, expected_data: list, working_data: TrackedList | None = None) -> bool:
    expected = sorted(expected_data)
    if result is None and working_data is not None:
        return working_data.raw == expected
    if isinstance(result, TrackedList):
        return result.raw == expected
    if isinstance(result, (list, tuple)):
        values = [unwrap_tracked(value) for value in result]
        return values == expected
    return False
