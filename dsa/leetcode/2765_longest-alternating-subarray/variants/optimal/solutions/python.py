from typing import List

def solve(nums: List[int]) -> int:
    max_len = -1
    n = len(nums)
    
    # We look for subarrays of length at least 2
    # Start index i, current length length
    i = 0
    while i < n - 1:
        # Check if the first pair is valid (difference must be 1)
        if nums[i + 1] - nums[i] == 1:
            length = 2
            # Continue checking the alternating pattern
            # The expected difference alternates between -1 and 1
            # For index k, the difference should be 1 if (k-i) is even, -1 if odd
            curr = i + 1
            while curr < n - 1:
                expected_diff = -1 if (curr - i) % 2 == 1 else 1
                if nums[curr + 1] - nums[curr] == expected_diff:
                    length += 1
                    curr += 1
                else:
                    break
            max_len = max(max_len, length)
            # Optimization: jump to the end of this sequence
            i = curr
        else:
            i += 1
            
    return max_len
