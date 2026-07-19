"""Optimal app-local solution for LeetCode 1119."""


def solve(s):
    vowels = {"a", "e", "i", "o", "u"}
    return "".join(character for character in s if character not in vowels)
