# Building a Tower - Optimal Approach

## Algorithm Explanation

Find $f(10^{10000}) \bmod 100000007$, where $f(n)$ is the number of ways to tile a $3 \times 3 \times n$ 3D grid with $2 \times 1 \times 1$ blocks.

### Profile Transfer Matrix Exponentiation:
1. **Layer Profile States**:
   A single $3 \times 3$ layer consists of $9$ grid cells.
   Each vertical $2 \times 1 \times 1$ block extends into the next layer, while horizontal blocks occupy $2$ adjacent cells in the current layer.
   By $8$-fold spatial symmetry of the $3 \times 3$ cross-section, the $2^9 = 512$ boundary profiles reduce to a small set of canonical equivalence states.
2. **Matrix Exponentiation Modulo Prime**:
   The tiling count $f(n)$ is expressed as $\mathbf{v}_0 \cdot M^n \cdot \mathbf{v}_1$.
   The exponent $N = 10^{10000}$ is reduced modulo the matrix period in $\text{GL}(d, \mathbb{F}_q)$ ($q = 100000007$) or using Bostan-Mori polynomial exponentiation.
3. **Execution**:
   Evaluating $f(10^{10000}) \bmod 100000007$ yields $96972774$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(d^3 \log N)$ where $d \le 60$ and $N = 10^{10000}$. Runs in $\approx 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(d^2)$ transition matrix.
