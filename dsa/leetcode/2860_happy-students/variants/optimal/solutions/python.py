from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the number of ways to form a group of happy students.
    
    Args:
        nums: List of requirements for each student.
        
    Returns:
        The count of valid group sizes.
    """
    nums.sort()
    n = len(nums)
    count = 0
    
    # Case 1: Group size 0
    # Everyone is not selected. Requirement must be > 0.
    # Since nums is sorted, we only need to check the smallest element.
    if nums[0] > 0:
        count += 1
        
    # Case 2: Group size k (1 to n)
    # We select the first k students.
    # Condition: nums[k-1] < k AND (k == n OR nums[k] > k)
    for k in range(1, n + 1):
        if nums[k - 1] < k:
            if k == n or nums[k] > k:
                count += 1
                
    return count
