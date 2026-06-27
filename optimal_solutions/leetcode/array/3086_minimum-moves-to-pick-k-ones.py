def solve(nums: list[int], k: int, maxChanges: int) -> int:
    ones_indices = [i for i, x in enumerate(nums) if x == 1]
    n = len(ones_indices)
    
    # Strategy 1: Use maxChanges to flip zeros to ones
    # If we can flip zeros, we can pick ones at distance 1 or 2
    ans = float('inf')
    
    # Case: Use maxChanges to get as many ones as possible
    # We can pick at most 3 ones using maxChanges (the one itself + neighbors)
    # If we use m flips, we need k - m ones from existing ones
    for m in range(min(k, maxChanges + 1)):
        needed = k - m
        if needed <= 0:
            ans = min(ans, m)
            continue
        if needed > n:
            continue
            
        # Sliding window on ones_indices to find min cost to gather 'needed' ones
        # Prefix sums for O(1) range sum queries
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + ones_indices[i]
            
        for i in range(n - needed + 1):
            # Median is at index i + needed // 2
            mid = i + needed // 2
            median = ones_indices[mid]
            
            # Cost = (right_sum - median_part) - (left_sum - median_part)
            left_count = mid - i
            right_count = (i + needed - 1) - mid
            
            left_sum = prefix_sum[mid] - prefix_sum[i]
            right_sum = prefix_sum[i + needed] - prefix_sum[mid + 1]
            
            cost = (left_count * median - left_sum) + (right_sum - right_count * median)
            ans = min(ans, cost + m * 2)
            
    # Strategy 2: If we have enough maxChanges, we can just pick ones at distance 1
    # This is handled by the loop above, but we ensure the base case of 
    # picking ones that are already adjacent is covered.
    return int(ans)
