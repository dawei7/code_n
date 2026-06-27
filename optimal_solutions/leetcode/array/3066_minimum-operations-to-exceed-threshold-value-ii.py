import heapq
from typing import List

def solve(nums: List[int], k: int) -> int:
    """
    Calculates the minimum operations to make all elements >= k.
    Uses a min-heap to greedily combine the two smallest elements.
    """
    # Transform the list into a min-heap in-place
    heapq.heapify(nums)
    
    operations = 0
    
    # Continue until the smallest element is at least k
    while nums[0] < k:
        # Extract the two smallest elements
        x = heapq.heappop(nums)
        y = heapq.heappop(nums)
        
        # Calculate the new value and push it back
        new_val = x * 2 + y
        heapq.heappush(nums, new_val)
        
        operations += 1
        
    return operations
