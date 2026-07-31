def solve(nums: list[int]) -> int:
    n = len(nums)
    distinct = len(set(nums))
    if distinct == 1:
        return n
    if distinct == n:
        return 1

    answer = 1
    for left in range(n):
        counts: dict[int, int] = {}
        frequency_counts: dict[int, int] = {}
        for right in range(left, n):
            value = nums[right]
            old_frequency = counts.get(value, 0)
            if old_frequency:
                frequency_counts[old_frequency] -= 1
                if frequency_counts[old_frequency] == 0:
                    del frequency_counts[old_frequency]

            new_frequency = old_frequency + 1
            counts[value] = new_frequency
            frequency_counts[new_frequency] = frequency_counts.get(new_frequency, 0) + 1

            if len(counts) == 1:
                answer = max(answer, right - left + 1)
            elif len(frequency_counts) == 2:
                low, high = sorted(frequency_counts)
                if high == 2 * low:
                    answer = max(answer, right - left + 1)

    return answer
