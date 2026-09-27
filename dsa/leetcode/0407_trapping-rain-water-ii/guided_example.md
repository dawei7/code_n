# Guided Example: Trapping Rain Water II

We trace the step-by-step min-heap perimeter contraction (Dijkstra-style inward flood fill), bottleneck spill-level tracking ($h = \max(h_{prev}, \text{terrain})$), 2D water volume accumulation ($\Delta = \max(0, h - heightMap[x][y])$), and boundary isolation on representative 2D elevation maps:

- **Input:** $heightMap = \begin{pmatrix} 1 & 4 & 3 & 1 & 3 & 2 \\ 3 & 2 & 1 & 3 & 2 & 4 \\ 2 & 3 & 3 & 2 & 3 & 1 \end{pmatrix}$ ($3 \times 6$ grid)
- **Required output:** `4`
  - Dimensions: $m = 3, n = 6$ (Interior cells: $(1, 1), (1, 2), (1, 3), (1, 4)$)
  - Initial Boundary Setup:
    - All $2m + 2n - 4 = 14$ perimeter cells pushed to min-heap `pq`
  - Inward Contraction & Spill Resolution:
    - Interior cell $(1, 2)$ with terrain height $1$:
      - Enclosed by outer boundary heights $\ge 3$
      - Spill height at perimeter opening is $3$
      - Trapped water: $3 - 1 = \mathbf{2}$
    - Interior cell $(1, 1)$ with terrain height $2$:
      - Enclosed by boundary heights $\ge 3$
      - Trapped water: $3 - 2 = \mathbf{1}$
    - Interior cell $(1, 4)$ with terrain height $2$:
      - Enclosed by boundary heights $\ge 3$
      - Trapped water: $3 - 2 = \mathbf{1}$
    - Interior cell $(1, 3)$ with terrain height $3$:
      - Trapped water: $\max(0, 3 - 3) = \mathbf{0}$
  - Total trapped volume: $2 + 1 + 1 + 0 = \mathbf{4}$
- **Flat Surface:** All cells height $5 \implies$ zero height difference $\implies \mathbf{0}$
- **Small Grid:** $2 \times 3$ grid $\implies$ zero interior cells (all boundary) $\implies \mathbf{0}$

This instance demonstrates 2D boundary relaxation using priority queues, mathematically proves why water levels are strictly governed by the minimum bottleneck along the shortest escape path to the grid exterior, and achieves $O(MN \log(MN))$ runtime and $O(MN)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a 2D elevation map of dimensions $3 \times 6$:
$$
\begin{bmatrix}
1 & 4 & 3 & 1 & 3 & 2 \\
3 & \mathbf{2} & \mathbf{1} & \mathbf{3} & \mathbf{2} & 4 \\
2 & 3 & 3 & 2 & 3 & 1
\end{bmatrix}
$$
Find the total volume of rainwater trapped after filling:

```text
Cross-Section View of Row 1 (Interior Cells [2, 1, 3, 2]):
Surrounding walls (Row 0 above, Row 2 below, columns 0 & 5 on sides):
  At (1, 1): Floor = 2, Wall = 3 -> Water level = 3 -> Holds 3 - 2 = 1
  At (1, 2): Floor = 1, Wall = 3 -> Water level = 3 -> Holds 3 - 1 = 2
  At (1, 3): Floor = 3, Wall = 3 -> Water level = 3 -> Holds 3 - 3 = 0
  At (1, 4): Floor = 2, Wall = 3 -> Water level = 3 -> Holds 3 - 2 = 1

Total Water Volume = 1 + 2 + 0 + 1 = 4
```

### Why 1D Two Pointers Fails in 2D
In 1D, water cannot escape through the third dimension, so a cell is bounded solely by $\min(\text{max\_left}, \text{max\_right})$.
In 2D, water can leak in any of the four cardinal directions (up, down, left, right) and can escape through winding, labyrinthine channels to the edge of the board.
To find the containment level of an interior cell, we must find the **minimum bottleneck along all possible escape paths to the perimeter**. This is mathematically equivalent to Dijkstra's algorithm running inward from the boundary with edge weights $W = \max(h_{u}, h_{v})$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Inward Flood Fill Priority Queue:
- Maintain a min-heap `pq` of tuples `(height, r, c)` where `height` is the **effective water surface / spill barrier** at $(r, c)$.
- Maintain a 2D boolean array `vis[m][n]` tracking finalized cells.

