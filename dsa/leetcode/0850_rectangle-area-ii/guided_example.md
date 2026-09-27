# Guided Example: Rectangle Area II

We trace the step-by-step sweep-line algorithm with coordinate compression, vertical segment event generation ($x_1 \to +1, x_2 \to -1$), 1D segment tree interval measure aggregation, rectangle strip area integration ($\text{height} \times \Delta x$), and modulo $10^9 + 7$ total union area accumulation on representative overlapping rectangle configurations:

- **Input:**
  $$
  rectangles = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]
  $$
- **Required output:** `6`
  - 2D Area of union specifications:
    - We are given a list of axis-aligned rectangles $[x_1, y_1, x_2, y_2]$.
    - We seek the **total area of their union**:
      $$
      \text{Area}\left( \bigcup_{i=1}^N R_i \right) \pmod{10^9 + 7}
      $$
    - Overlapping regions must be counted **exactly once** (not duplicated).
    - For $rectangles = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]$:
      - Rectangle 1: $[0, 0]$ to $[2, 2]$. Area 4.
      - Rectangle 2: $[1, 0]$ to $[2, 3]$. Area 3.
      - Rectangle 3: $[1, 0]$ to $[3, 1]$. Area 2.
      - Vertical slices along the $x$-axis:
        - Slice 1 ($x \in [0, 1]$, width $\Delta x = 1$): Only Rectangle 1 is present ($y \in [0, 2]$, height 2) $\implies 2 \times 1 = \mathbf{2}$.
        - Slice 2 ($x \in [1, 2]$, width $\Delta x = 1$): All three rectangles present. Union of $y$ is $[0, 3]$ (height 3) $\implies 3 \times 1 = \mathbf{3}$.
        - Slice 3 ($x \in [2, 3]$, width $\Delta x = 1$): Rectangles 1 and 2 ended at $x = 2$. Only Rectangle 3 remains ($y \in [0, 1]$, height 1) $\implies 1 \times 1 = \mathbf{1}$.
      - Total union area:
        $$
        2 + 3 + 1 = \mathbf{6}
        $$
- **Sweep-Line & Coordinate Compression Invariant:**
  - **Fubini's Slicing Theorem in Discrete Geometry:**
    - The 2D area of a polygon union can be integrated as a sequence of vertical 1D strips between discrete event boundaries:
      $$
      \text{Area} = \int \text{Length}(Y(x)) \, dx = \sum_{k=1}^{M-1} L(x_{k-1}) \cdot (x_k - x_{k-1})
      $$
    - The active vertical profile $Y(x)$ changes **only at the vertical edges of rectangles** ($x_1$ and $x_2$).
  - **Event Segmentation:**
    - Each rectangle $[x_1, y_1, x_2, y_2]$ generates two events:
      1. **Entry Event:** $(x_1, y_1, y_2, +1)$ — interval $[y_1, y_2]$ is added.
      2. **Exit Event:** $(x_2, y_1, y_2, -1)$ — interval $[y_1, y_2]$ is removed.
    - Sort all events by $x$-coordinate in ascending order.
  - **The 1D Segment Tree Measure:**
    - Collect and sort all distinct $y$-coordinates:
      $$
      alls = [y^{(0)}, y^{(1)}, \dots, y^{(K-1)}]
      $$
    - The $y$-axis is partitioned into $K - 1$ elementary base segments:
      $$
      I_j = [alls[j], \; alls[j+1]]
      $$
    - A segment tree tracks which elementary segments are covered by at least one active rectangle ($cnt > 0$).
    - When $cnt > 0$, the segment tree node reports full coverage of its range; when $cnt == 0$, it reports the sum of its children's covered lengths.
    - `tree.length` gives the exact measure (length) of the union of active vertical intervals in $\mathcal{O}(\log K)$ time.
