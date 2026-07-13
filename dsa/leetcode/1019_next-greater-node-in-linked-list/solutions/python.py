"""Optimal solution for LeetCode 1019: Next Greater Node In Linked List."""

from __future__ import annotations

from typing import Any


def solve(head: Any | None) -> list[int]:
    values: list[int] = []
    while head is not None:
        values.append(head.val)
        head = head.next

    answer = [0] * len(values)
    stack: list[int] = []
    for i, value in enumerate(values):
        while stack and values[stack[-1]] < value:
            answer[stack.pop()] = value
        stack.append(i)
    return answer
