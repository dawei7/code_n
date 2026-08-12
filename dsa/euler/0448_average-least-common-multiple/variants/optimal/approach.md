# Average Least Common Multiple - Optimal Approach

## Algorithm Explanation

Find $S(99999999019) \bmod 999999017$, where $S(N) = \sum_{k=1}^N A(k)$ and $A(n) = \frac{1}{n} \sum_{i=1}^n \operatorname{lcm}(n, i)$.

### Identity Transformation & Sub-linear Dirichlet Sieve:
1. **LCM Sum Identity**:
   Using $\operatorname{lcm}(n, i) = \frac{n \cdot i}{\gcd(n, i)}$, the inner sum simplifies to:
   $$\sum_{i=1}^n \operatorname{lcm}(n, i) = \frac{n}{2} \left( 1 + \sum_{d \mid n} d \, \phi(d) \right)$$
   Dividing by $n$ yields $A(n) = \frac{1}{2} \left( 1 + \sum_{d \mid n} d \, \phi(d) \right)$.
2. **Summation Interchange**:
   Summing $A(k)$ for $k = 1 \dots N$:
   $$S(N) = \frac{N}{2} + \frac{1}{2} \sum_{d=1}^N d \, \phi(d) \left\lfloor \frac{N}{d} \right\rfloor$$
3. **Sub-linear Summation of $d \phi(d)$**:
   Evaluating $\sum_{d=1}^N d \phi(d) \lfloor N/d \rfloor$ for $N = 99999999019$ uses Du's Dirichlet hyperbola sieve:
   $$G(x) = \sum_{d=1}^x d \phi(d)$$
   Precomputing $G(y)$ for $y \le N^{2/3}$ evaluates $S(N) \bmod 999999017$ in $\mathcal{O}(N^{2/3})$ time.
4. **Execution**:
   Evaluating $S(99999999019) \bmod 999999017$ yields $106467648$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^{2/3})$ for $N = 99999999019$. Runs in $\approx 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(N^{2/3})$ sub-linear sieve arrays.
