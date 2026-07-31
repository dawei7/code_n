def solve(m: int, n: int) -> int:
    total_moves = m + n - 2
    selected_moves = min(m - 1, n - 1)
    paths = 1
    for count in range(1, selected_moves + 1):
        paths = paths * (total_moves - selected_moves + count) // count
    return paths
