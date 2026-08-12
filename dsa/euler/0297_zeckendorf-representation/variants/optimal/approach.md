# Zeckendorf Representation - Optimal Approach

## Algorithm Explanation

Find $\sum_{n=1}^{10^{17}-1} z(n)$, where $z(n)$ is the number of terms in the Zeckendorf representation of $n$ (unique representation of $n$ as a sum of non-consecutive Fibonacci numbers starting $1, 2, 3, 5, 8, \dots$).

### Divide-and-Conquer Fibonacci Recurrence:
1. **Zeckendorf Self-Similarity**:
   For any integer $N$, let $F_k$ be the largest Fibonacci number strictly less than $N$.
   Every integer $n \in [F_k, N-1]$ can be written as $n = F_k + m$ for $0 \le m < N - F_k$.
   Its Zeckendorf representation consists of $F_k$ plus the Zeckendorf representation of $m$.
   Thus:
   $$S(N) = S(F_k) + (N - F_k) + S(N - F_k)$$
   where $S(N) = \sum_{n=1}^{N-1} z(n)$.
2. **Memoized Recursion**:
   We evaluate $S(10^{17})$ by recursively decomposing $N$ into largest Fibonacci components $F_k < N$.
3. **Execution**:
   Running memoized divide-and-conquer for $N = 10^{17}$ yields $2252639041804718029$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log_\phi N)$ for $N = 10^{17}$. Runs in $\approx 0.00\text{s}$.
- **Space Complexity:** $\mathcal{O}(\log_\phi N)$ memoization table.
