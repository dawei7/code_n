# Guided Example: Number of Corner Rectangles

We trace the step-by-step row-wise column pair enumeration ($c_1 < c_2$ with $grid[r][c_1] = grid[r][c_2] = 1$), dynamic column pair frequency accumulation ($cnt[(c_1, c_2)]$), combinatorial rectangle formation ($ans \leftarrow ans + cnt[(c_1, c_2)]$), duplicate row pairing prevention, and axis-aligned corner detection on representative binary matrices:

- **Input:**
  $$
  grid = \begin{bmatrix}
  1 & 0 & 0 & 1 & 0 \\
  0 & 0 & 1 & 0 & 1 \\
  0 & 0 & 0 & 1 & 0 \\
  1 & 0 & 1 & 0 & 1
  \end{bmatrix}
  $$
- **Required output:** `1`
  - Corner rectangle specifications:
    - An axis-aligned corner rectangle is defined by **four distinct positions** $(r_1, c_1)$, $(r_1, c_2)$, $(r_2, c_1)$, and $(r_2, c_2)$ with:
      $$
      r_1 < r_2 \quad \text{and} \quad c_1 < c_2
      $$
    - All four corners must contain value **`1`**:
      $$
      grid[r_1][c_1] = grid[r_1][c_2] = grid[r_2][c_1] = grid[r_2][c_2] = 1
      $$
    - Cells in the interior or on edges other than the 4 corners do not affect the validity of the rectangle.
    - For the input grid:
      - Check row 1: $1$s at columns $2$ and $4$ $\implies (1, 2) = 1, (1, 4) = 1$.
      - Check row 3: $1$s at columns $2$ and $4$ $\implies (3, 2) = 1, (3, 4) = 1$.
      - The 4 points $(1, 2), (1, 4), (3, 2), (3, 4)$ all have value 1 and form an axis-aligned rectangle spanning rows $\{1, 3\}$ and columns $\{2, 4\}$.
      - No other combination of 2 rows shares two identical columns of 1s.
      - Total corner rectangles: **1**.
- **Column Pair Hash Counting & Combinatorial Invariant:**
  - **The Geometric Decomposition:**
    - Any axis-aligned rectangle consists of two horizontal segments across the **exact same column pair** $(c_1, c_2)$ in two distinct rows $r_1 < r_2$.
    - Finding corner rectangles is therefore equivalent to finding pairs of rows that both have $1$s in columns $c_1$ and $c_2$.
  - **The Incremental Contribution Identity:**
    - Process the grid row by row. Maintain a frequency map $cnt[(c_1, c_2)]$ of how many earlier rows had $1$s in both columns $c_1$ and $c_2$.
    - When the current row $r$ also has $1$s at $c_1$ and $c_2$:
      - This row forms a new, distinct rectangle with **each of the previous rows** that shared this column pair:
        $$
        ans \leftarrow ans + cnt[(c_1, c_2)]
        $$
      - Then, increment the observed frequency for future rows:
        $$
        cnt[(c_1, c_2)] \leftarrow cnt[(c_1, c_2)] + 1
        $$
    - This eliminates any nested 4-loop search, counting every rectangle exactly once in a streaming fashion!
- **Step-by-Step Worked Execution Trace on the $4 \times 5$ Grid:**
  - Dimensions: $m = 4$ rows, $n = 5$ columns.
  - Initialize total rectangles: $ans = 0$.
  - Initialize empty pair frequency counter: $cnt = \{\}$.
  - **Row $r = 0$ ($[1, 0, 0, 1, 0]$):**
    - Indices with $1$: columns $\{0, 3\}$.
    - Column pairs:
      - Pair $(0, 3)$:
        - Previous occurrences: $cnt[(0, 3)] = 0$.
        - Add to answer: $ans \leftarrow ans + 0 = 0$.
        - Update map: $cnt[(0, 3)] \leftarrow \mathbf{1}$.
  - **Row $r = 1$ ($[0, 0, 1, 0, 1]$):**
    - Indices with $1$: columns $\{2, 4\}$.
    - Column pairs:
      - Pair $(2, 4)$:
        - Previous occurrences: $cnt[(2, 4)] = 0$.
        - Add to answer: $ans \leftarrow ans + 0 = 0$.
        - Update map: $cnt[(2, 4)] \leftarrow \mathbf{1}$.
  - **Row $r = 2$ ($[0, 0, 0, 1, 0]$):**
    - Indices with $1$: column $\{3\}$ (only one $1$).
    - Cannot form any column pairs ($c_1 < c_2$).
    - Move to next row.
  - **Row $r = 3$ ($[1, 0, 1, 0, 1]$):**
    - Indices with $1$: columns $\{0, 2, 4\}$.
    - Column pairs:
      1. **Pair $(0, 2)$:**
         - $cnt[(0, 2)] = 0 \implies ans += 0$.
         - $cnt[(0, 2)] \leftarrow \mathbf{1}$.
      2. **Pair $(0, 4)$:**
         - $cnt[(0, 4)] = 0 \implies ans += 0$.
         - $cnt[(0, 4)] \leftarrow \mathbf{1}$.
      3. **Pair $(2, 4)$:**
         - Lookup: $cnt[(2, 4)] = \mathbf{1}$ *(Present in Row 1!)*.
         - Forms a new corner rectangle with Row 1!
           $$
           ans \leftarrow ans + 1 = \mathbf{1}
           $$
         - Update map: $cnt[(2, 4)] \leftarrow 1 + 1 = \mathbf{2}$.
  - **Output Total Rectangles:**
    $$
    ans = \mathbf{1}
    $$
