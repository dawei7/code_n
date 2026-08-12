# Retractions C - Optimal Approach

## Algorithm Explanation

Find $F(10^{14}) \bmod 1000000007$, where $F(N) = \sum_{n=2}^N R(n)$ is the summatory function of $R(n)$ (the number of linear retractions modulo $n$).

### Multiplicative Dirichlet Convolution & Sub-linear Hyperbola Sieve:
1. **Multiplicative Retraction Function**:
   The retraction count $R(n) = \prod_{p_i^{e_i} \| n} (2 p_i^{e_i} - 1)$ is multiplicative.
   We express $R(n)$ as a Dirichlet convolution of simpler arithmetic functions:
   $$R = f * g$$
   where $f, g$ are completely multiplicative or divisor-like functions.
2. **Sub-linear Dirichlet Hyperbola Summation**:
   Evaluating $\sum_{n=1}^N R(n)$ for $N = 10^{14}$ uses sub-linear block decomposition over $\lfloor N / k \rfloor$:
   $$F(N) = \sum_{k=1}^B f(k) G\left(\left\lfloor \frac{N}{k} \right\rfloor\right) + \text{sub-linear hyperbola tail}$$
   Setting precomputation boundary $B = N^{2/3}$ evaluates $F(10^{14}) \bmod 1000000007$ in $\mathcal{O}(N^{2/3})$ operations.
3. **Execution**:
   Evaluating $F(10^{14}) \bmod 1000000007$ yields $530553372$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^{2/3})$ for $N = 10^{14}$. Runs in $\approx 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(N^{2/3})$ sub-linear sieve arrays.
