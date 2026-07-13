import math
from bisect import bisect_left

def solve(nums: list[int], queries: list[int]) -> list[int]:
    max_num = max(nums)
    
    # Count occurrences of each number
    counts = [0] * (max_num + 1)
    for x in nums:
        counts[x] += 1
        
    # Count how many numbers are multiples of i
    multiples_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        for j in range(i, max_num + 1, i):
            multiples_count[i] += counts[j]
            
    # Count how many pairs have a GCD that is a multiple of i
    # A pair (a, b) has gcd multiple of i if both a and b are multiples of i
    # Number of pairs = n * (n - 1) // 2
    pairs_with_gcd_multiple_of_i = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        n = multiples_count[i]
        pairs_with_gcd_multiple_of_i[i] = n * (n - 1) // 2
        
    # Use Inclusion-Exclusion to find exact count of pairs with GCD == i
    # Start from max_num down to 1
    gcd_counts = [0] * (max_num + 1)
    for i in range(max_num, 0, -1):
        count = pairs_with_gcd_multiple_of_i[i]
        # Subtract counts of multiples of i to get exact GCD == i
        for j in range(2 * i, max_num + 1, i):
            count -= gcd_counts[j]
        gcd_counts[i] = count
        
    # Create prefix sum array for binary search
    prefix_sums = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prefix_sums[i] = prefix_sums[i - 1] + gcd_counts[i]
        
    results = []
    for q in queries:
        # Find the smallest index i such that prefix_sums[i] > q
        idx = bisect_left(prefix_sums, q + 1)
        results.append(idx)
        
    return results
