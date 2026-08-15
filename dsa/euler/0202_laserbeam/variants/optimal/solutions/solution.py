def solve(bounces: int = 12017639147) -> int:
    """Find number of ways a laser beam can bounce off N surfaces and exit at vertex C.

    Mathematical Principles Applied:
    1. Triangular Tiling Unfolding:
       By unfolding the triangular room under reflections across sides, the laser trajectory is mapped
       to a straight line in an equilateral triangular lattice grid.
       The number of reflections N corresponds to lattice points (x, y) at grid distance x + y = k,
       where k = (N + 3) / 2.

    2. Exit Vertex C Condition:
       The laser beam exits at vertex C iff:
       - x > 0, y > 0
       - gcd(x, y) = 1 (coprime, so the beam hits no intermediate vertex)
       - x = (N + 3)/2 mod 3 (or 2*k % 3) to land specifically on vertex C!

    3. Inclusion-Exclusion Principle over Prime Factors of k:
       Since x + y = k, gcd(x, y) = 1 iff gcd(x, k) = 1.
       We factor k into distinct prime factors {p_1, p_2, ..., p_m}.
       By inclusion-exclusion, count x in (0, k) coprime to k with x = rem (mod 3).

    Time Complexity: O(sqrt(k) + 2^omega(k)) executing in ~0.0001s.
    Space Complexity: O(log k) auxiliary space.
    """
    k = (bounces + 3) // 2
    rem = (2 * k) % 3

    # Prime factorization of k
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

    # Inclusion-Exclusion Principle over subsets of prime factors
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

        # Sign flips based on parity of inclusion-exclusion subset size
        if bits % 2 == 1:
            ans -= count_x
        else:
            ans += count_x

    # Return total number of valid laserbeam trajectories
    return ans


if __name__ == "__main__":
    print(solve())
