from collections import deque

def solve(nums: list[int]) -> int:
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    # dp[i] is the max length of non-decreasing array ending at index i-1
    dp = [0] * (n + 1)
    # last[i] is the minimum value of the last element of the non-decreasing array of length dp[i]
    last = [0] * (n + 1)
    
    # queue stores indices j such that we can transition from j to i
    # We want to maintain a monotonic property to optimize the search
    queue = deque([0])
    
    for i in range(1, n + 1):
        # Remove indices from the front that cannot satisfy the non-decreasing condition
        while len(queue) >= 2 and last[queue[1]] <= prefix_sum[i] - prefix_sum[queue[1]]:
            queue.popleft()
        
        # The best previous index is at the front of the queue
        j = queue[0]
        dp[i] = dp[j] + 1
        last[i] = prefix_sum[i] - prefix_sum[j]
        
        # Maintain the monotonic property of the queue
        # We want to keep the queue such that dp[i] is non-decreasing and last[i] is non-decreasing
        while queue and (dp[i] < dp[queue[-1]] or (dp[i] == dp[queue[-1]] and last[i] <= last[queue[-1]])):
            queue.pop()
        queue.append(i)
        
    return dp[n]
