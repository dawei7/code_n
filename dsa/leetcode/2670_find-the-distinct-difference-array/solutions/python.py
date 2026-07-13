from typing import List

def solve(nums: List[int]) -> List[int]:
    n = len(nums)
    if n == 0:
        return []

    # Step 1: Calculate prefix distinct counts
    prefix_distinct_counts = [0] * n
    seen_prefix = set()
    for i in range(n):
        seen_prefix.add(nums[i])
        prefix_distinct_counts[i] = len(seen_prefix)

    # Step 2: Calculate suffix distinct counts
    # suffix_distinct_counts[i] will store the number of distinct elements in nums[i+1...n-1]
    suffix_distinct_counts = [0] * n
    seen_suffix = set()
    for i in range(n - 1, -1, -1):
        # The distinct count for the suffix nums[i+1...n-1] is the current size of seen_suffix
        # before adding nums[i]
        suffix_distinct_counts[i] = len(seen_suffix)
        seen_suffix.add(nums[i])

    # Step 3: Calculate the difference array
    diff = [0] * n
    for i in range(n):
        diff[i] = prefix_distinct_counts[i] - suffix_distinct_counts[i]

    return diff
