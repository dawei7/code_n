# Cube Digit Pairs - Optimal Approach

## Algorithm Explanation

Find the number of distinct unordered arrangements of two $6$-faced cubes that allow displaying all $2$-digit square numbers below $100$: $\{01, 04, 09, 16, 25, 36, 49, 64, 81\}$.

### Digit Inversion Rule:
Digits $6$ and $9$ are rotatable and interchangeable: if either $6$ or $9$ is present on a cube, both $\{6, 9\}$ are available for digit formation.

### Combinatorial Search Strategy:
1. Generate all $\binom{10}{6} = 210$ candidate $6$-digit combinations for a single cube.
2. For each unique pair of combinations $(C_1, C_2)$ ($210 \times 211 / 2 = 22155$ pairs):
   - Expand $6 \leftrightarrow 9$ availability in $C_1$ and $C_2$.
   - Test if all $9$ required square digit pairs $(d_1, d_2)$ can be formed by $C_1 \times C_2$ or $C_2 \times C_1$.
3. Accumulate and return the total count of valid cube pairs.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\binom{10}{6}^2)$ - Tests $22155$ pair configurations. Runs in $< 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory overhead is constant.
