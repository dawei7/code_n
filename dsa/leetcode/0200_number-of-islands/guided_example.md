# Guided Example: Number of Islands

We trace the step-by-step graph connected component extraction, in-place flood fill ("island sinking"), and 4-directional traversal mechanics on representative 2D binary grid maps:

- **Input Grid:**
  $$
  \text{grid} = \begin{bmatrix}
  \text{'1'} & \text{'1'} & \text{'0'} \\
  \text{'1'} & \text{'0'} & \text{'0'} \\
  \text{'0'} & \text{'0'} & \text{'1'}
  \end{bmatrix}
  $$
- **Required output:** $2$ (Island 1 spans $\{(0,0), (0,1), (1,0)\}$; Island 2 spans $\{(2,2)\}$)
- **Four-Corner Diagonal Instance:**
  $$
  \begin{bmatrix}
  \text{'1'} & \text{'0'} \\
  \text{'0'} & \text{'1'}
  \end{bmatrix} \implies 2 \quad \text{(Diagonals do not connect land)}
  $$
- **All Water Instance:** Grid of all `'0'`s $\implies 0$
- **All Land Instance:** Grid of all `'1'`s $\implies 1$ (Entire grid forms a single connected component)

This instance demonstrates modeling 2D grids as implicit undirected graphs, proves why in-place marking (`'1' \to '0'`) guarantees strictly $O(M \cdot N)$ time without auxiliary visited matrices, enforces 4-way orthogonal adjacency (excluding diagonals), and analyzes recursion stack safety.

---

## 1. Instance & Teaching Goal

Given an $M \times N$ binary matrix ($M = 3, N = 3$) where `'1'` denotes land and `'0'` denotes water:
$$
\text{grid} = \begin{bmatrix}
\text{'1'} & \text{'1'} & \text{'0'} \\
\text{'1'} & \text{'0'} & \text{'0'} \\
\text{'0'} & \text{'0'} & \text{'1'}
\end{bmatrix}
$$
Count the total number of islands. An island is a maximal connected component of land cells connected **orthogonally** (horizontally or vertically, **never diagonally**).

Visualizing the connectivity:
- Land cells $(0,0)$, $(0,1)$, and $(1,0)$ are adjacent to each other $\implies$ **Island 1**.
- Land cell $(2,2)$ touches only $(1,2)$ and $(2,1)$ inside the grid, both water `'0'`; its single in-grid diagonal neighbour $(1,1)$ is water as well, so no corner contact can join it to Island 1 either $\implies$ **Island 2**.
Total islands: $\mathbf{2}$.

The flood fill algorithm traverses the grid cell by cell:
- When a `'1'` is discovered, increment the island counter.
- Immediately trigger a traversal (DFS or BFS) to visit all reachable land cells in that island, flipping them to `'0'` ("sinking the island").
- When the outer loop reaches those cells later, they appear as water and are safely ignored.

---

## 2. Conceptual Foundation & Invariants

### Connected Components in Grid Graphs
Define an undirected graph $G = (V, E)$:
- $V = \{ (r, c) \mid \text{grid}[r][c] = \text{'1'} \}$.
- $E = \{ ((r, c), (r', c')) \mid |r - r'| + |c - c'| = 1 \}$.
The number of islands is the number of connected components in $G$.

### In-Place Flood Fill Algorithm:
Initialize $\text{islands} = 0$.

For row $r$ from $0$ to $M - 1$:
For column $c$ from $0$ to $N - 1$:
- If $\text{grid}[r][c] == \text{'1'}$:
  1. $\text{islands} \leftarrow \text{islands} + 1$.
  2. Invoke $\text{sink}(r, c)$ to flood-fill the component.

#### The `sink(r, c)` Procedure:
1. Bounds and Water Check:
   If $r < 0$ or $r \ge M$ or $c < 0$ or $c \ge N$ or $\text{grid}[r][c] \ne \text{'1'}$: return.
2. In-Place Visited Marking:
   $$
   \text{grid}[r][c] \leftarrow \text{'0'}
   $$
3. 4-Directional Recursive Expansion:
   $$
   \text{sink}(r - 1, c), \quad \text{sink}(r + 1, c), \quad \text{sink}(r, c - 1), \quad \text{sink}(r, c + 1)
   $$

> **Invariant.** Prior to visiting cell $(r, c)$, all land cells belonging to islands discovered earlier have been completely converted to `'0'`. Thus, encountering `'1'` guarantees the discovery of a distinct, uncounted island.

---

## 3. Step-by-Step Worked Execution

We trace the grid traversal and in-place component elimination:

