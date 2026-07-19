from typing import List

def solve(nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    if n == 0:
        return 0
    
    # dp1: length of non-decreasing subarray ending at index i using nums1[i]
    # dp2: length of non-decreasing subarray ending at index i using nums2[i]
    dp1 = 1
    dp2 = 1
    max_len = 1
    
    for i in range(1, n):
        # Calculate potential new lengths for index i
        # We can extend from either nums1[i-1] or nums2[i-1]
        new_dp1 = 1
        new_dp2 = 1
        
        if nums1[i] >= nums1[i-1]:
            new_dp1 = max(new_dp1, dp1 + 1)
        if nums1[i] >= nums2[i-1]:
            new_dp1 = max(new_dp1, dp2 + 1)
            
        if nums2[i] >= nums1[i-1]:
            new_dp2 = max(new_dp2, dp1 + 1)
        if nums2[i] >= nums2[i-1]:
            new_dp2 = max(new_dp2, dp2 + 1)
            
        dp1, dp2 = new_dp1, new_dp2
        max_len = max(max_len, dp1, dp2)
        
    return max_len
