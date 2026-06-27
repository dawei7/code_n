from typing import List

def solve(nums: List[int]) -> List[int]:
    # Step 1: XOR all numbers to get xor_sum = a ^ b
    xor_sum = 0
    for num in nums:
        xor_sum ^= num
    
    # Step 2: Find the rightmost set bit in xor_sum.
    # This bit must be set in either a or b, but not both.
    # Using the two's complement trick: x & -x isolates the lowest set bit.
    diff_bit = xor_sum & -xor_sum
    
    # Step 3: Partition numbers into two groups and XOR them separately.
    a, b = 0, 0
    for num in nums:
        if num & diff_bit:
            a ^= num
        else:
            b ^= num
            
    return [a, b]
