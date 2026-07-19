def solve(original: list[int], m: int, n: int) -> list[list[int]]:
    if len(original) != m * n:
        return []
    return [original[start : start + n] for start in range(0, len(original), n)]
