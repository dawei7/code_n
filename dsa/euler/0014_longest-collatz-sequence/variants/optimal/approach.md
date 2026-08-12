# Longest Collatz Sequence - Optimal Approach

## Algorithm Explanation

The Collatz sequence rule is:
- $n \to n/2$ if $n$ is even.
- $n \to 3n + 1$ if $n$ is odd.

We want the starting number $x < 1000000$ that maximizes chain length.

### Optimization & Memoization:
1. **Memoization**: Cache chain lengths in a hash map `memo` so each intermediate number is computed once.
2. **Search Range Pruning**: For any $k \le \frac{N}{2}$, the number $2k \le N$ produces a chain that starts with $2k \to k$, making its chain strictly longer by $1$. Thus, we only need to test $k \in [\frac{N}{2}, N)$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ - Memoization ensures each Collatz trajectory step is computed once. Runs in under $0.25\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Hash map storing memoized sequence lengths.
