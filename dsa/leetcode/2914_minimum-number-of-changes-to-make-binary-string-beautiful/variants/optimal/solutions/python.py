def solve(s: str) -> int:
    return sum(s[index] != s[index + 1] for index in range(0, len(s), 2))
