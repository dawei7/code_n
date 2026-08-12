def solve(limit: int = 50000000) -> int:
    """Find number of n < limit with exactly one solution to x^2 - y^2 - z^2 = n using prime classification.
    
    Time Complexity: O(limit)
    Space Complexity: O(limit)
    """
    is_p = [True] * limit
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, limit, i):
                is_p[j] = False

    count = 0

    # Special powers of 2
    if 4 < limit:
        count += 1
    if 16 < limit:
        count += 1

    # 1. n = p where p prime and p % 4 == 3
    # 2. n = 4p where p is odd prime (p < limit / 4)
    # 3. n = 16p where p is odd prime (p < limit / 16)
    for p in range(2, limit):
        if is_p[p]:
            # Form 1
            if p % 4 == 3:
                count += 1

            # Form 2
            if p > 2 and 4 * p < limit:
                count += 1

            # Form 3
            if p > 2 and 16 * p < limit:
                count += 1

    return count
