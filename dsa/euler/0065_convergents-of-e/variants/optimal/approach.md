# Convergents of e - Optimal Approach

## Algorithm Explanation

Find the sum of the digits in the numerator of the $100^{\text{th}}$ convergent of $e$.

### Continued Fraction Sequence for $e$
$$e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, \dots, 1, 2k, 1, \dots]$$

Sequence coefficients $a_i$ for $i \ge 0$:
- $a_0 = 2$
- $a_i = 2 \times \frac{i+1}{3}$ if $i \equiv 2 \pmod 3$, otherwise $a_i = 1$.

### Numerator Recurrence
- $N_0 = a_0$
- $N_1 = a_0 a_1 + 1$
- $N_k = a_k N_{k-1} + N_{k-2}$ for $k \ge 2$.

Iterate $100$ terms and compute the digital sum of $N_{99}$ in arbitrary precision.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K)$ where $K = 100$. Operates in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Memory overhead is constant.
