from collections import Counter

def solve(nums: list[int]) -> int:
    """
    Counts the number of complete subarrays using a sliding window approach.
    A subarray is complete if it contains all unique elements present in the original array.
    """
    total_unique_count = len(set(nums))
    n = len(nums)
    
    count = 0
    left = 0
    window_map = {}
    
    # Expand the right boundary of the window
    for right in range(n):
        window_map[nums[right]] = window_map.get(nums[right], 0) + 1
        
        # While the current window contains all unique elements,
        # all subarrays starting from 'left' to 'right' and ending at 'right'
        # are complete.
        while len(window_map) == total_unique_count:
            # If the window [left, right] is valid, then all subarrays
            # [left, right], [left+1, right], ..., [right, right] are valid.
            # There are (n - right) such subarrays.
            count += (n - right)
            
            # Shrink the window from the left
            window_map[nums[left]] -= 1
            if window_map[nums[left]] == 0:
                del window_map[nums[left]]
            left += 1
            
    return count
