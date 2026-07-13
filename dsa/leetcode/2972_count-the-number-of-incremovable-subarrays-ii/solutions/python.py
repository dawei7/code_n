from typing import List

def solve(nums: List[int]) -> int:
    n = len(nums)

    # Find the longest strictly increasing prefix
    left = 0
    while left + 1 < n and nums[left] < nums[left + 1]:
        left += 1

    # If the whole array is strictly increasing
    if left == n - 1:
        return n * (n + 1) // 2

    # Find the longest strictly increasing suffix
    right = n - 1
    while right - 1 >= 0 and nums[right - 1] < nums[right]:
        right -= 1

    count = 0
    j = right
    # i == -1 means the whole kept part, if any, comes from the suffix.
    for i in range(-1, left + 1):
        while i >= 0 and j < n and nums[j] <= nums[i]:
            j += 1
        count += (n - j + 1)

    return count
