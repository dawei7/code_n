# Guided Example: Lonely Pixel I

We trace the step-by-step row-wise and column-wise black pixel frequency aggregation ($rows[i], cols[j]$), lonely coordinate predicate testing ($picture[i][j] == \text{'B'} \land rows[i] == 1 \land cols[j] == 1$), row/column isolation verification, and total lonely pixel counting on representative 2D grids:

- **Input:**
  $$
  picture = \begin{bmatrix}
  W & W & B \\
  W & B & W \\
  B & W & W
  \end{bmatrix}
  $$
- **Required output:** `3`
  - Dimensions: $m = 3$ rows, $n = 3$ columns.
  - Black lonely pixel definition: A cell $(i, j)$ containing `'B'` such that **no other black pixel exists in row $i$**, and **no other black pixel exists in column $j$**.
- **Two-pass row and column aggregation trace:**
  - **Pass 1: Count `'B'` pixels per row and per column:**
    - Initialize counters: $rows = [0, 0, 0]$ and $cols = [0, 0, 0]$.
    - **Row 0:**
      - $(0, 0) = \text{'W'}$, $(0, 1) = \text{'W'}$, $(0, 2) = \text{'B'}$.
      - Row 0 count: $rows[0] = \mathbf{1}$.
      - Column 2 count: $cols[2] \leftarrow 0 + 1 = 1$.
    - **Row 1:**
      - $(1, 0) = \text{'W'}$, $(1, 1) = \text{'B'}$, $(1, 2) = \text{'W'}$.
      - Row 1 count: $rows[1] = \mathbf{1}$.
      - Column 1 count: $cols[1] \leftarrow 0 + 1 = 1$.
    - **Row 2:**
      - $(2, 0) = \text{'B'}$, $(2, 1) = \text{'W'}$, $(2, 2) = \text{'W'}$.
      - Row 2 count: $rows[2] = \mathbf{1}$.
      - Column 0 count: $cols[0] \leftarrow 0 + 1 = 1$.
    - Aggregate frequency vectors:
      $$
      rows = [1, \; 1, \; 1], \quad cols = [1, \; 1, \; 1]
      $$
  - **Pass 2: Identify Lonely Pixels:**
    - Initialize $ans = 0$.
    - **Cell $(0, 2)$ (`'B'`):**
      - $rows[0] == 1$ (no other `'B'` in row 0).
      - $cols[2] == 1$ (no other `'B'` in col 2).
      - Both conditions satisfied $\implies ans \leftarrow 0 + 1 = \mathbf{1}$.
    - **Cell $(1, 1)$ (`'B'`):**
      - $rows[1] == 1$ and $cols[1] == 1 \implies ans \leftarrow 1 + 1 = \mathbf{2}$.
    - **Cell $(2, 0)$ (`'B'`):**
      - $rows[2] == 1$ and $cols[0] == 1 \implies ans \leftarrow 2 + 1 = \mathbf{3}$.
  - Total black lonely pixels: **`3`**.
- **Dense Row Conflict Instance ($picture = [[\text{"B"}, \text{"B"}, \text{"B"}], [\text{"B"}, \text{"B"}, \text{"W"}], [\text{"B"}, \text{"B"}, \text{"B"}]]$):**
  - All rows have $\ge 2$ black pixels $\implies$ no row has count 1 $\implies \mathbf{0}$.
- **Cross Collision Instance:**
  - If $(0, 1)$ is `'B'` and $(0, 2)$ is `'B'`, row 0 has count 2 $\implies$ neither is lonely.

