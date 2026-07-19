from collections import Counter

def solve(nums: list[int]) -> bool:
    if not nums:
        return False
    
    n = max(nums)
    
    # A "good" array must have exactly n + 1 elements
    # (1 to n-1 once, and n twice)
    if len(nums) != n + 1:
        return False
    
    counts = Counter(nums)
    
    # Check for integers 1 to n-1
    for i in range(1, n):
        if counts[i] != 1:
            return False
            
    # Check for integer n
    if counts[n] != 2:
        return False
        
    return True
