from typing import List

def solve(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    if k == 0:
        return list(range(n))
    
    # inc[i] stores the length of the non-increasing sequence ending at i
    inc = [1] * n
    for i in range(1, n):
        if nums[i] <= nums[i - 1]:
            inc[i] = inc[i - 1] + 1
            
    # dec[i] stores the length of the non-decreasing sequence starting at i
    dec = [1] * n
    for i in range(n - 2, -1, -1):
        if nums[i] <= nums[i + 1]:
            dec[i] = dec[i + 1] + 1
            
    result = []
    # A good index i must have k elements before it non-increasing
    # and k elements after it non-decreasing.
    # Valid range for i is [k, n - k - 1]
    for i in range(k, n - k):
        if inc[i - 1] >= k and dec[i + 1] >= k:
            result.append(i)
            
    return result
