# Guided Example: Smallest Rectangle Enclosing Black Pixels

We trace the step-by-step projection of a 2D connected component onto orthogonal 1D axes, four-way binary search bisections for bounding box limits ($u, d, l, r$), row and column occupancy predicates, and rectangle area calculation on representative binary pixel matrices:

- **Input:**
  $$
  \text{image} = \begin{bmatrix}
  \text{"0010"} \\
  \text{"0110"} \\
  \text{"0100"}
  \end{bmatrix}, \quad x = 0, \quad y = 2
  $$
- **Required output:** $6$
  - Bounding rows: $u = 0$ (top), $d = 2$ (bottom) $\implies \text{height} = 2 - 0 + 1 = 3$
  - Bounding columns: $l = 1$ (left), $r = 2$ (right) $\implies \text{width} = 2 - 1 + 1 = 2$
  - Minimal bounding area: $3 \times 2 = 6$
- **Single Pixel Base Case:** $\text{image} = [["1"]], x = 0, y = 0 \implies \text{area} = 1$
- **Full Matrix Solid Region:** All cells contain `'1'` $\implies \text{area} = m \times n$
- **Elongated Line Segment:** Connected component forming a 1-pixel horizontal or vertical stripe

This instance demonstrates connected-component 1D projection monotonicity, proves why a full $O(M N)$ matrix scan is eliminated in favor of $O(N \log M + M \log N)$ binary search queries, explains upper/lower bisection branch boundaries, and operates in $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ ($3 \times 4$) binary grid containing exactly **one connected component of black pixels (`'1'`)**:
A seed pixel is provided at $(x, y) = (0, 2)$ where $\text{image}[0][2] == \text{'1'}$.

```text
       Col 0  Col 1  Col 2  Col 3
Row 0:   0      0     [1]     0     <- (x=0, y=2)
Row 1:   0      1      1      0
Row 2:   0      1      0      0

Black pixels: (0, 2), (1, 1), (1, 2), (2, 1)
Row extent:    from Row 0 to Row 2 -> Height = 3
Column extent: from Col 1 to Col 2 -> Width  = 2
Minimal enclosing box area = 3 * 2 = 6
```

### Why Binary Search Beats Full Traversal
- An exhaustive scan visits all $M \times N$ cells.
- Because the black pixels form a **single connected component**, projecting the 2D region onto either axis yields a **contiguous interval of non-empty slices**:
  - Row occupancy interval: $[u, d]$ with $0 \le u \le x \le d < m$.
  - Column occupancy interval: $[l, r]$ with $0 \le l \le y \le r < n$.
- For any row $k$, whether row $k$ contains a `'1'` is monotonic:
  - Rows before $u$: contain **only `'0'`**.
  - Rows in $[u, d]$: contain **at least one `'1'`**.
  - Rows after $d$: contain **only `'0'`**.
We can find all four boundary coordinates $u, d, l, r$ using **four independent binary searches**!

The two occupancy profiles those searches query are the following slices:

| Slice | Index | Cells in the slice | Contains a `'1'` | Interval role | Consequence for this instance |
|:---|:---:|:---|:---:|:---|:---|
| Row 0 | 0 | `"0010"` | Yes | $u = 0$, top endpoint | The $u$-search interval $[0, x] = [0, 0]$ is a singleton, so it evaluates no predicate and returns the seed row directly |
| Row 1 | 1 | `"0110"` | Yes | interior of $[u, d]$ | The probe $\text{mid} = 1$ in the $d$-search succeeds, proving $d \ge 1$ |
| Row 2 | 2 | `"0100"` | Yes | $d = 2$, bottom endpoint | The probe $\text{mid} = 2$ succeeds, and there is no row 3 left to test |
| Column 0 | 0 | `(0, 0, 0)` | No | left of $[l, r]$ | The probe $\text{mid} = 0$ fails, proving $l > 0$ |
| Column 1 | 1 | `(0, 1, 1)` | Yes | $l = 1$, left endpoint | The probe $\text{mid} = 1$ succeeds, proving $l \le 1$ |
| Column 2 | 2 | `(1, 1, 0)` | Yes | $r = 2$, right endpoint | This is the seed column, and the only column that can still hold $r$ once column 3 fails |
| Column 3 | 3 | `(0, 0, 0)` | No | right of $[l, r]$ | The probe $\text{mid} = 3$ fails, proving $r < 3$ |

