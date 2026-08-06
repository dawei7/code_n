"""Proposed app-local solution for LeetCode 395."""


def solve(s: str, k: int) -> int:
    best = 0
    base = ord("a")

    for target_unique in range(1, len(set(s)) + 1):
        counts = [0] * 26
        left = 0
        unique = 0
        qualified = 0

        for right, character in enumerate(s):
            i = ord(character) - base
            if counts[i] == 0:
                unique += 1
            counts[i] += 1
            if counts[i] == k:
                qualified += 1

            while unique > target_unique:
                j = ord(s[left]) - base
                if counts[j] == k:
                    qualified -= 1
                counts[j] -= 1
                if counts[j] == 0:
                    unique -= 1
                left += 1

            if unique == target_unique == qualified:
                best = max(best, right - left + 1)

    return best
