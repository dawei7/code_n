"""Optimal app-local solution for LeetCode 985."""


def solve(nums, queries):
    even_sum = sum(value for value in nums if value % 2 == 0)
    answer = []

    for value, index in queries:
        if nums[index] % 2 == 0:
            even_sum -= nums[index]
        nums[index] += value
        if nums[index] % 2 == 0:
            even_sum += nums[index]
        answer.append(even_sum)

    return answer
