import urllib.request


def solve() -> int:
    """Find minimal path sum from left column to right column moving UP, DOWN, RIGHT.
    
    Time Complexity: O(R * C)
    Space Complexity: O(R)
    """
    url = "https://projecteuler.net/resources/documents/0082_matrix.txt"
    with urllib.request.urlopen(url, timeout=5) as resp:
        text = resp.read().decode("utf-8")

    grid = [[int(x) for x in line.strip().split(",")] for line in text.strip().splitlines() if line.strip()]
    rows, cols = len(grid), len(grid[0])

    cost = [grid[r][0] for r in range(rows)]

    for c in range(1, cols):
        next_cost = [cost[r] + grid[r][c] for r in range(rows)]

        # Top-to-bottom relaxation
        for r in range(1, rows):
            next_cost[r] = min(next_cost[r], next_cost[r - 1] + grid[r][c])

        # Bottom-to-top relaxation
        for r in range(rows - 2, -1, -1):
            next_cost[r] = min(next_cost[r], next_cost[r + 1] + grid[r][c])

        cost = next_cost

    return min(cost)
