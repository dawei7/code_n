from collections import defaultdict


def solve(groupSizes):
    buckets = defaultdict(list)
    groups = []

    for person, size in enumerate(groupSizes):
        bucket = buckets[size]
        bucket.append(person)
        if len(bucket) == size:
            groups.append(bucket)
            buckets[size] = []

    return groups
