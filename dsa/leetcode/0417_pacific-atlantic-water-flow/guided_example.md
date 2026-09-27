# Guided Example: Pacific Atlantic Water Flow

We trace the step-by-step flow inversion, dual multi-source breadth-first search (BFS) queue propagation, non-decreasing elevation traversal ($h_{next} \ge h_{curr}$), and dual-ocean set intersection on representative topological grid matrices:

- **Input:**
  $$
  heights = \begin{bmatrix}
  1 & 2 & 2 & 3 & 5 \\
  3 & 2 & 3 & 4 & 4 \\
  2 & 4 & 5 & 3 & 1 \\
  6 & 7 & 1 & 4 & 5 \\
  5 & 1 & 1 & 2 & 4
  \end{bmatrix}
  $$
- **Required output:** `[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]`
  - Grid dimensions: $m = 5, n = 5$
  - Phase 1 (Pacific multi-source BFS from top row and left column):
    - Seeds: all $(0, c)$ and $(r, 0)$
    - Uphill flow condition: water flows backwards to neighbor if $heights[nr][nc] \ge heights[r][c]$
    - Reaches interior peaks such as $(2, 2)$ (height 5) via $(0, 2) \to (1, 2) \to (2, 2)$
  - Phase 2 (Atlantic multi-source BFS from bottom row and right column):
    - Seeds: all $(m-1, c)$ and $(r, n-1)$
    - Uphill flow condition: water flows backwards to neighbor if $heights[nr][nc] \ge heights[r][c]$
    - Reaches interior peaks such as $(2, 2)$ (height 5) via $(4, 4) \to (3, 4) \to (2, 3) \to (2, 2)$
  - Phase 3 (Boolean intersection $vis_{Pac}[r][c] \land vis_{Atl}[r][c]$):
    - Exactly 7 cells satisfy both reachability predicates:
      `[0, 4]`, `[1, 3]`, `[1, 4]`, `[2, 2]`, `[3, 0]`, `[3, 1]`, `[4, 0]`
- **Single Cell Grid ($1 \times 1$):** $heights = [[1]] \implies$ touches both Pacific and Atlantic borders $\implies [[0, 0]]$
- **Uniform Flat Plateau:** All cells equal height $\implies$ all cells reach both oceans $\implies$ all $m \times n$ coordinates.

This instance demonstrates inverting physical flow to achieve linear traversal, proves why dual multi-source graph search computes ocean reachability in $O(MN)$ rather than $O(M^2 N^2)$ time, and derives $O(MN)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ matrix $heights$ representing elevations of an island continent:
The **Pacific Ocean** touches the island's top and left edges.
The **Atlantic Ocean** touches the island's bottom and right edges.
Rainwater can flow to neighboring cells (north, south, east, west) if the neighboring cell's elevation is **less than or equal to** the current cell's elevation.
Water can flow from any border cell directly into the adjacent ocean.
Return a list of grid coordinates where rainwater can flow to **both** the Pacific and Atlantic oceans.

```text
         PACIFIC OCEAN (Top)
      0    1    2    3    4
   +----+----+----+----+----+
 0 |  1 |  2 |  2 |  3 |  5*|
   +----+----+----+----+----+
P1 |  3 |  2 |  3 |  4*|  4*| A
A  +----+----+----+----+----+ T
C2 |  2 |  4 |  5*|  3 |  1 | L
I  +----+----+----+----+----+ A
F3 |  6*|  7*|  1 |  4 |  5 | N
I  +----+----+----+----+----+ T
C4 |  5*|  1 |  1 |  2 |  4 | I
   +----+----+----+----+----+ C
        ATLANTIC OCEAN (Bottom)

(* denotes cells where water flows to both oceans)
```

### The Inversion Insight: Flowing Uphill from Coastlines
- **Naive Forward Search ($O(M^2 N^2)$):** Starting a BFS/DFS from every cell $(r, c)$ and simulating downward water flow is wasteful. Searching $M \times N$ cells repeatedly revisits paths, leading to Time Limit Exceeded.
- **Reverse Flow Multi-Source BFS ($O(MN)$):** Invert the problem. Water flows *downhill* into the ocean; therefore, if we start at the oceans and flow **uphill** ($h_{neighbor} \ge h_{current}$), every cell reached can drain into that ocean.
- Running one multi-source BFS from the Pacific coastline and a second from the Atlantic coastline identifies all reachable cells in exactly two linear passes.

---

## 2. Conceptual Foundation & Invariants

### 1. The Reverse Edge Condition:
In the original graph, a directed edge exists from $u \to v$ if $h(u) \ge h(v)$.
In the inverted search graph, an edge exists from $v \to u$ if:
$$
h(u) \ge h(v)
$$
Water from the ocean can climb to any neighbor whose elevation is greater than or equal to the current cell.

