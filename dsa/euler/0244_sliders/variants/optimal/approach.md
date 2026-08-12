# Sliders - Optimal Approach

## Algorithm Explanation

Find the sum of all checksums for all minimal length paths to reach configuration (T) from configuration (S) in a $4 \times 4$ sliding tile puzzle containing 7 Red tiles and 8 Blue tiles.

### BFS Shortest Path Trajectory & Checksum Accumulation:
1. **State Space Representation**:
   A state is uniquely identified by `(empty_row, empty_col, red_tile_bitmask)`.
   The total number of reachable states is bounded by $\binom{15}{7} \times 16 = 102\,960$.
2. **Breadth-First Search (BFS)**:
   We perform a BFS from configuration (S) to find all shortest paths to configuration (T).
   During BFS, we accumulate path checksums $\text{checksum} = (\text{checksum} \times 243 + \text{ASCII}) \bmod 100\,000\,007$ across all minimal length paths.
3. **Execution**:
   Aggregating all minimal path checksums yields $96356848$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(V + E)$ for $V \le 102\,960$ states and $E \le 4V$ edges. Runs in $\approx 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(V)$ for queue and distance tracking.
