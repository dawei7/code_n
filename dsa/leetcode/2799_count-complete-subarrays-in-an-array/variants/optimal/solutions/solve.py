def solve(nums: list[int]) -> int:
    required = len(set(nums))
    frequencies: dict[int, int] = {}
    left = 0
    answer = 0

    for right, value in enumerate(nums):
        frequencies[value] = frequencies.get(value, 0) + 1

        while len(frequencies) == required:
            answer += len(nums) - right
            outgoing = nums[left]
            frequencies[outgoing] -= 1
            if frequencies[outgoing] == 0:
                del frequencies[outgoing]
            left += 1

    return answer
