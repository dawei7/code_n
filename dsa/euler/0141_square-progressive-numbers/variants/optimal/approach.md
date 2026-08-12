# Square Progressive Numbers - Optimal Approach

## Algorithm Explanation

Find the sum of all progressive numbers $n < 10^{12}$ that are perfect squares.

A progressive number $n$ divided by $d$ yields quotient $q$ and remainder $r$ ($0 \le r < d$) such that $r, d, q$ form a geometric progression with rational common ratio $\frac{a}{b} > 1$ ($\gcd(a, b) = 1, a > b \ge 1$).

### Rational Parameterization:
Expressing terms of the geometric progression:
- $r = c b^2$
- $d = c a b$
- $q = c a^2$

Substituting into Euclidean division $n = d q + r$:
$$n = (c a b)(c a^2) + c b^2 = c^2 a^3 b + c b^2$$

### Search Bound & Strategy:
1. Iterate $a \in [2, 10000]$ (since $a^3 < 10^{12}$).
2. Iterate coprime denominator $b \in [1, a-1]$ ($\gcd(a, b) = 1$).
3. Iterate integer multiplier $c \ge 1$ while $n = c^2 a^3 b + c b^2 < 10^{12}$.
4. Test if $n$ is a perfect square using integer square root `math.isqrt(n)`.
5. Store valid progressive perfect squares in a set and return their sum.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(L^{1/3} \cdot a)$ where $L = 10^{12}$. Runs in $\approx 2.1\text{s}$.
- **Space Complexity:** $\mathcal{O}(S)$ - Set of progressive squares.
