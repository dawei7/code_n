"""Project Euler Problem 375: Minimum of Subsequences.

Find M(2*10^9) = sum_{1 <= i <= j <= 2*10^9} min(S_i, ..., S_j) for PRNG S_{n+1} = S_n^2 mod 50515093.
"""

from typing import List, Tuple


def solve(limit: int = 2000000000) -> int:
    """Compute M(limit) using monotonic stack and periodic cycle reduction."""
    if limit <= 0:
        return 0

    mod = 50515093
    cycle_len = 6308948

    # Generate the full sequence S[1..cycle_len]
    seq_s: List[int] = [0] * (cycle_len + 1)
    curr = 290797
    min_val = mod
    min_idx = 0
    for i in range(1, cycle_len + 1):
        curr = (curr * curr) % mod
        seq_s[i] = curr
        if curr < min_val:
            min_val = curr
            min_idx = i

    p = min_idx  # 1-based index of global minimum (3 at p = 2633997)

    # Monotonic stack for prefix S[1..p]
    stack: List[Tuple[int, int]] = []
    curr_sum = 0
    t_prefix = 0
    for j in range(1, p + 1):
        v = seq_s[j]
        c = 1
        while stack and stack[-1][0] >= v:
            old_v, old_c = stack.pop()
            curr_sum -= old_v * old_c
            c += old_c
        stack.append((v, c))
        curr_sum += v * c
        t_prefix += curr_sum

    if limit <= p:
        # If limit is within prefix, compute monotonic stack directly up to limit
        stack_small: List[Tuple[int, int]] = []
        curr_sum_small = 0
        tot_small = 0
        for j in range(1, limit + 1):
            v = seq_s[j]
            c = 1
            while stack_small and stack_small[-1][0] >= v:
                old_v, old_c = stack_small.pop()
                curr_sum_small -= old_v * old_c
                c += old_c
            stack_small.append((v, c))
            curr_sum_small += v * c
            tot_small += curr_sum_small
        return tot_small

    # Rotated array B[1..cycle_len]: S[p+1..cycle_len] + S[1..p]
    seq_b: List[int] = [0] * (cycle_len + 1)
    for i in range(1, cycle_len - p + 1):
        seq_b[i] = seq_s[p + i]
    for i in range(1, p + 1):
        seq_b[cycle_len - p + i] = seq_s[i]

    # Monotonic stack on rotated array B[1..cycle_len]
    stack.clear()
    curr_sum = 0
    f_b: List[int] = [0] * (cycle_len + 1)
    sum_f_b = 0
    for j in range(1, cycle_len + 1):
        v = seq_b[j]
        c = 1
        while stack and stack[-1][0] >= v:
            old_v, old_c = stack.pop()
            curr_sum -= old_v * old_c
            c += old_c
        stack.append((v, c))
        curr_sum += v * c
        f_b[j] = curr_sum
        sum_f_b += curr_sum

    k_blocks = (limit - p) // cycle_len
    rem_suffix = (limit - p) % cycle_len

    # Sum across full blocks
    sum_blocks = min_val * cycle_len * (
        k_blocks * p + cycle_len * k_blocks * (k_blocks - 1) // 2
    ) + k_blocks * sum_f_b

    # Sum across the final suffix
    sum_suffix_fb = sum(f_b[1 : rem_suffix + 1])
    sum_suffix = (
        min_val * (p + k_blocks * cycle_len) * rem_suffix + sum_suffix_fb
    )

    return t_prefix + sum_blocks + sum_suffix


if __name__ == "__main__":
    print(solve())
