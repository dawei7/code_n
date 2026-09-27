# Guided Example: K Highest Ranked Items Within a Price Range

We analyze and execute the multi-criteria Breadth-First Search (BFS) ranking algorithm on a representative shop grid instance, establishing how unweighted wavefront propagation orders candidates before secondary lexicographical resolution.

- **Input:** `grid = [[1, 2, 0, 1], [1, 3, 0, 1], [0, 2, 5, 1]]`, `pricing = [2, 5]`, `start = [0, 0]`, `k = 3`
- **Output:** `[[0, 1], [1, 1], [2, 1]]`

This instance illustrates obstacle avoidance, multi-attribute tuple prioritization, BFS layer progression, and extracting the top $k$ items.

---

## 1. Problem Overview & Representative Instance

A store is modeled as an $m \times n$ grid:
- Cell value `0`: Impassable wall (blocks movement).
- Cell value `1`: Empty aisle (traversable, contains no item).
- Cell value $\ge 2$: Traversable aisle containing an item priced at that value.

Moving between adjacent cells (up, down, left, right) costs $1$ step. We start at cell `start = [start_row, start_col]` and seek items whose prices fall within the inclusive interval `pricing = [low, high]`.

Eligible items are ranked using a 4-tuple comparison in ascending order:
1. **Shortest Path Distance:** Fewer steps from `start` ranks higher.
2. **Item Price:** Lower price ranks higher.
3. **Row Index:** Smaller row index ranks higher.
4. **Column Index:** Smaller column index ranks higher.

The goal is to return the coordinates of the top $k$ highest-ranked reachable items. If fewer than $k$ eligible items can be reached, all reachable items are returned in ranked order.

In our representative instance:
- Grid dimensions: $3 \times 4$.
- Obstacles at $(0, 2), (1, 2), (2, 0)$.
- Eligible price range: $[2, 5]$.
- Start coordinate: $(0, 0)$ (contains empty aisle value $1$).
- Target count: $k = 3$.

---

## 2. Mathematical & Algorithmic Principles

### Unweighted Shortest Path Invariance via BFS

In an unweighted grid graph where every step has cost $1$:
- Standard Breadth-First Search using a First-In First-Out (FIFO) queue expands cells in monotonically non-decreasing order of distance $d$.
- When a cell $(r, c)$ is first dequeued at distance $d$, that distance is guaranteed to be the exact shortest path from `start`.
- Any cell with distance $d_1 < d_2$ strictly precedes cells of distance $d_2$ in the primary ranking criterion.

### Multi-Key Lexicographical Tuple Ordering

Every eligible item encountered during the search is recorded as a priority tuple:
$$\text{Candidate} = (\text{distance}, \, \text{price}, \, \text{row}, \, \text{col})$$

Comparison between two candidates $A$ and $B$ proceeds lexicographically:
$$A < B \iff \begin{cases} 
d_A < d_B \\
d_A = d_B \land p_A < p_B \\
d_A = d_B \land p_A = p_B \land r_A < r_B \\
d_A = d_B \land p_A = p_B \land r_A = r_B \land c_A < c_B
\end{cases}$$

### Candidate Filtering & Selection

1. **Traversability Invariant:** A neighbor $(nr, nc)$ is enqueued if and only if $0 \le nr < m$, $0 \le nc < n$, it has not been visited previously, and $\text{grid}[nr][nc] \ne 0$.
2. **Eligibility Invariant:** A cell $(r, c)$ is added to the candidate pool if and only if $\text{low} \le \text{grid}[r][c] \le \text{high}$. Note that the starting cell itself may be eligible if its price falls within the range.
3. **Top-$k$ Extraction:** Once all reachable items are identified (or when all candidates up to the necessary distance layer have been collected), sorting the candidate list according to the 4-tuple key yields the required prefix of size $\min(k, |\text{Candidates}|)$.

| Priority Key Component | Source Metric | Tie-Breaking Role |
|---|---|---|
| Primary Key | BFS Level ($d$) | Prioritizes proximity to starting position |
| Secondary Key | $\text{grid}[r][c]$ | Prioritizes economical item affordability |
| Tertiary Key | Row Index ($r$) | Prioritizes top-to-bottom spatial ordering |
| Quaternary Key | Column Index ($c$) | Prioritizes left-to-right spatial ordering |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace the BFS traversal starting at $(0, 0)$ on the $3 \times 4$ grid:

