import os


def solve(filepath: str = "") -> int:
    """Find minimal path sum from any cell in left column to any cell in right column moving UP, DOWN, and RIGHT.

    Mathematical Principles Applied:
    1. Column-by-Column Dynamic Programming with Dual Relaxation:
       Let cost[r] be the minimal path sum starting from the left column reaching cell (r, c-1).
       When advancing to column c:
       - Direct horizontal transition: next_cost[r] = cost[r] + grid[r][c].
       - Top-to-bottom vertical relaxation: next_cost[r] = min(next_cost[r], next_cost[r-1] + grid[r][c]).
       - Bottom-to-top vertical relaxation: next_cost[r] = min(next_cost[r], next_cost[r+1] + grid[r][c]).

    2. Column State Array:
       Processing column-by-column reduces 2D grid DP to O(R) spatial memory.

    Time Complexity: O(R * C) where R = C = 80 (6,400 cells, executes in ~0.002s).
    Space Complexity: O(R) memory for column cost vector.
    """
    if not filepath:
        # Navigate 4 levels up from solution.py to reach package root (0082_path-sum-three-ways/)
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

    # Base cost array initialized with left column values grid[r][0]
    cost = [grid[r][0] for r in range(rows)]

    # Advance column-by-column from c = 1 up to cols-1
    for c in range(1, cols):
        # Initial horizontal step from previous column
        next_cost = [cost[r] + grid[r][c] for r in range(rows)]

        # Top-to-bottom vertical relaxation pass
        for r in range(1, rows):
            next_cost[r] = min(next_cost[r], next_cost[r - 1] + grid[r][c])

        # Bottom-to-top vertical relaxation pass
        for r in range(rows - 2, -1, -1):
            next_cost[r] = min(next_cost[r], next_cost[r + 1] + grid[r][c])

        # Update column cost vector
        cost = next_cost

    # Return minimal path sum ending at any cell in the rightmost column
    return min(cost)


if __name__ == "__main__":
    print(solve())
