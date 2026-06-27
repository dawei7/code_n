from typing import List

def solve(nums: List[int]) -> int:
    n = len(nums)
    # Create a list of (value, index) tuples to keep track of original positions
    indexed_nums = []
    for i in range(n):
        indexed_nums.append((nums[i], i))
    
    # Sort primarily by value, secondarily by index
    indexed_nums.sort()
    
    marked = [False] * n
    total_score = 0
    
    for val, idx in indexed_nums:
        # If the current element is already marked, skip it
        if marked[idx]:
            continue
        
        # Add to score and mark the current index and its neighbors
        total_score += val
        marked[idx] = True
        if idx > 0:
            marked[idx - 1] = True
        if idx < n - 1:
            marked[idx + 1] = True
            
    return total_score
