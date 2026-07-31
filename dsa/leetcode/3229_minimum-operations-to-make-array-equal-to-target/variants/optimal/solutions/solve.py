def solve(nums: list[int], target: list[int]) -> int:
    previous = target[0] - nums[0]
    operations = abs(previous)

    for index in range(1, len(nums)):
        current = target[index] - nums[index]
        if previous * current > 0:
            operations += max(0, abs(current) - abs(previous))
        else:
            operations += abs(current)
        previous = current

    return operations
