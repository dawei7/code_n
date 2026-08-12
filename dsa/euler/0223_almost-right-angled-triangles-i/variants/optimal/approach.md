# Almost Right-angled Triangles I - Optimal Approach

## Algorithm Explanation

Find the number of barely acute triangles ($a \le b \le c$) satisfying $a^2 + b^2 = c^2 + 1$ with perimeter $P = a + b + c \le 25\,000\,000$.

### Algebraic Factorization & Divisor Sieve:
1. **Case $a = 1$**:
   $1^2 + b^2 = b^2 + 1 \implies c = b$. Any $b \ge 1$ forms a valid isosceles triangle with perimeter $P = 1 + 2b \le 25\,000\,000 \implies b \le 12\,499\,999$.
   There are exactly $12\,499\,999$ solution triangles for $a = 1$.
2. **Case $a > 1$**:
   Rearranging gives $(a - 1)(a + 1) = c^2 - b^2 = (c - b)(c + b)$.
   Let $d_1 = c - b$ and $d_2 = c + b$ such that $d_1 d_2 = a^2 - 1$.
   The side lengths are $b = \frac{d_2 - d_1}{2}$ and $c = \frac{d_1 + d_2}{2}$.
3. **Divisor Conditions**:
   - $d_1, d_2$ must have the same parity.
   - $b \ge a \implies d_2 - d_1 \ge 2a$.
   - Perimeter $a + b + c = a + d_2 \le 25\,000\,000$.
4. **Execution**:
   Using prime factorizations of $(a - 1)$ and $(a + 1)$ from a linear sieve, we enumerate divisors $d_1 \mid (a^2 - 1)$ for $a \le 12\,499\,999$, obtaining $61614848$ solution triangles.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N)$ where $N = 12\,500\,000$. Runs in $\approx 10\text{s}$ (C++ compiled).
- **Space Complexity:** $\mathcal{O}(N)$ for min prime factor array.
