def solve(nums: list[int], k: int) -> int:
    """
    Finds the maximum beauty of the array after applying the operation.
    
    The beauty is the maximum number of elements that can be made equal.
    This is equivalent to finding the longest subarray in the sorted version
    of nums where the difference between the maximum and minimum elements 
    is at most 2 * k.
    """
    nums.sort()
    left = 0
    
    # Non-shrinking sliding window
    for right in range(len(nums)):
        if nums[right] - nums[left] > 2 * k:
            left += 1
            
    return len(nums) - left
