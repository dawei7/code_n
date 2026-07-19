from typing import List

def solve(nums: List[int]) -> List[int]:
    """
    Decomposes each integer in the input list into its individual digits
    and returns them as a flat list.
    """
    result = []
    for num in nums:
        # Convert number to string to iterate over digits
        for digit in str(num):
            result.append(int(digit))
    return result
