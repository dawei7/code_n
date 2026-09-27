# Guided Example: Number of Islands II

We trace the step-by-step dynamic land addition, 2D grid flattening ($i \times n + j$), disjoint set union (DSU) with path compression and union-by-size, duplicate query guards, and online connected component tracking on representative island evolution instances:

- **Input:** $m = 3, \; n = 3, \quad \text{positions} = [[0, 0], [0, 1], [1, 2], [2, 1]]$
- **Required output:** $[1, 1, 2, 3]$
  - After $[0, 0]$: Isolated single cell $\implies 1$ island
  - After $[0, 1]$: Adjacent to $[0, 0]$, unions into same component $\implies 1$ island
  - After $[1, 2]$: Disjoint from existing land $\implies 2$ islands
  - After $[2, 1]$: Disjoint from existing land $\implies 3$ islands
- **Multi-Island Bridge Merge:** If an added land cell touches multiple distinct islands simultaneously, each successful merge decrements the component count by $1$
- **Duplicate Position Invariance:** Re-adding an existing land cell leaves the island count unchanged without redundant union operations
- **Diagonal Independence:** Diagonally adjacent land cells do NOT share edges and remain separate components unless bridged horizontally or vertically

This instance demonstrates dynamic graph connectivity via Disjoint Set Union (DSU), proves why a full $O(K \cdot M N)$ recalculation is avoided in favor of $O(K \cdot \alpha(M N))$ near-linear online updates, details the component counter invariant ($\text{cnt} \leftarrow \text{cnt} + 1 - \sum \text{merges}$), and operates in $O(M N)$ space.

---

## 1. Instance & Teaching Goal

Given a $3 \times 3$ grid initially filled entirely with water (`0`):
Add land cells one by one at given coordinates:
$$
\text{positions} = [[0, 0], [0, 1], [1, 2], [2, 1]]
$$
After each addition, return the total count of connected islands.
- An island is a 4-directionally connected (horizontal/vertical) maximal component of land cells (`1`).

```text
Step 1: Add [0, 0]    Step 2: Add [0, 1]    Step 3: Add [1, 2]    Step 4: Add [2, 1]
   [1] 0  0              [1][1] 0              [1][1] 0              [1][1] 0
    0  0  0               0  0  0               0  0 [1]              0  0 [1]
    0  0  0               0  0  0               0  0  0               0 [1] 0

Islands: 1            Merged with (0,0)     Isolated island       Isolated island
                      Islands: 1            Islands: 2            Islands: 3
```

### Naive BFS/DFS vs Online Disjoint Set Union
- Running BFS/DFS after every position takes $O(M N)$ per addition, totaling $O(K \cdot M N)$ for $K$ additions (up to $10^8$ operations).
- **Disjoint Set Union (DSU):**
  - When turning water into land at $(i, j)$, temporarily increment island count by $1$.
  - Check all 4 adjacent cardinal neighbors $(x, y)$.
  - For each neighbor that is already land, attempt `union((i, j), (x, y))`.
  - If the roots differ, two previously disjoint islands have merged: decrement the island count by $1$!
Each step runs in nearly $O(1)$ amortized time $O(\alpha(M N))$.

---

## 2. Conceptual Foundation & Invariants

### 1D Cell Index Flattening
For a grid of width $n$, 2D coordinate $(i, j)$ maps to unique 1D index:
$$
\text{id}(i, j) = i \cdot n + j \quad \in [0, \; mn - 1]
$$

### Disjoint Set Union (DSU) Structure
- `p[x]`: Parent pointer for node $x$ (with path compression in `find`).
- `size[x]`: Size of component rooted at $x$ (for union-by-size).
- `grid[i][j]`: Tracks whether cell $(i, j)$ is already active land.

### Dynamic Processing Protocol for Position $(i, j)$:
1. **Duplicate Guard:**
   If $\text{grid}[i][j] == 1$, the cell is already land:
   Append current count and `continue`.
2. **Activate Land:**
   Set $\text{grid}[i][j] = 1$.
   Increment component count:
   $$
   \text{cnt} \leftarrow \text{cnt} + 1
   $$
3. **Inspect 4 Cardinal Neighbors $(x, y) \in \{(i-1, j), (i+1, j), (i, j-1), (i, j+1)\}$:**
   - If $0 \le x < m$ and $0 \le y < n$ and $\text{grid}[x][y] == 1$:
     If $\text{uf.union}(\text{id}(i, j), \; \text{id}(x, y))$ returns `True` (different roots merged):
     $$
     \text{cnt} \leftarrow \text{cnt} - 1
     $$
4. Append `cnt` to result list `ans`.

> **Invariant.** After processing position $k$, `cnt` reflects the exact number of connected components formed by the active land cells. Two cells share a DSU root if and only if they belong to the same 4-connected island.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $m = 3, n = 3$ with positions $[[0, 0], [0, 1], [1, 2], [2, 1]]$:
Initialize `grid` ($3 \times 3$ of 0s), `cnt = 0`, `ans = []`.

---

### Step 1: Add Position $[0, 0]$ ($\text{id} = 0 \times 3 + 0 = 0$)
- `grid[0][0]` was 0 $\implies$ set `grid[0][0] = 1`.
- Increment count: $\text{cnt} = 0 + 1 = \mathbf{1}$.
- Neighbors of $(0, 0)$:
  - $(0, 1)$: Water (`0`)
  - $(1, 0)$: Water (`0`)
