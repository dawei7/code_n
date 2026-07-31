class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0

        prefix = [[0] * (n + 1) for _ in range(n)]
        for column in range(n):
            for row in range(n):
                prefix[column][row + 1] = prefix[column][row] + grid[row][column]

        heights = n + 1
        dp = [[0] * heights for _ in range(heights)]
        for left_height in range(heights):
            for right_height in range(heights):
                if right_height > left_height:
                    dp[left_height][right_height] = prefix[0][right_height] - prefix[0][left_height]

        for column in range(1, n - 1):
            next_dp = [[0] * heights for _ in range(heights)]
            column_prefix = prefix[column]

            for center_height in range(heights):
                prefix_best = [0] * heights
                running = 0
                for left_height in range(heights):
                    running = max(running, dp[left_height][center_height])
                    prefix_best[left_height] = running

                suffix_best = [0] * (heights + 1)
                running = 0
                for left_height in range(heights - 1, -1, -1):
                    gain = max(
                        0,
                        column_prefix[left_height] - column_prefix[center_height],
                    )
                    running = max(running, dp[left_height][center_height] + gain)
                    suffix_best[left_height] = running

                for right_height in range(heights):
                    right_gain = max(
                        0,
                        column_prefix[right_height] - column_prefix[center_height],
                    )
                    next_dp[center_height][right_height] = max(
                        prefix_best[right_height] + right_gain,
                        suffix_best[right_height + 1],
                    )

            dp = next_dp

        answer = 0
        last_prefix = prefix[-1]
        for left_height in range(heights):
            for last_height in range(heights):
                gain = max(0, last_prefix[left_height] - last_prefix[last_height])
                answer = max(answer, dp[left_height][last_height] + gain)
        return answer