```
Grid layout (P = price, W = wall, E = empty):
Row 0:  E(1)   P(2)   W(0)   E(1)
Row 1:  E(1)   P(3)   W(0)   E(1)
Row 2:  W(0)   P(2)   P(5)   E(1)
```

### Step 1: Initialize BFS at Start Coordinate $(0, 0)$
- Mark $(0, 0)$ visited.
- Value at $(0, 0)$ is $1$ (empty aisle). Since $1 \notin [2, 5]$, it is not an eligible item.
- Enqueue $((0, 0), d = 0)$.
- Candidate pool: empty.

### Step 2: Expand Distance Level $0$
- Dequeue $((0, 0), d = 0)$.
- Explore 4-directional neighbors:
  - $(0, 1)$: Value is $2 \ne 0$. Unvisited. Mark visited, enqueue with $d = 1$.
  - $(1, 0)$: Value is $1 \ne 0$. Unvisited. Mark visited, enqueue with $d = 1$.
  - $(-1, 0)$ and $(0, -1)$: Out of grid bounds.

### Step 3: Expand Distance Level $1$
- **Process $(0, 1)$ at $d = 1$:**
  - Value is $2$. Check price range: $2 \le 2 \le 5$ (True).
  - Add to candidate pool: Tuple $(d=1, p=2, r=0, c=1)$.
  - Explore neighbors:
    - $(0, 2)$: Value is $0$ (Wall, blocked).
    - $(1, 1)$: Value is $3$. Unvisited. Mark visited, enqueue with $d = 2$.
- **Process $(1, 0)$ at $d = 1$:**
  - Value is $1$. Not in $[2, 5]$.
  - Explore neighbors:
    - $(2, 0)$: Value is $0$ (Wall, blocked).
    - $(1, 1)$: Already visited.

### Step 4: Expand Distance Level $2$
- **Process $(1, 1)$ at $d = 2$:**
  - Value is $3$. Check price range: $2 \le 3 \le 5$ (True).
  - Add to candidate pool: Tuple $(d=2, p=3, r=1, c=1)$.
  - Explore neighbors:
    - $(1, 2)$: Value is $0$ (Wall, blocked).
    - $(2, 1)$: Value is $2$. Unvisited. Mark visited, enqueue with $d = 3$.

### Step 5: Expand Distance Level $3$
- **Process $(2, 1)$ at $d = 3$:**
  - Value is $2$. Check price range: $2 \le 2 \le 5$ (True).
  - Add to candidate pool: Tuple $(d=3, p=2, r=2, c=1)$.
  - Explore neighbors:
    - $(2, 2)$: Value is $5$. Unvisited. Mark visited, enqueue with $d = 4$.

### Step 6: Expand Distance Level $4$
- **Process $(2, 2)$ at $d = 4$:**
  - Value is $5$. Check price range: $2 \le 5 \le 5$ (True).
  - Add to candidate pool: Tuple $(d=4, p=5, r=2, c=2)$.
  - Explore neighbors:
    - $(2, 3)$: Value is $1$. Unvisited. Mark visited, enqueue with $d = 5$.

### Step 7: Suffix Exploration & Candidate Ranking
- Traversal continues through empty aisles at $(2, 3), (1, 3), (0, 3)$ (all price $1$, not eligible).
- Final candidate pool contains $4$ items:
  1. $(1, 2, 0, 1)$ at coordinate $[0, 1]$
  2. $(2, 3, 1, 1)$ at coordinate $[1, 1]$
  3. $(3, 2, 2, 1)$ at coordinate $[2, 1]$
  4. $(4, 5, 2, 2)$ at coordinate $[2, 2]$
- Sorting by $(d, p, r, c)$ preserves this exact sequence because distances strictly increase ($1 < 2 < 3 < 4$).
- Extract top $k = 3$ coordinates:
  $$[[0, 1], [1, 1], [2, 1]]$$

---

## 4. Comprehensive State Trace

The table below catalogs every cell explored by BFS, its status, eligibility, and final ranking order:

