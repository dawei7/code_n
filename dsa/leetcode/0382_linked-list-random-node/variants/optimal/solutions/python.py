"""Optimal app-local solution for LeetCode 382: Linked List Random Node."""

from random import choice


def solve(head, draws: int) -> list[int]:
    values: list[int] = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next

    return [choice(values) for _ in range(draws)]
