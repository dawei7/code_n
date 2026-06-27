from collections import defaultdict

def solve(nums: list[int], m: int, k: int) -> int:
    n = len(nums)
    if k > n:
        return 0
    
    max_sum = 0
    current_sum = 0
    counts = defaultdict(int)
    
    # Initialize the first window
    for i in range(k):
        current_sum += nums[i]
        counts[nums[i]] += 1
        
    if len(counts) >= m:
        max_sum = current_sum
        
    # Slide the window across the array
    for i in range(k, n):
        # Add new element
        new_val = nums[i]
        old_val = nums[i - k]
        
        current_sum += new_val - old_val
        counts[new_val] += 1
        
        # Remove old element
        counts[old_val] -= 1
        if counts[old_val] == 0:
            del counts[old_val]
            
        # Check condition
        if len(counts) >= m:
            if current_sum > max_sum:
                max_sum = current_sum
                
    return max_sum
