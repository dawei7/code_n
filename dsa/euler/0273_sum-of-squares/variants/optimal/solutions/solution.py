import math


def solve(limit_prime: int = 150) -> int:
    """Find sum(S(N)) for all squarefree N only divisible by primes p = 1 (mod 4) < 150.
    
    Time Complexity: O(3^K) Gaussian integer tree multiplication for K = 16 primes
    Space Complexity: O(2^K)
    """

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [p for p in range(2, limit_prime) if is_prime(p) and p % 4 == 1]
    gaussian_primes = []
    for p in primes:
        for a in range(1, int(p**0.5) + 1):
            b2 = p - a * a
            b = math.isqrt(b2)
            if b * b == b2:
                gaussian_primes.append((a, b))
                break

    def mul(g1, g2):
        return (g1[0] * g2[0] - g1[1] * g2[1], g1[0] * g2[1] + g1[1] * g2[0])

    total_S = 0

    def dfs(idx, current_representations):
        nonlocal total_S
        if idx == len(primes):
            if current_representations:
                for a, b in current_representations:
                    total_S += min(abs(a), abs(b))
            return

        # Option 1: exclude prime idx
        dfs(idx + 1, current_representations)

        # Option 2: include prime idx
        g = gaussian_primes[idx]
        g_conj = (g[0], -g[1])
        if not current_representations:
            next_reps = [g]
        else:
            next_reps = []
            for r in current_representations:
                next_reps.append(mul(r, g))
                next_reps.append(mul(r, g_conj))

        dfs(idx + 1, next_reps)

    dfs(0, [])
    return total_S
