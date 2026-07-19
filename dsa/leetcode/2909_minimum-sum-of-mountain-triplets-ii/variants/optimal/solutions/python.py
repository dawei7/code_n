from typing import List

def solve(nums: List[int]) -> int:
    n = len(nums)
    if n < 3:
        return -1
    
    # min_left[i] stores the minimum value in nums[0...i-1]
    min_left = [float('inf')] * n
    curr_min = nums[0]
    for i in range(1, n):
        min_left[i] = curr_min
        if nums[i] < curr_min:
            curr_min = nums[i]
            
    # min_right[i] stores the minimum value in nums[i+1...n-1]
    min_right = [float('inf')] * n
    curr_min = nums[n - 1]
    for i in range(n - 2, -1, -1):
        min_right[i] = curr_min
        if nums[i] < curr_min:
            curr_min = nums[i]
            
    min_sum = float('inf')
    found = False
    
    # Check each index as a potential peak
    for i in range(1, n - 1):
        if min_left[i] < nums[i] and min_right[i] < nums[i]:
            current_triplet_sum = min_left[i] + nums[i] + min_right[i]
            if current_triplet_sum < min_sum:
                min_sum = current_triplet_sum
                found = True
                
    return int(min_sum) if found else -1
