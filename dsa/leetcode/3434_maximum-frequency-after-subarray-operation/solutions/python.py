from collections import defaultdict

def solve(nums: list[int], k: int) -> int:
    # Initial frequency of k
    initial_k_count = nums.count(k)
    
    # Identify all unique numbers in the array
    unique_elements = set(nums)
    
    max_gain = 0
    
    # For each candidate x, we want to maximize the gain:
    # Gain = (count of x in subarray) - (count of k in subarray)
    # This is equivalent to finding the maximum subarray sum where:
    # x contributes +1 and k contributes -1
    for x in unique_elements:
        if x == k:
            continue
            
        current_gain = 0
        for num in nums:
            if num == x:
                current_gain += 1
            elif num == k:
                current_gain -= 1
            
            if current_gain < 0:
                current_gain = 0
            
            if current_gain > max_gain:
                max_gain = current_gain
                
    return initial_k_count + max_gain
