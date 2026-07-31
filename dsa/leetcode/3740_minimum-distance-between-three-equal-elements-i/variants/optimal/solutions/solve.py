def solve(nums: list[int]) -> int:
    n = len(nums)
    latest = [-1] * (n + 1)
    second_latest = [-1] * (n + 1)
    answer = 2 * n + 1

    for index, value in enumerate(nums):
        if second_latest[value] != -1:
            answer = min(answer, 2 * (index - second_latest[value]))
        second_latest[value] = latest[value]
        latest[value] = index

    return -1 if answer == 2 * n + 1 else answer
