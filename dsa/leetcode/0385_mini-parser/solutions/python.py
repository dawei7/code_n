"""Optimal app-local solution for LeetCode 385: Mini Parser."""


def solve(s: str):
    if s[0] != "[":
        return int(s)

    stack: list[list] = []
    number_start: int | None = None

    for index, character in enumerate(s):
        if character == "[":
            nested: list = []
            if stack:
                stack[-1].append(nested)
            stack.append(nested)
        elif character == "," or character == "]":
            if number_start is not None:
                stack[-1].append(int(s[number_start:index]))
                number_start = None
            if character == "]":
                completed = stack.pop()
                if not stack:
                    return completed
        elif number_start is None:
            number_start = index

    raise ValueError("Incomplete nested-integer serialization")
