"""Optimal app-local solution for LeetCode 381: Randomized Collection."""

from collections import defaultdict
from random import choice


def solve(operations: list[list]) -> list:
    values: list[int] = []
    indices: dict[int, set[int]] = defaultdict(set)
    results: list = []

    for operation in operations:
        name = operation[0]
        if name == "insert":
            value = operation[1]
            is_new = not indices[value]
            indices[value].add(len(values))
            values.append(value)
            results.append(is_new)
        elif name == "remove":
            value = operation[1]
            if not indices.get(value):
                results.append(False)
                continue

            remove_index = indices[value].pop()
            final_index = len(values) - 1
            final_value = values[final_index]
            if remove_index != final_index:
                values[remove_index] = final_value
                indices[final_value].add(remove_index)
                indices[final_value].discard(final_index)
            values.pop()
            if not indices[value]:
                del indices[value]
            results.append(True)
        elif name == "getRandom":
            results.append(choice(values))
        else:
            raise ValueError(f"Unsupported RandomizedCollection operation: {name}")

    return results

