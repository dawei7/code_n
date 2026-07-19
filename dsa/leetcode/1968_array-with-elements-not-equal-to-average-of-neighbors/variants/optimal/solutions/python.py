def solve(nums: list[int]) -> list[int]:
    arranged = sorted(nums)
    for index in range(0, len(arranged) - 1, 2):
        arranged[index], arranged[index + 1] = arranged[index + 1], arranged[index]
    return arranged
