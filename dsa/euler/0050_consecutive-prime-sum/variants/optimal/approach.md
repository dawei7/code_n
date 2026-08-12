# Consecutive Prime Sum - Optimal Approach

## Algorithm Explanation

Find the prime below $N = 1000000$ that can be expressed as the sum of the longest sequence of consecutive primes.

1. Generate primes below $N = 1000000$ and build a hash set `prime_set`.
2. Construct prefix sums array `prefix[k] = \sum_{j=0}^{k-1} p_j$.
3. Determine maximum theoretical window length $L_{\max}$ where $\text{prefix}[L_{\max}] < N$.
4. Iterate window length $L$ downwards from $L_{\max}$ to $1$.
5. Test candidate subarray sums $S = \text{prefix}[i + L] - \text{prefix}[i] < N$.
6. The first sum $S \in \text{prime\_set}$ found is guaranteed to have the maximum consecutive prime length.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(P)$ where $P = 78498$ (number of primes $< 10^6$). Runs in $< 0.1\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Prime set and prefix sum array.
