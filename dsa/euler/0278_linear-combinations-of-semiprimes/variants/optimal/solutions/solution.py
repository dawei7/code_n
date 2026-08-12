def solve(limit: int = 5000) -> int:
    """Find sum(f(p*q, p*r, q*r)) for all primes p < q < r < 5000 where f(pq, pr, qr) = 2*p*q*r - (pq + pr + qr).
    
    Time Complexity: O(pi(limit)^3) or O(pi(limit)^2) via Prefix Sums
    Space Complexity: O(pi(limit))
    """
    is_p = bytearray([1]) * (limit + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            is_p[i * i :: i] = b"\x00" * len(is_p[i * i :: i])
    primes = [i for i in range(2, limit + 1) if is_p[i]]
    N = len(primes)

    ans = 0
    for i in range(N):
        pi = primes[i]
        for j in range(i + 1, N):
            pj = primes[j]
            pipj = pi * pj
            pi_plus_pj = pi + pj
            for k in range(j + 1, N):
                pk = primes[k]
                ans += 2 * pipj * pk - pipj - pi_plus_pj * pk

    return ans
