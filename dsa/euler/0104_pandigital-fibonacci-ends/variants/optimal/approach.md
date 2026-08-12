# Pandigital Fibonacci Ends - Optimal Approach

## Algorithm Explanation

Find the index $k$ of the first Fibonacci number $F_k$ for which both the **first $9$ digits** and the **last $9$ digits** are $1$-$9$ pandigital.

### Dual-End Acceleration Strategy:
1. **Last 9 Digits Modular Recurrence**:
   - Maintain $F_k \pmod{10^9}$ using $a, b \leftarrow b, (a + b) \bmod 10^9$.
   - Test $1$-$9$ pandigital property on last $9$ digits first.
2. **First 9 Digits Logarithmic Approximation**:
   - By Binet's formula, $F_k \approx \frac{\phi^k}{\sqrt{5}}$ where $\phi = \frac{1 + \sqrt{5}}{2}$.
   - Take base-10 logarithm: $\log_{10}(F_k) = k \log_{10}(\phi) - \log_{10}(\sqrt{5})$.
   - Extract fractional part $\text{frac} = \log_{10}(F_k) \bmod 1.0$.
   - Leading 9 digits are $\lfloor 10^{\text{frac} + 8} \rfloor$.
   - Evaluate first 9 digits pandigital test only when the last 9 digits pass.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(k)$ where $k \approx 329468$. Runs in $< 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Constant space.
