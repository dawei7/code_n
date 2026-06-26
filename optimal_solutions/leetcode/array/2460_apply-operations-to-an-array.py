from typing import List

def solve(nums: List[int]) -> List[int]:
    n = len(nums)
    # First pass: Apply the doubling operation
    for i in range(n - 1):
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0
            
    # Second pass: Shift non-zero elements to the front
    result = [0] * n
    write_idx = 0
    for val in nums:
        if val != 0:
            result[write_idx] = val
            write_idx += 1
            
    return result
