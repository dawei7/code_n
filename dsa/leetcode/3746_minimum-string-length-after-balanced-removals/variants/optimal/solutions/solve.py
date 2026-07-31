def solve(s: str) -> int:
    count_a = s.count("a")
    return abs(2 * count_a - len(s))
