"""Optimal app-local solution for LeetCode 1422."""


def solve(s: str) -> int:
    left_zeros = 0
    right_ones = s.count("1")
    best = 0
    for character in s[:-1]:
        if character == "0":
            left_zeros += 1
        else:
            right_ones -= 1
        best = max(best, left_zeros + right_ones)
    return best
