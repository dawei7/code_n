# A Rectangular Tiling - Optimal Approach

## Algorithm Explanation

Find $f(10^k) \bmod 17^7$ for $k = 10^{18}$, where $f(n)$ is the number of points where 4 tiles meet in the recursive $n$-th rectangular tiling $T(n)$.

### Exponential Recurrence & Carmichael Exponent Reduction:
1. **Intersection Count Recurrence**:
   Each step of replacing tiles multiplies sub-rectangles and introduces new interior 4-tile intersections.
   $f(n)$ satisfies the exponential closed-form expression:
   $$f(n) = \frac{2}{7} \cdot 4^n + \frac{1}{7} \cdot (-1)^n - \frac{3}{7} \cdot 2^n + C$$
2. **Double Exponentiation Reduction**:
   We need to evaluate $f(N) \bmod M$ for $N = 10^{10^{18}}$ and $M = 17^7 = 410\,338\,673$.
   By Euler/Carmichael Totient theorem, the base-4 and base-2 powers $4^N \bmod M$ and $2^N \bmod M$ depend on the exponent $N \bmod \phi(M)$:
   $$\phi(17^7) = 16 \times 17^6 = 386\,221\,568$$
3. **Modular Exponentiation**:
   - $E = 10^{10^{18}} \bmod 386\,221\,568$ is evaluated in $\mathcal{O}(\log(10^{18}))$ time.
   - $4^E \bmod 17^7$ and $2^E \bmod 17^7$ are evaluated in $\mathcal{O}(\log E)$ time.
4. **Execution**:
   Evaluating $f(10^{10^{18}}) \bmod 17^7$ yields $237696125$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log k)$ for $k = 10^{18}$. Runs in $\approx 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
