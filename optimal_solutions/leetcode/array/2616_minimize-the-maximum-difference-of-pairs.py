from typing import List

def solve(nums: List[int], p: int) -> int:
    if p == 0:
        return 0
    
    nums.sort()
    n = len(nums)
    
    def can_form_pairs(threshold: int) -> bool:
        count = 0
        i = 0
        while i < n - 1:
            if nums[i + 1] - nums[i] <= threshold:
                count += 1
                i += 2
            else:
                i += 1
            if count >= p:
                return True
        return count >= p

    low = 0
    high = nums[-1] - nums[0]
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        if can_form_pairs(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
