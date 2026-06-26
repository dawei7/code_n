from typing import List

def solve(nums: List[int]) -> int:
    n = len(nums)
    total_pairs = n * (n - 1) // 2
    good_pairs = 0
    diff_counts = {}
    
    for i, num in enumerate(nums):
        diff = num - i
        if diff in diff_counts:
            good_pairs += diff_counts[diff]
            diff_counts[diff] += 1
        else:
            diff_counts[diff] = 1
            
    return total_pairs - good_pairs
