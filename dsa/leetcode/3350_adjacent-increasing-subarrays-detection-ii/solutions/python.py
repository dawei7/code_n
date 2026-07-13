from typing import List

def solve(nums: List[int]) -> int:
    n = len(nums)
    if n < 2:
        return 0
    
    # inc_len[i] stores the length of the strictly increasing subarray ending at i
    inc_len = [1] * n
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            inc_len[i] = inc_len[i - 1] + 1
            
    # To check if a k exists, we need two adjacent subarrays of length k.
    # This means there exists an index i such that:
    # 1. The subarray ending at i has length >= k
    # 2. The subarray starting at i+1 has length >= k
    # We can precompute the length of the increasing subarray starting at i
    start_len = [1] * n
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            start_len[i] = start_len[i + 1] + 1
            
    def check(k: int) -> bool:
        if k == 0:
            return True
        # We need two adjacent blocks of length k.
        # The first ends at i, the second starts at i+1.
        # So inc_len[i] >= k and start_len[i+1] >= k
        for i in range(n - k):
            if inc_len[i] >= k and start_len[i + 1] >= k:
                return True
        return False

    # Binary search for the maximum k
    low = 0
    high = n // 2
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            low = mid + 1
            continue
        if check(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return ans
