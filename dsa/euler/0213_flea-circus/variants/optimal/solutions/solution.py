def solve(n: int = 30, steps: int = 50) -> str:
    """Find expected number of unoccupied squares after `steps` bell rings on an n x n grid.
    
    Time Complexity: O(n^4 * steps)
    Space Complexity: O(n^4)
    """
    N = n
    neighbors = {}
    for r in range(N):
        for c in range(N):
            nbrs = []
            if r > 0:
                nbrs.append((r - 1, c))
            if r < N - 1:
                nbrs.append((r + 1, c))
            if c > 0:
                nbrs.append((r, c - 1))
            if c < N - 1:
                nbrs.append((r, c + 1))
            neighbors[(r, c)] = nbrs

    def get_flea_dist(r0, c0):
        grid = [[0.0] * N for _ in range(N)]
        grid[r0][c0] = 1.0

        for step in range(steps):
            next_grid = [[0.0] * N for _ in range(N)]
            for r in range(N):
                for c in range(N):
                    val = grid[r][c]
                    if val > 0:
                        nbrs = neighbors[(r, c)]
                        prob = val / len(nbrs)
                        for nr, nc in nbrs:
                            next_grid[nr][nc] += prob
            grid = next_grid
        return grid

    flea_dists = {}
    for r0 in range(N):
        for c0 in range(N):
            flea_dists[(r0, c0)] = get_flea_dist(r0, c0)

    expected_empty = 0.0
    for r in range(N):
        for c in range(N):
            prob_empty = 1.0
            for r0 in range(N):
                for c0 in range(N):
                    prob_empty *= 1.0 - flea_dists[(r0, c0)][r][c]
            expected_empty += prob_empty

    return f"{expected_empty:.6f}"
