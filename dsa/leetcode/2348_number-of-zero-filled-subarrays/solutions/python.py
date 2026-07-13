from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the total number of zero-filled subarrays in the given array.

    A zero-filled subarray is a contiguous subarray where every element is 0.
    For any contiguous block of k zeros, it contributes k * (k + 1) / 2 zero-filled subarrays.

    Args:
        nums: A list of integers.

    Returns:
        The total count of zero-filled subarrays.
    """
    total_subarrays = 0
    current_zero_count = 0

    for num in nums:
        if num == 0:
            # If the current element is 0, increment the count of consecutive zeros.
            current_zero_count += 1
        else:
            # If the current element is not 0, it breaks a sequence of zeros.
            # Add the subarrays formed by the previous sequence of zeros to the total.
            # A sequence of k zeros forms k * (k + 1) / 2 subarrays.
            total_subarrays += current_zero_count * (current_zero_count + 1) // 2
            # Reset the consecutive zero count.
            current_zero_count = 0
    
    # After the loop, there might be a pending sequence of zeros at the end of the array.
    # Add the subarrays formed by this final sequence to the total.
    total_subarrays += current_zero_count * (current_zero_count + 1) // 2
    
    return total_subarrays
