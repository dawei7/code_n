# Goldbach's Other Conjecture - Optimal Approach

## Algorithm Explanation

Find the smallest odd composite number $C$ that cannot be represented as $C = p + 2k^2$ for some prime $p$ and integer $k \ge 1$.

1. Precompute boolean prime table `is_prime` up to $N = 10000$ using Sieve of Eratosthenes.
2. Iterate odd composite integers $C \in \{9, 15, 21, 25, 27, \dots\}$.
3. For each $C$, test integers $k \ge 1$ while $2k^2 < C$:
   - Check if $C - 2k^2$ is prime in $\mathcal{O}(1)$ time using `is_prime`.
4. If no integer $k$ satisfies the relation, $C$ is the first counterexample.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \sqrt{N})$ where $N < 6000$. Runs in $< 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Prime sieve boolean lookup array.
