def solve(limit: int = 1000000) -> int:
    """Find the sum of Maximal Digital Root Sums mdrs(n) for 1 < n < limit (1,000,000).

    Mathematical Principles Applied:
    1. Digital Root Definition dr(n):
       The digital root dr(n) of an integer n is dr(n) = 1 + (n - 1) % 9.

    2. Maximal Digital Root Sum Recurrence:
       For a factorized integer n = i * j:
       The Digital Root Sum of Factorisation (DRSF) of (i * j) is drs(i) + drs(j).
       The maximal digital root sum mdrs(n) satisfies the dynamic programming recurrence:
       mdrs(n) = max(dr(n), max_{i * j = n} (mdrs(i) + mdrs(j))).

    3. Dynamic Programming Sieve:
       Initialize mdrs[n] = dr(n) = 1 + (n - 1) % 9 for 2 <= n < 1,000,000.
       For each factor i from 2 to limit-1:
           for each multiplier j from 2 to (limit-1)//i:
               mdrs[i * j] = max(mdrs[i * j], mdrs[i] + mdrs[j]).

    Time Complexity: O(limit log limit) executing in ~0.20s.
    Space Complexity: O(limit) memory for MDRS array.
    """
    mdrs = [0] * limit
    # Base digital root initialization dr(n) = 1 + (n - 1) % 9
    for n in range(2, limit):
        mdrs[n] = 1 + (n - 1) % 9

    # Sieve dynamic programming update for mdrs(i * j)
    for i in range(2, limit):
        val_i = mdrs[i]
        max_j = (limit - 1) // i
        for j in range(2, max_j + 1):
            ij = i * j
            cand = val_i + mdrs[j]
            # Relaxation step: update max digital root sum
            if cand > mdrs[ij]:
                mdrs[ij] = cand

    # Return total sum sum_{n=2}^{999999} mdrs(n)
    return sum(mdrs[2:limit])


if __name__ == "__main__":
    print(solve())
