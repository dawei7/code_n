def solve(nums: list[int]) -> list[int]:
    maximum = 0
    score = 0
    answer = []

    for value in nums:
        maximum = max(maximum, value)
        score += value + maximum
        answer.append(score)

    return answer
