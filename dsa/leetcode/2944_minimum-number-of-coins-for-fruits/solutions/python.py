import heapq

def solve(prices: list[int]) -> int:
    n = len(prices)
    dp = [0] * (n + 1)
    candidates = [(0, n)]

    for i in range(n - 1, -1, -1):
        right = min(n, 2 * i + 2)
        while candidates and candidates[0][1] > right:
            heapq.heappop(candidates)
        dp[i] = prices[i] + candidates[0][0]
        heapq.heappush(candidates, (dp[i], i))

    return dp[0]
