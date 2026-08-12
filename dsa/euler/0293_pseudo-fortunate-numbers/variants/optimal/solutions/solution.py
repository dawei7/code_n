def solve(limit: int = 10**9) -> int:
    """Find the sum of all distinct pseudo-Fortunate numbers M for admissible N < 10^9.
    
    Time Complexity: O(count(N) * avg_gap)
    Space Complexity: O(count(N))
    """
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    admissible = []

    def generate(idx, current_val):
        if current_val >= limit:
            return
        admissible.append(current_val)
        generate(idx, current_val * primes[idx])
        if idx + 1 < len(primes):
            generate(idx + 1, current_val * primes[idx + 1])

    generate(0, 2)

    def is_prime(n):
        if n < 2:
            return False
        if n in (2, 3, 5, 7):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        d = n - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in (2, 7, 61):
            if n <= a:
                break
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(s - 1):
                x = (x * x) % n
                if x == n - 1:
                    break
            else:
                return False
        return True

    distinct_M = set()
    for N in admissible:
        M = 3
        while not is_prime(N + M):
            M += 2
        distinct_M.add(M)

    return sum(distinct_M)
