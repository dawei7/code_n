"""Optimal app-local solution for LeetCode 1100."""


def solve(s: str, k: int) -> int:
    if k > len(s) or k > 26:
        return 0

    frequencies: dict[str, int] = {}
    valid_windows = 0
    for right, character in enumerate(s):
        frequencies[character] = frequencies.get(character, 0) + 1
        if right >= k:
            outgoing = s[right - k]
            frequencies[outgoing] -= 1
            if frequencies[outgoing] == 0:
                del frequencies[outgoing]
        if right >= k - 1 and len(frequencies) == k:
            valid_windows += 1
    return valid_windows
