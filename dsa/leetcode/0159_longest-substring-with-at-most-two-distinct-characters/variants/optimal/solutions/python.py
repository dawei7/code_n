def solve(s: str) -> int:
    counts: dict[str, int] = {}
    left = 0
    best = 0
    for right, character in enumerate(s):
        counts[character] = counts.get(character, 0) + 1
        while len(counts) > 2:
            removed = s[left]
            counts[removed] -= 1
            if counts[removed] == 0:
                del counts[removed]
            left += 1
        best = max(best, right - left + 1)
    return best
