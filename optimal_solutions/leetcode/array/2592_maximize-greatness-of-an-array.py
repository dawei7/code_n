from typing import List

def solve(nums: List[int]) -> int:
    """
    Maximizes the number of indices i such that permuted_nums[i] > nums[i].
    
    Strategy:
    1. Sort the array to easily find the smallest elements that can satisfy the condition.
    2. Use two pointers: 'i' for the smallest element we are trying to beat,
       and 'j' for the candidate element we are using to beat it.
    3. If nums[j] > nums[i], we have a successful pair, increment count and move both pointers.
    4. If nums[j] <= nums[i], we must move 'j' to find a larger candidate.
    """
    nums.sort()
    n = len(nums)
    i = 0
    count = 0
    
    for j in range(n):
        if nums[j] > nums[i]:
            count += 1
            i += 1
            
    return count
