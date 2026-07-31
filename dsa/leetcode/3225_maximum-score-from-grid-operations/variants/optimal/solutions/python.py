def solve(grid: list[list[int]]) -> int:
    n = len(grid)
    if n == 1:
        return 0
    prefix = [[0] * (n + 1) for _ in range(n)]
    for column in range(n):
        for row in range(n):
            prefix[column][row + 1] = prefix[column][row] + grid[row][column]

    heights = n + 1
    dp = [[0] * heights for _ in range(heights)]
    for left in range(heights):
        for right in range(heights):
            dp[left][right] = max(0, prefix[0][right] - prefix[0][left])

    for column in range(1, n - 1):
        next_dp = [[0] * heights for _ in range(heights)]
        values = prefix[column]
        for center in range(heights):
            prefix_best = [0] * heights
            running = 0
            for left in range(heights):
                running = max(running, dp[left][center])
                prefix_best[left] = running
            suffix_best = [0] * (heights + 1)
            running = 0
            for left in range(heights - 1, -1, -1):
                gain = max(0, values[left] - values[center])
                running = max(running, dp[left][center] + gain)
                suffix_best[left] = running
            for right in range(heights):
                gain = max(0, values[right] - values[center])
                next_dp[center][right] = max(
                    prefix_best[right] + gain,
                    suffix_best[right + 1],
                )
        dp = next_dp

    answer = 0
    for left in range(heights):
        for center in range(heights):
            answer = max(
                answer,
                dp[left][center] + max(0, prefix[-1][left] - prefix[-1][center]),
            )
    return answer
