def solve(nums1: list[int], nums2: list[int], k: int) -> int:
    if k == 0:
        return 0 if nums1 == nums2 else -1
    
    diff_sum = 0
    pos_ops = 0
    neg_ops = 0
    
    for n1, n2 in zip(nums1, nums2):
        diff = n1 - n2
        
        # Each difference must be divisible by k
        if diff % k != 0:
            return -1
        
        diff_sum += diff
        if diff > 0:
            pos_ops += diff // k
        else:
            neg_ops += abs(diff) // k
            
    # The total sum must remain invariant, so the sum of differences must be 0
    if diff_sum != 0:
        return -1
        
    # The number of operations is the total amount moved, 
    # which is represented by either the total positive or total negative shifts
    return pos_ops
