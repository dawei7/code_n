from typing import List

def solve(nums: List[int], k: int) -> int:
    """
    Finds the minimum capability using binary search on the answer.
    """
    def can_pick(max_val: int, k: int, nums: List[int]) -> bool:
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] <= max_val:
                count += 1
                i += 2  # Skip adjacent house
            else:
                i += 1
        return count >= k

    low = min(nums)
    high = max(nums)
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if can_pick(mid, k, nums):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
