# Amazing Mazes! - Optimal Approach

## Algorithm Explanation

Find $C(100, 500)$, the number of distinct $100 \times 500$ mazes (spanning trees of a $100 \times 500$ grid graph), formatted in scientific notation rounded to 5 significant digits.

### Kirchhoff's Matrix Tree Theorem & Logarithmic Trigonometric Product:
1. **Grid Graph Spanning Tree Formula**:
   By Kirchhoff's Matrix Tree Theorem, the number of spanning trees $C(m, n)$ of an $m \times n$ grid graph is given by the exact eigenvalue product:
   $$C(m, n) = \prod_{j=1}^{m-1} \prod_{k=1}^{n-1} 4 \left( \sin^2\left(\frac{j \pi}{2 m}\right) + \sin^2\left(\frac{k \pi}{2 n}\right) \right)$$
2. **Logarithmic Stability Transformation**:
   Because $C(100, 500)$ exceeds $10^{25000}$, evaluating the product directly underflows/overflows.
   We compute $\log_{10} C(m, n)$ by summing base-10 logarithms of the terms:
   $$\log_{10} C(m, n) = \sum_{j=1}^{m-1} \sum_{k=1}^{n-1} \log_{10} \left( 4 \sin^2\left(\frac{j \pi}{2 m}\right) + 4 \sin^2\left(\frac{k \pi}{2 n}\right) \right)$$
3. **Scientific Notation Formatting**:
   Splitting $\log_{10} C = E + F$ into integer exponent $E$ and fractional part $F$, the mantissa is $10^F$, rounded to 5 significant digits (`x.xxxxeE`).
4. **Execution**:
   Evaluating $\log_{10} C(100, 500)$ yields scientific notation `6.3202e25093`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(m \cdot n)$ for $m = 100, n = 500$. Runs in $\approx 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