This instance demonstrates orthogonal projection frequency counting, mathematically proves why $O(M + N)$ marginal counts identify isolated matrix elements in $O(1)$ lookup time, and derives $O(M \cdot N)$ runtime and $O(M + N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ picture consisting of `'B'` (black) and `'W'` (white) pixels:
A **black lonely pixel** is a `'B'` that has:
1. Exactly one `'B'` in its entire row (itself).
2. Exactly one `'B'` in its entire column (itself).
Return the total number of black lonely pixels.

```text
Picture:
  [ W,  W,  B ]  -> Row 0 has 1 'B' (at col 2)
  [ W,  B,  W ]  -> Row 1 has 1 'B' (at col 1)
  [ B,  W,  W ]  -> Row 2 has 1 'B' (at col 0)
    |   |   |
    v   v   v
Cols:1  1   1   -> Col 0, 1, 2 each have exactly 1 'B'!

All 3 'B's are completely isolated in their rows and columns!
Result: 3
```

### Avoiding the $O(M \cdot N \cdot (M + N))$ Search
- Checking row and column isolation naively by scanning the entire row and column for every `'B'` takes $O(M + N)$ per pixel, leading to $O(M \cdot N \cdot (M + N))$ overall time.
- By precomputing the frequency of `'B'` in each row and column in a first pass:
  - Any pixel $(i, j)$ is lonely **if and only if**:
    $$
    picture[i][j] == \text{'B'} \quad \land \quad rows[i] == 1 \quad \land \quad cols[j] == 1
    $$
  - Every pixel is evaluated in $O(1)$ operations during the second pass.

---

## 2. Conceptual Foundation & Invariants

### 1. Marginal Frequency Vectors:
Let $rows$ be an array of size $m$, and $cols$ be an array of size $n$:
$$
rows[i] = \sum_{j=0}^{n-1} \mathbf{1}[picture[i][j] == \text{'B'}]
$$
$$
cols[j] = \sum_{i=0}^{m-1} \mathbf{1}[picture[i][j] == \text{'B'}]
$$

### 2. The Isolation Predicate:
A cell $(i, j)$ is a black lonely pixel if:
$$
picture[i][j] == \text{'B'} \quad \land \quad rows[i] == 1 \quad \land \quad cols[j] == 1
$$
- $rows[i] == 1$ guarantees no other pixel in row $i$ is black.
- $cols[j] == 1$ guarantees no other pixel in column $j$ is black.

> **Marginal Isolation Invariant.** The conditions $rows[i] = 1$ and $cols[j] = 1$ are necessary and sufficient to ensure that pixel $(i, j)$ shares its row and column with zero other black pixels.

---

## 3. Step-by-Step Worked Execution

We trace the $3 \times 3$ diagonal matrix:

---

### Step 1: Precompute Marginal Counts (Pass 1)
Initialize $rows = [0, 0, 0], cols = [0, 0, 0]$.
- Row 0: `['W', 'W', 'B']` $\implies rows[0] = 1, cols[2] = 1$.
- Row 1: `['W', 'B', 'W']` $\implies rows[1] = 1, cols[1] = 1$.
- Row 2: `['B', 'W', 'W']` $\implies rows[2] = 1, cols[0] = 1$.
Final marginal arrays:
$$
rows = [1, \; 1, \; 1], \quad cols = [1, \; 1, \; 1]
$$

---

### Step 2: Test Isolation (Pass 2)
Initialize $ans = 0$.

1. **Cell $(0, 2)$:**
   - $picture[0][2] = \text{'B'}$.
   - $rows[0] = 1$ and $cols[2] = 1$ (Pass!).
   - $ans \leftarrow 0 + 1 = \mathbf{1}$.

2. **Cell $(1, 1)$:**
   - $picture[1][1] = \text{'B'}$.
   - $rows[1] = 1$ and $cols[1] = 1$ (Pass!).
   - $ans \leftarrow 1 + 1 = \mathbf{2}$.

3. **Cell $(2, 0)$:**
   - $picture[2][0] = \text{'B'}$.
   - $rows[2] = 1$ and $cols[0] = 1$ (Pass!).
   - $ans \leftarrow 2 + 1 = \mathbf{3}$.

4. All other cells contain `'W'` and are skipped.

---

### Step 3: Final Output
$$
ans = \mathbf{3}
$$

---

## 4. Complete Execution Trace

| Cell $(i, j)$ | Pixel Value | Row Count $rows[i]$ | Col Count $cols[j]$ | Lonely Predicate Satisfied? | Running $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $(0, 0)$ | `'W'` | $1$ | $1$ | No (not `'B'`) | $0$ |
| $(0, 1)$ | `'W'` | $1$ | $1$ | No | $0$ |
| **$(0, 2)$** | **`'B'`** | **$1$** | **$1$** | **Yes** | **$1$** |
| $(1, 0)$ | `'W'` | $1$ | $1$ | No | $1$ |
| **$(1, 1)$** | **`'B'`** | **$1$** | **$1$** | **Yes** | **$2$** |
| $(1, 2)$ | `'W'` | $1$ | $1$ | No | $2$ |
| **$(2, 0)$** | **`'B'`** | **$1$** | **$1$** | **Yes** | **$3$** |
| $(2, 1)$ | `'W'` | $1$ | $1$ | No | $3$ |
| $(2, 2)$ | `'W'` | $1$ | $1$ | No | $3$ |
| **Final** | — | — | — | — | **Result: $3$** |

---

## 5. Boundary Cases & Failure Modes

- **No Black Pixels ($all \text{ 'W'}$):** All row and column counts are 0 $\implies ans = 0$.
- **Multiple Black Pixels in Same Row:** E.g. $rows[i] = 2 \implies$ neither pixel qualifies.
- **Multiple Black Pixels in Same Column:** E.g. $cols[j] = 2 \implies$ neither pixel qualifies.
- **$1 \times 1$ Matrix with `'B'`:** $rows[0] = 1, cols[0] = 1 \implies \mathbf{1}$.

---

## 6. Traps & Common Anti-Patterns

- **Checking Diagonals:** The problem statement only specifies row and column isolation. Diagonal neighbors are completely ignored.
- **Modifying the Grid In-Place:** Overwriting pixels with visited markers ruins column counting for subsequent rows. Using separate 1D count arrays is clean and non-destructive.
- **Counting Rows Without Checking Cells:** Simply counting how many rows have $rows[i] == 1$ without checking if that row's black pixel lies in a column with $cols[j] == 1$ produces false positives.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Pass 1 visits each cell once to compute marginal sums: $O(M \cdot N)$.
  - Pass 2 visits each cell once to check condition: $O(M \cdot N)$.
  - Total Time: $\mathcal{O}(M \cdot N)$. For $500 \times 500$, completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M + N)$ space for the row and column count arrays.
