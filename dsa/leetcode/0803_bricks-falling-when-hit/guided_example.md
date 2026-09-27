# Guided Example: Bricks Falling When Hit

We trace the step-by-step structural stability percolation on 2D lattices (top-row anchored components), offline time-reversal transformation, virtual ceiling anchor super-node ($m \cdot n$), reverse Disjoint Set Union (Union-Find) brick re-insertion, ceiling component size differential tracking ($\Delta = curr - prev - 1$), and falling brick tally reconstruction on representative grid hits:

- **Input:**
  $$
  grid = \begin{bmatrix}
  1 & 0 & 0 & 0 \\
  1 & 1 & 1 & 0
  \end{bmatrix}, \quad hits = [[1, 0]]
  $$
- **Required output:**
  $$
  [2]
  $$
  - Physical stability rules & falling cascades:
    - An $m \times n$ binary grid contains bricks (`1`) and empty spaces (`0`).
    - A brick is **stable** if and only if:
      1. It is in the top row ($row = 0$, anchored to the ceiling), or
      2. It is 4-directionally adjacent to at least one stable brick.
    - When a brick is hit at $(r, c)$, it is instantly destroyed.
    - Any bricks that lose their connection to the ceiling become unstable and fall.
    - Objective: Return an array where the $k$-th value is the number of bricks that **fall** due to the $k$-th hit. (The brick destroyed by the hit does not count as falling).
    - For the input grid:
      - Initial bricks: $(0, 0)$ in top row; $(1, 0), (1, 1), (1, 2)$ in row 1.
      - Brick $(1, 0)$ is the sole bridge anchoring $(1, 1)$ and $(1, 2)$ to $(0, 0)$.
      - When hit at $(1, 0)$ is applied:
        - $(1, 0)$ is erased.
        - Bricks $(1, 1)$ and $(1, 2)$ have no remaining path to row 0.
        - Both $(1, 1)$ and $(1, 2)$ fall ($2$ bricks fell).
      - Result: `[2]`.
- **Time-Reversal & Virtual Ceiling DSU Invariant:**
  - **The Computational Bottleneck of Deletion:**
    - Deleting an edge or node in a graph and detecting newly disconnected subgraphs is computationally expensive ($\mathcal{O}(V)$ per hit).
    - However, the reverse operation — **adding edges and merging components** — is efficiently handled by Disjoint Set Union (DSU) in nearly $\mathcal{O}(1)$ time per operation!
  - **The Virtual Ceiling Super-Node:**
    - Introduce a special node $C = m \cdot n$ representing the rigid ceiling.
    - Any brick at row 0 is connected directly to $C$.
    - A brick is stable if and only if its component is connected to $C$.
  - **Reverse Construction Algorithm:**
    - **Step 1 (Pre-Hit State):** Erase all bricks specified in $hits$ from a copy of the grid $g$.
    - **Step 2 (Initial Clustering):**
      - Union all row-0 bricks with $C$.
      - Union all adjacent remaining bricks in $g$.
    - **Step 3 (Reverse Re-insertion):**
      - Iterate through $hits$ from **last to first** ($k = |hits| - 1 \dots 0$):
        - If the hit location had no brick initially ($grid[r][c] == 0$), 0 bricks fell.
        - Otherwise:
          - Re-insert brick: $g[r][c] \leftarrow 1$.
          - Record current ceiling component size: $prev = size[find(C)]$.
          - If $r == 0$, union $(r, c)$ with $C$.
          - Union $(r, c)$ with all adjacent active bricks in $g$.
          - Record new ceiling component size: $curr = size[find(C)]$.
          - The re-inserted brick $(r, c)$ reconnected $curr - prev$ bricks to the ceiling.
          - Since $(r, c)$ itself was destroyed rather than fallen:
            $$
            \text{fallen bricks} = \max(0, \; curr - prev - 1)
            $$
    - Reverse the collected results to recover the chronological sequence.
