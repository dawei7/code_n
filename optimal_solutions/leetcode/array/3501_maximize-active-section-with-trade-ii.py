from collections import deque

def solve(nums: list[int], k: int) -> int:
    """
    Finds the length of the longest contiguous subarray where 
    max(subarray) - min(subarray) <= k.
    """
    if not nums:
        return 0
    
    max_dq = deque()
    min_dq = deque()
    left = 0
    max_len = 0
    
    for right in range(len(nums)):
        # Maintain max_dq: elements in decreasing order
        while max_dq and nums[max_dq[-1]] <= nums[right]:
            max_dq.pop()
        max_dq.append(right)
        
        # Maintain min_dq: elements in increasing order
        while min_dq and nums[min_dq[-1]] >= nums[right]:
            min_dq.pop()
        min_dq.append(right)
        
        # Shrink window if condition is violated
        while nums[max_dq[0]] - nums[min_dq[0]] > k:
            left += 1
            if max_dq[0] < left:
                max_dq.popleft()
            if min_dq[0] < left:
                min_dq.popleft()
        
        max_len = max(max_len, right - left + 1)
        
    return max_len