### 2. Dual Multi-Source Queues:
1. **Pacific Frontier ($Q_1$):**
   Seed with all boundary cells along row $0$ ($0 \le c < n$) and column $0$ ($0 \le r < m$).
   Mark $vis_{Pac}[r][c] = \text{True}$.
2. **Atlantic Frontier ($Q_2$):**
   Seed with all boundary cells along row $m - 1$ ($0 \le c < n$) and column $n - 1$ ($0 \le r < m$).
   Mark $vis_{Atl}[r][c] = \text{True}$.

### 3. Coordinate Intersection:
A cell $(r, c)$ is in the final answer if and only if:
$$
vis_{Pac}[r][c] \land vis_{Atl}[r][c] == \text{True}
$$

> **Invariant.** After the Pacific BFS completes, $vis_{Pac}[r][c] == \text{True}$ if and only if there exists a monotonically non-increasing path from $(r, c)$ to the Pacific Ocean. Symmetrically for $vis_{Atl}[r][c]$.

---

## 3. Step-by-Step Worked Execution

We trace the $5 \times 5$ island with dimensions $m = 5, n = 5$:

---

### Step 1: Pacific Multi-Source BFS
Initialize queue $Q_{Pac}$ with Pacific border cells and explore uphill neighbors:
- Top border $(0, 0\dots 4)$ and Left border $(0\dots 4, 0)$ are marked.
- Expansion examples:
  - From $(0, 4)$ [height 5]: All neighbors have height $\le 5$, but uphill condition requires $h_{neighbor} \ge 5$. No higher neighbors.
  - From $(0, 3)$ [height 3]: Neighbor $(1, 3)$ has height $4 \ge 3 \implies$ visited!
  - From $(1, 3)$ [height 4]: Neighbor $(1, 4)$ has height $4 \ge 4 \implies$ visited! Neighbor $(2, 2)$ has height $5 \ge 4 \implies$ visited!
  - From $(3, 0)$ [height 6]: Neighbor $(3, 1)$ has height $7 \ge 6 \implies$ visited!
- Complete Pacific reachability matrix ($1 = \text{True}, 0 = \text{False}$):
  $$
  vis_{Pac} = \begin{bmatrix}
  1 & 1 & 1 & 1 & 1 \\
  1 & 1 & 1 & 1 & 1 \\
  1 & 1 & 1 & 0 & 0 \\
  1 & 1 & 0 & 0 & 0 \\
  1 & 0 & 0 & 0 & 0
  \end{bmatrix}
  $$

---

### Step 2: Atlantic Multi-Source BFS
Initialize queue $Q_{Atl}$ with Atlantic border cells and explore uphill neighbors:
- Bottom border $(4, 0\dots 4)$ and Right border $(0\dots 4, 4)$ are marked.
- Expansion examples:
  - From $(4, 4)$ [height 4]: Neighbor $(3, 4)$ has height $5 \ge 4 \implies$ visited!
  - From $(3, 4)$ [height 5]: Neighbor $(2, 2)$ has height $5 \ge 5$ via $(2, 3)$ [height 3] (water flows $5 \to 3 \to 1 \to \text{ocean}$? No, uphill from Atlantic: $(4, 4)[4] \to (3, 4)[5]$; $(4, 3)[2] \to (3, 3)[4] \to (2, 2)[5]$).
  - From $(4, 0)$ [height 5]: Neighbor $(3, 0)$ has height $6 \ge 5 \implies$ visited!
  - From $(3, 0)$ [height 6]: Neighbor $(3, 1)$ has height $7 \ge 6 \implies$ visited!
  - From $(0, 4)$ [height 5]: touches Atlantic right boundary directly $\implies$ visited!
- Complete Atlantic reachability matrix:
  $$
  vis_{Atl} = \begin{bmatrix}
  0 & 0 & 0 & 0 & 1 \\
  0 & 0 & 0 & 1 & 1 \\
  0 & 0 & 1 & 1 & 1 \\
  1 & 1 & 0 & 1 & 1 \\
  1 & 1 & 1 & 1 & 1
  \end{bmatrix}
  $$

---

### Step 3: Set Intersection
Compute $vis_{Pac}[r][c] \land vis_{Atl}[r][c]$ for every coordinate $(r, c)$:

