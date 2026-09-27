# Guided Example: Cherry Pickup

We trace the step-by-step round-trip reduction to dual synchronous forward walkers, Manhattan distance step dimension ($k = i_1 + j_1 = i_2 + j_2$), thorn collision avoidance ($grid[i][j] == -1$), simultaneous same-cell deduplication ($i_1 == i_2 \implies \text{single count}$), 4-way predecessor transitions, and global maximum harvest attainment on representative obstacle grids:

- **Input:**
  $$
  grid = \begin{bmatrix}
  0 & 1 & -1 \\
  1 & 0 & -1 \\
  1 & 1 & 1
  \end{bmatrix}
  $$
- **Required output:** `5`
  - Field rules:
    - Grid cells:
      - `0`: Empty space.
      - `1`: Contains a cherry. Picking it empties the cell ($1 \to 0$).
      - `-1`: Contains a thorn. Impassable barrier.
    - Path requirements:
      - Phase 1: Walk from top-left $(0, 0)$ to bottom-right $(n - 1, n - 1)$, moving only **right or down**.
      - Phase 2: Walk from $(n - 1, n - 1)$ back to $(0, 0)$, moving only **left or up**.
    - Find the maximum cherries collected across both legs of the journey.
    - If no valid round trip exists (blocked by thorns), return `0`.
    - For the input grid:
      - Column 2 rows 0 and 1 are blocked by thorns (`-1`).
      - Forward leg: $(0, 0) \to (0, 1) \to (1, 1) \to (2, 1) \to (2, 2)$, collecting cherries at $(0, 1)$, $(2, 1)$, $(2, 2)$ (3 cherries).
      - Return leg: $(2, 2) \to (2, 1) \to (2, 0) \to (1, 0) \to (0, 0)$, collecting cherries at $(2, 0)$ and $(1, 0)$ (2 cherries; $(2, 1)$ and $(2, 2)$ were already emptied).
      - Total harvest: $3 + 2 = \mathbf{5}$.
- **Dual Synchronous Walkers & Step-Dimension Invariant:**
  - **The Round-Trip Isomorphism:**
    - A round trip $(0, 0) \to (n - 1, n - 1)$ and back to $(0, 0)$ is mathematically identical to **two walkers starting simultaneously at $(0, 0)$ and moving forward to $(n - 1, n - 1)$**, both using only right and down moves!
  - **The Step-Synchronous Coordinate Reduction:**
    - If both walkers take $k$ steps:
      - Walker 1 is at $(i_1, j_1)$ where $i_1 + j_1 = k \implies j_1 = k - i_1$.
      - Walker 2 is at $(i_2, j_2)$ where $i_2 + j_2 = k \implies j_2 = k - i_2$.
    - This reduces a 4D state space $(i_1, j_1, i_2, j_2)$ to a compact 3D state space $(k, i_1, i_2)$!
  - **Same-Cell Deduplication Invariant:**
    - If both walkers occupy the exact same cell ($i_1 == i_2 \implies j_1 == j_2$):
      - The cherry at $(i_1, j_1)$ can only be collected **once**:
        $$
        t = grid[i_1][j_1]
        $$
    - If the walkers occupy distinct cells ($i_1 \ne i_2$):
      - Both cherries are collected independently:
        $$
        t = grid[i_1][j_1] + grid[i_2][j_2]
        $$
  - **The 4-Way Transition Recurrence:**
    - At step $k$, each walker can arrive from the cell above (moved down, row $i$) or the cell to the left (moved right, row $i - 1$):
      $$
      f[k][i_1][i_2] = t + \max_{\substack{x_1 \in \{i_1 - 1, i_1\} \\ x_2 \in \{i_2 - 1, i_2\}}} f[k - 1][x_1][x_2]
      $$
