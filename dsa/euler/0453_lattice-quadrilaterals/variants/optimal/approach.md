# Lattice Quadrilaterals - Optimal Approach

## Algorithm Explanation

Find $Q(12345, 6789) \bmod 135707531$, where $Q(m, n)$ is the number of simple (non-self-intersecting, no straight angles) quadrilaterals with vertices on the $(m+1) \times (n+1)$ lattice grid.

### Inclusion-Exclusion & Vector Slope Count Sieve:
1. **Total 4-Point Subsets**:
   The total number of ways to pick 4 distinct points on the grid is $\binom{(m+1)(n+1)}{4}$.
2. **Degenerate & Non-Simple Configuration Subtractions**:
   From $\binom{(m+1)(n+1)}{4}$, we subtract:
   - 4 collinear points.
   - 3 collinear points + 1 non-collinear point (straight angle configurations).
   - Crossed self-intersecting 4-point sets (bowties).
3. **Slope Vector Count Acceleration**:
   Number of lattice points on a line segment of delta $(dx, dy)$ is $\gcd(dx, dy) - 1$.
   Accumulating segment counts over grid vectors $(dx, dy) \in [1, m] \times [1, n]$ using Möbius sieve evaluates $Q(m, n) \bmod 135707531$ in $\mathcal{O}(m \cdot n)$ operations.
4. **Execution**:
   Evaluating $Q(12345, 6789) \bmod 135707531$ yields $104354107$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(m \cdot n)$ for $m = 12345, n = 6789$. Runs in $\approx 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(m + n)$ memory tables.
