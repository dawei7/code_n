def solve(limit: int = 2 * 10**11) -> int:
    """Find the sum of all composite integers 1 < n <= limit for which C(n) is a unit fraction.
    
    Time Complexity: O(sqrt(limit) * log(limit)) via algebraic prefix completion
    Space Complexity: O(sqrt(limit))
    """
    if limit < 4:
        return 0

    sqrt_limit = int(limit**0.5)

    sieve = [True] * (sqrt_limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(sqrt_limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, sqrt_limit + 1, i):
                sieve[j] = False
    primes = [i for i in range(sqrt_limit + 1) if sieve[i]]

    def is_prime(n: int) -> bool:
        if n <= sqrt_limit:
            return sieve[n]
        if n % 2 == 0 or n % 3 == 0:
            return False
        d = 5
        while d * d <= n:
            if n % d == 0 or n % (d + 2) == 0:
                return False
            d += 6
        return True

    mod3_primes = [p for p in primes if p == 3 or p % 3 == 1]

    def get_divisors_mod3(val: int):
        temp = val
        factors = []
        for q in mod3_primes:
            if q * q > temp:
                break
            if temp % q == 0:
                cnt = 0
                while temp % q == 0:
                    cnt += 1
                    temp //= q
                factors.append((q, cnt))
        if temp > 1:
            factors.append((temp, 1))

        divs = [1]
        for p, count in factors:
            next_divs = []
            p_pow = 1
            for _ in range(count + 1):
                for div in divs:
                    next_divs.append(div * p_pow)
                p_pow *= p
            divs = next_divs
        return divs

    def get_divisors_gen(temp: int):
        factors = []
        d = 2
        while d * d <= temp:
            if temp % d == 0:
                cnt = 0
                while temp % d == 0:
                    cnt += 1
                    temp //= d
                factors.append((d, cnt))
            d += 1
        if temp > 1:
            factors.append((temp, 1))

        divs = [1]
        for p, count in factors:
            next_divs = []
            p_pow = 1
            for _ in range(count + 1):
                for div in divs:
                    next_divs.append(div * p_pow)
                p_pow *= p
            divs = next_divs
        return divs

    sol_set = set()

    def complete_prefix(m: int, phi_m: int, last_p: int, is_mod3: bool = False):
        A = m - phi_m
        B = phi_m
        V = m * B + A
        divs = get_divisors_mod3(V) if is_mod3 else get_divisors_gen(V)
        for d in divs:
            if d > B and (d - B) % A == 0:
                p_last = (d - B) // A
                if p_last > last_p and m * p_last <= limit:
                    if is_prime(p_last):
                        sol_set.add(m * p_last)

    # 1-prime prefix (for 2-prime solutions p1 * p2)
    for p1 in primes:
        if p1 * p1 > limit:
            break
        complete_prefix(p1, p1 - 1, p1, is_mod3=True)

    # 2-prime prefix (for 3-prime solutions)
    for i in range(len(primes)):
        p1 = primes[i]
        if p1 * p1 * p1 > limit:
            break
        for j in range(i + 1, len(primes)):
            p2 = primes[j]
            if p1 * p2 * p2 > limit:
                break
            complete_prefix(p1 * p2, (p1 - 1) * (p2 - 1), p2)

    # 3-prime prefix (for 4-prime solutions)
    for i in range(len(primes)):
        p1 = primes[i]
        if p1**4 > limit:
            break
        for j in range(i + 1, len(primes)):
            p2 = primes[j]
            if p1 * p2 * p2 * p2 > limit:
                break
            for k_idx in range(j + 1, len(primes)):
                p3 = primes[k_idx]
                if p1 * p2 * p3 * p3 > limit:
                    break
                complete_prefix(p1 * p2 * p3, (p1 - 1) * (p2 - 1) * (p3 - 1), p3)

    return sum(sol_set)

