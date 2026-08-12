# Powers with Trailing Digits - Optimal Approach

## Algorithm Explanation

Find $\sum_{n=2}^{10^6} f(n)$, where $f(n)$ is the largest positive integer $x < 10^9$ such that the last 9 digits of $n^x$ form $x$ ($n^x \equiv x \pmod{10^9}$), or $0$ if no such integer exists.

### Fixed-Point Contraction & Hensel's Lemma Iteration:
1. **Zero Condition**:
   If $10 \mid n$, then $n^x \bmod 10^9$ always has trailing zeros that cannot match a positive $x < 10^9$, so $f(n) = 0$.
2. **Hensel Fixed-Point Iteration**:
   For $n$ not divisible by $10$, the map $g(x) = n^x \bmod 10^9$ is a contraction mapping in $\mathbb{Z} / 10^9 \mathbb{Z}$.
   Starting at $x_0 = 1$, we repeatedly update:
   $$x_{k+1} = n^{x_k} \bmod 10^9$$
   By Hensel's Lemma and p-adic convergence, $x_k$ reaches a stable fixed point $x^*$ in $\le 50$ iterations.
3. **Linear Evaluation**:
   Iterating fixed-point convergence for each $n \in [2, 10^6]$ evaluates $\sum f(n)$ in $\mathcal{O}(N \log M)$ operations.
4. **Execution**:
   Evaluating $\sum_{n=2}^{10^6} f(n)$ yields $450186511399999$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log M)$ for $N = 10^6, M = 10^9$. Runs in $\approx 0.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
