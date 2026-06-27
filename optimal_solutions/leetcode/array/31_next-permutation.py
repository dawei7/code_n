from typing import List

def solve(nums: List[int]) -> None:
    """
    Modifies the input list nums in-place to the next lexicographical permutation.
    """
    n = len(nums)
    if n <= 1:
        return

    # Step 1: Find the first decreasing element from the right
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Step 2: Find the smallest element larger than nums[i] to its right
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Swap them
        nums[i], nums[j] = nums[j], nums[i]

    # Step 3: Reverse the suffix starting at i + 1
    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
