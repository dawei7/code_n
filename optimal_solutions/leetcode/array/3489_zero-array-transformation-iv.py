def solve(nums: list[int], queries: list[list[int]]) -> int:
    n = len(nums)
    
    def check(k: int) -> bool:
        # Create a difference array to track decrements
        diff = [0] * (n + 1)
        for i in range(k):
            l, r = queries[i]
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1
        
        current_decrements = 0
        for i in range(n):
            current_decrements += diff[i]
            if current_decrements < nums[i]:
                return False
        return True

    # Binary search for the minimum k in [0, len(queries)]
    low = 0
    high = len(queries)
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
