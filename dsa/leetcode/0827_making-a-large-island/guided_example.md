# Guided Example: Making A Large Island

We trace the step-by-step 2D lattice connected component labeling via depth-first search, component unique identifier coloring, area mapping ($cnt[root]$), candidate water cell ($grid[i][j] == 0$) 4-neighbor adjacency inspection, duplicate component suppression via neighborhood sets, bridge merge potential evaluation ($1 + \sum_{c \in S} cnt[c]$), and maximum island size determination on representative binary grids:

- **Input:**
  $$
  grid = \begin{bmatrix}
  1 & 0 \\
  0 & 1
  \end{bmatrix}
  $$
- **Required output:** `3`
  - Island creation rules:
    - An $n \times n$ binary grid consists of land (`1`) and water (`0`).
    - An **island** is a 4-directionally connected group of `1`s.
    - You are permitted to change **at most one** `0` to a `1`.
    - Objective: Find the maximum possible size (area in cells) of an island after changing at most one `0`.
    - For $grid = [[1, 0], [0, 1]]$:
      - Initially, there are two separate diagonal islands of size 1: cell $(0, 0)$ and cell $(1, 1)$.
      - Changing cell $(0, 1)$ from `0` to `1`:
        - Cell $(0, 1)$ connects to its left neighbor $(0, 0)$ and its bottom neighbor $(1, 1)$.
        - Combined island area: $1$ (the new cell) $+ 1$ (cell $(0, 0)$) $+ 1$ (cell $(1, 1)$) $= \mathbf{3}$.
      - Changing cell $(1, 0)$ also yields area $\mathbf{3}$.
      - Maximum island size achievable: **`3`**.
- **Component ID Coloring & Neighbor Bridging Invariant:**
  - **Phase 1: Connected Component Labeling:**
    - Perform DFS / BFS over all `1`s in the grid.
    - Assign each distinct island a unique positive integer label:
      $$
      root \in \{1, 2, 3, \dots\}
      $$
    - Store the assigned component ID for each cell in matrix $p[i][j]$.
    - Maintain a frequency dictionary $cnt$ where $cnt[root]$ records the exact cell count of island $root$.
    - Establish the baseline answer as the largest natural island:
      $$
      ans \leftarrow \max(cnt.\text{values}(), \; 0)
      $$
  - **Phase 2: Bridge Simulation on Water Cells ($grid[i][j] == 0$):**
    - For every water cell $(i, j)$:
      - Inspect its 4 orthogonal neighbors $(x, y) \in \{(i-1, j), (i+1, j), (i, j-1), (i, j+1)\}$.
      - Collect the set $S$ of **distinct adjacent island IDs**:
        $$
        S = \{ p[x][y] \mid 0 \le x < n, \; 0 \le y < n, \; p[x][y] > 0 \}
        $$
      - Using a mathematical set $S$ automatically **prevents double-counting** when multiple neighboring cells belong to the exact same island!
      - If we flip cell $(i, j)$ from `0` to `1`, it bridges all distinct islands in $S$:
        $$
        \text{merged area} = 1 + \sum_{c \in S} cnt[c]
        $$
      - Relax: $ans \leftarrow \max(ans, \; \text{merged area})$.
- **Step-by-Step Worked Execution Trace on the $2 \times 2$ Grid:**
  - Grid:
    $$
    grid = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
    $$
  - Initialize: $n = 2, root = 0, cnt = \{\}, p = [[0, 0], [0, 0]]$.
  - **Phase 1: Component Labeling:**
    - Cell $(0, 0)$ is land ($grid[0][0] = 1, p[0][0] = 0$):
      - Start new component: $root \leftarrow 1$.
      - DFS colors $(0, 0)$: $p[0][0] = 1, cnt[1] = 1$.
      - Neighbors $(0, 1)$ and $(1, 0)$ are water $\implies$ DFS finishes.
    - Cell $(1, 1)$ is land ($grid[1][1] = 1, p[1][1] = 0$):
      - Start new component: $root \leftarrow 2$.
      - DFS colors $(1, 1)$: $p[1][1] = 2, cnt[2] = 1$.
      - DFS finishes.
    - Component summary:
      $$
      cnt = \{ 1: 1, \; 2: 1 \}
      $$
      $$
      p = \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix}
      $$
    - Baseline maximum natural island: $ans = \max(1, 1) = \mathbf{1}$.
  - **Phase 2: Water Bridge Evaluation:**
    - **Cell $(0, 1)$ (Water):**
      - Up $( -1, 1)$: out of bounds.
      - Down $(1, 1)$: in bounds, $p[1][1] = 2 \implies$ Island 2.
      - Left $(0, 0)$: in bounds, $p[0][0] = 1 \implies$ Island 1.
      - Right $(0, 2)$: out of bounds.
      - Adjacent island set:
        $$
        S = \{1, \; 2\}
        $$
      - Merged island size:
        $$
        1 + cnt[1] + cnt[2] = 1 + 1 + 1 = \mathbf{3}
        $$
      - Update: $ans \leftarrow \max(1, 3) = \mathbf{3}$.
    - **Cell $(1, 0)$ (Water):**
      - Up $(0, 0)$: Island 1.
      - Down $(2, 0)$: out of bounds.
      - Left $(1, -1)$: out of bounds.
      - Right $(1, 1)$: Island 2.
      - Adjacent island set: $S = \{1, 2\}$.
      - Merged island size: $1 + 1 + 1 = \mathbf{3}$.
      - Update: $ans \leftarrow \max(3, 3) = \mathbf{3}$.
  - **Global Maximum Achieved:**
    $$
    ans = \mathbf{3}
    $$