- **Step-by-Step Worked Execution Trace on the 3-Rectangle Plane:**
  - Sorted distinct $y$-coordinates:
    $$
    alls = [0, \; 1, \; 2, \; 3]
    $$
    - Base intervals:
      - $I_0 = [0, 1]$ (length 1)
      - $I_1 = [1, 2]$ (length 1)
      - $I_2 = [2, 3]$ (length 1)
  - Events generated and sorted by $x$:
    1. $x = 0$: Add $[0, 2]$ (from Rec 1)
    2. $x = 1$: Add $[0, 3]$ (from Rec 2)
    3. $x = 1$: Add $[0, 1]$ (from Rec 3)
    4. $x = 2$: Remove $[0, 2]$ (from Rec 1)
    5. $x = 2$: Remove $[0, 3]$ (from Rec 2)
    6. $x = 3$: Remove $[0, 1]$ (from Rec 3)
  - Initialize total area: $ans = 0$.
  - **Slice 0 ($x = 0$ Event):**
    - Previous $x$: None (start of sweep).
    - Add $[0, 2]$ from Rec 1: covers $I_0 = [0, 1]$ and $I_1 = [1, 2]$.
    - Active vertical length:
      $$
      tree.length = (1 - 0) + (2 - 1) = \mathbf{2}
      $$
  - **Slice 1 ($x = 1$ Events, Transition from $x = 0$ to $x = 1$):**
    - Width of strip: $\Delta x = 1 - 0 = \mathbf{1}$.
    - Area contributed by strip $[0, 1]$:
      $$
      tree.length \times \Delta x = 2 \times 1 = \mathbf{2}
      $$
    - Accumulate: $ans \leftarrow 0 + 2 = \mathbf{2}$.
    - Process events at $x = 1$:
      - Add $[0, 3]$ from Rec 2: covers $I_0, I_1, I_2$.
      - Add $[0, 1]$ from Rec 3: covers $I_0$.
    - Active vertical length:
      $$
      tree.length = (3 - 0) = \mathbf{3}
      $$
  - **Slice 2 ($x = 2$ Events, Transition from $x = 1$ to $x = 2$):**
    - Width of strip: $\Delta x = 2 - 1 = \mathbf{1}$.
    - Area contributed by strip $[1, 2]$:
      $$
      tree.length \times \Delta x = 3 \times 1 = \mathbf{3}
      $$
    - Accumulate: $ans \leftarrow 2 + 3 = \mathbf{5}$.
    - Process events at $x = 2$:
      - Remove $[0, 2]$ (Rec 1 ends).
      - Remove $[0, 3]$ (Rec 2 ends).
    - Remaining active intervals: only Rec 3 ($[0, 1]$) remains!
    - Active vertical length:
      $$
      tree.length = (1 - 0) = \mathbf{1}
      $$
  - **Slice 3 ($x = 3$ Events, Transition from $x = 2$ to $x = 3$):**
    - Width of strip: $\Delta x = 3 - 2 = \mathbf{1}$.
    - Area contributed by strip $[2, 3]$:
      $$
      tree.length \times \Delta x = 1 \times 1 = \mathbf{1}
      $$
    - Accumulate: $ans \leftarrow 5 + 1 = \mathbf{6}$.
    - Process events at $x = 3$:
      - Remove $[0, 1]$ (Rec 3 ends).
    - Active vertical length drops to 0.
  - **All Events Consumed:**
    $$
    ans = \mathbf{6}
    $$
- **Disjoint Rectangles Trace ($rec_1 = [0, 0, 1, 1], rec_2 = [2, 2, 3, 3]$):**
  - Strip $[0, 1]$ contributes $1 \times 1 = 1$.
  - Strip $[1, 2]$ has $tree.length = 0 \implies 0 \times 1 = 0$.
  - Strip $[2, 3]$ contributes $1 \times 1 = 1$.
  - Total area: $1 + 0 + 1 = \mathbf{2}$.
- **Completely Nested Rectangles ($rec_1 = [0, 0, 4, 4], rec_2 = [1, 1, 2, 2]$):**
  - The outer rectangle covers all $y \in [0, 4]$ throughout $x \in [0, 4]$.
  - Segment tree maintains $cnt \ge 1$ across all sub-intervals, correctly measuring total area $4 \times 4 = \mathbf{16}$.

This instance demonstrates Klee's measure problem in computational geometry via Cartesian sweep-hyperplanes and dynamic interval segment tree maintenance, mathematically proves why sorting 1D project boundaries factors 2D union area into piecewise constant measure integration, and derives $O(N \log N)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a list of rectangles $[x_1, y_1, x_2, y_2]$:
Calculate the **total area covered** by the union of all rectangles modulo $10^9 + 7$.

```text
rectangles:
  Rec 1: [0, 0, 2, 2]
  Rec 2: [1, 0, 2, 3]
  Rec 3: [1, 0, 3, 1]

Sweep vertical line along x:
  x in [0, 1]: height = 2 (Rec 1)            -> area = 2 * 1 = 2
  x in [1, 2]: height = 3 (Recs 1, 2, 3)     -> area = 3 * 1 = 3
  x in [2, 3]: height = 1 (Rec 3 only)       -> area = 1 * 1 = 1

Total area = 2 + 3 + 1 = 6
Result: 6
```

### The Invariant of Sweep-Line Slicing
- Slice the 2D area into vertical strips between adjacent $x$-event coordinates.
- Area of each strip is $\Delta x \times \text{Length}(Y)$.
- A Segment Tree dynamically maintains the total active vertical length $\text{Length}(Y)$ as rectangles enter ($+1$) and exit ($-1$).

