def solve(nums: list[int]) -> int:
    total_sum = 0
    prefix_sum = 0
    peak_value = 0
    ascending_sum = 0

    for value in nums:
        total_sum += value
        prefix_sum += value
        if value > peak_value:
            peak_value = value
            ascending_sum = prefix_sum

    descending_sum = total_sum - ascending_sum + peak_value

    if ascending_sum > descending_sum:
        return 0
    if descending_sum > ascending_sum:
        return 1
    return -1