- **Step-by-Step Worked Execution Trace on the $3 \times 3$ Grid ($n = 3$):**
  - Total step count: $k$ runs from $0$ to $2n - 2 = 2(3) - 2 = \mathbf{4}$.
  - State table $f[k][i_1][i_2]$ initialized to $-\infty$.
  - **Base State ($k = 0$, both at $(0, 0)$):**
    $$
    f[0][0][0] = grid[0][0] = \mathbf{0}
    $$
  - **Step $k = 1$ (Distance 1 from origin):**
    - Possible row positions: $i \in \{0, 1\}$.
    - Cells: $(0, 1) \to \text{cherry } 1$; $(1, 0) \to \text{cherry } 1$.
    - Walker 1 at $(0, 1)$, Walker 2 at $(1, 0)$ ($i_1 = 0, i_2 = 1$):
      - Distinct cells: $t = grid[0][1] + grid[1][0] = 1 + 1 = 2$.
      - Predecessor: $f[0][0][0] = 0$.
      - State:
        $$
        f[1][0][1] = 0 + 2 = \mathbf{2}
        $$
  - **Step $k = 2$:**
    - Coordinates where $i + j = 2$:
      - $(0, 2)$: Thorn ($-1$, impassable!).
      - $(1, 1)$: Empty ($0$).
      - $(2, 0)$: Cherry ($1$).
    - Walker 1 at $(1, 1)$, Walker 2 at $(2, 0)$ ($i_1 = 1, i_2 = 2$):
      - $t = grid[1][1] + grid[2][0] = 0 + 1 = 1$.
      - Best predecessor from $k = 1$: $f[1][0][1] = 2$.
      - State:
        $$
        f[2][1][2] = 2 + 1 = \mathbf{3}
        $$
  - **Step $k = 3$:**
    - Coordinates where $i + j = 3$:
      - $(1, 2)$: Thorn ($-1$, impassable!).
      - $(2, 1)$: Cherry ($1$).
    - Both walkers must pass through $(2, 1)$! ($i_1 = 2, i_2 = 2$):
      - Both at same cell: $t = grid[2][1] = \mathbf{1}$ (collected once).
      - Predecessor from $k = 2$: $f[2][1][2] = 3$.
      - State:
        $$
        f[3][2][2] = 3 + 1 = \mathbf{4}
        $$
  - **Step $k = 4$ (Destination $(2, 2)$):**
    - Both walkers arrive at destination $(2, 2)$ ($i_1 = 2, i_2 = 2$):
      - Both at same cell: $t = grid[2][2] = \mathbf{1}$.
      - Predecessor: $f[3][2][2] = 4$.
      - State:
        $$
        f[4][2][2] = 4 + 1 = \mathbf{5}
        $$
  - **Step 5: Output Maximum Harvest:**
    $$
    ans = \max(0, \; f[4][2][2]) = \mathbf{5}
    $$
- **Unreachable Destination Trace ($grid = [[0, 1], [-1, 0]]$):**
  - Path to $(1, 1)$ is completely blocked by thorns.
  - Destination state remains $-\infty$.
  - $\max(0, -\infty) = \mathbf{0}$.
- **Isolated Starting Cell ($grid[0][0] = -1$):**
  - Origin itself is blocked.
  - Returns **`0`**.

This instance demonstrates multi-agent synchronous dynamic programming and 4D-to-3D manifold reduction under Manhattan metric slicing, mathematically proves why joint forward paths correctly model single-item consumption over bidirectional routes, and derives $O(N^3)$ execution time and $O(N^2)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an $n \times n$ grid with cherries (1), empty cells (0), and thorns (-1):
Walk $(0, 0) \to (n-1, n-1)$ (right/down), then back $(n-1, n-1) \to (0, 0)$ (left/up).
Collected cherries disappear. Find the **maximum total cherries**.
Return 0 if no complete path exists.

```text
grid:
   0  1 -1
   1  0 -1
   1  1  1

Trip 1: (0, 0) -> (0, 1) -> (1, 1) -> (2, 1) -> (2, 2)  [picks 3 cherries]
Trip 2: (2, 2) -> (2, 1) -> (2, 0) -> (1, 0) -> (0, 0)  [picks 2 cherries]

Total cherries collected = 3 + 2 = 5
Result: 5
```

### The Invariant of the Two Forward Walkers
- Going from start to end and returning is equivalent to **two people walking from start to end at the same time**.
- If both people are on step $k = i_1 + j_1 = i_2 + j_2$, then $j_1 = k - i_1$ and $j_2 = k - i_2$.
- If both occupy the same cell ($i_1 == i_2$), the cherry is counted only once!

---

## 2. Conceptual Foundation & Invariants

