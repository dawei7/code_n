class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        divisors = [[] for _ in range(n + 1)]
        for divisor in range(1, n):
            for length in range(divisor * 2, n + 1, divisor):
                divisors[length].append(divisor)

        repair = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            repetitions = [(d, length // d) for d in divisors[length]]
            for start in range(n - length + 1):
                best = length
                for divisor, group_length in repetitions:
                    changes = 0
                    for offset in range(divisor):
                        left = start + offset
                        right = left + (group_length - 1) * divisor
                        while left < right:
                            changes += s[left] != s[right]
                            left += divisor
                            right -= divisor
                    best = min(best, changes)
                repair[start][start + length - 1] = best

        infinity = n + 1
        dp = [[infinity] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for end in range(parts * 2, n + 1):
                for split in range((parts - 1) * 2, end - 1):
                    dp[parts][end] = min(
                        dp[parts][end],
                        dp[parts - 1][split] + repair[split][end - 1],
                    )

        return dp[k][n]
