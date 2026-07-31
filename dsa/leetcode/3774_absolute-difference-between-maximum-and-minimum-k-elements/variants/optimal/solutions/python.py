def solve(nums: list[int], k: int) -> int:
    counts = [0] * 101
    for number in nums:
        counts[number] += 1

    low_total = 0
    high_total = 0
    low_needed = k
    high_needed = k
    low_value = 1
    high_value = 100

    while low_needed or high_needed:
        if low_needed:
            low_take = min(low_needed, counts[low_value])
            low_total += low_value * low_take
            low_needed -= low_take
            low_value += 1
        if high_needed:
            high_take = min(high_needed, counts[high_value])
            high_total += high_value * high_take
            high_needed -= high_take
            high_value -= 1

    return high_total - low_total
