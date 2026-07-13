def solve(s: str) -> int:
    last_seen: dict[str, int] = {}
    left = 0
    best = 0
    for right, char in enumerate(s):
        if char in last_seen:
            left = max(left, last_seen[char] + 1)
        last_seen[char] = right
        best = max(best, right - left + 1)
    return best
