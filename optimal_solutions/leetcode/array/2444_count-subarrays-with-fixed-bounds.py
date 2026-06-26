def solve(nums: list[int], minK: int, maxK: int) -> int:
    ans = 0
    bad_idx = -1
    min_idx = -1
    max_idx = -1
    
    for i, x in enumerate(nums):
        # If the current number is outside the allowed range, 
        # it resets the potential window.
        if not (minK <= x <= maxK):
            bad_idx = i
        
        # Update the last seen positions of minK and maxK
        if x == minK:
            min_idx = i
        if x == maxK:
            max_idx = i
            
        # The number of valid subarrays ending at i is determined by the 
        # distance between the closest boundary (min or max) and the 
        # last 'bad' index.
        count = min(min_idx, max_idx) - bad_idx
        if count > 0:
            ans += count
            
    return ans
