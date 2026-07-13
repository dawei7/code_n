def solve(receiver: list[int], k: int) -> int:
    n = len(receiver)
    if k == 0:
        return n - 1

    # max_log is the number of bits needed to represent k
    max_log = k.bit_length()

    # jump[j][i] stores the player reached after 2^j passes starting from i
    # sum_val[j][i] stores the sum of indices visited in 2^j passes starting from i
    jump = [[0] * n for _ in range(max_log)]
    sum_val = [[0] * n for _ in range(max_log)]

    for i in range(n):
        jump[0][i] = receiver[i]
        sum_val[0][i] = i

    for j in range(1, max_log):
        for i in range(n):
            mid = jump[j-1][i]
            jump[j][i] = jump[j-1][mid]
            sum_val[j][i] = sum_val[j-1][i] + sum_val[j-1][mid]

    ans = 0
    for i in range(n):
        curr_sum = 0
        curr_pos = i
        temp_k = k

        # Use binary lifting to traverse k steps
        for j in range(max_log):
            if (temp_k >> j) & 1:
                curr_sum += sum_val[j][curr_pos]
                curr_pos = jump[j][curr_pos]

        # Add the final node reached after k passes
        curr_sum += curr_pos
        ans = max(ans, curr_sum)

    return ans
