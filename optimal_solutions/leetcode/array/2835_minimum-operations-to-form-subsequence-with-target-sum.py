from typing import List

def solve(nums: List[int], target: int) -> int:
    if sum(nums) < target:
        return -1
    
    # Count frequencies of each power of 2 (2^0 to 2^31)
    counts = [0] * 32
    for x in nums:
        counts[x.bit_length() - 1] += 1
        
    ops = 0
    current_sum = 0
    
    for i in range(32):
        # Add the value of the current bit if it's set in target
        if (target >> i) & 1:
            # If we have the power of 2 available, use it
            if counts[i] > 0:
                counts[i] -= 1
            else:
                # Need to split a larger power of 2
                j = i + 1
                while j < 32 and counts[j] == 0:
                    j += 1
                
                # Split the found larger power down to i
                counts[j] -= 1
                for k in range(j - 1, i - 1, -1):
                    counts[k] += 1
                    ops += 1
                counts[i] -= 1
        
        # Carry over excess powers to the next bit
        counts[i + 1] += counts[i] // 2
        
    return ops
