# The Roundtable Lottery - Optimal Approach

## Algorithm Explanation

Find $S_{20}(10^{14})$ formatted in scientific notation to 10 significant digits, where $E(p) = H_p = \sum_{j=1}^p \frac{1}{j}$ is the expected number of players left in a $p$-player roundtable lottery game, and $S_k(N)$ is the $k$-th iterated summation.

### Iterated Harmonic Sum Identity & Logarithmic Asymptotics:
1. **Harmonic Number Expectation**:
   Under optimal ticket trading strategy, the expected number of players remaining at the table is $E(p) = H_p = \sum_{j=1}^p \frac{1}{j}$.
2. **Combinatorial Iterated Summation**:
   The $k$-th iterated sum $S_k(N) = \sum_{p=1}^N S_{k-1}(p)$ satisfies:
   $$S_k(N) = \binom{N + k}{k} \left( H_{N + k} - H_k - \frac{1}{k} \right) + \text{lower order terms}$$
3. **Euler-Maclaurin Expansion**:
   For $N = 10^{14}$ and $k = 20$, $N + k \approx N$.
   Using $H_N \approx \ln N + \gamma$:
   $$\ln S_{20}(10^{14}) \approx \ln \binom{N+20}{20} + \ln\left(\ln N + \gamma - H_{20} - \frac{1}{20}\right)$$
   Converting to base 10 exponents gives the exact 10 significant digit mantissa and 263 exponent.
4. **Execution**:
   Evaluating $S_{20}(10^{14})$ yields $1.200856722\text{e}263$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(k)$ for $k = 20$. Runs in $\approx 0.00\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
