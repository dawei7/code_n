from collections import deque

def solve(prices: list[int]) -> int:
    n = len(prices)
    # dp[i] will store the minimum cost to acquire all fruits up to index i (1-indexed)
    # We use 1-based indexing for convenience: dp[i] corresponds to prices[i-1]
    dp = [0] * (n + 1)
    
    # Monotonic queue stores indices j such that dp[j] is increasing
    # We want to find min(dp[j]) in the range [ceil(i/2), i]
    dq = deque()
    
    for i in range(1, n + 1):
        # The fruit at index i (prices[i-1]) can cover fruits from i+1 to 2*i
        # To calculate dp[i], we look at the previous state j where j + (j) >= i
        # which simplifies to 2*j >= i, or j >= ceil(i/2)
        
        # Remove indices that are out of the valid range [ceil(i/2), i-1]
        while dq and dq[0] < (i + 1) // 2 - 1:
            dq.popleft()
            
        # The current dp[i] is the cost of the current fruit + min cost of previous state
        # If i=1, we just pay prices[0]. Otherwise, we add the min from the queue.
        prev_min = dp[dq[0]] if dq else 0
        dp[i] = prices[i - 1] + prev_min
        
        # Maintain monotonic property: remove elements larger than current dp[i]
        while dq and dp[dq[-1]] >= dp[i]:
            dq.pop()
        dq.append(i)
        
    # The answer is the minimum cost to cover all fruits from n/2 + 1 to n
    # Any fruit bought in this range will cover the rest of the fruits.
    ans = float('inf')
    for i in range((n + 1) // 2, n + 1):
        ans = min(ans, dp[i])
        
    return ans
