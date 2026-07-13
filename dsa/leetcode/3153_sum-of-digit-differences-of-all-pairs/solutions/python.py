from typing import List

def solve(nums: List[int]) -> int:
    if not nums:
        return 0
    
    n = len(nums)
    # Convert numbers to strings to easily access digits by position
    s_nums = [str(num) for num in nums]
    num_digits = len(s_nums[0])
    
    total_diff = 0
    
    # For each digit position, count occurrences of each digit (0-9)
    for pos in range(num_digits):
        counts = [0] * 10
        for s in s_nums:
            digit = int(s[pos])
            counts[digit] += 1
        
        # Total pairs at this position is n * (n - 1) // 2
        # Pairs that match are sum of (count * (count - 1) // 2) for each digit
        # Pairs that differ = Total pairs - Matching pairs
        total_pairs = n * (n - 1) // 2
        matching_pairs = 0
        for c in counts:
            if c > 1:
                matching_pairs += (c * (c - 1)) // 2
        
        total_diff += (total_pairs - matching_pairs)
        
    return total_diff
