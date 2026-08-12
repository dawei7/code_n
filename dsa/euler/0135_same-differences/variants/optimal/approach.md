# Same Differences - Optimal Approach

## Algorithm Explanation

Find the number of positive integers $n < 1,000,000$ for which the equation $x^2 - y^2 - z^2 = n$ has **exactly 10** distinct positive integer solutions $(x, y, z)$ in arithmetic progression.

### Algebraic Parameterization:
Let $y = a$, $x = a + d$, $z = a - d$ with common difference $d > 0$ and $a > d > 0$ (so $z > 0$).

Substituting into equation:
$$(a + d)^2 - a^2 - (a - d)^2 = n \implies 4ad - a^2 = n \implies a(4d - a) = n$$

Let $u = 4d - a$. Then $n = a \cdot u$ is a factorization of $n$:
1. $4d = a + u \implies d = \frac{a + u}{4}$ must be an integer: $(a + u) \equiv 0 \pmod 4$.
2. Positive $z = a - d > 0 \implies a > \frac{a + u}{4} \implies 3a > u$.

### Sieve Frequency Accumulation:
1. Initialize frequency array `sol_count[n] = 0` for $n \in [1, 10^6)$.
2. Iterate $a \in [1, 10^6)$ and $u \in [1, 3a - 1]$ with $a \cdot u < 10^6$.
3. If $(a + u) \bmod 4 == 0$, increment `sol_count[a * u] += 1`.
4. Count numbers $n$ with `sol_count[n] == 10`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N)$ where $N = 10^6$. Runs in $< 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Solution frequency array.
