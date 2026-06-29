


def solve():
    class Solution:
        def __init__(self):
            self.paths = []
            self.visited = []

        def is_valid(self, x, y, n, grid):
            return (
                0 <= x < n and 0 <= y < n and 
                grid[x][y] == 1 and 
                self.visited[x][y] == 0
            )

        def dfs(self, x, y, n, grid, path):
            if x == n - 1 and y == n - 1:
                self.paths.append(path)
                return

            self.visited[x][y] = 1

            # Down
            if self.is_valid(x + 1, y, n, grid):
                self.dfs(x + 1, y, n, grid, path + "D")

            # Left
            if self.is_valid(x, y - 1, n, grid):
                self.dfs(x, y - 1, n, grid, path + "L")

            # Right
            if self.is_valid(x, y + 1, n, grid):
                self.dfs(x, y + 1, n, grid, path + "R")

            # Up
            if self.is_valid(x - 1, y, n, grid):
                self.dfs(x - 1, y, n, grid, path + "U")

            self.visited[x][y] = 0  # backtrack

        def findAllPaths(self, n, grid):
            self.paths = []

            if grid[0][0] == 0:
                return []

            self.visited = [[0] * n for _ in range(n)]
            self.dfs(0, 0, n, grid, "")

            return self.paths


if __name__ == "__main__":
    solve()
