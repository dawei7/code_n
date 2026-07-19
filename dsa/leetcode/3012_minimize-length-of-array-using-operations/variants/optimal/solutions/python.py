from typing import List
import math

def solve(nums: List[int]) -> int:
    """
    To minimize the array length:
    1. Find the minimum element 'm' and its frequency 'count'.
    2. If there exists any element 'x' in nums such that x % m != 0,
       we can use 'm' to reduce 'x' to 'x % m', which is smaller than 'm'.
       This allows us to eventually reduce the entire array to a single element.
    3. If all elements are divisible by 'm', we can only reduce the 'count'
       number of 'm's. Each operation on two 'm's results in 0 (since m % m == 0).
       We can pair up the 'm's to reduce them. The number of remaining elements
       will be ceil(count / 2).
    """
    min_val = min(nums)
    count = nums.count(min_val)
    
    # Check if there is any element not divisible by the minimum
    for x in nums:
        if x % min_val != 0:
            return 1
            
    # If all are divisible, we can reduce the count of min_val by half
    return (count + 1) // 2
