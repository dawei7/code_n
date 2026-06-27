from typing import List

def solve(nums: List[int], k: int) -> List[int]:
    if k == 1:
        return nums
    
    n = len(nums)
    results = []
    # consecutive_count tracks how many elements in a row satisfy nums[i] == nums[i-1] + 1
    consecutive_count = 1
    
    for i in range(1, n):
        if nums[i] == nums[i - 1] + 1:
            consecutive_count += 1
        else:
            consecutive_count = 1
            
        # Once we have processed at least k-1 elements, we can start checking windows
        if i >= k - 1:
            if consecutive_count >= k:
                results.append(nums[i])
            else:
                results.append(-1)
                
    return results
