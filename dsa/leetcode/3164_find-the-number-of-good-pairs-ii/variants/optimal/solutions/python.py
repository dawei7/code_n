from collections import Counter

def solve(nums1: list[int], nums2: list[int], k: int) -> int:
    # Count frequencies of numbers in nums1
    count1 = Counter(nums1)
    
    # Find the maximum value in nums1 to bound our search
    if not nums1:
        return 0
    max_val = max(nums1)
    
    total_good_pairs = 0
    
    # Count frequencies of divisors in nums2
    # We only care about unique values in nums2 to avoid redundant work
    count2 = Counter(nums2)
    
    # For each unique divisor d = nums2[j] * k
    for val, freq in count2.items():
        divisor = val * k
        
        # Iterate through multiples of the divisor: divisor, 2*divisor, 3*divisor...
        # up to max_val
        for multiple in range(divisor, max_val + 1, divisor):
            if multiple in count1:
                total_good_pairs += count1[multiple] * freq
                
    return total_good_pairs
