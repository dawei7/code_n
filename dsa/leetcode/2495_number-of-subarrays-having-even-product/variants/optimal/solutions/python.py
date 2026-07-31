def solve(nums):
    answer = 0
    last_even = -1

    for index, value in enumerate(nums):
        if value % 2 == 0:
            last_even = index
        answer += last_even + 1

    return answer
