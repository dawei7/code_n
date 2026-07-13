from typing import List

def solve(nums: List[int], x: int) -> int:
    n = len(nums)
    # min_costs[i] will store the minimum cost to collect chocolate i so far
    min_costs = list(nums)
    ans = sum(min_costs)
    
    # Enumerate the number of operations k from 1 to n - 1
    for k in range(1, n):
        for i in range(n):
            # Python's negative indexing automatically handles (i - k) % n
            if nums[i - k] < min_costs[i]:
                min_costs[i] = nums[i - k]
        
        # Calculate the total cost with k operations
        ans = min(ans, k * x + sum(min_costs))
        
    return ans