- No merges occur.
- Total islands: $\text{cnt} = \mathbf{1}$. `ans = [1]`.

---

### Step 2: Add Position $[0, 1]$ ($\text{id} = 0 \times 3 + 1 = 1$)
- `grid[0][1]` was 0 $\implies$ set `grid[0][1] = 1`.
- Increment count: $\text{cnt} = 1 + 1 = 2$.
- Neighbors of $(0, 1)$:
  - **Left neighbor $(0, 0)$** ($\text{id} = 0$): Active land!
    - Call $\text{union}(1, 0)$:
      $\text{find}(1) \ne \text{find}(0) \implies$ Merge components!
      Decrement count: $\text{cnt} = 2 - 1 = \mathbf{1}$.
  - Right neighbor $(0, 2)$: Water.
  - Down neighbor $(1, 1)$: Water.
- Total islands: $\text{cnt} = \mathbf{1}$. `ans = [1, 1]`.

---

### Step 3: Add Position $[1, 2]$ ($\text{id} = 1 \times 3 + 2 = 5$)
- `grid[1][2]` was 0 $\implies$ set `grid[1][2] = 1`.
- Increment count: $\text{cnt} = 1 + 1 = \mathbf{2}$.
- Neighbors of $(1, 2)$:
  - Up $(0, 2)$: Water.
  - Down $(2, 2)$: Water.
  - Left $(1, 1)$: Water.
- No merges occur.
- Total islands: $\text{cnt} = \mathbf{2}$. `ans = [1, 1, 2]`.

---

### Step 4: Add Position $[2, 1]$ ($\text{id} = 2 \times 3 + 1 = 7$)
- `grid[2][1]` was 0 $\implies$ set `grid[2][1] = 1`.
- Increment count: $\text{cnt} = 2 + 1 = \mathbf{3}$.
- Neighbors of $(2, 1)$:
  - Up $(1, 1)$: Water.
  - Left $(2, 0)$: Water.
  - Right $(2, 2)$: Water.
- No merges occur.
- Total islands: $\text{cnt} = \mathbf{3}$. `ans = [1, 1, 2, 3]`.

---

### Execution Complete
Final collected sequence:
$$
\mathbf{[1, 1, 2, 3]}
$$

---

## 4. Complete Execution Trace

```text
m = 3, n = 3

1. pos = [0, 0]: cnt = 1, neighbors all water -> cnt = 1 -> ans = [1]
2. pos = [0, 1]: cnt = 2, neighbor (0, 0) is land -> union(1, 0) -> cnt = 1 -> ans = [1, 1]
3. pos = [1, 2]: cnt = 2, neighbors all water -> cnt = 2 -> ans = [1, 1, 2]
4. pos = [2, 1]: cnt = 3, neighbors all water -> cnt = 3 -> ans = [1, 1, 2, 3]

Results: [1, 1, 2, 3]
```

| Operation Step | Added Cell $(i, j)$ | Flattened ID | Land Neighbors Found | Successful Merges | Active Islands $\text{cnt}$ | Output Sequence `ans` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | $(0, 0)$ | 0 | None | 0 | **1** | `[1]` |
| **2** | **$(0, 1)$** | **1** | **$(0, 0)$** | **1 (Merged with ID 0)** | **1** | **`[1, 1]`** |
| 3 | $(1, 2)$ | 5 | None | 0 | **2** | `[1, 1, 2]` |
| 4 | $(2, 1)$ | 7 | None | 0 | **3** | `[1, 1, 2, 3]` |

---

## 5. Algorithmic Correctness

**Soundness.** Adding a new land cell initially increases the number of connected components by at most 1. Every adjacent cell that is already land belongs to some existing component. Merging the new cell with an adjacent component's root reduces the total count by 1 if and only if their roots were previously distinct. If multiple neighbors already belong to the same component, subsequent calls to `union` return `False`, preventing over-decrementing.

**Completeness.** Every added position is processed in arrival order. Because the 4 cardinal directions cover all topological adjacencies in the grid, all new connections are detected immediately upon activation. Duplicate queries are guarded by checking `grid[i][j]`, guaranteeing idempotent behavior.

---

## 6. Traps This Instance Exposes

- **Duplicate Additions:** If the same coordinate appears multiple times in `positions`, turning an already active land cell into land again without a guard would erroneously increment `cnt` by 1. Checking `grid[i][j]` prevents duplicate counts.
- **Multiple Neighbors in the Same Island:** If a new cell touches two cells that are already part of the same island, only the first `union` returns `True`. The second `union` sees identical roots and returns `False`. Blindly decrementing `cnt` for every adjacent land neighbor causes severe undercounting.
- **Diagonal Neighbors:** Two cells that touch diagonally (e.g. $(0, 0)$ and $(1, 1)$) do not share an edge. Attempting 8-way connectivity violates problem rules.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(K \cdot \alpha(M N))$, where $K$ is the number of operations in `positions` and $M N$ is the total grid cells. For each addition, at most 4 union-find operations are executed. Each operation takes nearly constant $O(\alpha(M N))$ time using path compression and union by size (where $\alpha$ is the inverse Ackermann function, $\alpha(n) \le 4$). Total runtime is strictly linear with respect to operations.
- **Auxiliary Space Complexity:** $O(M N)$ auxiliary memory for the 2D grid matrix and the DSU parent and size arrays of length $M N$.
