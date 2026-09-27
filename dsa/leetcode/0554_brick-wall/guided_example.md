# Guided Example: Brick Wall

We trace the step-by-step brick boundary prefix displacement accumulation ($s = \sum x$), vertical cut duality theorem ($\text{bricks crossed} = \text{total rows} - \text{aligned edges}$), terminal boundary exclusion ($row[:-1]$), hash-map edge frequency maximization ($\max(cnt.values())$), and minimum brick intersection calculation on representative masonry layouts:

- **Input:**
  $$
  wall = [
    [1, 2, 2, 1],
    [3, 1, 2],
    [1, 3, 2],
    [2, 4],
    [3, 1, 2],
    [1, 3, 1, 1]
  ]
  $$
- **Required output:** `2`
  - Dimensions: $m = 6$ rows. Total wall width: $1 + 2 + 2 + 1 = 6$ units.
  - Objective: Draw a continuous vertical line from top to bottom that intersects the **minimum number of bricks**.
  - Edge rule: If the vertical line passes through the edge between two bricks, that row is **not** cut!
  - Boundary constraint: The line cannot be drawn along the left boundary ($x = 0$) or the right boundary ($x = 6$).
- **Duality Maximization & Hash Frequency Trace:**
  - In each row, a vertical cut either:
    - Passes through a brick (cutting it).
    - Or passes through an existing gap between bricks (avoiding a cut).
  - Therefore, for any vertical coordinate $x$:
    $$
    \text{Bricks Crossed}(x) = \text{Total Rows} - \text{Aligned Brick Edges}(x)
    $$
  - To **minimize bricks crossed**, we must **maximize the number of brick edges that line up at the same vertical coordinate $x$**!
  - **Row-by-row prefix edge accumulation (excluding the final edge at $x = 6$):**
    - **Row 0 ($[1, 2, 2, 1]$):**
      - Edge 1: $x = 1$
      - Edge 2: $x = 1 + 2 = 3$
      - Edge 3: $x = 3 + 2 = 5$
      - Registered edges: $\{1, 3, 5\}$
    - **Row 1 ($[3, 1, 2]$):**
      - Edge 1: $x = 3$
      - Edge 2: $x = 3 + 1 = 4$
      - Registered edges: $\{3, 4\}$
    - **Row 2 ($[1, 3, 2]$):**
      - Edge 1: $x = 1$
      - Edge 2: $x = 1 + 3 = 4$
      - Registered edges: $\{1, 4\}$
    - **Row 3 ($[2, 4]$):**
      - Edge 1: $x = 2$
      - Registered edges: $\{2\}$
    - **Row 4 ($[3, 1, 2]$):**
      - Edge 1: $x = 3$
      - Edge 2: $x = 3 + 1 = 4$
      - Registered edges: $\{3, 4\}$
    - **Row 5 ($[1, 3, 1, 1]$):**
      - Edge 1: $x = 1$
      - Edge 2: $x = 1 + 3 = 4$
      - Edge 3: $x = 4 + 1 = 5$
      - Registered edges: $\{1, 4, 5\}$
  - **Frequency Distribution of Interior Edges:**
    - Coordinate $x = 1$: Rows $0, 2, 5 \implies \mathbf{3}$ edges
    - Coordinate $x = 2$: Row $3 \implies \mathbf{1}$ edge
    - Coordinate $x = 3$: Rows $0, 1, 4 \implies \mathbf{3}$ edges
    - Coordinate $x = 4$: Rows $1, 2, 4, 5 \implies \mathbf{4}$ edges (**Peak!**)
    - Coordinate $x = 5$: Rows $0, 5 \implies \mathbf{2}$ edges
  - Peak alignment: Coordinate $x = 4$ aligns with $4$ brick edges.
  - Minimal bricks crossed:
    $$
    \text{Min Crossed} = \text{Total Rows} - \text{Max Edges} = 6 - 4 = \mathbf{2}
    $$
    *(Only Rows 0 and 3 are sliced at $x = 4$; all other 4 rows slip through existing seams!)*
