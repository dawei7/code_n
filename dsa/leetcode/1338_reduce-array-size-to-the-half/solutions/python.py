from collections import Counter


def solve(arr):
    removed = 0
    answer = 0
    target = len(arr) // 2
    for count in sorted(Counter(arr).values(), reverse=True):
        removed += count
        answer += 1
        if removed >= target:
            return answer
    return answer
