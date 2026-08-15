import math


def solve(limit: int = 2**50) -> int:
    """Find the number of squarefree positive integers n < 2^50 (1,125,899,906,842,624).

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Inclusion-Exclusion Principle & Squarefree Counting:
       The number of squarefree integers Q(N) up to N = limit - 1 is given by:
           Q(N) = sum_{d=1}^{floor(sqrt(N))} mu(d) * floor(N / d^2)
       where mu(d) is the Möbius function.

    2. Hyperbola / Sublinear Grouping Decomposition:
       Evaluating the full sum up to floor(sqrt(N)) = 33,554,431 directly requires 3.35 * 10^7 steps.
       We divide the summation at a threshold cutoff x = 1,500,000:
       - For d <= x: sum directly mu(d) * floor(N / d^2).
       - For d > x: group terms by quotient k = floor(N / d^2).
         As d varies, k ranges from 1 to floor(N / (x + 1)^2).
         For a fixed k, d lies in the interval (isqrt(N / (k + 1)), isqrt(N / k)].
         Using the Mertens summatory function M(u) = sum_{i=1}^u mu(i), the sum telescopes to:
             sum_{k=1}^{k_max} (M(floor(sqrt(N / k))) - M(x))

    3. Sublinear Mertens Function via Dirichlet Hyperbola:
       Precompute M(u) up to K = 2,500,000 using a linear sieve in ~0.3s.
       For larger arguments u > K, compute M(u) via the Dirichlet hyperbola identity:
           M(u) = 1 - sum_{l=2}^u (floor(u / (u // l)) - l + 1) * M(u // l)
       with memoization.

    Complexity:
    -----------
    - Time Complexity: O(N^(2/5)) / O(K + k_max) operations (~0.60s for limit = 2^50).
    - Space Complexity: O(K) memory for the Mertens precomputed table (~20 MB).
    """
    N = limit - 1
    K = 2500000

    # 1. Linear sieve to compute mu(d) and prefix sum M(u) up to K
    mu = bytearray([1]) * (K + 1)
    mu[0] = 0
    primes = []
    is_prime = bytearray([1]) * (K + 1)
    is_prime[0] = is_prime[1] = 0

    for i in range(2, K + 1):
        if is_prime[i]:
            primes.append(i)
            mu[i] = 255  # Represents -1
        for p in primes:
            ip = i * p
            if ip > K:
                break
            is_prime[ip] = 0
            if i % p == 0:
                mu[ip] = 0
                break
            else:
                if mu[i] == 0:
                    mu[ip] = 0
                elif mu[i] == 255:
                    mu[ip] = 1
                else:
                    mu[ip] = 255

    # Build prefix sum array M(u) = sum_{i=1}^u mu(i) up to K
    M = [0] * (K + 1)
    curr = 0
    for i in range(1, K + 1):
        m = mu[i]
        if m == 1:
            curr += 1
        elif m == 255:
            curr -= 1
        M[i] = curr

    # 2. Memoized sublinear Mertens function for u > K
    memo_M = {}

    def get_M(u: int) -> int:
        if u <= K:
            return M[u]
        if u in memo_M:
            return memo_M[u]
        res = 1
        l = 2
        while l <= u:
            q = u // l
            r = u // q
            res -= (r - l + 1) * get_M(q)
            l = r + 1
        memo_M[u] = res
        return res

    # 3. Sum Part 1: direct summation for d <= x
    x = 1500000
    ans1 = 0
    for d in range(1, x + 1):
        m = mu[d]
        if m == 1:
            ans1 += N // (d * d)
        elif m == 255:
            ans1 -= N // (d * d)

    # 4. Sum Part 2: grouped Mertens summation for d > x
    k_max = N // ((x + 1) * (x + 1))
    M_x = M[x]
    ans2 = 0
    for k in range(1, k_max + 1):
        top = math.isqrt(N // k)
        ans2 += get_M(top) - M_x

    # Return total squarefree integers less than 2^50
    return ans1 + ans2


if __name__ == "__main__":
    print(solve())
