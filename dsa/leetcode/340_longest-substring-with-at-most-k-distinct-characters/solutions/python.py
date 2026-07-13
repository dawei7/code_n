def solve(s: str, k: int) -> int:
    if k <= 0:
        return 0

    counts: dict[str, int] = {}
    left = 0
    best = 0

    for right, character in enumerate(s):
        counts[character] = counts.get(character, 0) + 1
        while len(counts) > k:
            left_character = s[left]
            counts[left_character] -= 1
            if counts[left_character] == 0:
                del counts[left_character]
            left += 1
        best = max(best, right - left + 1)

    return best
