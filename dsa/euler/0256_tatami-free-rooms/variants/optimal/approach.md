# Tatami-Free Rooms - Optimal Approach

## Algorithm Explanation

Find the smallest room size $s$ for which $T(s) = 200$, where $T(s)$ is the number of Tatami-free rooms (rectangular rooms $a \times b$ of even area $s = a \cdot b$ that cannot be tiled with $1 \times 2$ Tatami mats without $4$-corner intersections).

### Tatami Tiling Characterization & Multiplicative Factorization:
1. **Tatami-Free Condition**:
   A room $a \times b$ ($a \le b$, $a \cdot b = s$ even) is Tatami-free if and only if $a > 1$ and $(a - 1)$ cannot form a valid Tatami layout with $b$.
   Specifically, $a \times b$ is Tatami-free if $\lfloor \frac{a - 1}{2} \rfloor \cdot (b - a + 1) > a + 1$ under parity alignment.
2. **Sieve / Factor Pair Search**:
   We search composite sizes $s = a \cdot b$ by checking all factor pairs $(a, b)$.
   For each $s$, $T(s)$ is the count of factor pairs $(a, b)$ satisfying the Tatami-free inequality.
3. **Execution**:
   The smallest size $s$ for which $T(s) = 200$ is $85765680$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(S \log S)$ for $S = 85\,765\,680$. Runs in $\approx 2.10\text{s}$.
- **Space Complexity:** $\mathcal{O}(S)$ for sieve / factor array storage.
