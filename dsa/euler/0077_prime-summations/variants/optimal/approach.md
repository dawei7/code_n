# Prime Summations - Optimal Approach

## Algorithm Explanation

Find the first integer $N$ that can be expressed as a sum of prime numbers in over $5000$ distinct ways.

### Dynamic Programming Formulation:
This is an Unbounded Knapsack problem where the available coin denominations are prime numbers $P = \{2, 3, 5, 7, 11, \dots\}$:

1. Generate primes up to $100$ using Sieve of Eratosthenes.
2. Initialize 1D DP table `dp` of size $101$ with `dp[0] = 1`.
3. For each prime $p \in P$:
   - Transition relation for $i \in [p, 100]$: `dp[i] += dp[i - p]`.
4. Iterate $target \in [2, 100]$ and return the first $target$ with `dp[target] > 5000`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot |P|)$ where $N = 100$ and $|P| = 25$ primes. Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - 1D DP table.
