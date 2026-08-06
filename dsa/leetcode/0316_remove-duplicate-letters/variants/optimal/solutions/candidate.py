"""Greedy monotonic-stack solution for LeetCode 316."""


def _remove_duplicate_letters(s: str) -> str:
    last_index = {letter: i for i, letter in enumerate(s)}
    stack: list[str] = []
    selected: set[str] = set()

    for i, letter in enumerate(s):
        if letter in selected:
            continue
        while stack and letter < stack[-1] and last_index[stack[-1]] > i:
            selected.remove(stack.pop())
        stack.append(letter)
        selected.add(letter)

    return "".join(stack)


def solve(s: str) -> str:
    return _remove_duplicate_letters(s)
