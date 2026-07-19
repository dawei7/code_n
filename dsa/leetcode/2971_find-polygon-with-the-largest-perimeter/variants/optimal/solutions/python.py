from typing import List

def solve(nums: List[int]) -> int:
    """
    Finds the largest perimeter of a polygon that can be formed using the given side lengths.
    
    The condition for a polygon with sides s1 <= s2 <= ... <= sk is:
    sk < s1 + s2 + ... + s(k-1)
    
    By sorting the array, we can greedily check this condition.
    """
    nums.sort()
    
    total_sum = sum(nums)
    n = len(nums)
    
    # Iterate backwards from the largest element
    # The current element nums[i] is the longest side.
    # The sum of all other sides is total_sum - nums[i].
    for i in range(n - 1, 1, -1):
        current_longest = nums[i]
        remaining_sum = total_sum - current_longest
        
        if remaining_sum > current_longest:
            return total_sum
        
        # If the condition isn't met, remove the current largest element
        # from the total sum and try the next largest.
        total_sum -= current_longest
        
    return -1
