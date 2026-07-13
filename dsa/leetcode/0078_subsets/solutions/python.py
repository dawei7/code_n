def solve(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []

    def build(index: int) -> None:
        if index == len(nums):
            result.append(path[:])
            return
        build(index + 1)
        path.append(nums[index])
        build(index + 1)
        path.pop()

    build(0)
    return result
