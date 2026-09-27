# Guided Example: Swim in Rising Water

We trace the step-by-step continuous water level rise simulation ($t \ge 0$), minimax bottleneck path characterization ($\min_{\text{paths}} \max_{(x, y) \in P} grid[x][y]$), elevation-indexed cell activation schedule ($hi[t] = (x, y)$), 4-directional percolation edge expansion ($grid[nx][ny] \le t$), Disjoint Set Union (Union-Find) component coalescence, and source-to-destination percolation connectivity ($find(0) == find(n^2 - 1)$) on representative 2D elevation terrains:

- **Input:**
  $$
  grid = \begin{bmatrix}
  0 & 2 \\
  1 & 3
  \end{bmatrix}
  $$
- **Required output:** `3`
  - Hydrological simulation specifications:
    - On an $n \times n$ grid, each cell $(i, j)$ has elevation $grid[i][j]$. Elevations are a permutation of $\{0, 1, \dots, n^2 - 1\}$.
    - At time $t$, water level everywhere is $t$.
    - A cell $(i, j)$ is submerged and traversable if and only if:
      $$
      grid[i][j] \le t
      $$
    - You can move between adjacent submerged cells instantaneously.
    - Objective: Find the **minimum time $t$** required to travel from $(0, 0)$ to $(n - 1, n - 1)$.
    - For $\begin{bmatrix} 0 & 2 \\ 1 & 3 \end{bmatrix}$:
      - Start cell $(0, 0)$ has elevation 0.
      - Target cell $(1, 1)$ has elevation 3.
      - At time $t = 0$: only cell $(0, 0)$ is underwater.
      - At time $t = 1$: cell $(1, 0)$ submerges. Submerged path exists from $(0, 0)$ to $(1, 0)$.
      - At time $t = 2$: cell $(0, 1)$ submerges.
      - At time $t = 3$: cell $(1, 1)$ submerges, connecting to $(1, 0)$ and $(0, 1)$.
      - Path $(0, 0) \to (1, 0) \to (1, 1)$ is now completely submerged!
      - Minimal required time is **3**.
- **Minimax Bottleneck & DSU Percolation Invariant:**
  - **The Minimax Formulation:**
    - The problem asks for the minimax bottleneck path:
      $$
      t^* = \min_{P: (0, 0) \rightsquigarrow (n-1, n-1)} \max_{(x, y) \in P} grid[x][y]
      $$
  - **Percolation via Inverted Activation:**
    - Because elevations are unique integers in $[0, n^2 - 1]$, precompute an array $hi$ where $hi[t]$ records the coordinate of the cell having elevation $t$:
      $$
      hi[grid[i][j]] = i \cdot n + j
      $$
    - As time $t$ increments from $0$ to $n^2 - 1$:
      1. Cell $(x, y) = hi[t]$ is activated (submerged).
      2. For each of its 4 cardinal neighbors $(nx, ny)$:
         - If $(nx, ny)$ is within grid bounds and already submerged ($grid[nx][ny] \le t$):
           - Merge their components in the Union-Find structure:
             $$
             uf.union((x, y), \; (nx, ny))
             $$
      3. Check connectivity between start $0$ and end $n^2 - 1$:
         $$
         uf.connected(0, \; n^2 - 1)
         $$
      4. The very first time $t$ that yields `true` is mathematically the exact minimum bottleneck elevation!