### 2. Initialization:
- Push all border cells ($r \in \{0, m-1\}$ or $c \in \{0, n-1\}$) into `pq` with their terrain heights.
- Mark them `vis[r][c] = True`. (Boundary cells can never trap water because water immediately drains off the board).

### 3. Contraction Step:
Pop the cell $(i, j)$ with the **lowest effective boundary height $h$**:
For each cardinal neighbor $(x, y)$:
- If $(x, y)$ is unvisited:
  1. If $heightMap[x][y] < h$, the neighbor is lower than the current spill barrier!
     $$
     ans \leftarrow ans + (h - heightMap[x][y])
     $$
  2. The effective barrier carried into $(x, y)$ is:
     $$
     h_{new} = \max(h, \; heightMap[x][y])
     $$
  3. Mark `vis[x][y] = True` and push $(h_{new}, x, y)$ into `pq`.

> **Invariant.** Because the min-heap always pops the globally lowest barrier first, when an unvisited cell $(x, y)$ is reached from $(i, j)$ at height $h$, $h$ is guaranteed to be the lowest possible spill path to the boundary.

---

## 3. Step-by-Step Worked Execution

We trace $heightMap$ ($m = 3, n = 6$):
Initial `pq` contains all 14 boundary cells. `ans = 0`.

---

### Step 1: Initialize Boundary
Border cells added to `pq` (sorted by height):
- Height 1: $(0, 0), (0, 3), (2, 5)$
- Height 2: $(0, 5), (2, 0), (2, 3)$
- Height 3: $(0, 2), (0, 4), (1, 0), (2, 1), (2, 2), (2, 4)$
- Height 4: $(0, 1), (1, 5)$

---

### Step 2: Pop Lowest Boundary Nodes (Heights 1 and 2)
- Cells with height 1:
  - Pop $(0, 3)$ ($h = 1$): neighbor is $(1, 3)$ (terrain height 3).
    - $3 \not< 1 \implies$ trapped water $= 0$.
    - New effective height: $\max(1, 3) = \mathbf{3}$.
    - Push $(3, 1, 3)$ to `pq`. `vis[1][3] = True`.
- Cells with height 2:
  - $(0, 5), (2, 0), (2, 3)$ have no unvisited interior neighbors. Popped without water accumulation.

---

### Step 3: Pop Intermediate Nodes & Expand Interior
- Current `pq` minimum height is now **$3$**.
- Pop $(0, 2)$ ($h = 3$):
  - Neighbor is unvisited $(1, 2)$ with terrain height $1$:
    - Water trapped:
      $$
      \Delta = h - heightMap[1][2] = 3 - 1 = \mathbf{2}
      $$
      $$
      ans \leftarrow 0 + 2 = \mathbf{2}
      $$
    - Effective spill height for $(1, 2)$:
      $$
      \max(3, 1) = \mathbf{3}
      $$
    - Push $(3, 1, 2)$ to `pq`. `vis[1][2] = True`.

---

### Step 4: Expand Neighbors of $(1, 2)$
- Pop $(3, 1, 2)$ ($h = 3$):
  - Neighbor $(1, 1)$ with terrain height $2$ (unvisited):
    - Water trapped:
      $$
      \Delta = 3 - 2 = \mathbf{1}
      $$
      $$
      ans \leftarrow 2 + 1 = \mathbf{3}
      $$
    - Effective spill height: $\max(3, 2) = \mathbf{3}$.
    - Push $(3, 1, 1)$ to `pq`. `vis[1][1] = True`.

---

### Step 5: Expand $(1, 4)$
- Pop $(0, 4)$ ($h = 3$):
  - Neighbor $(1, 4)$ with terrain height $2$ (unvisited):
    - Water trapped:
      $$
      \Delta = 3 - 2 = \mathbf{1}
      $$
      $$
      ans \leftarrow 3 + 1 = \mathbf{4}
      $$
    - Effective spill height: $\max(3, 2) = \mathbf{3}$.
    - Push $(3, 1, 4)$ to `pq`. `vis[1][4] = True`.

