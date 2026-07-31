from collections import Counter


def solve(nums: list[int], forbidden: list[int]) -> int:
    n = len(nums)
    nums_count = Counter(nums)
    forbidden_count = Counter(forbidden)

    if any(nums_count[value] + forbidden_count[value] > n for value in nums_count):
        return -1

    bad_count = Counter(
        nums[i]
        for i in range(n)
        if nums[i] == forbidden[i]
    )
    total_bad = sum(bad_count.values())
    largest_bad_group = max(bad_count.values(), default=0)
    return max(largest_bad_group, (total_bad + 1) // 2)
