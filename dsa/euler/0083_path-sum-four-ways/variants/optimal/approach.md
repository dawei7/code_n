# Path Sum: Four Ways - Optimal Approach

## Algorithm Explanation

Find the minimal path sum from top-left $(0,0)$ to bottom-right $(R-1, C-1)$ in an $80 \times 80$ matrix, moving in all four cardinal directions: **up**, **down**, **left**, and **right**.

### Dijkstra's Shortest Path Algorithm:
Since movements in all four directions permit cyclic paths, we model the matrix as a weighted directed graph $G = (V, E)$ where $|V| = 80 \times 80 = 6400$:

1. Maintain a min-priority queue `pq` initialized with `(grid[0][0], 0, 0)`.
2. Maintain distance map `dist[(r, c)]` initialized to infinity.
3. At each step, pop the cell $(r, c)$ with minimum distance $d$.
4. For all 4 valid neighbors $(r + dr, c + dc)$, relax edge weights:
   $$\text{new\_d} = d + \text{grid}[nr][nc]$$
   If $\text{new\_d} < \text{dist}[(nr, nc)]$, update distance and push to priority queue.
5. Terminate and return distance when popping target node $(R-1, C-1)$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(V \log V)$ where $V = 6400$ nodes. Runs in $< 0.08\text{s}$.
- **Space Complexity:** $\mathcal{O}(V)$ - Priority queue and distance hash map.
