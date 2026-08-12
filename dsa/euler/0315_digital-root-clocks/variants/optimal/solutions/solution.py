def solve(a: int = 10**7, b: int = 2 * 10**7) -> int:
    """Find the difference in transition counts between Sam's and Max's clocks for primes in [10^7, 2*10^7].
    
    Time Complexity: O(pi(B)) via Bitwise Segment Mask Intersection
    Space Complexity: O(B)
    """
    d_0 = {0, 1, 2, 4, 5, 6}
    d_1 = {2, 5}
    d_2 = {0, 2, 3, 4, 6}
    d_3 = {0, 2, 3, 5, 6}
    d_4 = {1, 2, 3, 5}
    d_5 = {0, 1, 3, 5, 6}
    d_6 = {0, 1, 3, 4, 5, 6}
    d_7 = {0, 1, 2, 5}
    d_8 = {0, 1, 2, 3, 4, 5, 6}
    d_9 = {0, 1, 2, 3, 5, 6}

    digits = [d_0, d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9]
    masks = [sum(1 << seg for seg in d) for d in digits]

    def sieve_primes(n_max):
        is_p = bytearray([1]) * (n_max + 1)
        is_p[0] = is_p[1] = 0
        for i in range(2, int(n_max**0.5) + 1):
            if is_p[i]:
                is_p[i * i :: i] = b"\x00" * len(is_p[i * i :: i])
        return [i for i in range(a, n_max + 1) if is_p[i]]

    primes = sieve_primes(b)
    total_saved = 0

    for p in primes:
        curr = p
        while curr >= 10:
            next_curr = sum(int(c) for c in str(curr))
            s1 = [int(c) for c in str(curr)]
            s2 = [int(c) for c in str(next_curr)]
            shared = 0
            for d1, d2 in zip(reversed(s1), reversed(s2)):
                shared += bin(masks[d1] & masks[d2]).count("1")
            total_saved += 2 * shared
            curr = next_curr

    return total_saved
