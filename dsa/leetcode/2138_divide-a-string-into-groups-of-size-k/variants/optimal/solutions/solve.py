def solve(s: str, k: int, fill: str) -> list[str]:
    groups = [s[start : start + k] for start in range(0, len(s), k)]
    groups[-1] += fill * (k - len(groups[-1]))
    return groups
