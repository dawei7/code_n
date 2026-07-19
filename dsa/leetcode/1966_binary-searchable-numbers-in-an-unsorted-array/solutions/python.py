def solve(nums: list[int]) -> int:
    length = len(nums)
    suffix_minimum = [float("inf")] * (length + 1)

    for index in range(length - 1, -1, -1):
        suffix_minimum[index] = min(
            nums[index],
            suffix_minimum[index + 1],
        )

    answer = 0
    prefix_maximum = float("-inf")

    for index, value in enumerate(nums):
        if prefix_maximum < value < suffix_minimum[index + 1]:
            answer += 1
        prefix_maximum = max(prefix_maximum, value)

    return answer
