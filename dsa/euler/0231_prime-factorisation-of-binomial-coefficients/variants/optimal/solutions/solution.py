def solve(n: int = 20000000, k: int = 15000000) -> int:
    """Find the sum of terms in the prime factorisation of C(n, k).
    
    Time Complexity: O(n * log(log(n)))
    Space Complexity: O(n)
    """
    N = n
    K = k
    NK = N - K

    is_p = bytearray([1]) * (N + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(N**0.5) + 1):
        if is_p[i]:
            is_p[i * i :: i] = b'\x00' * len(is_p[i * i :: i])

    primes = [i for i in range(2, N + 1) if is_p[i]]

    def leg(num, p):
        cnt = 0
        p_pow = p
        while p_pow <= num:
            cnt += num // p_pow
            p_pow *= p
        return cnt

    ans = 0
    for p in primes:
        e_p = leg(N, p) - leg(K, p) - leg(NK, p)
        if e_p > 0:
            ans += e_p * p

    return ans
