import os


def solve(filepath: str = "") -> int:
    """Find the maximum path sum from top to bottom in a 100-row triangle using dynamic programming.

    Mathematical Principles Applied:
    1. Bottom-Up Dynamic Programming Recurrence:
       Let T[r][c] be the cell value at row r, column c (0 <= c <= r < R).
       Define DP[r][c] as the maximum path sum starting at cell (r, c) down to the bottom.
       Base case at bottom row (r = R - 1): DP[R-1][c] = T[R-1][c].
       Recurrence relation moving upwards from r = R - 2 down to 0:
       DP[r][c] = T[r][c] + max(DP[r+1][c], DP[r+1][c+1])

    2. Single Matrix Collapse:
       By updating grid[r][c] in-place bottom-up, grid[0][0] accumulates the global maximum path sum.

    Time Complexity: O(R^2) where R = 100 rows (5,050 additions, executes in ~0.002s).
    Space Complexity: O(R^2) memory for grid matrix.
    """
    if not filepath:
        # Navigate 4 levels up from solution.py to reach package root (0067_maximum-path-sum-ii/)
        sol_dir = os.path.dirname(os.path.abspath(__file__))
        pkg_dir = os.path.abspath(os.path.join(sol_dir, "..", "..", ".."))
        filepath = os.path.join(pkg_dir, "triangle.txt")

    # Read triangle text file
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Parse 100-row integer triangle matrix
    grid = [
        [int(x) for x in line.strip().split()]
        for line in text.strip().splitlines()
        if line.strip()
    ]

    # Process rows bottom-up from row R-2 down to 0
    for r in range(len(grid) - 2, -1, -1):
        for c in range(len(grid[r])):
            # In-place DP update: add maximum of the two adjacent children in the row below
            grid[r][c] += max(grid[r + 1][c], grid[r + 1][c + 1])

    # Return global maximum path sum accumulated at the apex grid[0][0]
    return grid[0][0]


if __name__ == "__main__":
    print(solve())
