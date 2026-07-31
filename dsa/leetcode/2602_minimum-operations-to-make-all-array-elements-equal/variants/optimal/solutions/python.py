from bisect import bisect_left


def solve(nums, queries):
    values = sorted(nums)
    prefix = [0]
    for number in values:
        prefix.append(prefix[-1] + number)

    n = len(values)
    answer = []
    for query in queries:
        split = bisect_left(values, query)
        left_cost = query * split - prefix[split]
        right_cost = prefix[n] - prefix[split] - query * (n - split)
        answer.append(left_cost + right_cost)

    return answer
