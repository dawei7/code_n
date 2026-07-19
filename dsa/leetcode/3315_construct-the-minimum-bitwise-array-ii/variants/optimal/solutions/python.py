def solve(nums: list[int]) -> list[int]:
    """
    For each target in nums, we want to find the smallest x such that x | (x + 1) == target.
    Let target = x | (x + 1).
    If x has a 0 at bit position k (from right, 0-indexed), then x+1 will have 
    a 1 at position k and 0s at all positions < k.
    The OR operation will result in target having 1s at all positions <= k.
    To minimize x, we want to find the lowest bit k such that setting it to 0 
    and setting all bits < k to 1 results in a valid x.
    """
    ans = []
    for target in nums:
        # If target is even, it cannot be represented as x | (x + 1) 
        # because x | (x + 1) always results in an odd number (the last bit is always 1).
        if target % 2 == 0:
            ans.append(-1)
            continue
        
        # We look for the rightmost zero bit in target.
        # If we flip the rightmost zero bit of target to 0, and set the bit 
        # to its right to 1, we get the smallest x.
        # Example: target = 7 (111). Rightmost zero is at bit 3 (1000).
        # Actually, the logic is: find the first bit 'k' that is 0 in target.
        # The candidate x is target ^ (1 << (k - 1)).
        
        found = False
        # Check bits from 0 to 30
        for k in range(31):
            if not (target & (1 << k)):
                # Found the rightmost zero at position k
                # The smallest x is obtained by clearing the bit at k-1
                if k > 0:
                    candidate = target ^ (1 << (k - 1))
                    ans.append(candidate)
                    found = True
                    break
        
        if not found:
            # If target is all 1s (like 1, 3, 7, 15...), 
            # the smallest x is target >> 1
            ans.append(target >> 1)
            
    return ans
