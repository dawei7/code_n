from typing import List

def solve(nums: List[int], target: int) -> int:
    """
    Counts the number of pairs (i, j) such that i < j and nums[i] + nums[j] < target.
    Uses sorting and the two-pointer technique for O(n log n) efficiency.
    """
    nums.sort()
    count = 0
    left = 0
    right = len(nums) - 1
    
    while left < right:
        if nums[left] + nums[right] < target:
            # If the sum of elements at left and right is less than target,
            # then all elements between left and right will also satisfy
            # the condition when paired with nums[left].
            count += (right - left)
            left += 1
        else:
            # Sum is too large, move the right pointer to decrease the sum.
            right -= 1
            
    return count
