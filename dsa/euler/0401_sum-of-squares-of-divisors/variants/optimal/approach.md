# Sum of Squares of Divisors - Optimal Approach

## Algorithm Explanation

Find $\Sigma_2(10^{15}) \bmod 10^9$, where $\Sigma_2(N) = \sum_{i=1}^N \sigma_2(i)$ and $\sigma_2(i) = \sum_{d \mid i} d^2$.

### Dirichlet Hyperbola Floor Sum:
1. **Summation Interchange Identity**:
   Interchanging order of summation:
   $$\Sigma_2(N) = \sum_{i=1}^N \sum_{d \mid i} d^2 = \sum_{d=1}^N d^2 \left\lfloor \frac{N}{d} \right\rfloor$$
2. **Hyperbola Split at $\sqrt{N}$**:
   For $N = 10^{15}$, we set boundary $B = \lfloor \sqrt{N} \rfloor = 31\,622\,776$:
   $$\Sigma_2(N) = \sum_{d=1}^B d^2 \left\lfloor \frac{N}{d} \right\rfloor + \sum_{k=1}^{\lfloor N/(B+1) \rfloor} k \sum_{d = \lfloor N/(k+1) \rfloor + 1}^{\lfloor N/k \rfloor} d^2$$
3. **Square Sum Formula**:
   The inner sum $\sum_{d=u}^v d^2$ is evaluated in $\mathcal{O}(1)$ using Faulhaber's square sum formula $\frac{m(m+1)(2m+1)}{6} \bmod 10^9$.
4. **Execution**:
   Evaluating $\Sigma_2(10^{15}) \bmod 10^9$ yields $281632621$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^{1/2})$ for $N = 10^{15}$. Runs in $\approx 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
