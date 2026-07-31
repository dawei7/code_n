def solve(s: str) -> str:
    ones = s.count("1")
    zeros = len(s) - ones
    return "1" * (ones - 1) + "0" * zeros + "1"