### Step 1: Scan Cell $(0, 0)$
- $\text{grid}[0][0] = \text{'1'}$. Land encountered!
- Increment $\text{islands} = 0 + 1 = \mathbf{1}$.
- Launch $\text{sink}(0, 0)$:
  - Set $\text{grid}[0][0] = \text{'0'}$.
  - Recurse $(0, 1)$: $\text{grid}[0][1] = \text{'1'} \implies$ Set $\text{grid}[0][1] = \text{'0'}$.
    - Neighbors of $(0, 1)$: $(0, 2)$ is `'0'`, $(-1, 1)$ out of bounds, $(1, 1)$ is `'0'`.
  - Recurse $(1, 0)$: $\text{grid}[1][0] = \text{'1'} \implies$ Set $\text{grid}[1][0] = \text{'0'}$.
    - Neighbors of $(1, 0)$: $(2, 0)$ is `'0'`, $(1, 1)$ is `'0'`.

Grid state after sinking Island 1:
$$
\begin{bmatrix}
\mathbf{0} & \mathbf{0} & 0 \\
\mathbf{0} & 0 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

---

### Step 2: Intermediate Grid Scans (Water)
The outer loop continues row-major scanning:
- $(0, 1)$: `'0'` (Sunk by Island 1) $\implies$ Skip.
- $(0, 2)$: `'0'` (Water) $\implies$ Skip.
- $(1, 0)$: `'0'` (Sunk by Island 1) $\implies$ Skip.
- $(1, 1)$: `'0'` (Water) $\implies$ Skip.
- $(1, 2)$: `'0'` (Water) $\implies$ Skip.
- $(2, 0)$: `'0'` (Water) $\implies$ Skip.
- $(2, 1)$: `'0'` (Water) $\implies$ Skip.

---

### Step 3: Scan Cell $(2, 2)$
- $\text{grid}[2][2] = \text{'1'}$. Land encountered!
- Increment $\text{islands} = 1 + 1 = \mathbf{2}$.
- Launch $\text{sink}(2, 2)$:
  - Set $\text{grid}[2][2] = \text{'0'}$.
  - Check 4 neighbors: $(1, 2)$, $(3, 2)$, $(2, 1)$, $(2, 3)$ $\implies$ All are water `'0'` or out of bounds.

Final grid state:
$$
\begin{bmatrix}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & \mathbf{0}
\end{bmatrix}
$$

Scan completes. Total islands counted: $\mathbf{2}$.

---

## 4. Complete Execution Trace

```text
Initial Grid:
[ ['1', '1', '0'],
  ['1', '0', '0'],
  ['0', '0', '1'] ]

Encounter (0,0) = '1' -> ISLAND 1
  DFS sink: (0,0)->'0', (0,1)->'0', (1,0)->'0'
  Grid becomes all '0' except (2,2)

Encounter (2,2) = '1' -> ISLAND 2
  DFS sink: (2,2)->'0'
  Grid becomes all '0'

Total Islands: 2
```

| Cell $(r, c)$ | Initial Val | Action Taken | Cells Sunk During Fill | Sunk Grid Visualization | Island Count |
|:---:|:---:|:---|:---|:---:|:---:|
| **$(0, 0)$** | **`'1'`** | **New Island Found** | **$(0,0), (0,1), (1,0)$** | $\begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ | **1** |
| $(0, 1)$ | `'0'` | Skip (already sunk) | - | Unchanged | 1 |
| $(1, 0)$ | `'0'` | Skip (already sunk) | - | Unchanged | 1 |
| $(1, 1)$ | `'0'` | Skip (water) | - | Unchanged | 1 |
| **$(2, 2)$** | **`'1'`** | **New Island Found** | **$(2,2)$** | $\begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$ | **2 (Final)** |

### Complete Row-Major Scan Order

Every cell of the grid is examined exactly once, in row-major order, and only the cells that are still land when the scan reaches them can start a fill. The table records the value **as read**, which is why two cells that began as land appear here as water.

| Scan order | Cell $(r, c)$ | Value when scanned | Why it reads that way | Action | `islands` after the step |
|:---:|:---:|:---:|:---|:---|:---:|
| 1 | $(0, 0)$ | `'1'` | Original land, untouched by any earlier fill | New island seeded; fill launched | 1 |
| 2 | $(0, 1)$ | `'0'` | Land in the initial grid, sunk while Island 1 was filled | Skip | 1 |
| 3 | $(0, 2)$ | `'0'` | Water in the initial grid | Skip | 1 |
| 4 | $(1, 0)$ | `'0'` | Land in the initial grid, sunk while Island 1 was filled | Skip | 1 |
| 5 | $(1, 1)$ | `'0'` | Water in the initial grid, and the diagonal neighbour of $(2,2)$ | Skip | 1 |
| 6 | $(1, 2)$ | `'0'` | Water in the initial grid | Skip | 1 |
| 7 | $(2, 0)$ | `'0'` | Water in the initial grid | Skip | 1 |
| 8 | $(2, 1)$ | `'0'` | Water in the initial grid | Skip | 1 |
| 9 | $(2, 2)$ | `'1'` | Land that the first fill never reached, so it is still `'1'` | New island seeded; fill launched | 2 |

