def solve(nums1: list[int], nums2: list[int]) -> int:
    sum1 = 0
    zeros1 = 0
    for x in nums1:
        if x == 0:
            zeros1 += 1
        else:
            sum1 += x
            
    sum2 = 0
    zeros2 = 0
    for x in nums2:
        if x == 0:
            zeros2 += 1
        else:
            sum2 += x
            
    min_sum1 = sum1 + zeros1
    min_sum2 = sum2 + zeros2
    
    # If an array has no zeros, its sum is fixed.
    # We can only increase the sum of an array if it contains at least one zero.
    
    if zeros1 == 0 and zeros2 == 0:
        return sum1 if sum1 == sum2 else -1
    
    if zeros1 == 0:
        return sum1 if sum1 >= min_sum2 else -1
    
    if zeros2 == 0:
        return sum2 if sum2 >= min_sum1 else -1
        
    # If both have zeros, the minimum equal sum is the max of the two minimums.
    return max(min_sum1, min_sum2)
