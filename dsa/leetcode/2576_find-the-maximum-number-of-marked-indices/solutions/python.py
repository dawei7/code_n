from typing import List

def solve(nums: List[int]) -> int:
    """
    Finds the maximum number of marked indices using a greedy two-pointer approach.
    """
    nums.sort()
    n = len(nums)
    
    # We split the array into two halves. The first half contains potential 
    # 'small' elements, and the second half contains potential 'large' elements.
    # We try to match the smallest possible 'small' with the smallest possible 'large'.
    
    left = 0
    right = n // 2
    marked_count = 0
    
    while left < n // 2 and right < n:
        if 2 * nums[left] <= nums[right]:
            # Found a valid pair
            marked_count += 2
            left += 1
            right += 1
        else:
            # Current 'large' is too small, move to the next larger element
            right += 1
            
    return marked_count
