def solve(nums: list[int]) -> int:
    for index, value in enumerate(nums[:28]):
        if sum(map(int, str(value))) == index:
            return index
    return -1
