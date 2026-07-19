from collections import deque

def solve(nums: list[int]) -> int:
    n = len(nums)
    left = 0
    count = 0
    
    # Monotonic deques to store indices
    # max_dq stores indices of elements in decreasing order
    # min_dq stores indices of elements in increasing order
    max_dq = deque()
    min_dq = deque()
    
    for right in range(n):
        # Maintain max_dq
        while max_dq and nums[max_dq[-1]] <= nums[right]:
            max_dq.pop()
        max_dq.append(right)
        
        # Maintain min_dq
        while min_dq and nums[min_dq[-1]] >= nums[right]:
            min_dq.pop()
        min_dq.append(right)
        
        # If condition is violated, shrink window from left
        while nums[max_dq[0]] - nums[min_dq[0]] > 2:
            left += 1
            if max_dq[0] < left:
                max_dq.popleft()
            if min_dq[0] < left:
                min_dq.popleft()
        
        # All subarrays ending at 'right' and starting from any index 
        # between 'left' and 'right' are valid
        count += (right - left + 1)
        
    return count
