# Guided Example: Magic Squares In Grid

We trace the step-by-step $3 \times 3$ sliding window subgrid extraction, permutation validity verification (distinct digits in $\{1, \dots, 9\}$), magic constant sum derivation ($\sum = 15$), center element invariance ($grid[i+1][j+1] = 5$), row/column/diagonal sum equilibrium checks, and valid magic subgrid enumeration on representative 2D integer lattices:

- **Input:**
  $$
  grid = \begin{bmatrix}
  4 & 3 & 8 & 4 \\
  9 & 5 & 1 & 9 \\
  2 & 7 & 6 & 2
  \end{bmatrix}
  $$
- **Required output:** `1`
  - $3 \times 3$ Magic square mathematical specifications:
    - A $3 \times 3$ subgrid is a **magic square** if and only if:
      1. It contains all 9 distinct integers from $1$ to $9$ inclusive ($\{1, 2, 3, 4, 5, 6, 7, 8, 9\}$).
      2. Every row sums to the exact same value.
      3. Every column sums to the exact same value.
      4. Both main diagonals sum to that exact same value.
    - **The Unique Magic Constant ($15$):**
      - The sum of all integers from 1 to 9 is:
        $$
        \sum_{k=1}^9 k = \frac{9 \times 10}{2} = 45
        $$
      - Since the 3 rows partition the 9 cells without overlap, each row must sum to:
        $$
        S = \frac{45}{3} = \mathbf{15}
        $$
    - **The Center Cell Invariant ($5$):**
      - The center cell is shared by 1 row, 1 column, and 2 diagonals (4 lines in total).
      - Adding these 4 lines yields $4 \times 15 = 60$. The sum of all cells is 45, and the center is counted 3 extra times:
        $$
        45 + 3 \cdot center = 60 \iff 3 \cdot center = 15 \iff center = \mathbf{5}
        $$
    - For the $3 \times 4$ grid:
      - There are two possible $3 \times 3$ subgrids: starting at column 0 and starting at column 1.
      - Subgrid starting at column 0:
        $$
        \begin{bmatrix} 4 & 3 & 8 \\ 9 & 5 & 1 \\ 2 & 7 & 6 \end{bmatrix}
        $$
        - Rows: $4+3+8 = 15$, $9+5+1 = 15$, $2+7+6 = 15$.
        - Columns: $4+9+2 = 15$, $3+5+7 = 15$, $8+1+6 = 15$.
        - Diagonals: $4+5+6 = 15$, $8+5+2 = 15$.
        - Digits: all distinct $1 \dots 9$.
        - Valid magic square!
      - Subgrid starting at column 1:
        $$
        \begin{bmatrix} 3 & 8 & 4 \\ 5 & 1 & 9 \\ 7 & 6 & 2 \end{bmatrix}
        $$
        - Center is $1 \ne 5$ $\implies$ Fails center invariant immediately!
      - Total magic squares: **`1`**.
- **Sliding Window & Arithmetic Verification Invariant:**
  - **Grid Boundaries:**
    - For an $m \times n$ grid:
    - If $m < 3$ or $n < 3$, no $3 \times 3$ subgrid can fit $\implies ans = 0$.
    - Candidate top-left corners $(i, j)$ satisfy:
      $$
      0 \le i \le m - 3, \quad 0 \le j \le n - 3
      $$
  - **The Verification Pipeline for Window $(i, j)$:**
    1. **Digit Range & Set Uniqueness:**
       - Every cell $v = grid[x][y]$ ($x \in [i, i+2], y \in [j, j+2]$) must satisfy $1 \le v \le 9$.
       - The set of values must have cardinality $|S| = 9$.
    2. **Center Cell Fast Filter:**
       - $grid[i + 1][j + 1] == 5$.
    3. **Line Sum Equality:**
       - All 3 row sums must equal 15:
         $$
         \forall r \in \{0, 1, 2\}: \sum_{c=0}^2 grid[i+r][j+c] = 15
         $$
       - All 3 column sums must equal 15:
         $$
         \forall c \in \{0, 1, 2\}: \sum_{r=0}^2 grid[i+r][j+c] = 15
         $$
       - Both diagonals must equal 15:
         $$
         grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] = 15
         $$
         $$
         grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] = 15
         $$
