def solve(arr, m):
    n = len(arr)
    if m <= 0:
        return -1
    if m == n:
        return n
    length = [0] * (n + 2)
    active = [False] * (n + 2)
    count = 0
    answer = -1
    for step, raw_pos in enumerate(arr, 1):
        if not 1 <= raw_pos <= n or active[raw_pos]:
            if count > 0:
                answer = step
            continue
        active[raw_pos] = True
        left = length[raw_pos - 1]
        right = length[raw_pos + 1]
        merged = left + 1 + right
        if left == m:
            count -= 1
        if right == m:
            count -= 1
        if merged == m:
            count += 1
        length[raw_pos - left] = merged
        length[raw_pos + right] = merged
        length[raw_pos] = merged
        if count > 0:
            answer = step
    return answer
