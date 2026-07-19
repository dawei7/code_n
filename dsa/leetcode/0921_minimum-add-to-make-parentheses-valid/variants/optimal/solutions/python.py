"""Optimal app-local solution for LeetCode 921."""


def solve(s):
    open_count = 0
    additions = 0

    for character in s:
        if character == "(":
            open_count += 1
        elif open_count > 0:
            open_count -= 1
        else:
            additions += 1

    return additions + open_count

