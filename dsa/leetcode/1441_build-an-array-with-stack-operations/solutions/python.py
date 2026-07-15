"""Optimal app-local solution for LeetCode 1441."""


def solve(target: list[int], n: int) -> list[str]:
    del n
    operations = []
    target_index = 0
    for current in range(1, target[-1] + 1):
        operations.append("Push")
        if current == target[target_index]:
            target_index += 1
            if target_index == len(target):
                break
        else:
            operations.append("Pop")
    return operations
