def solve(target_index: int = 150000) -> int:
    """Find the N-th Alexandrian integer.
    
    Time Complexity: O(P * sqrt(P^2 + 1)) where P ~ 200,000
    Space Complexity: O(P * d_avg)
    """
    MAX_P = 200000
    alex = []

    for p in range(1, MAX_P + 1):
        val = p * p + 1
        d1 = 1
        while d1 * d1 <= val:
            if val % d1 == 0:
                d2 = val // d1
                A = p * (p + d1) * (p + d2)
                if 0 < A < 9000000000000000000:
                    alex.append(A)
            d1 += 1

    alex.sort()
    # Remove duplicates
    unique_alex = []
    prev = None
    for x in alex:
        if x != prev:
            unique_alex.append(x)
            prev = x

    return unique_alex[target_index - 1]