| Dequeue Order | Coordinate $(r, c)$ | Cell Value | Shortest Distance $d$ | In Price Range $[2, 5]$? | Candidate Tuple $(d, p, r, c)$ | Global Rank | Included in Top $k=3$? |
|---|---|---|---|---|---|---|---|
| 1 | $(0, 0)$ | $1$ | $0$ | No ($1 < 2$) | N/A | - | No |
| 2 | $(0, 1)$ | $2$ | $1$ | Yes | $(1, 2, 0, 1)$ | Rank 1 | **Yes** ($[0, 1]$) |
| 3 | $(1, 0)$ | $1$ | $1$ | No ($1 < 2$) | N/A | - | No |
| 4 | $(1, 1)$ | $3$ | $2$ | Yes | $(2, 3, 1, 1)$ | Rank 2 | **Yes** ($[1, 1]$) |
| 5 | $(2, 1)$ | $2$ | $3$ | Yes | $(3, 2, 2, 1)$ | Rank 3 | **Yes** ($[2, 1]$) |
| 6 | $(2, 2)$ | $5$ | $4$ | Yes | $(4, 5, 2, 2)$ | Rank 4 | No (Exceeds $k=3$) |
| 7 | $(2, 3)$ | $1$ | $5$ | No ($1 < 2$) | N/A | - | No |
| 8 | $(1, 3)$ | $1$ | $6$ | No ($1 < 2$) | N/A | - | No |
| 9 | $(0, 3)$ | $1$ | $7$ | No ($1 < 2$) | N/A | - | No |

Final selected top $k = 3$ list: `[[0, 1], [1, 1], [2, 1]]`.

---

## 5. Algorithmic Correctness & Soundness

### Optimality of Distance Discovery
Because edge transitions in the grid have uniform unit weights, BFS guarantees that the first time any cell is visited, the path length equals its unweighted geodesic distance. Thus no subsequent path can discover a shorter route to that cell.

### Monotonic Distance Partitioning
The BFS queue maintains the invariant that at any moment, the queue contains elements with distance at most $d$ and $d + 1$. Because distance is the primary sorting key, all candidates discovered at distance $d$ are strictly superior to candidates discovered at distance $d' > d$. Secondary sorting within distance buckets (by price, row, column) resolves ties without compromising the distance hierarchy.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Starting Cell Contains an Eligible Item:** If $\text{low} \le \text{grid}[\text{start}_r][\text{start}_c] \le \text{high}$, the start cell has distance $0$ and must be added to the candidate pool immediately.
2. **Fewer Than $k$ Reachable Items:** If only $j < k$ eligible items are reachable (or completely walled off), the algorithm safely returns all $j$ items without padding or throwing index errors.
3. **No Eligible Items Reachable:** If all reachable cells have price $1$ or are out of the pricing range, an empty list `[]` is returned.
4. **Ties Across All Criteria:** Since each coordinate $(r, c)$ in the grid is unique, no two cells can share the exact same $(r, c)$. The 4-tuple comparison is guaranteed to be a strict total order with zero unresolved ties.

### Common Anti-Patterns
- **Dijkstra's Algorithm on Unit Grid:** Using a priority queue with Dijkstra incurs an unnecessary $O(mn \log(mn))$ factor. Standard queue BFS achieves unit distance exploration in linear $O(mn)$ time.
- **Treating Items as Obstacles:** Only cells with value $0$ are impassable. Cells with item prices $\ge 2$ can be traversed freely to reach downstream cells.
- **Prematurely Stopping at $k$ Candidates:** One cannot stop BFS as soon as $k$ eligible candidates are found, because other cells at the same or equal distance could have lower prices or smaller row indices that rank higher. One can only prune after completing the current distance wavefront.

---

## 7. Complexity Analysis

### Time Complexity
- **Grid Traversal:** Each cell in the $m \times n$ matrix is visited at most once, and each of its $4$ edges is checked once. The BFS phase takes $O(m \cdot n)$ time.
- **Candidate Ranking:** Let $C$ be the number of eligible items discovered, where $C \le m \cdot n$. Sorting the candidate list of size $C$ takes $O(C \log C)$ time (or $O(C \log k)$ using a fixed-size max-heap).
- Total time complexity is $O(m \cdot n + C \log C)$, well within execution limits for $m \cdot n \le 10^5$.

### Auxiliary Space Complexity
- A 2D visited boolean array or in-place bitmask takes $O(m \cdot n)$ space.
- The BFS queue holds at most $O(m \cdot n)$ coordinates at any time.
- The candidate pool stores at most $C \le m \cdot n$ tuples.
- Total auxiliary space complexity is $O(m \cdot n)$.
