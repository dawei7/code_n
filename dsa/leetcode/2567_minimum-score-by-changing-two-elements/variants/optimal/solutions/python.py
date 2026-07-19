from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the minimum score by changing at most two elements.
    The strategy is to sort the array and compare the range after 
    removing the two smallest, two largest, or one of each.
    """
    n = len(nums)
    if n <= 3:
        return 0
    
    nums.sort()
    
    # Option 1: Change the two largest elements to match the third largest
    # The range becomes nums[n-3] - nums[0]
    option1 = nums[n - 3] - nums[0]
    
    # Option 2: Change the two smallest elements to match the third smallest
    # The range becomes nums[n-1] - nums[2]
    option2 = nums[n - 1] - nums[2]
    
    # Option 3: Change the smallest and the largest elements
    # The range becomes nums[n-2] - nums[1]
    option3 = nums[n - 2] - nums[1]
    
    return min(option1, option2, option3)
