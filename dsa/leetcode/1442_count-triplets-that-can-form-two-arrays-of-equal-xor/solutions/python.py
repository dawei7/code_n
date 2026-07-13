from collections import defaultdict


def solve(arr):
    count = defaultdict(int)
    total = defaultdict(int)
    prefix = 0
    answer = 0
    count[0] = 1
    for index, value in enumerate(arr):
        prefix ^= value
        answer += count[prefix] * index - total[prefix]
        count[prefix] += 1
        total[prefix] += index + 1
    return answer
