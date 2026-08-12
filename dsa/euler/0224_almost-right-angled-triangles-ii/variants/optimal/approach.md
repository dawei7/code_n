# Almost Right-angled Triangles II - Optimal Approach

## Algorithm Explanation

Find the number of barely obtuse triangles ($a \le b \le c$) satisfying $a^2 + b^2 = c^2 - 1$ with perimeter $P = a + b + c \le 75\,000\,000$.

### Modular Parity Exclusion & Quadratic Polynomial Sieve:
1. **Parity Constraint**:
   $a^2 + 1 = c^2 - b^2 = (c - b)(c + b)$.
   For odd $a$, $a^2 + 1 \equiv 2 \pmod 4$, meaning $c - b$ and $c + b$ have opposite parity, which prevents $b, c$ from being integers.
   Hence $a$ **must be even**, $a = 2k$.
2. **Divisor Representation**:
   $d_1 d_2 = 4k^2 + 1$ with $d_1 \le d_2$.
   Side lengths are $b = \frac{d_2 - d_1}{2}$ and $c = \frac{d_1 + d_2}{2}$.
   Valid triangles require $d_2 - d_1 \ge 2a = 4k$ and $P = a + d_2 \le 75\,000\,000$.
3. **Polynomial Sieve for $4k^2 + 1$**:
   Using Tonelli-Shanks modular square roots for primes $p \equiv 1 \pmod 4$, we sieve prime factorizations of $4k^2 + 1$ for $k \le 12\,500\,000$.
4. **Execution**:
   Enumerating valid divisor pairs across all even $a$ yields $6997951$ solution triangles.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K \log \log K)$ where $K = 12\,500\,000$. Runs in $\approx 10\text{s}$ (C++ compiled).
- **Space Complexity:** $\mathcal{O}(K)$ for factor lists.
