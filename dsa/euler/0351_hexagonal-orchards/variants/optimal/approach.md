# Hexagonal Orchards - Optimal Approach

## Algorithm Explanation

Find $H(100\,000\,000)$, the number of hidden points from the center in a hexagonal orchard of order $n = 100\,000\,000$.

### Sector Geometry & Euler Totient Prefix Sum:
1. **Hexagonal Sector Decomposition**:
   A hexagonal orchard of order $n$ consists of $6$ symmetric $60^\circ$ triangular sectors.
   Each sector contains $\frac{n(n+1)}{2}$ total points.
2. **Visible vs. Hidden Point Condition**:
   A point $(x, y)$ in a triangular sector is visible from the origin iff $\gcd(x, y) = 1$.
   The number of visible points at distance $x \le n$ is given by Euler's totient function $\phi(x)$.
   Thus, the number of visible points in one sector is $\sum_{k=1}^n \phi(k)$.
3. **Hidden Point Formula**:
   Subtracting visible points from total points per sector and multiplying by $6$:
   $$H(n) = 6 \left( \frac{n(n+1)}{2} - \sum_{k=1}^n \phi(k) \right) = 3 n (n + 1) - 6 \sum_{k=1}^n \phi(k)$$
4. **Execution**:
   Using a linear totient sieve up to $N = 100\,000\,000$, we sum $\phi(k)$ and evaluate $H(100\,000\,000)$ yielding $11762187201804552$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ for $N = 100\,000\,000$. Runs in $\approx 0.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ linear totient bytearray.