- **All Land Matrix Trace ($grid = [[1, 1], [1, 1]]$):**
  - All cells belong to Island 1 of size $4$.
  - No water cells exist ($x == 0$ loop never executes).
  - Baseline initialization returns $\max(cnt.\text{values}()) = \mathbf{4}$.
- **Duplicate Neighbor Island Suppression ($grid = [[1, 0, 1], [1, 1, 1]]$):**
  - Land forms a single U-shaped island wrapping around water cell $(0, 1)$.
  - Cell $(0, 1)$ has neighbors $(0, 0)$, $(1, 1)$, and $(0, 2)$, all belonging to Island 1.
  - Set $S = \{1\}$ ensures Island 1's area is added **only once**, correctly calculating $1 + cnt[1]$ rather than triple-counting.

This instance demonstrates vertex cut augmentation and connected component bridge optimization on planar grid graphs, mathematically proves why neighborhood ID set deduplication is necessary and sufficient for 1-hop hyperedge contraction, and derives $O(N^2)$ execution time and $O(N^2)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an $n \times n$ binary grid:
Change at most **one** 0 into a 1 to make the **largest possible island**.

```text
grid:
  1 0
  0 1

Islands before change:
  Island 1: at (0, 0), size = 1
  Island 2: at (1, 1), size = 1

Change water cell (0, 1) to 1:
  Connects to Island 1 (left) and Island 2 (down).
  New island size = 1 (new cell) + 1 (Island 1) + 1 (Island 2) = 3

Result: 3
```

### The Invariant of Neighbor Deduplication
- Color each connected island with a unique ID and store its size.
- For each 0 cell, collect the **set** of adjacent island IDs.
- A set avoids counting the same island multiple times if the water cell touches it on several sides.
- Total new size $= 1 + \sum_{id \in S} size[id]$.

---

## 2. Conceptual Foundation & Invariants

### 1. Connected Component Decomposition:
$$
V(grid) = \bigsqcup_{k = 1}^K C_k \quad \text{where each } C_k \text{ is a 4-connected land component}
$$
$$
cnt[k] = |C_k|, \quad p[i][j] = k \iff (i, j) \in C_k
$$

### 2. Bridge Augmentation Metric:
For each water cell $(i, j)$ with $grid[i][j] = 0$:
$$
S(i, j) = \{ p[x][y] \mid (x, y) \in \mathcal{N}(i, j) \;\land\; p[x][y] > 0 \}
$$
$$
ans = \max \left( \max_k |C_k|, \; \max_{(i, j), grid[i][j]=0} \Big( 1 + \sum_{k \in S(i, j)} cnt[k] \Big) \right)
$$

> **Vertex Addition Contraction Invariant.** Flipping a 0-cell to 1 creates a star contraction on the quotient component graph. The union of adjacent components $S(i, j)$ merged through the single vertex $(i, j)$ has cardinality exactly $1 + \sum_{c \in S} |C_c|$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Label Islands
- Island 1 at $(0, 0)$: size 1.
- Island 2 at $(1, 1)$: size 1.

---

### Step 2: Water Cell $(0, 1)$
- Neighbors: $(0, 0)$ (ID 1) and $(1, 1)$ (ID 2).
- Unique ID set: $\{1, 2\}$.
- Size $= 1 + 1 + 1 = \mathbf{3}$.

---

### Step 3: Water Cell $(1, 0)$
- Neighbors: $(0, 0)$ (ID 1) and $(1, 1)$ (ID 2).
- Size $= 1 + 1 + 1 = \mathbf{3}$.

---

### Step 4: Output
$$
\mathbf{3}
$$

---

## 4. Complete Execution Trace

| Water Cell $(i, j)$ | Adjacent Neighbors Valid | Neighbor Component IDs | Unique ID Set $S$ | Merged Island Size | Running Max $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Initial Baseline | — | — | — | — | $1$ |
| $(0, 1)$ | $(0, 0), (1, 1)$ | $1, 2$ | $\{1, 2\}$ | $1 + 1 + 1 = 3$ | **$3$** |
| **$(1, 0)$** | **$(0, 0), (1, 1)$** | **$1, 2$** | **$\{1, 2\}$** | **$1 + 1 + 1 = 3$** | **`3`** |

---

## 5. Boundary Cases & Failure Modes

- **All 1s ($grid = [[1, 1], [1, 1]]$):** No 0 cells to flip; baseline check returns $n^2 = 4$.
- **All 0s ($grid = [[0, 0], [0, 0]]$):** Any cell flipped becomes an island of size 1 $\implies 1$.
- **Single Cell ($[[0]]$):** Flipping gives $1$.
- **Single Island Surrounding a Zero:** Water cell touches the same island on 3 sides; set $S$ prevents tripling the count.

---

## 6. Traps & Common Anti-Patterns

- **Running BFS for Every 0 Cell ($O(N^4)$):** For $N = 500$, running a complete BFS for each of the $250,000$ water cells takes $\approx 6 \times 10^{10}$ operations (massive TLE). Pre-labeling islands in $O(N^2)$ allows evaluating each water cell in $O(1)$.
- **Using a List Instead of a Set for Adjacent Island IDs:** If a water cell touches the same island on multiple sides, adding counts from a list double- or triple-counts the island's cells! Always use `set()`.
- **Forgetting the All-1s Grid Case:** If there are no 0s in the grid, the loop over water cells never runs; initialize $ans = \max(cnt.\text{values}() \text{ or } [0])$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - DFS component labeling visits each cell once: $\mathcal{O}(N^2)$ where $N \le 500$.
  - Water cell evaluation checks 4 neighbors per cell: $4 \times N^2 = \mathcal{O}(N^2)$.
  - Total Time: strictly linear in grid area $\mathcal{O}(N^2) \le 2.5 \times 10^5$ operations. Completes in $< 20$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N^2)$ memory for the component ID matrix $p$ and frequency map.
