def solve(n: int = 2000000000) -> int:
    """Find M(2*10^9) for the sum of minimums over all contiguous subsequences of pseudo-random generator S_n.

    Time Complexity: O(P) where P = 6308948 period length via Monotonic Stack Periodicity Extrapolation
    Space Complexity: O(P)
    """
    MOD = 50515093
    S0 = 290797
    P = 6308948

    # Find global minimum value and its 1-based index in the first period
    curr = S0
    min_val = MOD + 1
    m = -1
    seq_P = []
    for i in range(1, P + 1):
        curr = (curr * curr) % MOD
        seq_P.append(curr)
        if curr < min_val:
            min_val = curr
            m = i

    if n <= m:
        # Small n: direct monotonic stack calculation
        curr = S0
        stack: list[tuple[int, int]] = []
        total_sum = 0
        current_sum = 0
        for _ in range(n):
            curr = (curr * curr) % MOD
            count = 1
            while stack and stack[-1][0] >= curr:
                val, cnt = stack.pop()
                current_sum -= val * cnt
                count += cnt
            stack.append((curr, count))
            current_sum += curr * count
            total_sum += current_sum
        return total_sum

    # Phase 1: Sum from 1 to m (prefix up to the first global minimum)
    curr = S0
    stack = []
    total_sum_m = 0
    current_sum = 0
    for i in range(1, m + 1):
        curr = (curr * curr) % MOD
        count = 1
        while stack and stack[-1][0] >= curr:
            val, cnt = stack.pop()
            current_sum -= val * cnt
            count += cnt
        stack.append((curr, count))
        current_sum += curr * count
        total_sum_m += current_sum

    # Phase 2: Circularly shift the period so it starts right after index m (min_val at the end)
    T = seq_P[m:] + seq_P[:m]

    # Precompute local stack sums for one full period T
    local_sum_list = []
    local_stack: list[tuple[int, int]] = []
    curr_local_sum = 0
    for val in T:
        count = 1
        while local_stack and local_stack[-1][0] >= val:
            v, c = local_stack.pop()
            curr_local_sum -= v * c
            count += c
        local_stack.append((val, count))
        curr_local_sum += val * count
        local_sum_list.append(curr_local_sum)

    sum_local_full = sum(local_sum_list)

    # Phase 3: Extrapolate for all full periods and remaining steps after index m
    num_full_periods = (n - m) // P
    rem_steps = (n - m) % P

    ans = total_sum_m

    K = num_full_periods
    if K > 0:
        base_sum_k = K * m + P * (K * (K - 1) // 2)
        ans += P * min_val * base_sum_k + K * sum_local_full

    if rem_steps > 0:
        B = m + K * P
        ans += rem_steps * min_val * B + sum(local_sum_list[:rem_steps])

    return ans