### 1. Step-Dimension Reduction:
$$
k = i_1 + j_1 = i_2 + j_2 \implies j_1 = k - i_1, \quad j_2 = k - i_2
$$

### 2. The Recurrence:
$$
t = grid[i_1][j_1] + (grid[i_2][j_2] \text{ if } i_1 \ne i_2 \text{ else } 0)
$$
$$
f[k][i_1][i_2] = t + \max_{\substack{x_1 \in \{i_1-1, i_1\} \\ x_2 \in \{i_2-1, i_2\}}} f[k - 1][x_1][x_2]
$$

> **Bilateral Synchronous Path Duality.** The maximum weight pair of forward-backward vertex-disjoint paths on a DAG is isomorphic to the optimal synchronous flow of two particles under common progress parameter $k$, with joint intersection penalty $c(u, u) = f(u)$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Base
- $f[0][0][0] = 0$.

---

### Step 2: $k = 1$
- Walker 1 at $(0, 1)$, Walker 2 at $(1, 0) \implies$ earn $1 + 1 = 2$.
- $f[1][0][1] = 2$.

---

### Step 3: $k = 2$
- Walker 1 at $(1, 1)$, Walker 2 at $(2, 0) \implies$ earn $0 + 1 = 1$.
- $f[2][1][2] = 2 + 1 = 3$.

---

### Step 4: $k = 3$
- Both at $(2, 1) \implies$ earn $1$ (counted once).
- $f[3][2][2] = 3 + 1 = 4$.

---

### Step 5: $k = 4$
- Both reach $(2, 2) \implies$ earn $1$.
- $f[4][2][2] = 4 + 1 = \mathbf{5}$.

---

### Step 6: Output
$$
\mathbf{5}
$$

---

## 4. Complete Execution Trace

| Step $k$ | Walker 1 Position $(i_1, j_1)$ | Walker 2 Position $(i_2, j_2)$ | Same Cell? | Cherries Collected $t$ | Best Previous $f[k-1]$ | Accumulated Total |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $(0, 0)$ | $(0, 0)$ | Yes | $0$ | Base | $0$ |
| $1$ | $(0, 1)$ | $(1, 0)$ | No | $1 + 1 = 2$ | $0$ | $2$ |
| $2$ | $(1, 1)$ | $(2, 0)$ | No | $0 + 1 = 1$ | $2$ | $3$ |
| $3$ | $(2, 1)$ | $(2, 1)$ | **Yes** | **$1$ (Deduplicated)** | $3$ | $4$ |
| **$4$** | **$(2, 2)$** | **$(2, 2)$** | **Yes** | **$1$ (Deduplicated)** | **$4$** | **`5`** |

---

## 5. Boundary Cases & Failure Modes

- **Blocked Path:** If thorns prevent reaching destination $\implies f[2n-2][n-1][n-1] = -\infty \implies$ returns 0.
- **No Cherries ($N \times N$ of 0s):** Returns 0.
- **Single Cell ($[[1]]$):** $k = 0$, both at $(0, 0) \implies$ returns 1.
- **$1 \times 1$ with Thorn ($[[-1]]$):** Blocked $\implies$ returns 0.

---

## 6. Traps & Common Anti-Patterns

- **Greedy Two-Pass Approach:** Running DP once to find the best path, zeroing cherries, and running DP again fails because the first greedy path might block the second path from collecting an even larger total. Both paths must be computed **simultaneously**.
- **Double Counting Same Cell:** If $i_1 == i_2$, both walkers are on the identical cell $(i_1, k - i_1)$. Add $grid[i_1][j_1]$ only once.
- **Thorns Handling:** Cells with $-1$ must be skipped immediately, remaining $-\infty$ so no future transitions pass through them.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Outer loop $k$ runs from $0$ to $2N - 2$: $2N$ steps.
  - Inner loops $i_1$ and $i_2$ run from $0$ to $N - 1$: $N^2$ pairs.
  - Each state considers at most 4 transitions: $\mathcal{O}(1)$.
  - Total Time: strictly cubic $\mathcal{O}(N^3)$. For $N = 50$, total operations $\approx 2.5 \times 10^5$, completing in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N^3)$ for the full 3D array, or $\mathcal{O}(N^2)$ using rolling step planes $k$ and $k - 1$.