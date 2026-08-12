def solve(
    start: int = 10**14, count: int = 100000, mod: int = 1234567891011
) -> int:
    """Find sum_{n=1..100000} F(a(n)) mod 1234567891011 for primes a(n) starting after 10^14.
    
    Time Complexity: O(count * log(a_max)) via Segmented Sieve & Doubling Fibonacci Fast Ladder
    Space Complexity: O(seg_size)
    """

    def get_primes(s_val, cnt):
        limit = int((s_val + 4 * 10**6) ** 0.5) + 100
        is_p = bytearray([1]) * (limit + 1)
        is_p[0] = is_p[1] = 0
        for i in range(2, int(limit**0.5) + 1):
            if is_p[i]:
                is_p[i * i :: i] = b"\x00" * len(is_p[i * i :: i])
        base_primes = [i for i in range(2, limit + 1) if is_p[i]]

        seg_size = 4 * 10**6
        seg = bytearray([1]) * seg_size
        for p in base_primes:
            min_mult = ((s_val + 1 + p - 1) // p) * p
            first_idx = min_mult - (s_val + 1)
            seg[first_idx::p] = b"\x00" * len(seg[first_idx::p])

        res = []
        for i in range(seg_size):
            if seg[i]:
                res.append(s_val + 1 + i)
                if len(res) == cnt:
                    break
        return res

    primes = get_primes(start, count)

    def fib_pair(n):
        if n == 0:
            return (0, 1)
        a, b = fib_pair(n >> 1)
        c = (a * (2 * b - a)) % mod
        d = (a * a + b * b) % mod
        if n & 1:
            return (d, (c + d) % mod)
        else:
            return (c, d)

    ans = 0
    for p in primes:
        fn, _ = fib_pair(p)
        ans = (ans + fn) % mod

    return ans
