from collections import defaultdict


def solve(group_sizes):
    buckets = defaultdict(list)
    answer = []
    for i, size in enumerate(group_sizes):
        buckets[size].append(i)
        if len(buckets[size]) == size:
            answer.append(buckets[size])
            buckets[size] = []
    return answer
