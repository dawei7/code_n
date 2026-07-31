"""Optimal app-local solution for LeetCode 844."""


def solve(s, t):
    def next_visible(text, index):
        skipped = 0
        while index >= 0:
            if text[index] == "#":
                skipped += 1
            elif skipped > 0:
                skipped -= 1
            else:
                break
            index -= 1
        return index

    left = len(s) - 1
    right = len(t) - 1

    while left >= 0 or right >= 0:
        left = next_visible(s, left)
        right = next_visible(t, right)
        if left < 0 or right < 0:
            return left == right
        if s[left] != t[right]:
            return False
        left -= 1
        right -= 1

    return True
