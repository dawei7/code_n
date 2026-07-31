from collections import Counter


def solve(nums: list[int]) -> int:
    modulo = 1_000_000_007
    left = Counter()
    right = Counter(nums)
    answer = 0

    for value in nums:
        right[value] -= 1
        target = value * 2
        answer = (answer + left[target] * right[target]) % modulo
        left[value] += 1

    return answer
