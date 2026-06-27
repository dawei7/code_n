from typing import List

def solve(nums: List[int]) -> bool:
    """
    Determines if Alice can win by removing either all single-digit numbers
    or all double-digit numbers.
    """
    single_digit_sum = 0
    double_digit_sum = 0
    
    for num in nums:
        if num < 10:
            single_digit_sum += num
        else:
            double_digit_sum += num
            
    # Alice wins if she can remove a set such that the sum of the removed
    # numbers is strictly greater than the sum of the remaining numbers.
    # This is equivalent to saying the sum of the removed set is greater
    # than the sum of the other set.
    return single_digit_sum != double_digit_sum
