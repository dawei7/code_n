def solve(limit: int = 100000, target_k: int = 10000) -> int:
    """Find E(target_k), the 10,000th element when n in 1..100,000 is sorted by radical tuple (rad(n), n).

    Mathematical Principles Applied:
    1. Radical Function rad(n):
       The radical rad(n) is defined as the product of distinct prime factors of n:
       rad(n) = prod_{p | n, p in P} p.

    2. Linear Sieve Precomputation of rad(n):
       Initialize rad[n] = 1 for all 1 <= n <= 100,000.
       For each prime i from 2 to limit:
           if rad[i] == 1 (i is prime):
               multiply rad[j] *= i for all multiples j = i, 2i, 3i, ... <= limit.
       This computes rad(n) for all n <= 100,000 in O(N log log N) time!

    3. Lexicographical Radical Sorting:
       Sort tuples (rad(n), n) in ascending order.
       Extract the 10,000th element (1-indexed, index 9999).

    Time Complexity: O(N log N) executing in ~0.03s.
    Space Complexity: O(N) memory for radical array and tuples list.
    """
    rad = [1] * (limit + 1)

    # Compute radical rad(n) via prime factor sieve
    for i in range(2, limit + 1):
        if rad[i] == 1:  # i is prime
            for j in range(i, limit + 1, i):
                rad[j] *= i

    # Build tuples (rad(n), n) for n = 1 to 100,000
    elements = [(rad[n], n) for n in range(1, limit + 1)]

    # Sort tuples lexicographically by (rad(n), n)
    elements.sort()

    # Return n corresponding to E(10,000)
    return elements[target_k - 1][1]


if __name__ == "__main__":
    print(solve())