The row profile reads occupied, occupied, occupied, and the column profile reads
empty, occupied, occupied, empty. Both therefore have the shape
$\text{No}^{*}\,\text{Yes}^{+}\,\text{No}^{*}$: one contiguous block of occupied
slices, with the seed's own slice inside it. That shape — and not merely the
existence of black pixels — is what makes a single bisection per boundary sound.

---

## 2. Conceptual Foundation & Invariants

### The 4 Boundary Bisections
We know the seed $(x, y)$ contains `'1'`. Hence:
1. **Top Boundary $u \in [0, x]$:** First row containing a `'1'`.
   - Probe `mid = (left + right) // 2`.
   - If row `mid` contains `'1'`: $u \le mid \implies right = mid$.
   - Else: $u > mid \implies left = mid + 1$.
2. **Bottom Boundary $d \in [x, m - 1]$:** Last row containing a `'1'`.
   - Probe `mid = (left + right + 1) // 2`.
   - If row `mid` contains `'1'`: $d \ge mid \implies left = mid$.
   - Else: $d < mid \implies right = mid - 1$.
3. **Left Boundary $l \in [0, y]$:** First column containing a `'1'`.
   - Probe `mid = (left + right) // 2`.
   - If col `mid` contains `'1'`: $l \le mid \implies right = mid$.
   - Else: $l > mid \implies left = mid + 1$.
4. **Right Boundary $r \in [y, n - 1]$:** Last column containing a `'1'`.
   - Probe `mid = (left + right + 1) // 2`.
   - If col `mid` contains `'1'`: $r \ge mid \implies left = mid$.
   - Else: $r < mid \implies right = mid - 1$.

### Area Calculation:
$$
\text{Area} = (d - u + 1) \times (r - l + 1)
$$

> **Invariant.** Connectedness guarantees that if any row or column contains a black pixel, the set of all such rows and columns forms a single closed interval containing the seed coordinates $(x, y)$.

---

## 3. Step-by-Step Worked Execution

We trace the four binary searches on $\text{image} = [\text{"0010"}, \text{"0110"}, \text{"0100"}]$ with $(x, y) = (0, 2)$:
Dimensions: $m = 3, n = 4$.

---

### Step 1: Find Top Boundary $u \in [0, 0]$
- Initial interval: $[0, x] = [0, 0]$.
- Left $= 0$, Right $= 0$.
- Loop condition `left < right` ($0 < 0$) is immediately false.
- **Top bound $u = 0$**.

---

### Step 2: Find Bottom Boundary $d \in [x, m - 1] = [0, 2]$
- Initial interval: $left = 0, right = 2$.
- **Iteration 1:**
  - $\text{mid} = (0 + 2 + 1) // 2 = 1$.
  - Probe row 1: `"0110"` has `'1'` at col 1. (Contains `'1'`).
  - $left \leftarrow mid = 1$. Active range: $[1, 2]$.
- **Iteration 2:**
  - $\text{mid} = (1 + 2 + 1) // 2 = 2$.
  - Probe row 2: `"0100"` has `'1'` at col 1. (Contains `'1'`).
  - $left \leftarrow mid = 2$. Active range: $[2, 2]$.
- Converged!
- **Bottom bound $d = 2$**.

---

### Step 3: Find Left Boundary $l \in [0, y] = [0, 2]$
- Initial interval: $left = 0, right = 2$.
- **Iteration 1:**
  - $\text{mid} = (0 + 2) // 2 = 1$.
  - Probe column 1:
    - $\text{image}[0][1] = \text{'0'}$
    - $\text{image}[1][1] = \text{'1'}$ (Contains `'1'`).
  - $right \leftarrow mid = 1$. Active range: $[0, 1]$.
