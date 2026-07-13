def solve(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts = [0] * 26
    for left, right in zip(s, t):
        counts[ord(left) - ord("a")] += 1
        counts[ord(right) - ord("a")] -= 1
    return all(count == 0 for count in counts)