- **Dense All-Ones Grid Trace ($3 \times 3$ Matrix of 1s):**
  - Every row has $\binom{3}{2} = 3$ column pairs: $(0, 1), (0, 2), (1, 2)$.
  - Row 0: registers each pair with count 1 ($ans += 0$).
  - Row 1: each pair contributes $1$ ($ans += 3 \times 1 = 3$). Counts become 2.
  - Row 2: each pair contributes $2$ ($ans += 3 \times 2 = 6$).
  - Total: $3 + 6 = \mathbf{9}$ rectangles ($=\binom{3}{2} \times \binom{3}{2} = 9$).
- **Single Row Grid ($grid = [[1, 1, 1, 1]]$):**
  - Only 1 row $\implies r_1 < r_2$ is impossible.
  - Zero rectangles formed $\implies$ returns **`0`**.

This instance demonstrates bipartite incidence matching and column-pair projection hashing, mathematically proves why pairwise edge frequency summation computes the exact edge chromatic matchings of $K_{2,2}$ subgraphs, and derives $O(M \cdot N^2)$ runtime and $O(N^2)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ binary matrix:
Find the number of **corner rectangles** (4 corners of an axis-aligned rectangle having value 1).

```text
grid:
  1 0 0 1 0
  0 0 1 0 1  <- 1s at cols 2, 4
  0 0 0 1 0
  1 0 1 0 1  <- 1s at cols 2, 4

Rows 1 and 3 both have 1s at columns 2 and 4!
Corners: (1, 2), (1, 4), (3, 2), (3, 4).
Result: 1
```

### The Invariant of the Column Pair Multiplicity
- Two 1s in the same row at columns $(c_1, c_2)$ form a horizontal edge.
- If $k$ previous rows also had 1s at $(c_1, c_2)$, the current row creates $k$ new rectangles.
- Tracking $cnt[(c_1, c_2)]$ dynamically counts all rectangles in a single row pass without checking all row quadruplets.

---

## 2. Conceptual Foundation & Invariants

### 1. Row Column-Pair Iteration:
For each row with $c_1 < c_2$ and $row[c_1] = row[c_2] = 1$:
$$
ans \leftarrow ans + cnt[(c_1, c_2)]
$$
$$
cnt[(c_1, c_2)] \leftarrow cnt[(c_1, c_2)] + 1
$$

### 2. Global Closed-Form Identity:
$$
ans = \sum_{0 \le c_1 < c_2 < n} \binom{cnt[(c_1, c_2)]}{2}
$$

> **Bipartite $K_{2,2}$ Graph Counting Invariant.** The number of axis-aligned rectangles is the number of induced 4-cycles $C_4$ in the bipartite graph $G = (R, C, E)$ between rows and columns, reducible to $\sum_{u < v \in C} \binom{|N(u) \cap N(v)|}{2}$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Row 0
- Pairs: $(0, 3) \to cnt[(0, 3)] = 1$.

---

### Step 2: Row 1
- Pairs: $(2, 4) \to cnt[(2, 4)] = 1$.

---

### Step 3: Row 2
- Single 1 $\implies$ no pairs.

---

### Step 4: Row 3
- Pairs: $(0, 2), (0, 4), (2, 4)$.
- $(2, 4)$ was seen in Row 1!
- $ans \leftarrow ans + cnt[(2, 4)] = 0 + 1 = \mathbf{1}$.

---

### Step 5: Output
$$
\mathbf{1}
$$

---

## 4. Complete Execution Trace

| Row $r$ | Row Content | 1-Column Indices | Generated Pairs $(c_1, c_2)$ | Existing $cnt$ in Map | Rectangles Added |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | `[1, 0, 0, 1, 0]` | $\{0, 3\}$ | $(0, 3)$ | $0$ | $+0$ |
| $1$ | `[0, 0, 1, 0, 1]` | $\{2, 4\}$ | $(2, 4)$ | $0$ | $+0$ |
| $2$ | `[0, 0, 0, 1, 0]` | $\{3\}$ | None | — | $+0$ |
| **$3$** | **`[1, 0, 1, 0, 1]`** | **$\{0, 2, 4\}$** | **$(2, 4)$** | **`1` (from Row 1)** | **`+1`** |
| **Total** | — | — | — | — | **`1`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Row ($m = 1$):** Cannot form $r_1 < r_2 \implies$ returns 0.
- **Single Column ($n = 1$):** Cannot form $c_1 < c_2 \implies$ returns 0.
- **No Ones / Sparse Grid with No Rectangles:** Returns 0.
- **All Ones Grid ($M \times N$):** Returns $\binom{M}{2} \times \binom{N}{2}$.

---

## 6. Traps & Common Anti-Patterns

- **Brute Force 4-Loop ($O(M^2 N^2)$):** Checking all $(r_1, r_2, c_1, c_2)$ takes $\approx (200)^4 = 1.6 \times 10^9$ operations (TLE). The column-pair hash table reduces this to $O(M \cdot N^2)$.
- **Degenerate Rectangles ($r_1 == r_2$ or $c_1 == c_2$):** Corner rectangles require 4 *distinct* points ($r_1 < r_2$ and $c_1 < c_2$). Lines of 1s do not form rectangles.
- **Sparse vs Dense Optimization:** When rows are sparse, iterating only over indices with $row[j] == 1$ is significantly faster than checking all $N^2$ pairs.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - $M$ rows. For each row, iterating over pairs of 1-columns takes $\mathcal{O}(K^2)$ where $K \le N$ is the number of 1s in the row.
  - In the worst case (all 1s): $M \times \binom{N}{2} = \mathcal{O}(M \cdot N^2)$. For $M, N \le 200$, total operations $\le 4 \times 10^6$. Completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N^2)$ space for the column-pair frequency hash map.