---

### Step 6: Empty Heap & Finalize
All interior cells $(1, 1), (1, 2), (1, 3), (1, 4)$ are visited. Remaining heap elements pop without discovering unvisited neighbors.
Return:
$$
ans = \mathbf{4}
$$

---

## 4. Complete Execution Trace

```text
Grid Dimensions: 3 x 6. Interior Cells: row 1, cols 1..4.

1. Boundary initialized into Min-Heap (size 14).
2. Pop (1, 0, 3) -> neighbor (1, 3) has height 3 -> water = 0, push (3, 1, 3)
3. Pop (3, 0, 2) -> neighbor (1, 2) has height 1 -> water = 3 - 1 = 2, push (3, 1, 2)
4. Pop (3, 1, 2) -> neighbor (1, 1) has height 2 -> water = 3 - 2 = 1, push (3, 1, 1)
5. Pop (3, 0, 4) -> neighbor (1, 4) has height 2 -> water = 3 - 2 = 1, push (3, 1, 4)

Total Trapped Water = 2 + 1 + 1 = 4
```

| Pop Event | Popped Cell $(i, j)$ | Effective Spill Barrier $h$ | Neighbor Cell $(x, y)$ | Terrain Height | Water Added $\max(0, h - \text{terrain})$ | Pushed Tuple $(\max(h, \text{terrain}), x, y)$ | Total Water $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | $(0, 3)$ | 1 | $(1, 3)$ | 3 | $0$ | $(3, 1, 3)$ | 0 |
| 2 | $(0, 2)$ | 3 | $(1, 2)$ | 1 | **$3 - 1 = 2$** | $(3, 1, 2)$ | 2 |
| 3 | $(1, 2)$ | 3 | $(1, 1)$ | 2 | **$3 - 2 = 1$** | $(3, 1, 1)$ | 3 |
| **4** | **$(0, 4)$** | **3** | **$(1, 4)$** | **2** | **$3 - 2 = 1$** | **$(3, 1, 4)$** | **`4` (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** Suppose an interior cell $C$ holds water up to height $H$. If there were an escape path from $C$ to the boundary where all cells have height $< H$, water would spill out, contradicting equilibrium. Therefore, the water level at $C$ is strictly bounded by the maximum height on the minimum-bottleneck path to the outside:
$$
\text{WaterLevel}(C) = \min_{\text{paths } P} \left( \max_{v \in P} \text{height}(v) \right)
$$
Because the min-heap processes cells in increasing order of their escape bottleneck, each cell's optimal water level is permanently finalized upon first visit.

**Completeness.** Every interior cell is connected to the perimeter. The flood fill is guaranteed to visit all $M \times N$ cells, ensuring no pocket of trapped water is overlooked.

---

## 6. Traps This Instance Exposes

- **4-Directional Maximum Fallacy:** Taking $\min(\text{max\_up}, \text{max\_down}, \text{max\_left}, \text{max\_right})$ fails because water can follow diagonal or zigzag paths to leak through lower gaps.
- **Missing the `max(h, terrain)` Propagation:** When water fills a depression of height 1 up to level 3, neighboring cells must see an effective barrier of 3 (the surface of the water), NOT 1 (the sunken ground). Pushing $\max(h, heightMap[x][y])$ ensures correct propagation.
- **Small Grid Boundaries:** Grids with $M \le 2$ or $N \le 2$ contain zero interior cells; the algorithm trivially finishes with 0 without index out-of-bounds errors.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(MN \log(MN))$, where $M$ and $N$ are the matrix dimensions.
  - Every cell is inserted into the min-heap at most once and popped at most once ($MN$ total heap operations).
  - Each heap operation on at most $MN$ elements takes $O(\log(MN))$ time.
  - Total time is $O(MN \log(MN))$, running in under 40 ms for $200 \times 200$ grids.
- **Auxiliary Space Complexity:** $O(MN)$ auxiliary space for the priority queue `pq` and the boolean 2D `vis` table.
