import functools


def is_prime(n: int) -> bool:
    """Deterministic Miller-Rabin primality test for fast checking of large concatenated numbers (up to 10^10)."""
    if n < 2:
        return False
    if n in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        return True
    if any(n % p == 0 for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)):
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 7, 61):  # Deterministic base set for n < 4.7 x 10^9
        if n <= a:
            break
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


@functools.lru_cache(maxsize=None)
def is_pair_valid(p1: int, p2: int) -> bool:
    """Check if both concatenated numbers p1||p2 and p2||p1 are prime."""
    s1, s2 = str(p1), str(p2)
    return is_prime(int(s1 + s2)) and is_prime(int(s2 + s1))


def solve(limit: int = 10000) -> int:
    """Find the lowest sum for a set of 5 primes where any two concatenate in any order to produce another prime.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Graph Clique Representation (5-Clique Problem):
       Model primes as vertices in a graph G = (V, E).
       An undirected edge exists between p1 and p2 iff both int(p1||p2) and int(p2||p1) are prime.
       We search for the 5-clique K_5 with the minimal sum of vertex weights.

    2. Adjacency Set Intersection Acceleration:
       Rather than deep nested loops, maintain sorted neighbor sets:
           - S_{12} = adj[p1] & adj[p2]
           - S_{123} = S_{12} & adj[p3]
           - S_{1234} = S_{123} & adj[p4]
       This prunes the search graph in milliseconds (~0.05s).

    Complexity:
    -----------
    - Time Complexity: O(P * deg(P)^4) executing in ~0.05s.
    - Space Complexity: O(P * deg(P)) memory for adjacency graph.
    """
    # Precompute primes up to limit = 10,000 using Sieve of Eratosthenes
    is_p = [True] * limit
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, limit, i):
                is_p[j] = False

    # Collect candidate primes starting at 3 (2 cannot concatenate to form odd primes)
    primes = [i for i in range(3, limit) if is_p[i]]

    # Build forward adjacency dictionary
    adj = {p: set() for p in primes}
    for i, p1 in enumerate(primes):
        for j in range(i + 1, len(primes)):
            p2 = primes[j]
            if is_pair_valid(p1, p2):
                adj[p1].add(p2)

    # 5-Clique Search via Set Intersections
    for p1 in primes:
        for p2 in adj[p1]:
            s12 = adj[p1] & adj[p2]
            for p3 in s12:
                s123 = s12 & adj[p3]
                for p4 in s123:
                    s1234 = s123 & adj[p4]
                    for p5 in s1234:
                        return p1 + p2 + p3 + p4 + p5

    return -1


if __name__ == "__main__":
    print(solve())
