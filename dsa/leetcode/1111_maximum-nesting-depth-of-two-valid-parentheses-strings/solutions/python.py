"""Optimal app-local solution for LeetCode 1111."""


def solve(seq):
    answer = []
    depth = 0
    for character in seq:
        if character == "(":
            depth += 1
            answer.append(depth % 2)
        else:
            answer.append(depth % 2)
            depth -= 1
    return answer
