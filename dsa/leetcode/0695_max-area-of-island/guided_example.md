# Guided Example: Max Area of Island

We trace the step-by-step connected component exploration over binary matrices, 4-directional flood fill depth-first search, in-place cell sinking ($grid[i][j] \leftarrow 0$), recursive branch area summation ($area = 1 + \sum area(neighbor)$), and global maximum island size tracking on representative grid instances:

- **Input:**
  $$
  grid = \begin{bmatrix}
  1 & 1 \\
  0 & 1
  \end{bmatrix}
  $$
- **Required output:** `3`
  - Island definitions:
    - An island is a maximal connected component of land cells (`1`s) connected 4-directionally (up, down, left, right).
    - The area of an island is defined as the total number of `1` cells it contains.
    - If no land cells exist, the maximum area is `0`.
    - In the $2 \times 2$ grid above:
      - The three cells $(0, 0)$, $(0, 1)$, and $(1, 1)$ are connected together.
      - Total area is $3$.
- **Flood Fill & In-Place Sinking Invariant:**
  - **Component Area Recurrence:**
    - Let $dfs(i, j)$ compute the total area of the connected component containing cell $(i, j)$:
      - If $grid[i][j] == 0$, the cell is water (or already counted) $\implies$ area is $0$.
      - If $grid[i][j] == 1$:
        - Mark the cell as visited by sinking it:
          $$
          grid[i][j] \leftarrow 0
          $$
        - Contribute $1$ for the current cell.
        - Recursively explore all four adjacent neighbors $(x, y) \in \{(i-1, j), (i+1, j), (i, j-1), (i, j+1)\}$:
          $$
          dfs(i, j) = 1 + \sum_{(x, y) \text{ valid}} dfs(x, y)
          $$
  - **Single-Visit Guarantee:**
    - By mutating $grid[i][j] \to 0$ the moment a cell is entered, no cell can ever be visited or counted more than once.
    - This eliminates the need for an external visited matrix and guarantees linear runtime.
  - **Global Maximum Reduction:**
    $$
    ans = \max_{\substack{0 \le i < m \\ 0 \le j < n}} dfs(i, j)
    $$
- **Step-by-Step Worked Execution Trace on the $2 \times 2$ Grid:**
  - Dimensions: $m = 2, n = 2$.
  - Grid:
    $$
    \begin{bmatrix}
    (0, 0): 1 & (0, 1): 1 \\
    (1, 0): 0 & (1, 1): 1
    \end{bmatrix}
    $$
  - Global maximum tracker: $max\_area = 0$.
  - **Cell $(0, 0)$:**
    - $grid[0][0] == 1 \implies$ Start $dfs(0, 0)$:
      - Base contribution: $area = 1$.
      - Sink cell: $grid[0][0] \leftarrow 0$.
      - **Explore Neighbor 1: Up $(-1, 0)$:** Out of bounds.
      - **Explore Neighbor 2: Down $(1, 0)$:** $grid[1][0] == 0$ (Water). Returns $0$.
      - **Explore Neighbor 3: Left $(0, -1)$:** Out of bounds.
      - **Explore Neighbor 4: Right $(0, 1)$:**
        - $grid[0][1] == 1 \implies$ Recurse $dfs(0, 1)$:
          - Base contribution: $area = 1$.
          - Sink cell: $grid[0][1] \leftarrow 0$.
          - **Explore $(0, 1)$ Up $(-1, 1)$:** Out of bounds.
          - **Explore $(0, 1)$ Left $(0, 0)$:** Already sunk ($grid[0][0] == 0$). Returns $0$.
          - **Explore $(0, 1)$ Right $(0, 2)$:** Out of bounds.
          - **Explore $(0, 1)$ Down $(1, 1)$:**
            - $grid[1][1] == 1 \implies$ Recurse $dfs(1, 1)$:
              - Base contribution: $area = 1$.
              - Sink cell: $grid[1][1] \leftarrow 0$.
              - All 4 neighbors of $(1, 1)$ are either out of bounds or $0$.
              - $dfs(1, 1) = 1 + 0 = \mathbf{1}$.
              - Returns $1$ to $(0, 1)$.
          - $dfs(0, 1) = 1 + dfs(1, 1) = 1 + 1 = \mathbf{2}$.
          - Returns $2$ to $(0, 0)$.
      - $dfs(0, 0) = 1 + dfs(0, 1) = 1 + 2 = \mathbf{3}$.
    - Island area found: $3$.
    - Update maximum:
      $$
      max\_area \leftarrow \max(0, 3) = \mathbf{3}
      $$
  - **Remaining Grid Scans:**
    - $(0, 1)$: Already sunk ($0$).
    - $(1, 0)$: Water ($0$).
    - $(1, 1)$: Already sunk ($0$).
  - **Step 4: Output:**
    $$
    ans = max\_area = \mathbf{3}
    $$