- **Step-by-Step Worked Execution Trace on the Sample Grid:**
  - Grid dimensions: $m = 2, n = 4$. Virtual ceiling node: $C = 2 \times 4 = \mathbf{8}$.
  - Initial bricks: $(0, 0), (1, 0), (1, 1), (1, 2)$.
  - Single hit at $(1, 0)$.
  - **Phase 0: Remove Hit Bricks:**
    - Erase $(1, 0) \implies g[1][0] = 0$.
    - Remaining active bricks in $g$:
      - $(0, 0)$ (Node 0)
      - $(1, 1)$ (Node 5)
      - $(1, 2)$ (Node 6)
  - **Phase 1: Build Initial DSU on Post-Hit Grid:**
    - Anchor row 0 to ceiling $C = 8$:
      - $g[0][0] == 1 \implies union(0, 8)$.
      - Component $C$ size becomes $1 + 1 = 2$ (virtual node 8 + brick 0).
    - Connect adjacent bricks in $g$:
      - $(1, 1)$ is adjacent to $(1, 2) \implies union(5, 6)$.
      - Component $\{5, 6\}$ has size 2, but is **disconnected from $C$**.
    - Post-hit ceiling size:
      $$
      size[find(8)] = \mathbf{2} \quad (\text{nodes } 0 \text{ and } 8)
      $$
  - **Phase 2: Reverse Re-insertion of Hit $(1, 0)$ (Node 4):**
    - Brick exists in original grid ($grid[1][0] == 1$).
    - Re-activate: $g[1][0] \leftarrow 1$.
    - Measure baseline ceiling size:
      $$
      prev = size[find(8)] = \mathbf{2}
      $$
    - Neighbor connections for Node 4 ($(1, 0)$):
      1. Up neighbor $(0, 0)$ (Node 0): active!
         - $union(4, 0) \implies$ merges with ceiling component $\{0, 8\}$!
      2. Right neighbor $(1, 1)$ (Node 5): active!
         - $union(4, 5) \implies$ merges component $\{5, 6\}$ into ceiling component!
    - New ceiling component contains: $\{8, 0, 4, 5, 6\}$.
    - Measure new ceiling size:
      $$
      curr = size[find(8)] = \mathbf{5}
      $$
    - Calculate newly restored bricks:
      $$
      \Delta = curr - prev = 5 - 2 = \mathbf{3} \text{ bricks}
      $$
    - Subtract the hit brick itself:
      $$
      \text{fallen} = \max(0, \; \Delta - 1) = \max(0, \; 3 - 1) = \mathbf{2}
      $$
    - Add to result: $ans = [2]$.
  - **Phase 3: Chronological Output:**
    - Only 1 hit $\implies$ output:
      $$
      ans = \mathbf{[2]}
      $$
- **Hit Empty Cell Trace ($grid[i][j] == 0$):**
  - Hitting an empty space destroys no brick and releases no cascade.
  - The algorithm checks $grid[i][j] == 0$ and immediately records $0$ without DSU mutation.
- **Hit Independent Unstable Brick Trace:**
  - If a brick was already detached or its removal doesn't disconnect any component from the ceiling ($curr == prev$), $\Delta - 1 = -1 \implies \max(0, -1) = \mathbf{0}$.