Rows 2 and 4 carry the whole idea of in-place marking: those two cells were land at the start, but by the time the outer loop arrives they are indistinguishable from water. The mutation is performing the job an auxiliary visited set would otherwise do, which is exactly why no separate visited matrix is needed.

### Island Inventory

| Island | Seed cell (first member in scan order) | Member cells | Size | Neighbours examined and rejected during the fill | Why this seed, and not another member |
|:---:|:---|:---|:---:|:---|:---|
| 1 | $(0, 0)$ | $(0,0), (0,1), (1,0)$ | 3 | $(0,2)$ is water, $(1,1)$ is water, $(2,0)$ is water, and the top and left edges are out of bounds | Row-major order reaches $(0,0)$ before any other member, and every other member lies below or to the right of it. |
| 2 | $(2, 2)$ | $(2,2)$ | 1 | $(1,2)$ is water, $(2,1)$ is water, the bottom and right edges are out of bounds, and the in-grid diagonal $(1,1)$ is water besides not being an edge | By the time the scan reaches row 2, $(2,2)$ is the only land cell left, so it cannot have been absorbed by an earlier fill. |

---

## 5. Algorithmic Correctness

**Soundness.** In a flood fill traversal, every land cell reachable via horizontal or vertical steps from the root seed is visited. Because each visited cell is mutated to `'0'` immediately upon entry, it cannot be traversed again or counted as the root of another island. Each connected component is thus counted exactly once.

**Completeness.** Every cell $(r, c)$ in the $M \times N$ matrix is examined by the outer loop. Any land component present in the grid is guaranteed to have at least one cell visited and counted.

---

## 6. Traps This Instance Exposes

- **Diagonal Adjacency Fallacy:** Cells meeting only at a corner are not joined by an edge. In this grid the diagonal pair is $(0,1)$ and $(1,0)$, and 4-connectivity ignores that contact entirely: the two cells are joined only through $(0,0)$. The rule becomes decisive on other instances, which is why the lesson instance cannot prove it on its own. Only the 4 cardinal directions ($(-1,0), (1,0), (0,-1), (0,1)$) are valid edges.
- **Marking Visited on Pop Instead of Push (BFS):** In a queue-based BFS, if cells are marked `'0'` only when popped from the queue, adjacent nodes will enqueue the same neighbor multiple times, causing exponential memory growth and Time Limit Exceeded (TLE). A cell must be marked `'0'` **immediately upon enqueuing**.
- **Python Recursion Limit:** For large grids (e.g. $300 \times 300 = 90,000$ cells), recursive DFS can trigger `RecursionError`. BFS with `collections.deque` or iterative DFS with an explicit stack avoids stack overflow.

### Connectivity Rules and Their Boundary Instances

The adjacency rule is a property of the graph, not of the traversal, so the instances below are grouped by what they can and cannot discriminate. The fourth column counts components under the required orthogonal rule; the fifth recounts them as if corner contact also joined cells.

| Instance | Shape | Land cells | Islands under orthogonal adjacency | Islands if corner contact counted | What the instance exposes |
|:---|:---:|:---:|:---:|:---:|:---|
| Lesson grid | $3 \times 3$ | 4 | 2 | 2 | The two counts agree, so this instance cannot test the rule at all: $(2,2)$ is corner-adjacent only to $(1,1)$, which is water. |
| Four corners | $2 \times 2$ | 2 | 2 | 1 | The minimal discriminating case: the only contact between the two cells is at a corner, so the adjacency rule alone decides the answer. |
| All water | $2 \times 2$ | 0 | 0 | 0 | Every scan step is a skip; the counter is never incremented and no fill is ever launched, so the answer is $0$ rather than an error. |
| All land | $3 \times 3$ | 9 | 1 | 1 | One component that absorbs every cell, so the traversal reaches depth equal to the number of land cells: the worst case for a recursive stack. |
| Winding corridor | $3 \times 3$ | 5 | 1 | 1 | Connectivity is transitive: $(0,0)$ reaches $(2,2)$ through a chain of four orthogonal steps, so counting local patterns rather than components would overcount. |
| Three-island sample | $4 \times 5$ | 7 | 3 | 1 | Its three components are corner-adjacent in a chain, so counting corner contact would merge all of them and answer $1$ instead of $3$. |

Two rows carry the real content. The four-corner grid isolates the adjacency rule in its smallest possible form, and the three-island sample shows that the rule is not a cosmetic detail: it changes the answer by a factor of three on an ordinary instance.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot N)$, where $M$ is the number of rows and $N$ is the number of columns. The outer double loop visits all $M \cdot N$ cells once. During flood fills, each land cell is flipped from `'1'` to `'0'` exactly once. Total operations are strictly bounded by $O(M \cdot N)$.
- **Auxiliary Space Complexity:** $O(M \cdot N)$ in the worst case (e.g. a grid completely filled with land) for the call stack or BFS queue; modifying the grid in-place eliminates extra visited matrices.
