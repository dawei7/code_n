# Stone Game - Optimal Approach

## Algorithm Explanation

Find $\sum (x_i + y_i + z_i)$ where $(x_i, y_i, z_i)$ ranges over all losing configurations (P-positions) with $x_i \le y_i \le z_i \le 1000$ in a 3-pile Nim game where a player may remove $N > 0$ stones from 1, 2, or 3 piles.

### 3D Game Theory DP & P-Position Sieve:
1. **Losing State Identification**:
   A state $(x, y, z)$ ($x \le y \le z$) is a losing configuration (P-position) if every legal move leads to a winning configuration.
2. **Reverse Move Marking**:
   Iterating states $(x, y, z)$ in order of increasing total stones $x + y + z$:
   When an unvisited losing state $(x, y, z)$ is encountered, we accumulate $(x + y + z)$ into our total sum.
   We then mark all states reachable from $(x, y, z)$ by adding $k > 0$ to 1, 2, or 3 piles as WINNING states.
3. **Execution**:
   Summing all losing configurations for $x \le y \le z \le 1000$ yields $167542018$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(M^3)$ for $M = 1000$. Runs in $\approx 1.20\text{s}$.
- **Space Complexity:** $\mathcal{O}(M^3)$ 3D bitset table.