- **Wall with No Interior Edges ($wall = [[3], [3], [3]]$):**
  - No interior edges exist $\implies \max(edges) = 0$.
  - Must cut every row $\implies 3 - 0 = \mathbf{3}$.
- **Single Row Wall ($wall = [[1, 2]]$):**
  - Edge at $x = 1 \implies 1 - 1 = \mathbf{0}$.

This instance demonstrates geometric complement duality in discrete spatial scheduling, mathematically proves why maximizing edge collision frequencies minimizes cut intersections, and derives $O(N)$ runtime (where $N$ is total brick count) and $O(U)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a brick wall where each row contains a series of positive brick widths:
Draw a vertical line from the top to the bottom that cuts through the **fewest number of bricks**.
A line passing through the seam between two bricks does not count as cutting a brick.
You cannot draw the line at the extreme left or right borders.

```text
Wall Layout (Width = 6):
  Row 0: [ 1 |   2   |   2   | 1 ]   -> Edges at: 1, 3, 5
  Row 1: [     3     | 1 |   2   ]   -> Edges at: 3, 4
  Row 2: [ 1 |     3     |   2   ]   -> Edges at: 1, 4
  Row 3: [   2   |       4       ]   -> Edges at: 2
  Row 4: [     3     | 1 |   2   ]   -> Edges at: 3, 4
  Row 5: [ 1 |     3     | 1 | 1 ]   -> Edges at: 1, 4, 5

Best vertical line at x = 4:
  Passes through seams in rows 1, 2, 4, 5 (4 seams avoided!).
  Cuts through bricks only in rows 0 and 3 (2 cuts).

Minimum Bricks Crossed = 2
```

### The Seam-Cut Duality Theorem
- Instead of counting how many bricks are crossed:
  Count how many brick **edges (seams)** are intersected.
- Every seam intersected means **one fewer brick cut** in that row:
  $$
  \text{Cuts} = \text{len}(wall) - \text{Aligned Seams}
  $$
- Therefore, the line that cuts the fewest bricks is the line that passes through the **greatest number of aligned seams**.

---

## 2. Conceptual Foundation & Invariants

### 1. Seam Position Calculation:
For each row $[b_0, b_1, \dots, b_{k-1}]$:
Compute running prefix sums of all bricks **except the last brick**:
$$
s_i = \sum_{j=0}^i b_j \quad \text{for } i \in [0, k - 2]
$$
- The last brick is excluded because its end corresponds to the right border of the entire wall, which is forbidden.

### 2. Frequency Hash Map:
Maintain a counter `cnt` where $cnt[x]$ is the number of rows having an interior seam at coordinate $x$.
- For every row, iterate through $b \in row[:-1]$, updating $s \leftarrow s + b$ and incrementing $cnt[s] \leftarrow cnt[s] + 1$.

### 3. Complement Evaluation:
$$
\text{Answer} = \text{len}(wall) - \max(cnt.values(), \text{default}=0)
$$

> **Duality Invariant.** The vertical line $x = \text{argmax}(cnt)$ maximizes the non-intersected rows, uniquely minimizing the total brick crossings across the entire wall.

---

## 3. Step-by-Step Worked Execution

We trace $wall$ with 6 rows:

---

### Step 1: Initialize
- `cnt = Counter()`
- `len(wall) = 6`

---

### Step 2: Accumulate Seams per Row
- Row 0: `[1, 2, 2, 1]` $\implies$ seams at $1, 3, 5$.
  `cnt[1]+=1, cnt[3]+=1, cnt[5]+=1`.
- Row 1: `[3, 1, 2]` $\implies$ seams at $3, 4$.
  `cnt[3]+=1, cnt[4]+=1`.
- Row 2: `[1, 3, 2]` $\implies$ seams at $1, 4$.
  `cnt[1]+=1, cnt[4]+=1`.
- Row 3: `[2, 4]` $\implies$ seam at $2$.
  `cnt[2]+=1`.
- Row 4: `[3, 1, 2]` $\implies$ seams at $3, 4$.
  `cnt[3]+=1, cnt[4]+=1`.
