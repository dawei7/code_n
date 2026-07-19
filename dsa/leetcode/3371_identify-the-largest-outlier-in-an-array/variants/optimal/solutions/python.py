from collections import Counter

def solve(nums: list[int]) -> int:
    total_sum = sum(nums)
    counts = Counter(nums)
    max_outlier = float('-inf')
    
    for x in nums:
        # If x is the outlier, the sum of the remaining elements is (total_sum - x)
        # We need to find if there exists an element 'special' such that:
        # special = (total_sum - x) / 2
        # Which implies: 2 * special = total_sum - x
        
        remaining_sum = total_sum - x
        
        # The remaining sum must be even to have an integer 'special'
        if remaining_sum % 2 == 0:
            special = remaining_sum // 2
            
            # Check if 'special' exists in the array.
            # If special == x, we need at least two occurrences of that value
            # (one for the outlier, one for the special element).
            if special in counts:
                if special != x or counts[special] > 1:
                    if x > max_outlier:
                        max_outlier = x
                        
    return int(max_outlier)
