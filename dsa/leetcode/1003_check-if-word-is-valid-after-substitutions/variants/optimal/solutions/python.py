"""Optimal app-local solution for LeetCode 1003."""


def solve(s):
    stack = []
    for character in s:
        stack.append(character)
        if (
            len(stack) >= 3
            and stack[-3] == "a"
            and stack[-2] == "b"
            and stack[-1] == "c"
        ):
            stack.pop()
            stack.pop()
            stack.pop()
    return not stack
