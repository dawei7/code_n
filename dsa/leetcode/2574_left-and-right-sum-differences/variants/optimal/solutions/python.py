def solve(nums: list[int]) -> list[int]:
    left_sum = 0
    right_sum = sum(nums)
    answer = []

    for value in nums:
        right_sum -= value
        answer.append(abs(left_sum - right_sum))
        left_sum += value

    return answer
