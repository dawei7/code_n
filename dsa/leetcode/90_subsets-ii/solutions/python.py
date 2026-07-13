def solve(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result: list[list[int]] = []
    path: list[int] = []

    def build(start: int) -> None:
        result.append(path[:])
        for index in range(start, len(nums)):
            if index > start and nums[index] == nums[index - 1]:
                continue
            path.append(nums[index])
            build(index + 1)
            path.pop()

    build(0)
    return result
