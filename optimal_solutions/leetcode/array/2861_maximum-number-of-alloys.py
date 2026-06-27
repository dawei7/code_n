from typing import List

def solve(n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
    def can_produce(alloy_idx: int, count: int) -> bool:
        needed_budget = 0
        for j in range(n):
            required = composition[alloy_idx][j] * count
            if required > stock[j]:
                needed_budget += (required - stock[j]) * cost[j]
            if needed_budget > budget:
                return False
        return needed_budget <= budget

    max_alloys = 0
    # The upper bound is budget + max(stock) because even if cost is 1, 
    # we can't exceed total resources. 2*10^9 is a safe upper bound.
    low = 0
    high = 2 * 10**9 
    
    ans = 0
    for i in range(k):
        l, r = 0, high
        best_for_alloy = 0
        while l <= r:
            mid = (l + r) // 2
            if can_produce(i, mid):
                best_for_alloy = mid
                l = mid + 1
            else:
                r = mid - 1
        ans = max(ans, best_for_alloy)
        
    return ans
