"""Optimal app-local solution for LeetCode 1012."""


def solve(n):
    def permutations(available, slots):
        result = 1
        for offset in range(slots):
            result *= available - offset
        return result

    digits = [int(character) for character in str(n)]
    length = len(digits)
    unique = 0

    for shorter in range(1, length):
        unique += 9 * permutations(9, shorter - 1)

    used = set()
    for index, digit in enumerate(digits):
        first = 1 if index == 0 else 0
        for candidate in range(first, digit):
            if candidate not in used:
                unique += permutations(10 - index - 1, length - index - 1)

        if digit in used:
            break
        used.add(digit)
    else:
        unique += 1

    return n - unique
