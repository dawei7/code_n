def solve(bounces: int = 12017639147) -> int:
    """Find number of ways a laser beam can bounce off N surfaces and exit at vertex C.
    
    Time Complexity: O(sqrt(N) + 2^omega(N))
    Space Complexity: O(log N)
    """
    k = (bounces + 3) // 2
    rem = (2 * k) % 3

    temp = k
    primes = []
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            primes.append(p)
            while temp % p == 0:
                temp //= p
        p += 1
    if temp > 1:
        primes.append(temp)

    ans = 0
    num_p = len(primes)

    for mask in range(1 << num_p):
        prod = 1
        bits = 0
        for i in range(num_p):
            if (mask >> i) & 1:
                prod *= primes[i]
                bits += 1

        prod_mod3 = prod % 3
        if prod_mod3 == 0:
            count_x = 0
        else:
            m_rem = (rem * prod_mod3) % 3
            max_m = (k - 1) // prod
            if max_m <= 0:
                count_x = 0
            else:
                if m_rem == 0:
                    count_x = max_m // 3
                else:
                    count_x = (max_m - m_rem) // 3 + 1 if max_m >= m_rem else 0

        if bits % 2 == 1:
            ans -= count_x
        else:
            ans += count_x

    return ans
