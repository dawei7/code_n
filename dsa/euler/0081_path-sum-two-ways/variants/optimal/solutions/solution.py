import urllib.request


def solve() -> int:
    """Find minimal path sum from top-left to bottom-right in an 80x80 matrix moving right and down.
    
    Time Complexity: O(R * C)
    Space Complexity: O(R * C)
    """
    url = "https://projecteuler.net/resources/documents/0081_matrix.txt"
    with urllib.request.urlopen(url, timeout=5) as resp:
        text = resp.read().decode("utf-8")

    grid = [[int(x) for x in line.strip().split(",")] for line in text.strip().splitlines() if line.strip()]
    rows, cols = len(grid), len(grid[0])

    for c in range(1, cols):
        grid[0][c] += grid[0][c - 1]
    for r in range(1, rows):
        grid[r][0] += grid[r - 1][0]

    for r in range(1, rows):
        for c in range(1, cols):
            grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

    return grid[-1][-1]