- **Iteration 2:**
  - $\text{mid} = (0 + 1) // 2 = 0$.
  - Probe column 0:
    - $\text{image}[0][0] = \text{'0'}$
    - $\text{image}[1][0] = \text{'0'}$
    - $\text{image}[2][0] = \text{'0'}$ (All `'0'`, no black pixels).
  - $left \leftarrow mid + 1 = 1$. Active range: $[1, 1]$.
- Converged!
- **Left bound $l = 1$**.

---

### Step 4: Find Right Boundary $r \in [y, n - 1] = [2, 3]$
- Initial interval: $left = 2, right = 3$.
- **Iteration 1:**
  - $\text{mid} = (2 + 3 + 1) // 2 = 3$.
  - Probe column 3:
    - $\text{image}[0][3] = \text{'0'}$
    - $\text{image}[1][3] = \text{'0'}$
    - $\text{image}[2][3] = \text{'0'}$ (All `'0'`).
  - $right \leftarrow mid - 1 = 2$. Active range: $[2, 2]$.
- Converged!
- **Right bound $r = 2$**.

---

### Step 5: Area Calculation
- $\text{Height} = d - u + 1 = 2 - 0 + 1 = \mathbf{3}$.
- $\text{Width} = r - l + 1 = 2 - 1 + 1 = \mathbf{2}$.
- $\text{Area} = 3 \times 2 = \mathbf{6}$.

---

## 4. Complete Execution Trace

```text
Image (3x4), Seed: (0, 2)

Search 1: Top row u in [0, 0]      -> u = 0
Search 2: Bottom row d in [0, 2]:
  mid = 1: row 1 contains '1'      -> left = 1
  mid = 2: row 2 contains '1'      -> left = 2 -> d = 2
Search 3: Left col l in [0, 2]:
  mid = 1: col 1 contains '1'      -> right = 1
  mid = 0: col 0 has NO '1'        -> left = 1  -> l = 1
Search 4: Right col r in [2, 3]:
  mid = 3: col 3 has NO '1'        -> right = 2 -> r = 2

Bounding box: rows [0..2], cols [1..2]
Area = (2 - 0 + 1) * (2 - 1 + 1) = 3 * 2 = 6
```

| Boundary Target | Search Space | Midpoint Probed | Slice Inspected | Contains `'1'`? | Range Transition | Final Value |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Top $u$** | $[0, 0]$ | - | - | - | $left == right$ | **$u = 0$** |
| Bottom $d$ | $[0, 2]$ | 1 | Row 1 (`"0110"`) | Yes | $left \leftarrow 1$ | - |
| **Bottom $d$** | $[1, 2]$ | 2 | Row 2 (`"0100"`) | Yes | $left \leftarrow 2$ | **$d = 2$** |
| Left $l$ | $[0, 2]$ | 1 | Col 1 (`['0', '1', '1']`) | Yes | $right \leftarrow 1$ | - |
| **Left $l$** | $[0, 1]$ | 0 | Col 0 (`['0', '0', '0']`) | No | $left \leftarrow 1$ | **$l = 1$** |
| **Right $r$** | $[2, 3]$ | 3 | Col 3 (`['0', '0', '0']`) | No | $right \leftarrow 2$ | **$r = 2$** |

---

## 5. Algorithmic Correctness

**Soundness.** Because black pixels are 4-way connected, the set of rows containing at least one black pixel forms a single contiguous range $[u, d]$, and the set of columns forms a single contiguous range $[l, r]$. The seed $(x, y)$ is guaranteed to lie within $[u, d] \times [l, r]$. Binary searching outward from the seed correctly identifies the transition points where occupancy drops from positive to zero.

**Completeness.** Since the component is connected, no disjoint black pixels can exist outside $[u, d] \times [l, r]$. The four extreme coordinates $u, d, l, r$ precisely encompass all black pixels with minimal possible width and height, guaranteeing the calculated area is exact and minimal.

---

## 6. Traps This Instance Exposes

