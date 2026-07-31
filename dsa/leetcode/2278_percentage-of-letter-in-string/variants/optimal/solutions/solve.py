def solve(s: str, letter: str) -> int:
    return s.count(letter) * 100 // len(s)