---

## 2. Conceptual Foundation & Invariants

### 1. Riemann-Stieltjes Area Integral:
$$
\text{Area} = \sum_{k=1}^{2N - 1} \text{Measure}\big(Y(x_{k-1})\big) \times (x_k - x_{k-1})
$$

### 2. Segment Tree Pushup Invariant:
For node $u$ covering range $[l, r]$:
$$
length(u) = \begin{cases}
y_{r+1} - y_l & cnt(u) > 0 \\
0 & cnt(u) == 0 \;\land\; l == r \\
length(left) + length(right) & cnt(u) == 0 \;\land\; l < r
\end{cases}
$$

> **Klee's Measure Invariant.** The continuous Lebesque measure of a finite union of rectangles in $\mathbb{R}^2$ is piecewise constant along any axis between vertex projections. A 1D interval segment tree computes the exact measure of the 1D projection fiber in $\mathcal{O}(\log N)$ per transition.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Events Sorted by $x$
- $x = 0$: add $[0, 2]$.
- $x = 1$: add $[0, 3]$ and $[0, 1]$.
- $x = 2$: remove $[0, 2]$ and $[0, 3]$.
- $x = 3$: remove $[0, 1]$.

---

### Step 2: Strip $x \in [0, 1]$
- Width $\Delta x = 1 - 0 = 1$. Height $= 2$.
- Area $= 2 \times 1 = \mathbf{2}$.

---

### Step 3: Strip $x \in [1, 2]$
- Width $\Delta x = 2 - 1 = 1$. Height $= 3$.
- Area $= 3 \times 1 = \mathbf{3}$.

---

### Step 4: Strip $x \in [2, 3]$
- Width $\Delta x = 3 - 2 = 1$. Height $= 1$.
- Area $= 1 \times 1 = \mathbf{1}$.

---

### Step 5: Output
- Total $= 2 + 3 + 1 = \mathbf{6}$.

---

## 4. Complete Execution Trace

| Event Index | Event Coordinate $x$ | Strip Width $\Delta x$ | Active Vertical Segments | Active Height | Strip Area Added | Cumulative Area |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $x = 0$ | — | Rec 1 added ($[0, 2]$) | $2$ | Start | $0$ |
| $1$ | $x = 1$ | $1 - 0 = 1$ | Recs 2, 3 added | $3$ | $2 \times 1 = 2$ | $2$ |
| $2$ | $x = 2$ | $2 - 1 = 1$ | Recs 1, 2 removed | $1$ | $3 \times 1 = 3$ | $5$ |
| **$3$** | **$x = 3$** | **$3 - 2 = 1$** | **Rec 3 removed** | **$0$** | **$1 \times 1 = 1$** | **`6`** |
| **Final** | — | — | — | — | — | **`6`** |

---

## 5. Boundary Cases & Failure Modes

- **Disjoint Rectangles:** Height becomes 0 across empty horizontal gaps; width $\times 0 = 0$ added correctly.
- **Large Coordinates ($10^9$):** Modulo $10^9 + 7$ applied to total sum.
- **Completely Overlapping Rectangles:** Segment tree $cnt$ increments to 2; `length` reports the interval only once.
- **Single Rectangle:** Single strip evaluated from $x_1$ to $x_2 \implies (x_2 - x_1)(y_2 - y_1)$.

---

## 6. Traps & Common Anti-Patterns

- **Grid Matrix Allocation ($O(W \cdot H)$):** Coordinates reach $10^9$; allocating a 2D boolean grid causes Out-Of-Memory. Coordinate compression and sweep-line use $O(N)$ memory.
- **Inclusion-Exclusion Principle ($O(2^N)$):** For $N = 200$, inclusion-exclusion requires $2^{200}$ terms. Sweep-line solves in $O(N \log N)$.
- **Using Points Instead of Intervals in Segment Tree:** A segment tree over coordinate points must represent intervals $[y_j, y_{j+1}]$ (leaf $j$ represents length $y_{j+1} - y_j$), NOT single discrete coordinates.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Generating and sorting $2N$ events: $\mathcal{O}(N \log N)$.
  - Sorting $2N$ unique $y$-coordinates: $\mathcal{O}(N \log N)$.
  - Segment tree modification per event: $\mathcal{O}(\log N)$ across $2N$ events $\implies \mathcal{O}(N \log N)$.
  - Total Time: strictly $\mathcal{O}(N \log N)$ where $N \le 200 \implies \le 2000$ operations. Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory for the event list, coordinate map, and segment tree.
