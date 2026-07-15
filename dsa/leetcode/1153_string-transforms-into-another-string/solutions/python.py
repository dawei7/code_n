"""Optimal app-local solution for LeetCode 1153."""


def solve(str1: str, str2: str) -> bool:
    if str1 == str2:
        return True

    mapping: dict[str, str] = {}
    for source, target in zip(str1, str2):
        if source in mapping and mapping[source] != target:
            return False
        mapping[source] = target

    return len(set(str2)) < 26
