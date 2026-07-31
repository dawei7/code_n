from collections import Counter


def solve(s: str, t: str) -> str:
    need = Counter(t)
    missing = len(t)
    left = 0
    best_start = 0
    best_length = len(s) + 1

    for right, character in enumerate(s):
        if need[character] > 0:
            missing -= 1
        need[character] -= 1

        while missing == 0:
            length = right - left + 1
            if length < best_length:
                best_start, best_length = left, length
            outgoing = s[left]
            need[outgoing] += 1
            left += 1
            if need[outgoing] > 0:
                missing += 1

    if best_length > len(s):
        return ""
    return s[best_start : best_start + best_length]
