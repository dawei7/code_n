def solve(nums: list[int], queries: list[list[int]]) -> int:
    n = len(nums)
    q_len = len(queries)

    def check(k: int) -> bool:
        # Create a difference array to apply range subtractions
        diff = [0] * (n + 1)
        for i in range(k):
            l, r, val = queries[i]
            diff[l] += val
            if r + 1 < n:
                diff[r + 1] -= val
        
        current_reduction = 0
        for i in range(n):
            current_reduction += diff[i]
            if nums[i] - current_reduction > 0:
                return False
        return True

    # Binary search for the minimum k in range [0, q_len]
    low = 0
    high = q_len
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
