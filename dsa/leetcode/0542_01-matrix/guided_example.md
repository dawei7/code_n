# Guided Example: 01 Matrix

We trace the step-by-step multi-source breadth-first search initialization (seeding all zero-cells at distance 0), queue-driven wavefront expansion ($ans[x][y] = ans[i][j] + 1$), 4-directional Manhattan neighborhood traversal, visited state demarcation ($ans == -1$), and shortest-distance matrix generation on representative binary grids:

- **Input:**
  $$
  mat = \begin{bmatrix}
  0 & 0 & 0 \\
  0 & 1 & 0 \\
  1 & 1 & 1
  \end{bmatrix}
  $$
- **Required output:**
  $$
  ans = \begin{bmatrix}
  0 & 0 & 0 \\
  0 & 1 & 0 \\
  1 & 2 & 1
  \end{bmatrix}
  $$
  - Objective: For each cell $(r, c)$, find the Manhattan distance $|r - r_0| + |c - c_0|$ to the nearest zero-valued cell $(r_0, c_0)$.
- **Multi-Source BFS Wavefront Trace:**
  - Initialize distance grid $ans$ of size $3 \times 3$ with $-1$ (unvisited):
    $$
    ans = \begin{bmatrix}
    -1 & -1 & -1 \\
    -1 & -1 & -1 \\
    -1 & -1 & -1
    \end{bmatrix}
    $$
  - **Step 1: Multi-Source Seeding (Distance 0):**
    - Identify all cells with $mat[i][j] == 0$:
      - $(0, 0), (0, 1), (0, 2), (1, 0), (1, 2)$
    - Set their distances to $0$ and push into queue $q$:
      $$
      ans[i][j] \leftarrow 0 \quad \forall (i, j) \in \text{Zeroes}
      $$
      $$
      q = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2)]
      $$
    - Current distance matrix:
      $$
      ans = \begin{bmatrix}
      0 & 0 & 0 \\
      0 & -1 & 0 \\
      -1 & -1 & -1
      \end{bmatrix}
      $$
  - **Step 2: Wavefront Layer 1 (Distance $0 + 1 = 1$):**
    - Dequeue sources $(0, 0), (0, 1), (0, 2), (1, 0), (1, 2)$:
      - From $(0, 1)$ and $(1, 0)$: neighbor $(1, 1)$ has $ans[1][1] == -1$:
        $$
        ans[1][1] \leftarrow 0 + 1 = \mathbf{1}, \quad q.\text{append}((1, 1))
        $$
      - From $(1, 0)$: neighbor $(2, 0)$ has $ans[2][0] == -1$:
        $$
        ans[2][0] \leftarrow 0 + 1 = \mathbf{1}, \quad q.\text{append}((2, 0))
        $$
      - From $(1, 2)$: neighbor $(2, 2)$ has $ans[2][2] == -1$:
        $$
        ans[2][2] \leftarrow 0 + 1 = \mathbf{1}, \quad q.\text{append}((2, 2))
        $$
    - Layer 1 cells registered: $(1, 1), (2, 0), (2, 2)$.
    - Distance matrix:
      $$
      ans = \begin{bmatrix}
      0 & 0 & 0 \\
      0 & \mathbf{1} & 0 \\
      \mathbf{1} & -1 & \mathbf{1}
      \end{bmatrix}
      $$
  - **Step 3: Wavefront Layer 2 (Distance $1 + 1 = 2$):**
    - Dequeue $(1, 1), (2, 0), (2, 2)$:
      - From $(1, 1)$ (down) and from $(2, 0)$ (right) and from $(2, 2)$ (left):
        - Neighbor $(2, 1)$ is unvisited ($ans[2][1] == -1$).
        - Update distance:
          $$
          ans[2][1] \leftarrow 1 + 1 = \mathbf{2}, \quad q.\text{append}((2, 1))
        $$
    - Distance matrix:
      $$
      ans = \begin{bmatrix}
      0 & 0 & 0 \\
      0 & 1 & 0 \\
      1 & \mathbf{2} & 1
      \end{bmatrix}
      $$
  - **Step 4: Queue Depletion:**
    - Dequeue $(2, 1)$: all 4 neighbors already have non-negative distances.
    - Queue becomes empty.
  - Final distance matrix:
    $$
    \begin{bmatrix}
    0 & 0 & 0 \\
    0 & 1 & 0 \\
    1 & 2 & 1
    \end{bmatrix}
    $$
- **Single Center Zero Instance ($mat = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]$):**
  - Concentric Manhattan diamonds expand outward: ring 1 at distance 1, corners at distance 2.
- **All Zeros Instance ($mat = [[0, 0], [0, 0]]$):**
  - All seeded at distance 0; queue empties immediately $\implies$ all zeros.

