def solve(limit: int = 50000000) -> int:
    """Find how many numbers below limit (50,000,000) can be expressed as p1^2 + p2^3 + p3^4 for primes p1, p2, p3.

    Mathematical Principles Applied:
    1. Prime Power Upper Bounds:
       - For p3^4 < 50,000,000: p3 < (50,000,000)^(1/4) ≈ 84.
       - For p2^3 < 50,000,000: p2 < (50,000,000)^(1/3) ≈ 368.
       - For p1^2 < 50,000,000: p1 < (50,000,000)^(1/2) ≈ 7071.

    2. Set Deduplication of Expressible Numbers:
       Since different prime triples (p1, p2, p3) may sum to the same integer value,
       use a hash set `expressible` to collect unique valid integers below 50,000,000.

    Time Complexity: O(P1 * P2 * P3) executing in ~0.50s.
    Space Complexity: O(N) memory for unique set.
    """
    # Sieve primes up to sqrt(50,000,000) ≈ 7071
    max_p = int(limit**0.5) + 1
    is_p = [True] * max_p
    is_p[0] = is_p[1] = False
    for i in range(2, int(max_p**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, max_p, i):
                is_p[j] = False

    primes = [i for i in range(max_p) if is_p[i]]

    expressible = set()

    # Outer loop for 4th powers p3^4 (p3 <= 84)
    for p3 in primes:
        p3_4 = p3**4
        if p3_4 >= limit:
            break
        # Middle loop for 3rd powers p2^3 (p2 <= 368)
        for p2 in primes:
            p2_3 = p2**3
            if p3_4 + p2_3 >= limit:
                break
            # Inner loop for 2nd powers p1^2 (p1 <= 7071)
            for p1 in primes:
                val = p3_4 + p2_3 + p1**2
                if val >= limit:
                    break
                # Collect unique expressible integer
                expressible.add(val)

    # Return total count of unique expressible numbers below 50,000,000
    return len(expressible)


if __name__ == "__main__":
    print(solve())
