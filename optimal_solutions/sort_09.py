"""Optimal solution for sort_09: Bucket Sort.

Auto-generated from challenges/algorithms/sorting.py:SPECS.
O(n) time.
"""


def solve(data, n):
    if n == 0:
        return data
    min_val = min(data)
    max_val = max(data)
    span = max_val - min_val
    if span == 0:
        return data
    bucket_count = min(n, 10)
    bucket_size = span / bucket_count
    buckets = [[] for _ in range(bucket_count)]
    for value in data:
        idx = int((value - min_val) / bucket_size)
        if idx == bucket_count:
            # Float rounding: the max value can land one bucket too far.
            idx -= 1
        buckets[idx].append(value)
    for bucket in buckets:
        bucket.sort()
    index = 0
    for bucket in buckets:
        for value in bucket:
            data[index] = value
            index += 1
    return data
