from collections import Counter


def solve(nums):
    answer = 0
    left = 0
    right = len(nums)

    for count in Counter(nums).values():
        right -= count
        answer += left * count * right
        left += count

    return answer
