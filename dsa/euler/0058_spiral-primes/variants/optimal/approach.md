# Spiral Primes - Optimal Approach

## Algorithm Explanation

Find the side length $S$ of an odd square spiral for which the ratio of prime numbers along both main diagonals first falls below $10\%$.

### Corner Formulas
For a spiral layer with odd side length $S$:
- Bottom-Right corner $= S^2$ (perfect square, always composite).
- Bottom-Left corner $= S^2 - (S - 1)$.
- Top-Left corner $= S^2 - 2(S - 1)$.
- Top-Right corner $= S^2 - 3(S - 1)$.
- Total diagonal elements $= 2S - 1$.

### Strategy:
1. Increment side length $S = 3, 5, 7 \dots$.
2. Test primality of the $3$ non-square corner numbers using fast deterministic primality testing.
3. Update cumulative diagonal prime count.
4. Return side length $S$ when $\frac{\text{prime\_count}}{2S - 1} < 0.10$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(S \sqrt{S})$ where $S \approx 26241$. Runs in $< 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
