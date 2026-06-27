def solve(nums: list[int]) -> list[int]:
    n = len(nums)
    # dp[mask][last] stores the minimum cost to visit indices in mask, ending at last
    # Initialize with infinity
    dp = [[float('inf')] * n for _ in range(1 << n)]
    # parent[mask][last] stores the previous index to reconstruct the path
    parent = [[-1] * n for _ in range(1 << n)]
    
    # Base case: start at index 0
    dp[1][0] = 0
    
    for mask in range(1, 1 << n):
        for last in range(n):
            if dp[mask][last] == float('inf'):
                continue
            
            # Try moving to next index 'nxt'
            for nxt in range(n):
                if not (mask & (1 << nxt)):
                    new_mask = mask | (1 << nxt)
                    cost = abs(nums[last] - nxt)
                    if dp[new_mask][nxt] > dp[mask][last] + cost:
                        dp[new_mask][nxt] = dp[mask][last] + cost
                        parent[new_mask][nxt] = last
                    elif dp[new_mask][nxt] == dp[mask][last] + cost:
                        # Lexicographical requirement: 
                        # If costs are equal, we don't strictly need to update 
                        # because we reconstruct backwards or use a specific order.
                        pass
                        
    # Final step: add cost to return to index 0
    min_total_cost = float('inf')
    last_idx = -1
    full_mask = (1 << n) - 1
    
    for i in range(1, n):
        total = dp[full_mask][i] + abs(nums[i] - 0)
        if total < min_total_cost:
            min_total_cost = total
            last_idx = i
            
    # Reconstruct path
    res = []
    curr_mask = full_mask
    curr_idx = last_idx
    
    while curr_idx != -1:
        res.append(curr_idx)
        prev = parent[curr_mask][curr_idx]
        curr_mask ^= (1 << curr_idx)
        curr_idx = prev
        
    return res[::-1]
