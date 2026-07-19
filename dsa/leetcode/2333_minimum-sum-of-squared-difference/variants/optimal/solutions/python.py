import collections

def solve(nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
    n = len(nums1)
    total_k = k1 + k2

    # Max possible difference is 10^5 - 1 = 99999.
    # An array of size 100001 is sufficient for counts (indices 0 to 100000).
    MAX_DIFF_VAL = 100000 
    counts = [0] * (MAX_DIFF_VAL + 1)
    
    max_current_diff = 0
    for i in range(n):
        diff = abs(nums1[i] - nums2[i])
        counts[diff] += 1
        if diff > max_current_diff:
            max_current_diff = diff

    # Greedily reduce the largest differences
    # Iterate from the largest observed difference down to 1
    for d in range(max_current_diff, 0, -1):
        if total_k == 0:
            break # No operations left

        if counts[d] > 0:
            # Number of items with current difference 'd'
            num_items_at_d = counts[d]
            
            # If we have enough operations to reduce all these items by 1
            if total_k >= num_items_at_d:
                total_k -= num_items_at_d
                counts[d-1] += num_items_at_d
                counts[d] = 0 # All items at 'd' moved to 'd-1'
            else:
                # We only have 'total_k' operations left.
                # Reduce 'total_k' items from 'd' to 'd-1'.
                counts[d-1] += total_k
                counts[d] -= total_k
                total_k = 0 # No operations left
                break # Exit loop as no more operations

    # Calculate the final sum of squared differences
    min_sum_sq_diff = 0
    # Iterate through all possible differences (from 0 up to max_current_diff, or MAX_DIFF_VAL)
    # Using max_current_diff as upper bound is slightly more efficient if max_current_diff is small.
    # Using MAX_DIFF_VAL is also correct and safe.
    for d in range(max_current_diff + 1): 
        if counts[d] > 0:
            min_sum_sq_diff += counts[d] * d * d
            
    return min_sum_sq_diff
