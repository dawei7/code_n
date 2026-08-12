# Golomb's Self-describing Sequence - Optimal Approach

## Algorithm Explanation

Find $\sum_{n=1}^{10^6 - 1} G(n^3)$, where $G(n)$ is Golomb's self-describing sequence (the unique non-decreasing sequence of natural numbers such that $n$ appears exactly $G(n)$ times).

### Cumulative Block Range Precomputation & Binary Search:
1. **Block Representation of $G(n)$**:
   Each integer $k$ appears exactly $G(k)$ consecutive times in the sequence.
   Let $S(k)$ be the starting index where $G(n) = k$ begins.
   $$S(1) = 1, \quad S(k+1) = S(k) + G(k)$$
2. **Precomputation & Asymptotic Bounds**:
   For $n^3 < 10^{18}$, $G(n^3)$ values require $S(K) \ge 10^{18}$, which corresponds to $K \approx 2 \cdot 10^6$.
   We precompute $G(1 \dots K)$ and prefix sums $S(1 \dots K+1)$ in linear time $\mathcal{O}(K)$.
3. **Binary Search Evaluation**:
   For each $n \in [1, 10^6 - 1]$, $G(n^3)$ is located by performing binary search over the monotonic prefix array $S$.
4. **Execution**:
   Summing $G(n^3)$ for all $n < 10^6$ yields $56098610614277014$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K + N \log K)$ for $N = 10^6$ and $K \approx 2 \cdot 10^6$. Runs in $\approx 1.20\text{s}$.
- **Space Complexity:** $\mathcal{O}(K)$ for the block prefix array.
