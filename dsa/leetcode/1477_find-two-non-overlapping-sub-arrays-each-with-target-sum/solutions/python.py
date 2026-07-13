def solve(arr, target):
    best_left = [10**9] * len(arr)
    seen = {0: -1}
    prefix = 0
    best = 10**9
    answer = 10**9
    for index, value in enumerate(arr):
        prefix += value
        need = prefix - target
        if need in seen:
            start = seen[need] + 1
            length = index - seen[need]
            if start > 0 and best_left[start - 1] < 10**9:
                answer = min(answer, length + best_left[start - 1])
            best = min(best, length)
        best_left[index] = best
        seen[prefix] = index
    return -1 if answer == 10**9 else answer
