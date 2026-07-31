def solve(nums: list[int]) -> int:
    answer = 0
    for index, value in enumerate(nums):
        if index % 2 == 0:
            answer += value
        else:
            answer -= value
    return answer
