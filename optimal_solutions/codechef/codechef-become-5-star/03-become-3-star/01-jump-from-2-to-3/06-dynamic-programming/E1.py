def solve(i, j, n, grid, dp):
    if i < 1 or j < 1 or i > n or (j > n):
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = (1 if grid[i][j] == 'P' else 0) + max(solve(i - 1, j + 2, n, grid, dp), solve(i + 1, j + 2, n, grid, dp), solve(i - 2, j + 1, n, grid, dp), solve(i + 2, j + 1, n, grid, dp))
    return dp[i][j]

def main():
    a = int(input())
    for _ in range(a):
        n = int(input())
        grid = [[''] * (n + 1) for _ in range(n + 1)]
        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        start_i, start_j = (-1, -1)
        for i in range(1, n + 1):
            row = input()
            for j in range(1, n + 1):
                grid[i][j] = row[j - 1]
                if grid[i][j] == 'K':
                    start_i, start_j = (i, j)
        print(solve(start_i, start_j, n, grid, dp))


if __name__ == "__main__":
    solve()
