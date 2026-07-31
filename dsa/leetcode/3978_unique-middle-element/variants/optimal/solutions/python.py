def solve(nums: list[int]) -> bool:
    middle = nums[len(nums) // 2]
    occurrences = 0

    for value in nums:
        if value == middle:
            occurrences += 1
            if occurrences > 1:
                return False

    return True
