def solve(s: str, t: str) -> int:
    n = len(s)
    m = len(t)

    suffix_start = [-1] * (m + 1)
    suffix_start[m] = n
    s_index = n - 1

    for t_index in range(m - 1, -1, -1):
        while s_index >= 0 and s[s_index] != t[t_index]:
            s_index -= 1
        if s_index < 0:
            break
        suffix_start[t_index] = s_index
        s_index -= 1

    answer = m
    suffix_index = 0
    prefix_end = -1
    s_index = 0

    for prefix_length in range(m + 1):
        if suffix_index < prefix_length:
            suffix_index = prefix_length
        while suffix_index < m and suffix_start[suffix_index] <= prefix_end:
            suffix_index += 1
        answer = min(answer, suffix_index - prefix_length)

        if prefix_length == m:
            break
        while s_index < n and s[s_index] != t[prefix_length]:
            s_index += 1
        if s_index == n:
            break
        prefix_end = s_index
        s_index += 1

    return answer
