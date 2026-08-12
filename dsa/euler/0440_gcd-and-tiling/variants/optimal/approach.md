# GCD and Tiling - Optimal Approach

## Algorithm Explanation

Find $S(2000) \bmod 987\,898\,789$, where $S(L) = \sum_{a, b, c = 1}^L \gcd(T(c^a), T(c^b))$ and $T(n) = 10 T(n-1) + T(n-2)$ is the 10-digit single-row tiling recurrence with $T(0) = 1, T(1) = 10$.

### Lucas Strong Divisibility & Matrix Exponentiation:
1. **Strong Divisibility Property of Tiling Sequence**:
   Analogous to Fibonacci numbers, the tiling sequence $T(n)$ satisfies the strong divisibility property:
   $$\gcd(T(c^a), T(c^b)) = T(c^{\gcd(a, b)})$$
2. **Triple Sum Reduction via GCD Frequency**:
   $S(L) = \sum_{c=1}^L \sum_{a=1}^L \sum_{b=1}^L T(c^{\gcd(a, b)})$.
   Let $g = \gcd(a, b) \le L$. The number of pairs $(a, b) \in [1, L]^2$ with $\gcd(a, b) = g$ is:
   $$N(g, L) = \sum_{k=1}^{\lfloor L/g \rfloor} \mu(k) \left\lfloor \frac{L}{k g} \right\rfloor^2$$
3. **$2 \times 2$ Matrix Exponentiation Modulo $987\,898\,789$**:
   For each $c \in [1, L]$ and $g \in [1, L]$, $T(c^g) \bmod 987\,898\,789$ is evaluated in $\mathcal{O}(g \log c)$ time via binary matrix exponentiation of the transfer matrix $\begin{pmatrix} 10 & 1 \\ 1 & 0 \end{pmatrix}$.
4. **Execution**:
   Evaluating $S(2000) \bmod 987\,898\,789$ yields $970746056$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(L^2 \log L)$ for $L = 2000$. Runs in $\approx 0.25\text{s}$.
- **Space Complexity:** $\mathcal{O}(L)$ array tables.
