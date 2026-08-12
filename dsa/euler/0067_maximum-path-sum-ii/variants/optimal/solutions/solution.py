import urllib.request


def solve() -> int:
    """Find maximum path sum from top to bottom in a 100-row triangle using DP.
    
    Time Complexity: O(R^2)
    Space Complexity: O(R^2)
    """
    url = "https://projecteuler.net/resources/documents/0067_triangle.txt"
    with urllib.request.urlopen(url, timeout=5) as resp:
        text = resp.read().decode("utf-8")

    grid = [[int(x) for x in line.strip().split()] for line in text.strip().splitlines() if line.strip()]

    for r in range(len(grid) - 2, -1, -1):
        for c in range(len(grid[r])):
            grid[r][c] += max(grid[r + 1][c], grid[r + 1][c + 1])

    return grid[0][0]
