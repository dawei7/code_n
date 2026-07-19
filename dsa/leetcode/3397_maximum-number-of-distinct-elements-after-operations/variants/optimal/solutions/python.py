def solve(nums: list[int], k: int) -> int:
    """
    Maximizes the number of distinct elements by greedily picking the smallest
    available valid integer for each element in sorted order.
    """
    nums.sort()
    
    # last_used tracks the value assigned to the previous element
    # Initialize with a value smaller than any possible range start
    last_used = -float('inf')
    distinct_count = 0
    
    for x in nums:
        # The range for the current element is [x - k, x + k]
        lower_bound = x - k
        upper_bound = x + k
        
        # We want to pick the smallest value >= lower_bound that is > last_used
        # If last_used + 1 is within the valid range, we pick it.
        # Otherwise, we pick the lower_bound if it's > last_used.
        target = max(lower_bound, last_used + 1)
        
        if target <= upper_bound:
            distinct_count += 1
            last_used = target
            
    return distinct_count
