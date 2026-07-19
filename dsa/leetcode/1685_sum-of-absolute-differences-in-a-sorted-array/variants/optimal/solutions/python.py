def solve(nums: list[int]) -> list[int]:
    total = sum(nums)
    left_sum = 0
    n = len(nums)
    answer = []

    for index, value in enumerate(nums):
        right_sum = total - left_sum - value
        left_cost = value * index - left_sum
        right_cost = right_sum - value * (n - index - 1)
        answer.append(left_cost + right_cost)
        left_sum += value

    return answer
