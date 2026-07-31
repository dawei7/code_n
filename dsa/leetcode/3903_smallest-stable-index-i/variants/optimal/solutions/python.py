def solve(nums: list[int], k: int) -> int:
    suffix_minimum = [nums[-1]]
    for value in reversed(nums[:-1]):
        suffix_minimum.append(min(value, suffix_minimum[-1]))
    suffix_minimum.reverse()

    prefix_maximum = nums[0]
    for index, value in enumerate(nums):
        prefix_maximum = max(prefix_maximum, value)
        if prefix_maximum - suffix_minimum[index] <= k:
            return index

    return -1
