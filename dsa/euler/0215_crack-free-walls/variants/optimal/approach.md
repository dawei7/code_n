# Crack-free Walls - Optimal Approach

## Algorithm Explanation

Find $W(32, 10)$, the number of ways to build a $32 \times 10$ crack-free wall using $2 \times 1$ and $3 \times 1$ bricks.

### Row Crack Representation & Transfer Matrix DP:
1. **Row Crack Pattern**:
   A row configuration of length $W = 32$ is uniquely defined by its set of internal crack coordinates $C \subset \{1, 2, \dots, 31\}$.
   DFS enumeration yields $M = 3329$ valid single-row configurations for $W = 32$.
2. **Compatibility Graph**:
   Two adjacent rows $R_i$ and $R_j$ are compatible if and only if their crack sets are disjoint ($C_i \cap C_j = \emptyset$).
3. **Dynamic Programming Transitions**:
   Let $v^{(h)}_i$ be the number of valid walls of height $h$ ending with row configuration $i$.
   $$v^{(h+1)}_j = \sum_{(i, j) \text{ compatible}} v^{(h)}_i$$
4. **Execution**:
   Iterating $h = 1 \dots 10$ starting from $v^{(1)} = \mathbf{1}$ yields $806844323190414$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(M^2 + H \cdot |E|)$ where $M = 3329$ and $H = 10$. Runs in $\approx 0.38\text{s}$.
- **Space Complexity:** $\mathcal{O}(M^2)$ to store the compatibility adjacency list.
