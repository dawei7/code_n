"""Optimal solution for backtrack_04: Word Break.

Given a string s and a list of dictionary words, return True
iff s can be segmented into a sequence of one or more dict
words. Backtracking: at each step, try each dict word as a
prefix; recurse on the remaining suffix.
"""


def solve(s, dictionary, n):
    if n == 0:
        return True

    def helper(remaining):
        if not remaining:
            return True
        for word in dictionary:
            if remaining.startswith(word) and helper(remaining[len(word):]):
                return True
        return False

    return helper(s)
