# Fractions and Sum of Powers of Two - Optimal Approach

## Algorithm Explanation

Find the Shortened Binary Expansion of the smallest integer $n$ such that $\frac{f(n)}{f(n-1)} = \frac{p}{q} = \frac{123,456,789}{987,654,321}$.

### Calkin-Wilf / Stern-Brocot Tree Duality:
Recall from Problem 169 that $f(2k) = f(k) + f(k-1)$ and $f(2k+1) = f(k)$.
The sequence of ratios $R(n) = \frac{f(n)}{f(n-1)}$ traverses all positive irreducible fractions in the Calkin-Wilf tree.

1. **Fraction Reduction**:
   Reduce $p / q$ to lowest terms by dividing by $\gcd(p, q)$:
   $$\frac{123,456,789}{987,654,321} = \frac{13,717,421}{109,739,369}$$
2. **Continued Fraction Expansion**:
   Compute the continued fraction representation of $q / p$:
   $$\frac{109,739,369}{13,717,421} = [8, 13717421]$$
3. **Binary Run-Length Duality**:
   When $q > p$ and $a_0 > 1$, the MSB `1` is explicitly prepended, splitting the last term $a_1 \to (1, a_1 - 1, a_0)$:
   $$\text{Shortened Binary Expansion} = [1, 13717420, 8]$$

Formatting result as comma-separated string `1,13717420,8`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log(\min(p, q)))$ via Euclidean algorithm. Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(\log(\min(p, q)))$ - List of continued fraction terms.
