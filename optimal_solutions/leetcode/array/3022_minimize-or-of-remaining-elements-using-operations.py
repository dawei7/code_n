def solve(nums: list[int], k: int) -> int:
    def can_achieve(target_or: int) -> bool:
        ops = 0
        current_and = -1  # All bits set to 1
        
        for x in nums:
            if current_and == -1:
                current_and = x
            else:
                current_and &= x
            
            # If current_and only contains bits allowed in target_or
            if (current_and | target_or) == target_or:
                current_and = -1
            else:
                ops += 1
        
        return ops <= k

    ans = 0
    # Iterate from most significant bit to least significant
    for i in range(30, -1, -1):
        # Try to see if we can keep the i-th bit as 0
        # We assume all bits higher than i are already fixed in 'ans'
        target = ans | ((1 << i) - 1)
        
        # If we cannot force the i-th bit to be 0, we must accept it as 1
        if not can_achieve(target):
            ans |= (1 << i)
            
    return ans
