from typing import List

def solve(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return -1

    # Step 1: Find a candidate for the dominant element of the entire array
    # using Boyer-Moore Voting Algorithm.
    candidate = -1
    count = 0
    for x in nums:
        if count == 0:
            candidate = x
            count = 1
        elif x == candidate:
            count += 1
        else:
            count -= 1

    # Step 2: Verify if the candidate is truly dominant and get its total count.
    # If the candidate is not dominant in the entire array, no valid split is possible.
    global_dominant_count = 0
    for x in nums:
        if x == candidate:
            global_dominant_count += 1

    if global_dominant_count * 2 <= n:
        return -1 # No dominant element in the entire array

    global_dominant = candidate

    # Step 3: Iterate through all possible split points (i from 0 to n-2).
    # Maintain the count of the global_dominant in the left subarray.
    left_dominant_count = 0
    for i in range(n - 1):
        # Update count for the left subarray
        if nums[i] == global_dominant:
            left_dominant_count += 1

        # Calculate lengths of left and right subarrays
        left_len = i + 1
        right_len = n - left_len

        # Calculate count of global_dominant in the right subarray
        right_dominant_count = global_dominant_count - left_dominant_count

        # Check if global_dominant is dominant in both subarrays
        is_left_dominant = (left_dominant_count * 2 > left_len)
        is_right_dominant = (right_dominant_count * 2 > right_len)

        if is_left_dominant and is_right_dominant:
            return i # Found the smallest valid split index

    # If no valid split is found after checking all possible indices
    return -1
