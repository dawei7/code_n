def solve(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []

    def arrange(first: int) -> None:
        if first == len(nums):
            result.append(nums[:])
            return
        for index in range(first, len(nums)):
            nums[first], nums[index] = nums[index], nums[first]
            arrange(first + 1)
            nums[first], nums[index] = nums[index], nums[first]

    arrange(0)
    return result
