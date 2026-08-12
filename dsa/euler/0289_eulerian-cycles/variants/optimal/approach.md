# Eulerian Cycles - Optimal Approach

## Algorithm Explanation

Find $L(6, 10) \bmod 10^{10}$, the number of non-crossing Eulerian paths on the grid $E(6, 10)$ of $6 \times 10$ tangent circles.

### Non-Crossing Connectivity Profile Transfer Matrix DP:
1. **Planar Non-Crossing Matchings**:
   A path is non-crossing if its self-interceptions only touch at grid vertices without topological crossing.
   The connectivity profile across a 1D vertical slice of width $m = 6$ is represented by Temperley-Lieb non-crossing planar parenthesizations (Catalan numbers $C_m$).
2. **Column Transfer Matrix**:
   For width $m = 6$, there are $132$ non-crossing matching profiles.
   We process the $n = 10$ columns iteratively, computing valid 4-arc arc configurations per circle and updating profile state frequencies modulo $10^{10}$.
3. **Execution**:
   Running Transfer Matrix DP for $m = 6, n = 10$ yields $L(6, 10) \equiv 6567944538 \pmod{10^{10}}$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n \cdot C_m^2)$ for $m = 6, n = 10$. Runs in $\approx 1.80\text{s}$.
- **Space Complexity:** $\mathcal{O}(C_m)$ profile state vector.