- **Step-by-Step Worked Execution Trace on the $3 \times 4$ Grid:**
  - Dimensions: $m = 3, n = 4$.
  - Possible corner indices: $(i = 0, j = 0)$ and $(i = 0, j = 1)$.
  - **Evaluating Window at $(0, 0)$:**
    - Subgrid:
      $$
      \begin{bmatrix} 4 & 3 & 8 \\ 9 & 5 & 1 \\ 2 & 7 & 6 \end{bmatrix}
      $$
    - Center check: $grid[0+1][0+1] = grid[1][1] = 5 == 5 \implies \mathbf{Pass.}$
    - Distinct digit check:
      $$
      S = \{4, 3, 8, 9, 5, 1, 2, 7, 6\} = \{1, 2, 3, 4, 5, 6, 7, 8, 9\} \implies |S| = 9 \implies \mathbf{Pass.}
      $$
    - Row sums:
      - Row 0: $4 + 3 + 8 = \mathbf{15}$
      - Row 1: $9 + 5 + 1 = \mathbf{15}$
      - Row 2: $2 + 7 + 6 = \mathbf{15}$
    - Column sums:
      - Col 0: $4 + 9 + 2 = \mathbf{15}$
      - Col 1: $3 + 5 + 7 = \mathbf{15}$
      - Col 2: $8 + 1 + 6 = \mathbf{15}$
    - Diagonal sums:
      - Main: $4 + 5 + 6 = \mathbf{15}$
      - Anti: $8 + 5 + 2 = \mathbf{15}$
    - All 8 line sums equal 15!
    - Outcome: $\mathbf{Valid\ Magic\ Square\ (Count\ = 1).}$
  - **Evaluating Window at $(0, 1)$:**
    - Subgrid:
      $$
      \begin{bmatrix} 3 & 8 & 4 \\ 5 & 1 & 9 \\ 7 & 6 & 2 \end{bmatrix}
      $$
    - Center check: $grid[1][2] = \mathbf{1 \ne 5} \implies \mathbf{Fail!}$
    - Outcome: $\mathbf{Invalid\ (Count\ = 0).}$
  - **Global Sum of Magic Squares:**
    $$
    ans = 1 + 0 = \mathbf{1}
    $$
- **Grid Too Small Trace ($grid = [[1, 2], [3, 4]]$):**
  - Dimensions $2 \times 2$.
  - $i + 3 > m \implies$ loop bounds empty $\implies ans = \mathbf{0}$.
- **Numbers Outside $[1, 9]$ ($grid$ contains 0 or 15):**
  - Digits check rejects values $< 1$ or $> 9$, preventing sum tricks like $0 + 5 + 10 = 15$.