- **Step-by-Step Worked Execution Trace on $grid = [[0, 2], [1, 3]]$:**
  - Grid size: $n = 2$, total cells $m = 2 \times 2 = 4$.
  - Start node: index $0$ (cell $(0, 0)$).
  - Target node: index $3$ (cell $(1, 1)$).
  - **Phase 0: Inverted Index Mapping:**
    - $grid[0][0] = 0 \implies hi[0] = (0, 0)$ (Node 0)
    - $grid[1][0] = 1 \implies hi[1] = (1, 0)$ (Node 2)
    - $grid[0][1] = 2 \implies hi[2] = (0, 1)$ (Node 1)
    - $grid[1][1] = 3 \implies hi[3] = (1, 1)$ (Node 3)
  - **Phase 1: Time $t = 0$ (Activate $(0, 0)$):**
    - Cell $(0, 0)$ submerged.
    - Check neighbors: $(0, 1)$ has elevation $2 > 0$ (unsubmerged), $(1, 0)$ has elevation $1 > 0$ (unsubmerged).
    - No edges added.
    - $find(0) \ne find(3)$ ($0 \ne 3$).
  - **Phase 2: Time $t = 1$ (Activate $(1, 0)$):**
    - Cell $(1, 0)$ (Node 2) submerged.
    - Check neighbor $(0, 0)$: $grid[0][0] = 0 \le 1 \implies \mathbf{Submerged!}$
      - Union Node 2 and Node 0:
        $$
        p[find(2)] \leftarrow find(0) \implies \text{Component: } \{0, 2\}
        $$
    - Check neighbor $(1, 1)$: $grid[1][1] = 3 > 1$ (unsubmerged).
    - Connectivity check: $find(0) \ne find(3)$ (Node 3 still isolated).
  - **Phase 3: Time $t = 2$ (Activate $(0, 1)$):**
    - Cell $(0, 1)$ (Node 1) submerged.
    - Check neighbor $(0, 0)$: $grid[0][0] = 0 \le 2 \implies \mathbf{Submerged!}$
      - Union Node 1 and Node 0:
        $$
        p[find(1)] \leftarrow find(0) \implies \text{Component: } \{0, 1, 2\}
        $$
    - Check neighbor $(1, 1)$: $grid[1][1] = 3 > 2$ (unsubmerged).
    - Connectivity check: $find(0) \ne find(3)$.
  - **Phase 4: Time $t = 3$ (Activate $(1, 1)$):**
    - Cell $(1, 1)$ (Node 3, Destination) submerged!
    - Check neighbor $(1, 0)$: $grid[1][0] = 1 \le 3 \implies$ Union Node 3 and Node 2.
    - Check neighbor $(0, 1)$: $grid[0][1] = 2 \le 3 \implies$ Union Node 3 and Node 1.
    - All 4 nodes are now in the single component $\{0, 1, 2, 3\}$!
    - Connectivity check:
      $$
      find(0) == find(3) \implies \mathbf{Path\ Established!}
      $$
    - Stop simulation and return time:
      $$
      ans = \mathbf{3}
      $$
- **Winding Low Route Trace ($n = 5$):**
  - Even if a direct diagonal path exists with high elevations (e.g. 24), a winding path through cells $\le 16$ connects start to end at time $t = 16$.
  - DSU percolation naturally discovers the lowest bottleneck path regardless of route length.
- **Single Cell Grid ($n = 1$):**
  - $grid = [[0]]$.
  - Start is destination $\implies$ returns **0**.

This instance demonstrates lattice percolation theory and Kruskal-style minimum bottleneck spanning forest generation, mathematically proves why activation order monotonicity establishes earliest connected component coalescence, and derives $O(N^2 \alpha(N^2))$ runtime and $O(N^2)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an $n \times n$ elevation grid:
At time $t$, you can traverse any cell with elevation $\le t$.
Find the **minimum time $t$** to travel from $(0, 0)$ to $(n - 1, n - 1)$.

```text
grid:
  0 2
  1 3

t = 0: Cell (0, 0) submerged.
t = 1: Cell (1, 0) submerged. Connected to (0, 0).
t = 2: Cell (0, 1) submerged. Connected to (0, 0).
t = 3: Cell (1, 1) submerged. Connects to (1, 0) and (0, 1).
       Path from (0, 0) to (1, 1) is now OPEN!

Result: 3
```

### The Invariant of the Percolation Threshold
- Finding the minimum time to connect start and end is identical to finding the percolation threshold on the grid.
- Activating cells in order of elevation $t = 0, 1, \dots$ and unioning with adjacent already-submerged neighbors finds the connection point at the first moment $(0, 0)$ and $(n-1, n-1)$ share the same DSU component.

---

## 2. Conceptual Foundation & Invariants

