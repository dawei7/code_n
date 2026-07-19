def solve(nums: list[int]) -> int:
    length = len(nums)
    values = sorted(set(nums))
    answer = length
    right = 0

    for left, minimum in enumerate(values):
        while right < len(values) and values[right] < minimum + length:
            right += 1
        answer = min(answer, length - (right - left))

    return answer