This instance demonstrates spatial convolution on discrete affine lattices and dihedral symmetry group $D_4$ invariance of Lo Shu magic squares, mathematically proves why conservation of arithmetic progression sums fixes the centroid value to 5, and derives $O(M \cdot N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ integer grid:
Count how many $3 \times 3$ subgrids are **magic squares** (contain distinct numbers $1 \dots 9$, and all rows, columns, and diagonals sum to the same value).

```text
grid:
  4 3 8 4
  9 5 1 9
  2 7 6 2

Subgrid 1 at (0, 0):
  4 3 8 -> sum 15
  9 5 1 -> sum 15
  2 7 6 -> sum 15
  Cols: 15, 15, 15
  Diagonals: 15, 15
  Numbers: 1 to 9 all present! -> MAGIC SQUARE!

Subgrid 2 at (0, 1):
  Center is 1 != 5 -> NOT magic!

Result: 1
```

### The Invariant of the Lo Shu Magic Square
- In any $3 \times 3$ magic square of digits $1 \dots 9$:
  - The magic sum is always $15$ ($45 / 3$).
  - The center element is always **$5$**.
  - All 8 line sums (3 rows, 3 columns, 2 diagonals) must equal $15$.
  - All 9 digits must be distinct and in $[1, 9]$.

---

## 2. Conceptual Foundation & Invariants

### 1. Magic Constant:
$$
S = \frac{1}{3} \sum_{k=1}^9 k = 15
$$

### 2. Centroid Constraint:
$$
grid[i+1][j+1] = 5
$$

### 3. Magic Predicate:
$$
\text{IsMagic}(i, j) \iff \Big( \{ grid[x][y] \} = \{1, \dots, 9\} \Big) \;\land\; \Big( \text{all 8 lines sum to } 15 \Big)
$$
$$
ans = \sum_{i=0}^{m-3} \sum_{j=0}^{n-3} \mathbb{I}[\text{IsMagic}(i, j)]
$$

> **$D_4$ Orbit Invariant.** Up to rotation and reflection (the dihedral group $D_4$), there exists exactly ONE unique $3 \times 3$ magic square using digits $1 \dots 9$ (the ancient Chinese Lo Shu square). The 8 elements of its symmetry orbit all share center 5, even corners $\{2, 4, 6, 8\}$, and odd edges $\{1, 3, 7, 9\}$.

---

## 3. Step-by-Step Worked Execution

We trace the sample $3 \times 4$ grid:

---

### Step 1: Subgrid at $(0, 0)$
- Center is 5.
- Numbers: $\{1, 2, 3, 4, 5, 6, 7, 8, 9\}$.
- Row sums: $15, 15, 15$.
- Col sums: $15, 15, 15$.
- Diag sums: $15, 15$.
- Valid $\implies +1$.

---

### Step 2: Subgrid at $(0, 1)$
- Center is $1 \ne 5 \implies$ invalid.

---

### Step 3: Output
$$
\mathbf{1}
$$

---

## 4. Complete Execution Trace

| Top-Left Corner $(i, j)$ | Center Value | Distinct Digits in $[1, 9]$? | Row Sums | Column Sums | Diagonals | Magic Square? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$(0, 0)$** | **$5$** | **$\{1 \dots 9\}$** | **$15, 15, 15$** | **$15, 15, 15$** | **$15, 15$** | **`Yes`** |
| $(0, 1)$ | $1$ | Fails (Center $\ne 5$) | — | — | — | No |
| **Total** | — | — | — | — | — | **`1`** |

---

## 5. Boundary Cases & Failure Modes

- **Grid Smaller than $3 \times 3$ ($m < 3$ or $n < 3$):** No subgrids fit $\implies 0$.
- **Values Outside $[1, 9]$:** E.g. 0 and 10 can sum to 15, but fail the $1 \le v \le 9$ condition.
- **Duplicate Values in $[1, 9]$:** Set cardinality $|S| \ne 9$ catches duplicates (e.g. $[5, 5, 5]$ row).
- **Correct Row Sums but Wrong Diagonals:** The diagonal check ensures diagonals also equal 15.

---

## 6. Traps & Common Anti-Patterns

- **Checking Only Row Sums:** Subgrids can have rows summing to 15 without columns or diagonals summing to 15. All 8 lines must be checked.
- **Forgetting Set Uniqueness:** Numbers like $0, 5, 10$ or repeated $5$s can produce line sums of 15; ensure elements are strictly a permutation of $\{1, \dots, 9\}$.
- **Unbounded Sliding:** Always stop corner loops at $m - 3$ and $n - 3$ to avoid indexing past matrix boundaries.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Number of $3 \times 3$ windows in an $M \times N$ grid: $(M - 2)(N - 2)$.
  - Each window has exactly 9 cells; checking takes $\mathcal{O}(1)$ operations (constant 9 cell inspections and 8 sums).
  - Total Time: strictly $\mathcal{O}(M \cdot N)$ where $M, N \le 10 \implies \le 100$ cell checks. Completes in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space.
