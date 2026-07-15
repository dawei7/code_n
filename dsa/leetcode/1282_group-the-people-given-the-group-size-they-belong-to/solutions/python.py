from collections import defaultdict


def solve(group_sizes):
    buckets = defaultdict(list)
    groups = []

    for person, size in enumerate(group_sizes):
        bucket = buckets[size]
        bucket.append(person)
        if len(bucket) == size:
            groups.append(bucket)
            buckets[size] = []

    return groups
