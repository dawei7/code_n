# Digit Cancelling Fractions - Optimal Approach

## Algorithm Explanation

Find non-trivial fractions $\frac{a}{b} < 1$ with $2$-digit numerator and denominator where cancelling a shared digit yields an equivalent fraction $\frac{c}{e}$.

1. Iterate numerators $a \in [10, 99]$ and denominators $b \in [a + 1, 99]$.
2. Skip trivial multiples of $10$ ($a \bmod 10 = 0$ and $b \bmod 10 = 0$).
3. Identify common digits between $a$ and $b$.
4. Check if cancelling the shared digit leaves single digits $c$ and $e$ such that $a \times e = b \times c$.
5. Compute cumulative product of valid numerators $N_{\text{prod}}$ and denominators $D_{\text{prod}}$.
6. Simplify fraction by dividing $D_{\text{prod}}$ by $\text{GCD}(N_{\text{prod}}, D_{\text{prod}})$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ - Fixed search space ($90 \times 90 = 8100$ iterations).
- **Space Complexity:** $\mathcal{O}(1)$ - Constant memory.
