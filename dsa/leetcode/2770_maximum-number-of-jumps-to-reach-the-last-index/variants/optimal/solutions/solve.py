def solve(nums: list[int], target: int) -> int:
    maximum_jumps = [-1] * len(nums)
    maximum_jumps[0] = 0

    for destination in range(1, len(nums)):
        for source in range(destination):
            if maximum_jumps[source] != -1 and abs(nums[destination] - nums[source]) <= target:
                maximum_jumps[destination] = max(
                    maximum_jumps[destination],
                    maximum_jumps[source] + 1,
                )

    return maximum_jumps[-1]
