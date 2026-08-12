def solve(limit: int = 10**11) -> int:
    """Find sum of N <= limit such that f(N) = 420.
    
    Time Complexity: O(primes_1mod4 * valid_cores)
    Space Complexity: O(max_m)
    """
    LIMIT = limit

    def sieve_primes(n):
        is_p = bytearray([1]) * (n + 1)
        is_p[0] = is_p[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if is_p[i]:
                is_p[i * i :: i] = b'\x00' * len(is_p[i * i :: i])
        return [i for i in range(2, n + 1) if is_p[i]]

    primes = sieve_primes(2000000)
    p1 = [p for p in primes if p % 4 == 1]

    MAX_M = 300000
    has_p1 = [False] * (MAX_M + 1)
    for p in p1:
        if p > MAX_M:
            break
        for j in range(p, MAX_M + 1, p):
            has_p1[j] = True

    prefix_sum_M = [0] * (MAX_M + 1)
    curr = 0
    for m in range(1, MAX_M + 1):
        if not has_p1[m]:
            curr += m
        prefix_sum_M[m] = curr

    def get_sum_M(max_m):
        if max_m > MAX_M:
            return 0
        return prefix_sum_M[max_m]

    ans_total = 0

    # 1. Pattern 3: p1^10 * p2^2
    for i in range(len(p1)):
        c1 = p1[i] ** 10
        if c1 > LIMIT:
            break
        for j in range(len(p1)):
            if i == j:
                continue
            core = c1 * (p1[j] ** 2)
            if core > LIMIT:
                break
            max_m = LIMIT // core
            ans_total += core * get_sum_M(max_m)

    # 2. Pattern 4: p1^7 * p2^3
    for i in range(len(p1)):
        c1 = p1[i] ** 7
        if c1 > LIMIT:
            break
        for j in range(len(p1)):
            if i == j:
                continue
            core = c1 * (p1[j] ** 3)
            if core > LIMIT:
                break
            max_m = LIMIT // core
            ans_total += core * get_sum_M(max_m)

    # 3. Pattern 5: p1^3 * p2^2 * p3^1
    for i in range(len(p1)):
        c1 = p1[i] ** 3
        if c1 > LIMIT:
            break
        for j in range(len(p1)):
            if i == j:
                continue
            c2 = c1 * (p1[j] ** 2)
            if c2 > LIMIT:
                break
            for k in range(len(p1)):
                if k == i or k == j:
                    continue
                core = c2 * p1[k]
                if core > LIMIT:
                    break
                max_m = LIMIT // core
                ans_total += core * get_sum_M(max_m)

    return ans_total
