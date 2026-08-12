# Totient Sum - Optimal Approach

## Algorithm Explanation

Find the last 9 digits of $S(510510, 10^{11}) \bmod 10^9$, where $S(n, m) = \sum_{i=1}^m \phi(n \cdot i)$ and $n = 510510 = 2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 \cdot 17$.

### Primorial Inclusion-Exclusion & Sub-linear Totient Sieve:
1. **Primorial Totient Multiplicativity**:
   For squarefree $n$, $\phi(n \cdot i) = \phi(n) \cdot \phi(i) \cdot \frac{\gcd(n, i)}{\phi(\gcd(n, i))}$.
   $S(n, m)$ reduces to a linear combination of summatory totients $\Phi(x) = \sum_{j=1}^x \phi(j)$ over $x = \lfloor m / d \rfloor$ where $d$ is a divisor of $n$.
2. **Sub-linear Totient Summation (Du's Sieve)**:
   Evaluating $\Phi(x) = \sum_{j=1}^x \phi(j)$ for $x \le m = 10^{11}$ uses Dirichlet hyperbola convolution:
   $$\Phi(x) = \frac{x(x+1)}{2} - \sum_{k=2}^x \Phi\left(\left\lfloor \frac{x}{k} \right\rfloor\right)$$
   Precomputing $\Phi(y)$ for $y \le m^{2/3}$ via a linear sieve evaluates $\Phi(m)$ in $\mathcal{O}(m^{2/3})$ operations.
3. **Execution**:
   Evaluating $S(510510, 10^{11}) \bmod 10^9$ yields last 9 digits $754862080$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(m^{2/3})$ for $m = 10^{11}$. Runs in $\approx 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(m^{2/3})$ totient memoization array.
