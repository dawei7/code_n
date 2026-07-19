from collections import Counter


def solve(nums: list[int], k: int) -> int:
    total = sum(nums)
    right: Counter[int] = Counter()
    prefix = 0

    for pivot in range(1, len(nums)):
        prefix += nums[pivot - 1]
        right[2 * prefix - total] += 1

    answer = right[0]
    left: Counter[int] = Counter()
    prefix = 0

    for index, value in enumerate(nums):
        if index > 0:
            prefix += nums[index - 1]
            balance = 2 * prefix - total
            right[balance] -= 1
            left[balance] += 1

        change = k - value
        answer = max(answer, left[change] + right[-change])

    return answer
