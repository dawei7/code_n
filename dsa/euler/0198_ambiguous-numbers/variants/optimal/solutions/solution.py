def solve(limit: int = 10**8) -> int:
    """Find number of ambiguous numbers x in (0, 1/100) with denominator <= limit.
    
    Time Complexity: O(limit^0.5) with Stern-Brocot tree acceleration.
    Space Complexity: O(limit^0.5)
    """
    limit_q = limit
    ans = 0
    stack = [(1, 100)]

    while stack:
        q1, q2 = stack.pop()
        if 2 * q1 * q2 > limit_q:
            continue

        ans += 1

        k_max = (limit_q // (2 * q1) - q2) // q1
        if k_max > 0:
            ans += k_max
            for k in range(1, k_max + 1):
                new_q2 = q2 + k * q1
                new_q1 = q1 + new_q2
                if 2 * new_q1 * new_q2 <= limit_q:
                    stack.append((new_q1, new_q2))

        new_q1 = q1 + q2
        if 2 * new_q1 * q2 <= limit_q:
            stack.append((new_q1, q2))

    return ans