### 1. Minimax Bottleneck Path:
$$
t^* = \min_{P} \max_{(x, y) \in P} grid[x][y]
$$

### 2. DSU Percolation Ingestion:
For $t = 0, 1, \dots, n^2 - 1$:
$$
(x, y) = hi[t]
$$
$$
\forall (nx, ny) \in \text{neighbors}(x, y): \quad \text{if } grid[nx][ny] \le t \implies uf.union((x, y), (nx, ny))
$$
$$
\text{if } uf.find(0) == uf.find(n^2 - 1) \implies \text{return } t
$$

> **Lattice Percolation Threshold Invariant.** The bond percolation on the finite grid $\mathbb{Z}_n^2$ ordered by cell elevation generates an increasing filtration of subgraphs $G_0 \subseteq G_1 \subseteq \dots \subseteq G_{n^2-1}$. The target event $s \rightsquigarrow t$ is monotone, certified at the minimal index $t^*$ via the disjoint-set forest.

---

## 3. Step-by-Step Worked Execution

We trace $grid = [[0, 2], [1, 3]]$:

---

### Step 1: $t = 0$
- Activate $(0, 0) = 0$. No neighbors.

---

### Step 2: $t = 1$
- Activate $(1, 0) = 1$. Connects to $(0, 0) \implies \{ (0, 0), (1, 0) \}$.

---

### Step 3: $t = 2$
- Activate $(0, 1) = 2$. Connects to $(0, 0) \implies \{ (0, 0), (1, 0), (0, 1) \}$.

---

### Step 4: $t = 3$
- Activate $(1, 1) = 3$. Connects to $(1, 0)$ and $(0, 1)$.
- $(0, 0)$ and $(1, 1)$ connected!

---

### Step 5: Output
$$
\mathbf{3}
$$

---

## 4. Complete Execution Trace

| Time Step $t$ | Submerged Cell $(x, y)$ | Neighbors $\le t$ | DSU Edge Added | Start & End Connected? | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $(0, 0)$ | None | None | No | Continue |
| $1$ | $(1, 0)$ | $(0, 0)$ | $union((1, 0), (0, 0))$ | No | Continue |
| $2$ | $(0, 1)$ | $(0, 0)$ | $union((0, 1), (0, 0))$ | No | Continue |
| **$3$** | **$(1, 1)$** | **$(1, 0), (0, 1)$** | **$union((1, 1), (1, 0))$** | **Yes** | **Return `3`** |

---

## 5. Boundary Cases & Failure Modes

- **Start/End Bottleneck:** The answer is always $\ge \max(grid[0][0], grid[n-1][n-1])$ because both endpoints must be submerged.
- **Single Cell ($n = 1$):** Start is end $\implies$ returns 0.
- **High Winding Path:** The lowest path may twist and visit nearly all cells before reaching the end.
- **Dijkstra Equivalent:** Modified Dijkstra with priority queue prioritizing minimum edge elevation achieves the same optimal answer.

---

## 6. Traps & Common Anti-Patterns

- **Standard BFS / DFS at Every $t$ ($O(N^4)$):** Running a full search from scratch at every time step recomputes connectivity from zero. Using DSU or Binary Search avoids this waste.
- **Sorting Grid Cells with Comparison Sort ($O(N^2 \log N)$):** Because the elevations are a known permutation of $0 \dots n^2 - 1$, an array `hi` of size $n^2$ indexes them directly in $O(N^2)$ time with zero comparisons.
- **Forgetting Grid Boundary Checks:** Ensure adjacent neighbors $(nx, ny)$ satisfy $0 \le nx < n$ and $0 \le ny < n$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initializing $hi$ table: $\mathcal{O}(N^2)$.
  - Iterating through $N^2$ levels, each adding at most 4 edges: $\mathcal{O}(N^2 \alpha(N^2))$.
  - Total Time: strictly $\mathcal{O}(N^2 \alpha(N^2))$ where $N \le 50 \implies \le 2500$ operations. Completes in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N^2)$ memory for the DSU parent array and $hi$ coordinate index table.
