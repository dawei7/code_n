def solve(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []

    def build(i: int) -> None:
        if i == len(nums):
            result.append(path[:])
            return

        build(i + 1)
        path.append(nums[i])
        build(i + 1)
        path.pop()

    build(0)
    return result
