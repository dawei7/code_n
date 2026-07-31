def solve(s: str) -> int:
    return sum((123 - ord(ch)) * index for index, ch in enumerate(s, 1))
