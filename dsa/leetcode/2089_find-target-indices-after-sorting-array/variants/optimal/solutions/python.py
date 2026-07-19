def solve(nums: list[int], target: int) -> list[int]:
    smaller = 0
    equal = 0

    for value in nums:
        if value < target:
            smaller += 1
        elif value == target:
            equal += 1

    return list(range(smaller, smaller + equal))
