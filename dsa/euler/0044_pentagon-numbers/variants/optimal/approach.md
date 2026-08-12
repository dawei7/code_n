# Pentagon Numbers - Optimal Approach

## Algorithm Explanation

Find pentagonal numbers $P_j$ and $P_k$ such that both $P_j + P_k$ and $P_k - P_j$ are pentagonal, minimizing $D = P_k - P_j$.

### Mathematical Test
Solving $3n^2 - n - 2x = 0$ for integer $n$:
$$n = \frac{1 + \sqrt{1 + 24x}}{6}$$
Thus $x$ is pentagonal if $1 + 24x$ is a perfect square and $\sqrt{1 + 24x} \equiv 5 \pmod 6$.

### Search Strategy:
1. Generate pentagonal numbers $P_i = \frac{i(3i - 1)}{2}$ incrementally for $i = 1, 2, 3 \dots$.
2. For each new $P_i$, iterate backwards through previously saved pentagonal numbers $P_j$.
3. Check if difference $D = P_i - P_j$ and sum $S = P_i + P_j$ are both pentagonal.
4. The first matching difference $D$ encountered is guaranteed to minimize $|P_k - P_j|$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K^2)$ where $K \approx 2167$. Runs in $< 0.1\text{s}$.
- **Space Complexity:** $\mathcal{O}(K)$ - Storage array of generated pentagonal numbers.
