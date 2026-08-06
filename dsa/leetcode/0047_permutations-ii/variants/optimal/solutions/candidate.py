def solve(nums: list[int]) -> list[list[int]]:
    nums.sort()
    used = [False] * len(nums)
    path: list[int] = []
    result: list[list[int]] = []

    def arrange() -> None:
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i, value in enumerate(nums):
            if used[i]:
                continue
            if i > 0 and value == nums[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(value)
            arrange()
            path.pop()
            used[i] = False

    arrange()
    return result
