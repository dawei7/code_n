import functools

def solve(nums: list[int], andValues: list[int]) -> int:
    n = len(nums)
    m = len(andValues)
    inf = float('inf')

    @functools.lru_cache(None)
    def dp(i, j, current_and):
        # Base cases
        if j == m:
            return 0 if i == n else inf
        if i == n:
            return inf
        
        # Update current_and with the current element
        new_and = current_and & nums[i]
        
        # Pruning: if new_and is already smaller than the target, this path is invalid
        if (new_and & andValues[j]) != andValues[j]:
            return inf
        
        # Option 1: Continue the current subarray
        res = dp(i + 1, j, new_and)
        
        # Option 2: End the current subarray here if it matches the target
        if new_and == andValues[j]:
            res_end = dp(i + 1, j + 1, -1)
            if res_end != inf:
                res = min(res, nums[i] + res_end)
                
        return res

    # Initial call: -1 acts as a mask of all 1s (identity for AND)
    result = dp(0, 0, -1)
    return int(result) if result != inf else -1
