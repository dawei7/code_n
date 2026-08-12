# Crazy Function - Optimal Approach

## Algorithm Explanation

Find the last 9 digits of $S(21^7, 7^{21}, 12^7) \bmod 10^9$, where $S(a, b, c) = \sum_{n=0}^{b} F(n)$ for the recursively defined function $F(n) = n - c$ for $n > b$ and $F(n) = F(a + F(a + F(a + F(a + n))))$ for $n \le b$.

### Linear Block Reduction & Closed-Form Arithmetic Progression:
1. **Linear Unfolding of $F(n)$**:
   For $n \le b$, each 4-fold nesting step simplifies to:
   $$F(n) = F(n + a) + 4a - 3c$$
   Let $k = \left\lfloor \frac{b - n}{a} \right\rfloor + 1$. Unrolling the recursion yields:
   $$F(n) = n - c + k(4a - 3c)$$
2. **Interval Summation**:
   Partitioning the domain $n \in [0, b]$ into $a$-sized blocks where $k$ is constant allows summing $n - c + k(4a - 3c)$ as a sum of arithmetic progressions in $\mathcal{O}(1)$ time using modular big-integer arithmetic.
3. **Execution**:
   Evaluating $S(21^7, 7^{21}, 12^7) \bmod 10^9$ yields $291504964$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$. Runs in $\approx 0.00\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