- Row 5: `[1, 3, 1, 1]` $\implies$ seams at $1, 4, 5$.
  `cnt[1]+=1, cnt[4]+=1, cnt[5]+=1`.

---

### Step 3: Final Seam Counts
- $cnt[1] = 3$
- $cnt[2] = 1$
- $cnt[3] = 3$
- $cnt[4] = \mathbf{4}$
- $cnt[5] = 2$

---

### Step 4: Compute Minimum Cuts
- Maximum aligned seams:
  $$
  \max(cnt.values()) = \mathbf{4} \quad (\text{at coordinate } x = 4)
  $$
- Resulting cuts:
  $$
  \text{len}(wall) - 4 = 6 - 4 = \mathbf{2}
  $$

---

## 4. Complete Execution Trace

| Row Index | Bricks | Prefix Sums Calculated | Seam Coordinates Registered | Running Frequency Map |
|:---:|:---:|:---:|:---:|:---:|
| $0$ | `[1, 2, 2, 1]` | $1, 3, 5$ (skip 6) | $1, 3, 5$ | $\{1:1, 3:1, 5:1\}$ |
| $1$ | `[3, 1, 2]` | $3, 4$ (skip 6) | $3, 4$ | $\{1:1, 3:2, 4:1, 5:1\}$ |
| $2$ | `[1, 3, 2]` | $1, 4$ (skip 6) | $1, 4$ | $\{1:2, 3:2, 4:2, 5:1\}$ |
| $3$ | `[2, 4]` | $2$ (skip 6) | $2$ | $\{1:2, 2:1, 3:2, 4:2, 5:1\}$ |
| $4$ | `[3, 1, 2]` | $3, 4$ (skip 6) | $3, 4$ | $\{1:2, 2:1, 3:3, 4:3, 5:1\}$ |
| $5$ | `[1, 3, 1, 1]` | $1, 4, 5$ (skip 6) | $1, 4, 5$ | $\{1:3, 2:1, 3:3, \mathbf{4:4}, 5:2\}$ |
| **Result** | — | — | Peak: $4$ at $x = 4$ | **$6 - 4 = 2$** |

---

## 5. Boundary Cases & Failure Modes

- **Solid Bricks with No Seams ($[[3], [3]]$):** $row[:-1]$ is empty $\implies cnt$ is empty $\implies \max$ defaults to $0 \implies 2 - 0 = \mathbf{2}$.
- **All Rows Identical ($[[1, 1], [1, 1]]$):** Seam at $x = 1$ in both rows $\implies \max = 2 \implies 2 - 2 = \mathbf{0}$.
- **Single Row ($[[1, 2, 3]]$):** Max seam count is $1 \implies 1 - 1 = \mathbf{0}$.
- **Wide Bricks ($10^4$ width):** Coordinate space is sparse; hash map only stores actual brick seam coordinates, independent of wall width.

---

## 6. Traps & Common Anti-Patterns

- **Simulating Every Integer Coordinate $x \in [1, \text{Width}-1]$:** Total wall width can be up to $2 \times 10^9$, making linear coordinate scanning impossible. Hashing only the coordinates where seams actually occur takes $O(\text{total bricks})$ time.
- **Including the Right Border Seam:** If you include the sum of all bricks in the row, coordinate $x = \text{Width}$ will appear in every row with count equal to $\text{len}(wall)$, leading to $6 - 6 = 0$ along the illegal outer wall edge. Slicing with `row[:-1]` strictly excludes the right edge.
- **Counting Bricks Directly:** Tracking which brick each row cuts requires interval trees or binary search per row ($O(M \log K)$). Counting seams with a hash map runs in linear $O(N)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $B$ be the total number of bricks across all rows in the wall ($\le 2 \times 10^4$).
  - Computing the prefix sums and updating the hash map takes $O(B)$ time.
  - Finding the maximum value in the hash map takes $O(U)$ where $U \le B$ is the number of unique seam positions.
  - Total Time: $\mathcal{O}(B)$. For $B = 2 \times 10^4$, completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(U)$ space to store the seam frequencies in hash map `cnt`.
