def solve(nums: list[int]) -> int:
    points = [0] * (max(nums) + 1)
    for value in nums:
        points[value] += value

    skip = 0
    take = 0
    for total in points:
        skip, take = max(skip, take), skip + total

    return max(skip, take)
