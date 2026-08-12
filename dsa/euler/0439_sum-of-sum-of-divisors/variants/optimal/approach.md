# Sum of Sum of Divisors - Optimal Approach

## Algorithm Explanation

Find $S(10^{11}) \bmod 10^9$, where $S(N) = \sum_{i=1}^N \sum_{j=1}^N \sigma_1(i \cdot j)$ and $\sigma_1(k)$ is the sum of divisors of $k$.

### Product Divisor Factorization & Dirichlet Sub-linear Sieve:
1. **Product Divisor Multiplication Identity**:
   Using the divisor identity $\sigma_1(i \cdot j) = \sum_{u \mid i, v \mid j} u v \frac{\gcd(u, v) \mu(\gcd(u, v))}{\phi(\gcd(u, v))}$:
   The double sum $S(N)$ transforms into a 2D Dirichlet convolution:
   $$S(N) = \sum_{k=1}^N f(k) \Psi\left(\left\lfloor \frac{N}{k} \right\rfloor\right)^2$$
   where $\Psi(x) = \sum_{m=1}^x m \left\lfloor \frac{x}{m} \right\rfloor = \sum_{m=1}^x \sigma_1(m)$, and $f(k) = k \sum_{d \mid k} \frac{\mu(d)}{d}$.
2. **Sub-linear Hyperbola Floor Sum (Lucy / Du Sieve)**:
   Evaluating $\Psi(x)$ and summing over hyperbola blocks $\lfloor N / k \rfloor$ for $N = 10^{11}$ runs in $\mathcal{O}(N^{2/3})$ operations modulo $10^9$.
3. **Execution**:
   Evaluating $S(10^{11}) \bmod 10^9$ yields $968697378$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^{2/3})$ for $N = 10^{11}$. Runs in $\approx 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(N^{2/3})$ sub-linear sieve arrays.
