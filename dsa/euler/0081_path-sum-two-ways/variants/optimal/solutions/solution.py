import os


def solve(filepath: str = "") -> int:
    """Find the minimal path sum from top-left to bottom-right in an 80x80 matrix moving only right and down.

    Mathematical Principles Applied:
    1. 2D Grid Path Dynamic Programming:
       Let T[r][c] be the cell value at row r, column c.
       Define DP[r][c] as the minimal path sum from top-left (0,0) to cell (r, c).
       Recurrence relation:
       DP[0][0] = T[0][0]
       DP[0][c] = T[0][c] + DP[0][c-1]  (first row)
       DP[r][0] = T[r][0] + DP[r-1][0]  (first column)
       DP[r][c] = T[r][c] + min(DP[r-1][c], DP[r][c-1])  for r, c > 0.

    2. In-Place Matrix Update:
       Update grid[r][c] in-place, yielding minimal path sum at grid[-1][-1].

    Time Complexity: O(R * C) where R = C = 80 (6,400 cells, executes in ~0.001s).
    Space Complexity: O(R * C) memory for matrix.
    """
    if not filepath:
        # Navigate 4 levels up from solution.py to reach package root (0081_path-sum-two-ways/)
        sol_dir = os.path.dirname(os.path.abspath(__file__))
        pkg_dir = os.path.abspath(os.path.join(sol_dir, "..", "..", ".."))
        filepath = os.path.join(pkg_dir, "matrix.txt")

    # Read matrix text file
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Parse 80x80 matrix grid
    grid = [
        [int(x) for x in line.strip().split(",")]
        for line in text.strip().splitlines()
        if line.strip()
    ]
    rows, cols = len(grid), len(grid[0])

    # Initialize first row cumulative sums
    for c in range(1, cols):
        grid[0][c] += grid[0][c - 1]

    # Initialize first column cumulative sums
    for r in range(1, rows):
        grid[r][0] += grid[r - 1][0]

    # Fill 2D DP matrix for r > 0 and c > 0
    for r in range(1, rows):
        for c in range(1, cols):
            # Minimal path arriving at (r, c) from top (r-1, c) or left (r, c-1)
            grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

    # Return minimal path sum at bottom-right cell
    return grid[-1][-1]


if __name__ == "__main__":
    print(solve())
