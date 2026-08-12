def solve(limit: int = 50000000) -> int:
    """Find how many numbers below limit can be expressed as p1^2 + p2^3 + p3^4 for primes p1, p2, p3.
    
    Time Complexity: O(P1 * P2 * P3)
    Space Complexity: O(limit)
    """
    max_p = int(limit**0.5) + 1
    is_p = [True] * max_p
    is_p[0] = is_p[1] = False
    for i in range(2, int(max_p**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, max_p, i):
                is_p[j] = False

    primes = [i for i in range(max_p) if is_p[i]]

    expressible = set()

    for p3 in primes:
        p3_4 = p3**4
        if p3_4 >= limit:
            break
        for p2 in primes:
            p2_3 = p2**3
            if p3_4 + p2_3 >= limit:
                break
            for p1 in primes:
                val = p3_4 + p2_3 + p1**2
                if val >= limit:
                    break
                expressible.add(val)

    return len(expressible)
