"""Optimal app-local solution for LeetCode 917."""


def solve(s):
    characters = list(s)
    left = 0
    right = len(characters) - 1

    while left < right:
        if not characters[left].isalpha():
            left += 1
        elif not characters[right].isalpha():
            right -= 1
        else:
            characters[left], characters[right] = characters[right], characters[left]
            left += 1
            right -= 1

    return "".join(characters)

