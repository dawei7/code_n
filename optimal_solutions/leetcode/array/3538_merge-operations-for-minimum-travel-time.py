def solve(nums: list[int]) -> int:
    """
    To make the array non-decreasing with minimum merges, we process the array
    from right to left. We keep track of the value of the current segment 
    (the rightmost segment of the suffix we are considering) and ensure that 
    the segment to its left is smaller than or equal to it.
    """
    n = len(nums)
    if n <= 1:
        return 0
    
    merges = 0
    # current_val represents the value of the segment we are currently comparing against
    current_val = nums[-1]
    # current_sum represents the sum of the segment we are currently building
    current_sum = 0
    
    # Iterate backwards from the second to last element
    for i in range(n - 2, -1, -1):
        current_sum += nums[i]
        
        if current_sum <= current_val:
            # We found a valid segment, update current_val and reset current_sum
            current_val = current_sum
            current_sum = 0
        else:
            # We must merge the current element with the next one
            merges += 1
            
    return merges
