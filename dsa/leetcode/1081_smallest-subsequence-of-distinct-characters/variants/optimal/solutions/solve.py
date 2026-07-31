"""Optimal solution for LeetCode 1081: Smallest Subsequence of Distinct Characters."""


def solve(s: str) -> str:
    last_index = {character: index for index, character in enumerate(s)}
    stack: list[str] = []
    included: set[str] = set()

    for index, character in enumerate(s):
        if character in included:
            continue
        while stack and stack[-1] > character and last_index[stack[-1]] > index:
            included.remove(stack.pop())
        stack.append(character)
        included.add(character)

    return "".join(stack)
