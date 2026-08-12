# Hexagonal Tile Differences - Optimal Approach

## Algorithm Explanation

Find the $2000^{\text{th}}$ tile $n$ in ascending order for which $\operatorname{PD}(n) = 3$, where $\operatorname{PD}(n)$ is the number of prime differences between tile $n$ and its six adjacent hexagonal neighbors.

### Geometric Hexagonal Topology Reduction:
Tiles with $\operatorname{PD}(n) = 3$ can **only** occur at two specific positions on each ring $r \ge 1$:

1. **Top Start Tile of Ring $r$**: $S_r = 3r^2 - 3r + 2$
   - Candidate prime differences: $(6r - 1), (6r + 1), (12r + 5)$.
   - $\operatorname{PD}(S_r) = 3 \iff$ all three candidate differences are prime.

2. **End Corner Tile of Ring $r$** ($r > 1$): $E_r = 3r^2 + 3r + 1$
   - Candidate prime differences: $(6r - 1), (6r + 5), (12r - 7)$.
   - $\operatorname{PD}(E_r) = 3 \iff$ all three candidate differences are prime (note $E_1 = 7$ has $\operatorname{PD}(7) = 2$ due to inner center boundary conditions).

### Strategy:
Count tile $1$ first ($\operatorname{PD}(1) = 3$). Then iterate ring index $r = 1, 2, 3 \dots$, evaluate primality of candidate triple for $S_r$ and $E_r$ ($r > 1$), and return when count reaches $2000$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(R \cdot \text{Primality})$ where $R \approx 70000$ rings. Runs in $< 0.4\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary space is constant.
