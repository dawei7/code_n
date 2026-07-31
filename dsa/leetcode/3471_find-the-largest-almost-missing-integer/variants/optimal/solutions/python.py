def solve(nums: list[int], k: int) -> int:
    if k == len(nums):
        return max(nums)

    frequencies: dict[int, int] = {}
    for value in nums:
        frequencies[value] = frequencies.get(value, 0) + 1

    if k == 1:
        return max(
            (value for value, count in frequencies.items() if count == 1),
            default=-1,
        )

    answer = -1
    if frequencies[nums[0]] == 1:
        answer = nums[0]
    if frequencies[nums[-1]] == 1:
        answer = max(answer, nums[-1])
    return answer
