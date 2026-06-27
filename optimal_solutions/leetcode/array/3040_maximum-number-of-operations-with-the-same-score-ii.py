from functools import lru_cache

def solve(nums: list[int]) -> int:
    n = len(nums)
    
    @lru_cache(None)
    def get_max_ops(i, j, target):
        if i >= j:
            return 0
        
        res = 0
        # Option 1: Remove two from the front
        if i + 1 <= j and nums[i] + nums[i + 1] == target:
            res = max(res, 1 + get_max_ops(i + 2, j, target))
        
        # Option 2: Remove two from the back
        if j - 1 >= i and nums[j] + nums[j - 1] == target:
            res = max(res, 1 + get_max_ops(i, j - 2, target))
            
        # Option 3: Remove one from front and one from back
        if i < j and nums[i] + nums[j] == target:
            res = max(res, 1 + get_max_ops(i + 1, j - 1, target))
            
        return res

    # The first operation determines the target sum.
    # There are three possible first operations:
    # 1. First two elements
    # 2. Last two elements
    # 3. First and last element
    
    ans1 = 1 + get_max_ops(2, n - 1, nums[0] + nums[1])
    ans2 = 1 + get_max_ops(0, n - 3, nums[n - 1] + nums[n - 2])
    ans3 = 1 + get_max_ops(1, n - 2, nums[0] + nums[n - 1])
    
    return max(ans1, ans2, ans3)
