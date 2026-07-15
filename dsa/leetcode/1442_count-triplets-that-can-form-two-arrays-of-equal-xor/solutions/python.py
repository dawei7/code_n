from collections import defaultdict


def solve(arr):
    occurrence_count = defaultdict(int)
    position_sum = defaultdict(int)
    prefix = 0
    answer = 0
    occurrence_count[0] = 1

    for index, value in enumerate(arr):
        prefix ^= value
        answer += occurrence_count[prefix] * index - position_sum[prefix]
        occurrence_count[prefix] += 1
        position_sum[prefix] += index + 1

    return answer
