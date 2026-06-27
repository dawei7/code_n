from typing import List

def solve(nums: List[int], k: int) -> int:
    """
    Calculates the minimum operations to make the median of nums equal to k.
    """
    nums.sort()
    n = len(nums)
    mid = n // 2
    
    operations = 0
    
    # If the current median is less than k, we need to increase the median
    # and potentially elements to the right of the median.
    if nums[mid] < k:
        for i in range(mid, n):
            if nums[i] < k:
                operations += (k - nums[i])
            else:
                # Since the array is sorted, if nums[i] >= k, 
                # no further elements need to be increased.
                break
    
    # If the current median is greater than k, we need to decrease the median
    # and potentially elements to the left of the median.
    elif nums[mid] > k:
        for i in range(mid, -1, -1):
            if nums[i] > k:
                operations += (nums[i] - k)
            else:
                # Since the array is sorted, if nums[i] <= k, 
                # no further elements need to be decreased.
                break
                
    return operations
