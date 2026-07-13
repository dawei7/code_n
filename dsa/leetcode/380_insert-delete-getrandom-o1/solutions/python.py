"""Optimal app-local solution for LeetCode 380: Insert Delete GetRandom O(1)."""

from random import choice


def solve(operations: list[list]) -> list:
    values: list[int] = []
    indices: dict[int, int] = {}
    results: list = []

    for operation in operations:
        name = operation[0]
        if name == "insert":
            value = operation[1]
            if value in indices:
                results.append(False)
            else:
                indices[value] = len(values)
                values.append(value)
                results.append(True)
        elif name == "remove":
            value = operation[1]
            if value not in indices:
                results.append(False)
            else:
                remove_index = indices[value]
                final_value = values[-1]
                values[remove_index] = final_value
                indices[final_value] = remove_index
                values.pop()
                del indices[value]
                results.append(True)
        elif name == "getRandom":
            results.append(choice(values))
        else:
            raise ValueError(f"Unsupported RandomizedSet operation: {name}")

    return results

