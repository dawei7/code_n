def solve(nums: list[int]) -> int:
    if len(nums) < 2:
        return 0
    lowest = min(nums)
    highest = max(nums)
    if lowest == highest:
        return 0

    width = (highest - lowest + len(nums) - 2) // (len(nums) - 1)
    bucket_count = (highest - lowest) // width + 1
    bucket_min: list[int | None] = [None] * bucket_count
    bucket_max: list[int | None] = [None] * bucket_count

    for value in nums:
        index = (value - lowest) // width
        current_min = bucket_min[index]
        current_max = bucket_max[index]
        bucket_min[index] = value if current_min is None else min(current_min, value)
        bucket_max[index] = value if current_max is None else max(current_max, value)

    best = 0
    previous_max = lowest
    for current_min, current_max in zip(bucket_min, bucket_max):
        if current_min is None or current_max is None:
            continue
        best = max(best, current_min - previous_max)
        previous_max = current_max
    return best
