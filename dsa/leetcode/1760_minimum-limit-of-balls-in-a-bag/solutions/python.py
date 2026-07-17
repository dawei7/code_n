def solve(nums: list[int], maxOperations: int) -> int:
    low = 1
    high = max(nums)

    while low < high:
        penalty = (low + high) // 2
        required = sum((balls - 1) // penalty for balls in nums)

        if required <= maxOperations:
            high = penalty
        else:
            low = penalty + 1

    return low