This instance demonstrates offline time-reversal graph percolation and connected component incremental maintenance via union-find forests, mathematically proves why dynamic disconnection translates to adjoint addition on the dual timeline, and derives $O(M \cdot N \cdot \alpha(M \cdot N) + H \cdot \alpha(M \cdot N))$ runtime and $O(M \cdot N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a brick grid and a sequence of $hits$:
When a brick is hit, it is destroyed, and any bricks no longer connected to the top row fall.
Find the **number of falling bricks** for each hit.

```text
grid:
  1 0 0 0
  1 1 1 0

hits = [ [1, 0] ]

Brick (1, 0) is the bridge connecting (1, 1) and (1, 2) to the ceiling (0, 0).
Destroying (1, 0) causes (1, 1) and (1, 2) to fall!

Result: [ 2 ]
```

### The Invariant of Offline Time-Reversal
- Deleting nodes from a graph is hard; adding nodes using Disjoint Set Union (Union-Find) is fast.
- By running the hits in **reverse order**, each hit becomes a brick being **re-inserted**.
- The change in the size of the ceiling component ($curr - prev - 1$) gives the exact number of falling bricks.

---

## 2. Conceptual Foundation & Invariants

### 1. Ceiling Component Anchor:
$$
C = m \cdot n \quad (\text{Virtual Ceiling Node})
$$
$$
\forall j \in [0, n - 1]: \quad \text{if } g[0][j] == 1 \implies uf.union(j, C)
$$

### 2. Reverse Delta Counting:
For each hit $(i, j)$ in reverse order:
$$
prev = size[find(C)]
$$
$$
\text{re-insert and connect } (i, j) \text{ to adjacent active bricks}
$$
$$
curr = size[find(C)]
$$
$$
fallen = \max(0, \; curr - prev - 1)
$$

> **Offline Percolation Adjoint Invariant.** The bond-removal percolation process on the half-plane lattice is non-monotone in forward time, but dual monotone in reverse time. The virtual ceiling anchor reduces the multi-sink reachability problem to a single-source connected component size differential.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Remove All Hits
- Erase $(1, 0) \implies g$ has only $(0, 0)$ connected to ceiling; $(1, 1)$ and $(1, 2)$ isolated.
- Ceiling size: 2 (node $(0, 0)$ + ceiling $C$).

---

### Step 2: Reverse Hit $(1, 0)$
- $prev = 2$.
- Restore $(1, 0) \implies$ merges $(0, 0)$ and $\{ (1, 1), (1, 2) \}$ into ceiling component.
- New ceiling size $curr = 5$.

---

### Step 3: Compute Difference
- Restored to ceiling: $5 - 2 = 3$.
- Excluding hit brick itself: $3 - 1 = \mathbf{2}$.

---

### Step 4: Output
$$
\mathbf{[2]}
$$

---

## 4. Complete Execution Trace

| Reverse Step | Restored Hit $(i, j)$ | Baseline Ceiling Size $prev$ | Merged Neighbors | New Ceiling Size $curr$ | Restored Other Bricks | Chronological Result |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Initial Post-Hit | — | — | Only $(0, 0)$ to $C$ | $2$ | — | — |
| **$1$ (Last Hit)** | **$(1, 0)$** | **$2$** | **$(0, 0)$ and $(1, 1)$** | **$5$** | **$5 - 2 - 1 = \mathbf{2}$** | **`[2]`** |

---

## 5. Boundary Cases & Failure Modes

- **Hit on Empty Space ($grid[i][j] == 0$):** Hit was already empty $\implies 0$ bricks fall.
- **Hit Brick Already Detached:** The brick was already unsupported before this hit $\implies 0$ bricks fall.
- **Top Row Hit:** Brick connected directly to ceiling; may cause large tree below to fall.
- **Single Brick Left:** Returns $[0]$.

---

## 6. Traps & Common Anti-Patterns

- **Simulating BFS from Ceiling on Every Hit ($O(H \cdot MN)$):** Running BFS after every hit to find connected bricks takes $O(H \cdot MN) \approx 4 \times 10^4 \times 4 \times 10^4 \approx 1.6 \times 10^9$ operations (massive TLE). Reverse DSU takes nearly linear $O(MN + H)$ time.
- **Counting the Hit Brick as a Falling Brick:** The hit brick is obliterated by the hammer, not dropped by gravity. Always subtract 1 ($curr - prev - 1$).
- **Modifying the Original Grid Irreversibly:** Check `grid[i][j] == 0` against the original grid, not the temporary mutated grid $g$, to detect phantom hits.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initializing DSU and post-hit grid: $\mathcal{O}(M \cdot N \cdot \alpha(M \cdot N))$.
  - Processing each hit in reverse (at most 4 edge unions): $\mathcal{O}(H \cdot \alpha(M \cdot N))$.
  - Total Time: strictly $\mathcal{O}((M \cdot N + H) \alpha(M \cdot N))$ where $M, N \le 200, H \le 4 \times 10^4$. Completes in $< 25$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ memory for DSU parent and component size arrays.
