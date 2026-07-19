import math
from typing import List

def solve(nums: List[int], k: int) -> int:
    n = len(nums)
    if n == 0:
        return 0

    # Calculate 2^k
    power_of_2k = 1 << k

    # 1. Compute prefix OR sums
    prefix_or = [0] * n
    prefix_or[0] = nums[0]
    for i in range(1, n):
        prefix_or[i] = prefix_or[i-1] | nums[i]

    # 2. Compute suffix OR sums
    suffix_or = [0] * n
    suffix_or[n-1] = nums[n-1]
    for i in range(n - 2, -1, -1):
        suffix_or[i] = suffix_or[i+1] | nums[i]

    max_or_sum = 0

    # 3. Iterate through each element, apply the operation, and calculate total OR
    for i in range(n):
        # Value of nums[i] after multiplication
        modified_val = nums[i] * power_of_2k

        # OR sum of elements before nums[i]
        or_before = 0
        if i > 0:
            or_before = prefix_or[i-1]

        # OR sum of elements after nums[i]
        or_after = 0
        if i < n - 1:
            or_after = suffix_or[i+1]

        # Total OR sum for this specific modification
        current_total_or = modified_val | or_before | or_after

        # Update the maximum OR sum found so far
        max_or_sum = max(max_or_sum, current_total_or)

    return max_or_sum
