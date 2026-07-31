def solve(nums: list[int]) -> int:
    last_one = -1
    last_two = -1
    answer = len(nums) + 1

    for index, value in enumerate(nums):
        if value == 1:
            if last_two >= 0:
                answer = min(answer, index - last_two)
            last_one = index
        elif value == 2:
            if last_one >= 0:
                answer = min(answer, index - last_one)
            last_two = index

    return -1 if answer > len(nums) else answer