$$
\begin{bmatrix}
1\land 0 & 1\land 0 & 1\land 0 & 1\land 0 & \mathbf{1\land 1} \\
1\land 0 & 1\land 0 & 1\land 0 & \mathbf{1\land 1} & \mathbf{1\land 1} \\
1\land 0 & 1\land 0 & \mathbf{1\land 1} & 0\land 1 & 0\land 1 \\
\mathbf{1\land 1} & \mathbf{1\land 1} & 0\land 0 & 0\land 1 & 0\land 1 \\
\mathbf{1\land 1} & 0\land 1 & 0\land 1 & 0\land 1 & 0\land 1
\end{bmatrix}
=
\begin{bmatrix}
0 & 0 & 0 & 0 & \mathbf{1} \\
0 & 0 & 0 & \mathbf{1} & \mathbf{1} \\
0 & 0 & \mathbf{1} & 0 & 0 \\
\mathbf{1} & \mathbf{1} & 0 & 0 & 0 \\
\mathbf{1} & 0 & 0 & 0 & 0
\end{bmatrix}
$$

The coordinates containing $\mathbf{1}$ are:
`[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]`.

---

## 4. Complete Execution Trace

| Coordinate $(r, c)$ | Height | Pacific Reachable? ($vis_{Pac}$) | Atlantic Reachable? ($vis_{Atl}$) | Dual Drainage ($vis_{Pac} \land vis_{Atl}$) | Valid Output Cell? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $(0, 4)$ | $5$ | **True** (Top coast) | **True** (Right coast) | **True** | **Yes (`[0, 4]`)** |
| $(1, 3)$ | $4$ | **True** (via $(0, 3)$) | **True** (via $(1, 4)$) | **True** | **Yes (`[1, 3]`)** |
| $(1, 4)$ | $4$ | **True** (via $(1, 3)$) | **True** (Right coast) | **True** | **Yes (`[1, 4]`)** |
| $(2, 2)$ | $5$ | **True** (via $(1, 2) \to (0, 2)$) | **True** (via $(3, 3) \to (4, 3)$) | **True** | **Yes (`[2, 2]`)** |
| $(3, 0)$ | $6$ | **True** (Left coast) | **True** (via $(4, 0)$) | **True** | **Yes (`[3, 0]`)** |
| $(3, 1)$ | $7$ | **True** (via $(3, 0)$) | **True** (via $(3, 0) \to (4, 0)$) | **True** | **Yes (`[3, 1]`)** |
| $(4, 0)$ | $5$ | **True** (Left coast) | **True** (Bottom coast) | **True** | **Yes (`[4, 0]`)** |
| $(2, 1)$ | $4$ | **True** | **False** | False | No |
| $(3, 3)$ | $4$ | **False** | **True** | False | No |

---

## 5. Boundary Cases & Failure Modes

- **$1 \times 1$ Grid ($heights = [[10]]$):** The lone cell simultaneously touches top, left, bottom, and right borders. $Q_1$ and $Q_2$ both visit $(0, 0)$. Output is `[[0, 0]]`.
- **Monotonically Sloping Mountain ($1 \times N$ or $N \times 1$):** In a $1 \times N$ row, every cell can reach the Pacific from the left or Atlantic from the right. The highest peak divides the watersheds, but all cells can reach at least one, and any plateau peak reaches both.
- **Flat Elevation ($all \ h_{r,c} == C$):** Since water flows freely between equal heights ($h_{next} \ge h_{curr}$ is satisfied with equality), every single cell in the grid reaches both oceans. Output contains all $M \times N$ cells.
- **Deep Interior Canyon:** Interior cells lower than all coastline cells can never be reached by uphill flow from oceans, correctly preventing water trapped in a depression from reaching either coast.

---

## 6. Traps & Common Anti-Patterns

- **Forward Simulation from Every Cell:** Launching a fresh DFS from each $(r, c)$ costs $O(MN)$ per cell, resulting in $O(M^2 N^2)$ time. On a $200 \times 200$ grid ($40,000$ cells), $40000^2 \approx 1.6 \times 10^9$ operations causes severe Time Limit Exceeded.
- **Missing Equal Height Flow:** Checking strict inequality ($h_{next} > h_{curr}$) instead of non-strict inequality ($h_{next} \ge h_{curr}$) prevents water from crossing horizontal plateaus.
- **Infinite Recursion / Cycling:** Without an explicit `visited` array, water can slosh back and forth between two adjacent cells of equal elevation ($h_A == h_B$) forever. Marking cells visited upon queue push prevents cycles.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - In each BFS phase (Pacific and Atlantic), each cell is pushed into the queue at most once and processed in $O(1)$ time.
  - Number of grid cells is $M \times N$.
  - Traversing 4 neighbors per cell takes $4 \times MN$ edge checks.
  - Final intersection pass checks $M \times N$ boolean flags.
  - Total Time: $\mathcal{O}(M \cdot N)$. For a $200 \times 200$ grid, $\approx 4 \times 10^4$ operations execute in under 15 ms.
- **Auxiliary Space Complexity:**
  - Two boolean grids $vis_{Pac}$ and $vis_{Atl}$ of size $M \times N$.
  - Queue storage holds at most $O(M \cdot N)$ coordinates.
  - Total Auxiliary Space: $\mathcal{O}(M \cdot N)$.
