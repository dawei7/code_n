from typing import List

def solve(nums: List[int]) -> int:
    n = len(nums)
    
    # Find the longest strictly increasing prefix
    left = 0
    while left + 1 < n and nums[left] < nums[left + 1]:
        left += 1
    
    # If the whole array is strictly increasing
    if left == n - 1:
        return n * (n + 1) // 2
    
    # Find the longest strictly increasing suffix
    right = n - 1
    while right - 1 >= 0 and nums[right - 1] < nums[right]:
        right -= 1
        
    # Count subarrays:
    # 1. Removing everything after the prefix (left + 1 subarrays)
    # 2. Removing everything before the suffix (n - right subarrays)
    # 3. Removing a middle part that connects a prefix ending at i and suffix starting at j
    count = (left + 1) + (n - right + 1)
    
    # Check combinations of prefix [0...i] and suffix [j...n-1]
    # where nums[i] < nums[j]
    j = right
    for i in range(left + 1):
        while j < n and nums[j] <= nums[i]:
            j += 1
        # All suffixes starting from j to n-1 are valid
        count += (n - j + 1)
        
    return count
