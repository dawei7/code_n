def solve(nums: list[int]) -> int:
    added = nums[0]
    subtracted = float("-inf")

    for value in nums[1:]:
        added, subtracted = max(added, subtracted) + value, added - value

    return max(added, subtracted)
