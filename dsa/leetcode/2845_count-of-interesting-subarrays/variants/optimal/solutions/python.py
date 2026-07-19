from collections import defaultdict

def solve(nums: list[int], modulo: int, k: int) -> int:
    """
    Counts the number of subarrays where the count of elements 
    satisfying (x % modulo == k) is congruent to k (mod modulo).
    """
    # count_map stores the frequency of (prefix_sum % modulo)
    # Initialize with 0: 1 to handle subarrays starting from index 0
    count_map = defaultdict(int)
    count_map[0] = 1
    
    current_prefix_sum = 0
    total_interesting_subarrays = 0
    
    for x in nums:
        # Check if the current element satisfies the condition
        if x % modulo == k:
            current_prefix_sum += 1
        
        # We need: (current_prefix_sum - previous_prefix_sum) % modulo == k
        # This rearranges to: previous_prefix_sum % modulo == (current_prefix_sum - k) % modulo
        target = (current_prefix_sum - k) % modulo
        
        if target in count_map:
            total_interesting_subarrays += count_map[target]
            
        # Update the map with the current prefix sum remainder
        count_map[current_prefix_sum % modulo] += 1
        
    return total_interesting_subarrays
