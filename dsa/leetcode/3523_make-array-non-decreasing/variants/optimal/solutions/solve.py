def solve(nums: list[int]) -> int:
    answer = 0
    maximum = 0

    for value in nums:
        if value >= maximum:
            answer += 1
            maximum = value

    return answer
