from collections import defaultdict

def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    if k > n:
        return 0
    
    max_sum = 0
    current_sum = 0
    counts = defaultdict(int)
    distinct_count = 0
    
    for i in range(n):
        # Add current element to window
        val = nums[i]
        if counts[val] == 0:
            distinct_count += 1
        counts[val] += 1
        current_sum += val
        
        # Remove element sliding out of window
        if i >= k:
            out_val = nums[i - k]
            counts[out_val] -= 1
            if counts[out_val] == 0:
                distinct_count -= 1
            current_sum -= out_val
            
        # Check if window is valid
        if i >= k - 1:
            if distinct_count == k:
                max_sum = max(max_sum, current_sum)
                
    return max_sum
