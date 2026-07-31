def _maximum_subarray_length(nums: list[int], k: int) -> int:
    earliest = {0: -1}
    running = 0
    best = 0
    for index, value in enumerate(nums):
        running += value
        needed = running - k
        if needed in earliest:
            best = max(best, index - earliest[needed])
        if running not in earliest:
            earliest[running] = index
    return best


def solve(nums: list[int], k: int) -> int:
    return _maximum_subarray_length(nums, k)