- **All Water Grid ($grid = [[0, 0], [0, 0]]$):**
  - No cell triggers DFS $\implies$ returns **`0`**.
- **Disjoint Multiple Islands ($grid = [[1, 0], [0, 1]]$):**
  - Island 1 at $(0, 0)$: area 1.
  - Island 2 at $(1, 1)$: area 1.
  - Maximum area: $\max(1, 1) = \mathbf{1}$.

This instance demonstrates connected component size computation on planar adjacency graphs, mathematically proves why in-place state mutation provides strict cycle-free DFS traversal without auxiliary sets, and derives $O(M \cdot N)$ execution time and $O(M \cdot N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a 2D binary grid:
Find the **maximum area** of an island (number of connected 1s).
If no island exists, return 0.

```text
grid:
  1  1
  0  1

Connected land cells: (0, 0), (0, 1), (1, 1)
Total cells in this island = 3
Result: 3
```

### The Invariant of In-Place Sinking
- When visiting a land cell $(i, j)$, immediately flip it from $1 \to 0$.
- This prevents infinite loops, guarantees each cell is processed exactly once, and avoids allocating a separate $O(M \cdot N)$ visited array.

---

## 2. Conceptual Foundation & Invariants

### 1. The Component Area DFS:
$$
dfs(i, j) = \begin{cases} 0 & \text{if } grid[i][j] == 0 \\ 1 + \sum_{(x, y) \in N(i, j)} dfs(x, y) & \text{if } grid[i][j] == 1 \ (\text{after } grid[i][j] \leftarrow 0) \end{cases}
$$

### 2. Global Maxima:
$$
ans = \max_{i, j} dfs(i, j)
$$

> **Connected Component Cardinality Invariant.** In any finite graph $G = (V, E)$, the cardinality of the connected component containing vertex $v$ equals the sum of vertices discovered during breadth-first or depth-first search rooted at $v$, with each vertex visited at most once.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Discover $(0, 0)$
- $grid[0][0] = 1$. Sink to $0$.
- Recurse to $(0, 1)$.

---

### Step 2: Discover $(0, 1)$
- $grid[0][1] = 1$. Sink to $0$.
- Recurse to $(1, 1)$.

---

### Step 3: Discover $(1, 1)$
- $grid[1][1] = 1$. Sink to $0$.
- No more unvisited neighbors $\implies$ return 1.

---

### Step 4: Unwind
- $(0, 1)$ returns $1 + 1 = 2$.
- $(0, 0)$ returns $1 + 2 = \mathbf{3}$.
- Max area = **`3`**.

---

## 4. Complete Execution Trace

| Scanned Cell $(i, j)$ | Value | Action Taken | Sub-Calls Generated | Area Returned | Global Max Area |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $(0, 0)$ | $1$ | Sink to $0$, start DFS | $(0, 1)$ | $3$ | **`3`** |
| $(0, 1)$ | $0$ (sunk) | Skip | — | $0$ | $3$ |
| $(1, 0)$ | $0$ | Skip | — | $0$ | $3$ |
| $(1, 1)$ | $0$ (sunk) | Skip | — | $0$ | $3$ |
| **Final** | — | — | — | — | **`3`** |

---

## 5. Boundary Cases & Failure Modes

- **All Water Grid:** Returns 0.
- **Entire Grid is One Island ($M \times N$ of 1s):** Returns $M \cdot N$.
- **Single Cell Grid ($[[1]]$):** Returns 1.
- **Diagonal Cells Only ($[[1, 0], [0, 1]]$):** Diagonal cells do not connect $\implies$ returns 1.

---

## 6. Traps & Common Anti-Patterns

- **Diagonal Connections:** The problem explicitly specifies **4-directionally** connected (horizontal or vertical only). Do not explore diagonal neighbors.
- **Sinking After Children Calls:** You must sink the cell ($grid[i][j] = 0$) **before** making recursive calls to neighbors; otherwise, a neighbor will immediately call back to $(i, j)$, causing an infinite recursion stack overflow.
- **Allocating Separate Boolean Visited Array:** Sinking in-place on `grid` saves memory and simplifies code.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Every cell is visited at most once during the outer scan.
  - Every cell is entered at most once during the DFS.
  - Total Time: strictly linear $\mathcal{O}(M \cdot N)$. Completes in $< 5$ ms for $M = N = 50$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ auxiliary space for the recursion call stack in the worst-case serpentine island.
