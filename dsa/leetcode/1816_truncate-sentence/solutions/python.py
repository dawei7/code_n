"""App-local reference solution for LeetCode 1816."""


def solve(s: str, k: int) -> str:
    spaces = 0
    for index, character in enumerate(s):
        if character != " ":
            continue
        spaces += 1
        if spaces == k:
            return s[:index]
    return s
