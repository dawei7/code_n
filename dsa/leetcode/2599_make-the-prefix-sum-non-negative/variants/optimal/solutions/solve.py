from heapq import heappop, heappush


def solve(nums: list[int]) -> int:
    prefix_sum = 0
    operations = 0
    negatives: list[int] = []

    for number in nums:
        prefix_sum += number
        if number < 0:
            heappush(negatives, number)

        if prefix_sum < 0:
            prefix_sum -= heappop(negatives)
            operations += 1

    return operations
