"""Optimal app-local solution for LeetCode 1021."""


def solve(s):
    depth = 0
    answer = []

    for character in s:
        if character == "(":
            if depth > 0:
                answer.append(character)
            depth += 1
        else:
            depth -= 1
            if depth > 0:
                answer.append(character)

    return "".join(answer)