- **Linear Scanning ($O(M N)$):** Running BFS/DFS or scanning every cell takes $O(M N)$ time. The problem explicitly requires a solution with less than $O(M N)$ complexity. Four 1D binary searches achieve this in $O(N \log M + M \log N)$.
- **Midpoint Biasing for Upper vs Lower Bounds:** When finding the upper boundaries ($d$ and $r$), the midpoint must be biased upward: `(left + right + 1) // 2`. Using integer floor division without `+ 1` causes infinite loops when `left = right - 1`.
- **Assuming Multiple Components:** The problem guarantees only ONE connected component of black pixels. If multiple disjoint components existed, the 1D projection would not be monotonic and binary search would fail.

### Boundary scenarios around this instance

The traced instance uses every search at full strength. These neighbours of it
show which search does the work when the geometry is degenerate; the probe counts
are the number of slice predicates each boundary costs.

| Scenario | Instance | $(u, d, l, r)$ | Probes on $u, d, l, r$ | Area | What keeps the result exact |
|:---|:---|:---:|:---:|:---:|:---|
| Isolated seed | `["1"]`, $(x, y) = (0, 0)$ | $(0, 0, 0, 0)$ | 0, 0, 0, 0 | 1 | All four intervals are singletons, so no predicate is evaluated at all and the area formula alone produces the answer |
| Seed pinned to the top-left corner | `["11000", "10000", "10000"]`, $(0, 0)$ | $(0, 2, 0, 1)$ | 0, 2, 0, 2 | 6 | Both lower-bound searches start already converged at the seed; only the two upper-bound searches still have larger candidates to confirm |
| Seed pinned to the bottom-right corner | `["0000", "0001", "0011"]`, $(2, 3)$ | $(1, 2, 2, 3)$ | 2, 0, 2, 0 | 4 | Both upper-bound searches are singletons fixed by the seed, so the lower-bound searches must rule out the empty slices above and to the left |
| Single pixel inside a white border | `["00000", "00000", "00100", "00000"]`, $(2, 2)$ | $(2, 2, 2, 2)$ | 1, 1, 1, 1 | 1 | Each interval has exactly two candidates, so one probe per axis decides on which side of the seed the empty slice lies |
| Dense rectangle | `["1111", "1111", "1111"]`, $(1, 2)$ | $(0, 2, 0, 3)$ | 1, 1, 2, 1 | 12 | Every probe succeeds, so each interval shrinks only from the outside and no occupied slice is ever discarded |
| Maximum-width single row | one row of 100 `'1'` cells, $(0, 99)$ | $(0, 0, 0, 99)$ | 0, 0, 7, 0 | 100 | The lone row makes both row intervals singletons; only the $l$-search runs, spending seven probes to walk from $\text{mid} = 49$ down to $\text{mid} = 0$ |

### Approaches this instance eliminates

| Approach | State maintained | Time | Auxiliary space | Why it is chosen or eliminated |
|:---|:---|:---:|:---:|:---|
| Full raster scan | Four running extremes, updated per cell | $O(M N)$ | $O(1)$ | Correct, but it reads every cell and the statement demands strictly less than $O(M N)$ |
| BFS or DFS flood fill from the seed | A frontier plus a visited set | $O(M N)$ worst case | $O(M N)$ worst case | It must touch every black cell; on the dense $3 \times 4$ rectangle that is all 12 cells, plus a visited structure the bisections never need |
| Four seed-bounded bisections (the method used here) | Four intervals $[left, right]$ and one occupancy predicate | $O(N \log M + M \log N)$ | $O(1)$ | Each probe costs one slice read, and the seed bound keeps every predicate monotone |
| Bisections over the whole axis $[0, m-1]$ or $[0, n-1]$ | The same four intervals, widened | $O(N \log M + M \log N)$ | $O(1)$ | Rejected: a full axis has the profile empty–occupied–empty, so the predicate is not monotone. On the eight-row single column $(0, 0, 0, 0, 0, 1, 1, 1)$ with the seed at row 6, the upper-bound search converges to $d = 0$ although the true bottom row is $7$ |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log M + M \log N)$.
  - Finding $u$ and $d$: $O(\log M)$ bisection steps, each scanning a row of length $N \implies O(N \log M)$.
  - Finding $l$ and $r$: $O(\log N)$ bisection steps, each scanning a column of length $M \implies O(M \log N)$.
  - Sublinear compared to $O(M N)$.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory. No additional grid buffers or visited matrices are allocated.
