"""Optimal app-local solution for LeetCode 942."""


def solve(s):
    low = 0
    high = len(s)
    permutation = []

    for character in s:
        if character == "I":
            permutation.append(low)
            low += 1
        else:
            permutation.append(high)
            high -= 1

    permutation.append(low)
    return permutation
