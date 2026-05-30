"""Saved solution for intro_01: Hello Grid."""

from code_n.api import TrackedList


def solve(data: TrackedList) -> int:
    max_value = data[0]
    for index in range(1, len(data)):
        value = data[index]
        if value > max_value:
            max_value = value
    return max_value
