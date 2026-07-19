from typing import List

def solve(nums: List[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    
    # Precompute divisibility relations to optimize transitions
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    adj[i].append(j)
                    
    # memo[mask][last_idx] stores the number of valid ways to complete
    # the permutation given the current mask of visited elements and the last visited index.
    memo = [[-1] * n for _ in range(1 << n)]
    target_mask = (1 << n) - 1
    
    def dp(mask: int, last_idx: int) -> int:
        if mask == target_mask:
            return 1
        if memo[mask][last_idx] != -1:
            return memo[mask][last_idx]
        
        ans = 0
        for nxt in adj[last_idx]:
            if not (mask & (1 << nxt)):
                ans = (ans + dp(mask | (1 << nxt), nxt)) % MOD
                
        memo[mask][last_idx] = ans
        return ans

    total_permutations = 0
    # Start the permutation with each element as the first element
    for i in range(n):
        total_permutations = (total_permutations + dp(1 << i, i)) % MOD
        
    return total_permutations
