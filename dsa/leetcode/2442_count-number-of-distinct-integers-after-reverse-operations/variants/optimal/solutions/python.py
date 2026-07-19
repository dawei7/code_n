from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the number of distinct integers after adding the reversed 
    versions of each number in the input list to the set.
    """
    distinct_elements = set(nums)
    
    for num in nums:
        # Reverse the integer mathematically
        reversed_num = 0
        temp = num
        while temp > 0:
            reversed_num = (reversed_num * 10) + (temp % 10)
            temp //= 10
        
        distinct_elements.add(reversed_num)
        
    return len(distinct_elements)
