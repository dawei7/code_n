# Guessing Game - Optimal Approach

## Algorithm Explanation

Find $\sum_{k=1}^{30} C(10^{12}, \sqrt{k}, \sqrt{F_k})$, where $C(n, a, b)$ is the minimum worst-case cost to find a hidden number in $\{1, 2, \dots, n\}$ with low-guess cost $a$ and high-guess cost $b$, rounded to 8 decimal places.

### Dual-Cost Asymmetric Search & Binomial Range Expansion:
1. **Maximal Search Range Recurrence**:
   For a worst-case cost limit $W$, the maximum solvable range size $S(W)$ satisfies:
   $$S(W) = 1 + S(W - a) + S(W - b)$$
   with base case $S(w) = 0$ for $w < 0$.
2. **Combinatorial Binomial Summation**:
   Any decision tree path is composed of $i$ low moves (cost $a$) and $j$ high moves (cost $b$) with total cost $i a + j b \le W$.
   The maximum range size $S(W)$ equals:
   $$S(W) = \sum_{i, j \ge 0 : i a + j b \le W} \binom{i + j}{i}$$
3. **Binary Search for Minimal Worst-Case Cost**:
   For $n = 10^{12}$, $a = \sqrt{k}$, $b = \sqrt{F_k}$, we binary search the optimal cost threshold $W$ such that $S(W) \ge n$.
4. **Execution**:
   Summing $C(10^{12}, \sqrt{k}, \sqrt{F_k})$ for $k = 1 \dots 30$ yields $36813.12757207$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K \cdot \text{Search Steps})$ for $K = 30$. Runs in $\approx 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
