def solve() -> int:
    """Find the maximum path sum from top to bottom in a 15-row number triangle.

    Mathematical Principles Applied:
    1. Bellman's Principle of Optimality (Bottom-Up Dynamic Programming):
       For a triangle T with R rows, let DP[r][c] be the maximum path sum starting at cell (r, c)
       and moving down to the base (row R - 1).
       Recurrence relation:
       DP[r][c] = T[r][c] + max(DP[r+1][c], DP[r+1][c+1])

    2. Bottom-Up Reduction:
       By iterating rows from R - 2 upwards to 0 (bottom-to-top), each row r updates in-place.
       Upon reaching row 0, DP[0][0] holds the exact global maximum path sum.

    Time Complexity: O(R^2) where R = 15 rows (120 cells total).
    Space Complexity: O(R^2) to store triangle array.
    """
    triangle_str = """
    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    """

    # Parse 15-row triangle string into a 2D ragged integer list
    grid = [[int(x) for x in line.split()] for line in triangle_str.strip().splitlines() if line.strip()]

    # Execute bottom-up dynamic programming pass from row R - 2 down to row 0
    for r in range(len(grid) - 2, -1, -1):
        for c in range(len(grid[r])):
            # Each cell accumulates its value + max of its two adjacent children in the row below
            grid[r][c] += max(grid[r + 1][c], grid[r + 1][c + 1])

    # The apex cell grid[0][0] contains the global maximum path sum
    return grid[0][0]


if __name__ == "__main__":
    print(solve())
