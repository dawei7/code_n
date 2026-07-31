def solve(nums: list[int], min_k: int, max_k: int) -> int:
    last_invalid = -1
    last_minimum = -1
    last_maximum = -1
    answer = 0

    for index, value in enumerate(nums):
        if value < min_k or value > max_k:
            last_invalid = index
        if value == min_k:
            last_minimum = index
        if value == max_k:
            last_maximum = index

        answer += max(0, min(last_minimum, last_maximum) - last_invalid)

    return answer
