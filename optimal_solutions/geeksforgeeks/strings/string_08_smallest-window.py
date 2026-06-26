"""Optimal solution for string_08: Smallest Window.

Sliding window: smallest substring of s containing all chars of p.
"""


def solve(s, p):
    n = len(s)
    if not p or not s:
        return ""
    need = set(p)
    best = ""
    left = 0
    have = set()
    for right in range(n):
        if s[right] in need:
            have.add(s[right])
        while True:
            # Check if we have everything in the current window.
            covered = all((c in have) for c in need) if have else False
            if not covered or left > right:
                break
            window = s[left:right + 1]
            if not best or len(window) < len(best):
                best = window
            if s[left] in need:
                pass
            left += 1
            have = set()
            for k in range(left, right + 1):
                if s[k] in need:
                    have.add(s[k])
    return best
