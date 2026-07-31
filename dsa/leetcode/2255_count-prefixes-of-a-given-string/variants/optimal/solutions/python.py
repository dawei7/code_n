def solve(words: list[str], s: str) -> int:
    return sum(s.startswith(word) for word in words)
