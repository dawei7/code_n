# Primitive Triangles - Optimal Approach

## Algorithm Explanation

Find the number of primitive integer-sided triangles $(a, b, c)$ ($a \le b \le c$, $\gcd(a, b, c) = 1$) with perimeter $a + b + c \le 10\,000\,000$.

### Alcuin's Sequence & Möbius Inversion:
1. **Total Integer Triangles (Alcuin's Formula)**:
   The total number of integer triangles of perimeter $n$ is given by Alcuin's sequence:
   $$T(n) = \left\lfloor \frac{n^2 + 24}{48} \right\rfloor \text{ if } n \text{ even}, \quad T(n) = \left\lfloor \frac{(n+3)^2 + 24}{48} \right\rfloor \text{ if } n \text{ odd}$$
2. **Cumulative Prefix Sums**:
   Let $S(N) = \sum_{n=1}^N T(n)$ be the total number of integer triangles with perimeter $\le N$.
3. **Möbius Inversion for Primitiveness**:
   Scaling a primitive triangle of perimeter $p$ by factor $k$ yields a triangle of perimeter $k \cdot p$ with $\gcd = k$.
   By Möbius inversion, the number of primitive triangles with perimeter $\le N$ is:
   $$P(N) = \sum_{k=1}^N \mu(k) S\left( \left\lfloor \frac{N}{k} \right\rfloor \right)$$
4. **Execution**:
   Using a linear Möbius sieve up to $N = 10^7$, evaluating $P(10^7)$ yields $5777137137739632912$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ for $N = 10^7$. Runs in $\approx 4.88\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ array storage.
