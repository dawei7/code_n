"""Optimal app-local solution for LeetCode 984."""


def solve(a, b):
    answer = []
    while a or b:
        if len(answer) >= 2 and answer[-1] == answer[-2]:
            character = "b" if answer[-1] == "a" else "a"
        else:
            character = "a" if a >= b else "b"

        if (a if character == "a" else b) == 0:
            character = "b" if character == "a" else "a"

        answer.append(character)
        if character == "a":
            a -= 1
        else:
            b -= 1

    return "".join(answer)
