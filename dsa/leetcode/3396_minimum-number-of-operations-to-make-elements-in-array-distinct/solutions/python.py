def solve(nums: list[int]) -> int:
    seen = set()

    for index in range(len(nums) - 1, -1, -1):
        if nums[index] in seen:
            return index // 3 + 1
        seen.add(nums[index])

    return 0
