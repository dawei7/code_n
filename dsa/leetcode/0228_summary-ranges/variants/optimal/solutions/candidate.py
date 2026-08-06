def solve(nums: list[int]) -> list[str]:
    ranges: list[str] = []
    i = 0

    while i < len(nums):
        start = i
        while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
            i += 1

        if start == i:
            ranges.append(str(nums[start]))
        else:
            ranges.append(f"{nums[start]}->{nums[i]}")

        i += 1

    return ranges