This instance demonstrates multi-source unweighted shortest path propagation, mathematically proves why breadth-first FIFO search discovers minimum Manhattan distances in a single pass, and derives $O(M \cdot N)$ runtime and $O(M \cdot N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ binary matrix $mat$:
Find the shortest distance to the nearest `0` for every cell.
The distance between two adjacent cells (up, down, left, right) is 1.

```text
Input Grid:
  [ 0,  0,  0 ]
  [ 0,  1,  0 ]
  [ 1,  1,  1 ]

Distance Expansion:
  Zeros start at distance 0.
  Layer 1: cells adjacent to zeros reach distance 1.
  Layer 2: cell (2, 1) is adjacent to distance 1 -> reaches distance 2.

Output:
  [ 0,  0,  0 ]
  [ 0,  1,  0 ]
  [ 1,  2,  1 ]
```

### Multi-Source BFS vs Single-Source BFS
- If we run a separate BFS from each `1` to find the nearest `0`:
  There are up to $O(M \cdot N)$ ones, and each BFS takes $O(M \cdot N)$, giving an unacceptably slow $O((M \cdot N)^2)$ time.
- By **reversing the perspective**:
  - We seed all `0` cells into the queue simultaneously at distance $0$.
  - A single multi-source BFS expands outward like ripples in a pond.
  - Every cell is visited **at most once**, reducing the total time to strictly linear $O(M \cdot N)$!

---

## 2. Conceptual Foundation & Invariants

### 1. BFS Invariant:
In an unweighted graph where all edges have weight 1:
- Nodes visited at level $d$ are pushed to the back of the queue.
- Every node dequeued is processed in strictly non-decreasing order of distance.
- The first time an unvisited cell $(x, y)$ is reached from cell $(i, j)$:
  $$
  ans[x][y] = ans[i][j] + 1
  $$
  This value is mathematically guaranteed to be the shortest path distance.

### 2. Visited State Encoding:
- Initialize the answer matrix $ans$ with $-1$.
- Any cell with $ans \ne -1$ has already been visited or is in the queue.
- Setting $ans[x][y] = ans[i][j] + 1$ upon pushing prevents duplicate insertions into the queue.

> **Wavefront Monotonicity Invariant.** The FIFO queue maintains elements with distance values that differ by at most 1 ($[d, \dots, d, d+1, \dots, d+1]$), ensuring optimal distance assignments without Dijkstra priority heaps.

---

## 3. Step-by-Step Worked Execution

We trace the $3 \times 3$ grid with 5 zeros:

---

### Step 1: Queue Initialization
- Seed all coordinates $(i, j)$ where $mat[i][j] == 0$:
  - $(0, 0), (0, 1), (0, 2), (1, 0), (1, 2)$
- Mark $ans[i][j] = 0$.
- All other cells set to $-1$.

---

### Step 2: Expand Distance 0 Sources
Dequeue each zero source:
- Neighbor $(1, 1)$ is adjacent to $(0, 1)$ and $(1, 0)$:
  $$
  ans[1][1] = 0 + 1 = \mathbf{1}, \quad \text{queue } (1, 1)
  $$
- Neighbor $(2, 0)$ is adjacent to $(1, 0)$:
  $$
  ans[2][0] = 0 + 1 = \mathbf{1}, \quad \text{queue } (2, 0)
  $$
- Neighbor $(2, 2)$ is adjacent to $(1, 2)$:
  $$
  ans[2][2] = 0 + 1 = \mathbf{1}, \quad \text{queue } (2, 2)
  $$

---

### Step 3: Expand Distance 1 Nodes
- Dequeue $(1, 1), (2, 0), (2, 2)$:
  - Cell $(2, 1)$ is adjacent to $(1, 1)$, $(2, 0)$, and $(2, 2)$.
  - $ans[2][1] == -1 \implies$ updated by first arriving edge:
    $$
    ans[2][1] = 1 + 1 = \mathbf{2}, \quad \text{queue } (2, 1)
    $$

---

### Step 4: Dequeue $(2, 1)$
- Neighbors are $(1, 1), (2, 0), (2, 2)$.
- All are already $\ne -1$.
- Queue empties.

---

### Step 5: Output Grid
$$
ans = \begin{bmatrix}
0 & 0 & 0 \\
0 & 1 & 0 \\
1 & 2 & 1
\end{bmatrix}
$$

---

## 4. Complete Execution Trace

| Queue Step | Dequeued Cell | Value $ans[i][j]$ | Unvisited Neighbors Discovered | Assigned Distance |
|:---:|:---:|:---:|:---:|:---:|
| **Init** | All 5 zeros | $0$ | $(1, 1), (2, 0), (2, 2)$ | $0 + 1 = 1$ |
| **$1$** | $(1, 1)$ | $1$ | $(2, 1)$ | $1 + 1 = 2$ |
| **$2$** | $(2, 0)$ | $1$ | $(2, 1)$ (already marked) | — |
| **$3$** | $(2, 2)$ | $1$ | $(2, 1)$ (already marked) | — |
| **$4$** | $(2, 1)$ | $2$ | None | — |
| **Done** | Queue empty | — | — | **Matrix Complete** |

---

## 5. Boundary Cases & Failure Modes

- **Grid Full of Zeros:** All cells are seeded at distance 0 $\implies$ returns identical grid of zeros in $O(M \cdot N)$ time.
- **Single Zero in Corner ($mat[0][0] = 0$):** Manhattan distance creates a continuous gradient $r + c$.
- **Large Grids ($10^4$ cells):** Single-pass BFS processes every cell exactly once without recursion stack overflow.
- **Narrow $1 \times N$ or $M \times 1$ Grids:** Boundary checking $0 \le x < m, 0 \le y < n$ prevents indexing errors along linear arrays.

---

## 6. Traps & Common Anti-Patterns

- **Searching from 1s to 0s:** Running BFS from each 1 causes $O((M \cdot N)^2)$ TLE. Inverting the search to start from all 0s solves the entire matrix in a single $O(M \cdot N)$ sweep.
- **Marking Visited When Dequeuing:** If you mark cells visited only after popping from the queue, adjacent nodes will push the same cell multiple times, causing exponential queue bloat. Mark cells visited *immediately upon pushing*.
- **Using 8 Directions Instead of 4:** Manhattan distance specifies adjacent cells (up, down, left, right). Diagonal moves are not allowed.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initial matrix scan to find zeros takes $O(M \cdot N)$ time.
  - Each cell is pushed into the queue at most once and popped at most once.
  - For each popped cell, exactly 4 neighbors are examined in $O(1)$ time.
  - Total Time: $\mathcal{O}(M \cdot N)$. For $10^4$ cells, completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ space for the queue and distance matrix $ans$.
