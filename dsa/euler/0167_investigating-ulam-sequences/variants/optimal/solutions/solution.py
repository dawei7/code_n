def ulam_kth_fast(v: int, target_k: int) -> int:
    """Find target_k-th element of Ulam sequence U(2, v) for odd v >= 5 using LFSR period detection."""
    u = [2, v]
    count_map = {2 + v: 1}
    evens = [2]
    curr = v
    while len(evens) < 2:
        curr += 1
        while count_map.get(curr, 0) != 1:
            curr += 1
        u.append(curr)
        if curr % 2 == 0:
            evens.append(curr)
        for x in u[:-1]:
            s = x + curr
            count_map[s] = count_map.get(s, 0) + 1

    E = evens[1]
    e_idx = u.index(E)
    e = E // 2

    # Bit array of odd terms up to E-1 (m = 0 .. e-1 representing odds 1 .. E-1)
    B_init = [0] * e
    for x in u:
        if x % 2 != 0:
            B_init[(x - 1) // 2] = 1

    state = 0
    for i in range(e):
        if B_init[i]:
            state |= (1 << i)

    seen_states = {}
    m = e
    b_prev = B_init[e - 1]

    history = []

    while state not in seen_states:
        seen_states[state] = len(history)

        bit_oldest = state & 1
        bit_new = b_prev ^ bit_oldest

        history.append((state, bit_new, m))

        state = (state >> 1) | (bit_new << (e - 1))
        b_prev = bit_new
        m += 1

    period_start = seen_states[state]
    period_history = history[period_start:]

    P_bits = len(period_history)
    P_terms = sum(b for _, b, _ in period_history)
    P_sum = 2 * P_bits

    rem_k = target_k - (e_idx + 1)

    prefix_history = history[:period_start]
    prefix_terms = sum(b for _, b, _ in prefix_history)

    if rem_k <= prefix_terms:
        c = 0
        for _, b, m_val in prefix_history:
            if b:
                c += 1
                if c == rem_k:
                    return 2 * m_val + 1

    rem_k -= prefix_terms
    full_periods = rem_k // P_terms
    rem_in_period = rem_k % P_terms

    if rem_in_period == 0:
        full_periods -= 1
        rem_in_period = P_terms

    c = 0
    target_m_in_period = 0

    for _, b, m_val in period_history:
        if b:
            c += 1
            if c == rem_in_period:
                target_m_in_period = m_val
                break

    return (2 * target_m_in_period + 1) + full_periods * P_sum


def solve(target_k: int = 10**11) -> int:
    """Find sum of U(2, 2n+1)_k for 2 <= n <= 10 and k = 10^11.
    
    Time Complexity: O(Period_Length) per sequence
    Space Complexity: O(Period_Length)
    """
    return sum(ulam_kth_fast(2 * n + 1, target_k) for n in range(2, 11))
