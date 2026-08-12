from collections import defaultdict


def solve() -> int:
    """Find the 12-digit number formed by concatenating the other 4-digit prime permutation arithmetic sequence.
    
    Time Complexity: O(P^2)
    Space Complexity: O(P)
    """
    limit = 10000
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    groups = defaultdict(list)
    for p in range(1000, 10000):
        if is_prime[p]:
            key = "".join(sorted(str(p)))
            groups[key].append(p)

    for key, primes in groups.items():
        if len(primes) >= 3:
            s_primes = sorted(primes)
            for i in range(len(s_primes)):
                for j in range(i + 1, len(s_primes)):
                    p1, p2 = s_primes[i], s_primes[j]
                    p3 = 2 * p2 - p1
                    if p3 in s_primes and p1 != 1487:
                        return int(f"{p1}{p2}{p3}")

    return -1
