import random


def solve(nums: list[int], k: int) -> int:
    if k == 0:
        return len(nums)

    rank = len(nums) - k
    candidates = nums[:]
    while True:
        pivot = random.choice(candidates)
        smaller = [value for value in candidates if value < pivot]
        equal = [value for value in candidates if value == pivot]
        if rank < len(smaller):
            candidates = smaller
        elif rank < len(smaller) + len(equal):
            threshold = pivot
            break
        else:
            rank -= len(smaller) + len(equal)
            candidates = [value for value in candidates if value > pivot]

    return sum(value < threshold for value in nums)
