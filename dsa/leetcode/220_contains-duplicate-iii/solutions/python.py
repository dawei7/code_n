def solve(nums: list[int], indexDiff: int, valueDiff: int) -> bool:
    width = valueDiff + 1
    buckets: dict[int, int] = {}
    for index, value in enumerate(nums):
        bucket = value // width
        if bucket in buckets:
            return True
        if bucket - 1 in buckets and value - buckets[bucket - 1] <= valueDiff:
            return True
        if bucket + 1 in buckets and buckets[bucket + 1] - value <= valueDiff:
            return True
        buckets[bucket] = value
        if index >= indexDiff:
            expired = nums[index - indexDiff] // width
            buckets.pop(expired, None)
    return False
