def solve(n: int, edges: list[list[int]]) -> int:
    path_score = n * (n + 1) * (2 * n + 1) // 6 - 2 * n + 1
    return path_score + (2 if len(edges) == n else 0)
