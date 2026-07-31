from math import isqrt


def solve(nums: list[int]) -> int:
    def feasible(k: int) -> bool:
        limit = k * k
        operations = 0
        for value in nums:
            operations += (value + k - 1) // k
            if operations > limit:
                return False
        return True

    low = 1
    high = max(max(nums), isqrt(len(nums) - 1) + 1)

    while low < high:
        middle = (low + high) // 2
        if feasible(middle):
            high = middle
        else:
            low = middle + 1

    return low
