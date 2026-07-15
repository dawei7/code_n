"""Optimal solution for LeetCode 1047: Remove All Adjacent Duplicates In String."""


def solve(s: str) -> str:
    stack: list[str] = []

    for character in s:
        if stack and stack[-1] == character:
            stack.pop()
        else:
            stack.append(character)

    return "".join(stack)

