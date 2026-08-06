def solve(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result: list[list[int]] = []
    path: list[int] = []

    def build(start: int) -> None:
        result.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            build(i + 1)
            path.pop()

    build(0)
    return result
