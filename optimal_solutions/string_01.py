"""Optimal solution for string_01: Anagram Check.

Check whether two strings are anagrams (same character counts).
"""


def solve(s, t):
    return sorted(s) == sorted(t)
