# Guided Example: Toeplitz Matrix

We trace the step-by-step 2D grid diagonal coordinate invariant ($i - j = \text{constant}$), local predecessor neighbor verification ($matrix[i][j] == matrix[i-1][j-1]$), single-pass nested loop traversal over the interior $(1 \dots m-1) \times (1 \dots n-1)$, early mismatch termination, and global matrix validity on representative rectangular arrays:

- **Input:**
  $$
  matrix = \begin{bmatrix}
  1 & 2 & 3 & 4 \\
  5 & 1 & 2 & 3 \\
  9 & 5 & 1 & 2
  \end{bmatrix}
  $$
- **Required output:** `true`
  - Toeplitz matrix definition:
    - A matrix is **Toeplitz** if and only if **every descending diagonal** (from top-left to bottom-right) contains identical elements.
    - Formally, along each diagonal, the difference between row and column indices is constant:
      $$
      i - j = c \implies matrix[i][j] = \text{constant}
      $$
    - For the input matrix:
      - Diagonal $i - j = 0$: $[1, 1, 1]$ (cells $(0, 0), (1, 1), (2, 2)$) $\implies$ all 1.
      - Diagonal $i - j = -1$: $[2, 2, 2]$ (cells $(0, 1), (1, 2), (2, 3)$) $\implies$ all 2.
      - Diagonal $i - j = -2$: $[3, 3]$ (cells $(0, 2), (1, 3)$) $\implies$ all 3.
      - Diagonal $i - j = -3$: $[4]$ (cell $(0, 3)$) $\implies$ single element 4.
      - Diagonal $i - j = 1$: $[5, 5]$ (cells $(1, 0), (2, 1)$) $\implies$ all 5.
      - Diagonal $i - j = 2$: $[9]$ (cell $(2, 0)$) $\implies$ single element 9.
      - Every diagonal contains uniform values $\implies$ output is **`true`**.
- **Local Predecessor Comparison Invariant:**
  - **Transitivity of Constant Diagonals:**
    - A diagonal sequence $x_0, x_1, x_2, \dots$ has all identical elements if and only if every adjacent pair satisfies:
      $$
      x_k == x_{k - 1}
      $$
    - In matrix coordinates, the element immediately preceding $(i, j)$ along the descending diagonal is $(i - 1, j - 1)$.
    - Therefore, the global Toeplitz condition reduces to checking the local relation:
      $$
      matrix[i][j] == matrix[i - 1][j - 1] \quad \forall i \in [1, m - 1], \; j \in [1, n - 1]
      $$
    - If even a single cell violates this equality, the matrix is disqualified immediately (`return false`).
- **Step-by-Step Worked Execution Trace on the $3 \times 4$ Matrix:**
  - Dimensions: $m = 3$ rows, $n = 4$ columns.
  - Interior scan ranges: rows $i = 1 \dots 2$, columns $j = 1 \dots 3$.
  - **Row $i = 1$:**
    - **Cell $(1, 1)$ ($v = 1$):**
      - Top-left predecessor: $(0, 0) \to 1$.
      - Compare: $matrix[1][1] == matrix[0][0] \iff 1 == 1 \implies \mathbf{Match.}$
    - **Cell $(1, 2)$ ($v = 2$):**
      - Top-left predecessor: $(0, 1) \to 2$.
      - Compare: $matrix[1][2] == matrix[0][1] \iff 2 == 2 \implies \mathbf{Match.}$
    - **Cell $(1, 3)$ ($v = 3$):**
      - Top-left predecessor: $(0, 2) \to 3$.
      - Compare: $matrix[1][3] == matrix[0][2] \iff 3 == 3 \implies \mathbf{Match.}$
  - **Row $i = 2$:**
    - **Cell $(2, 1)$ ($v = 5$):**
      - Top-left predecessor: $(1, 0) \to 5$.
      - Compare: $matrix[2][1] == matrix[1][0] \iff 5 == 5 \implies \mathbf{Match.}$
    - **Cell $(2, 2)$ ($v = 1$):**
      - Top-left predecessor: $(1, 1) \to 1$.
      - Compare: $matrix[2][2] == matrix[1][1] \iff 1 == 1 \implies \mathbf{Match.}$
    - **Cell $(2, 3)$ ($v = 2$):**
      - Top-left predecessor: $(1, 2) \to 2$.
      - Compare: $matrix[2][3] == matrix[1][2] \iff 2 == 2 \implies \mathbf{Match.}$
  - **Termination:**
    - All $(m - 1)(n - 1) = 2 \times 3 = 6$ interior cells matched their top-left predecessors.
    - Matrix is strictly Toeplitz:
      $$
      ans = \mathbf{true}
      $$
- **Mismatch Violation Trace ($matrix = [[1, 2], [2, 2]]$):**
  - Dimensions $2 \times 2$.
  - Cell $(1, 1) = 2$.
  - Top-left predecessor $(0, 0) = 1$.
  - Compare: $matrix[1][1] \ne matrix[0][0]$ ($2 \ne 1$).
  - Mismatch detected $\implies$ returns **`false`**.
- **Single Row or Single Column Matrix ($[[1, 2, 3]]$ or $[[1], [2]]$):**
  - Rows or columns have size 1 $\implies$ no interior cells with $i \ge 1, j \ge 1$ exist.
  - Loop does not execute; trivially returns **`true`**.

This instance demonstrates shift-invariance validation on discrete 2D lattices and pairwise local differential testing, mathematically proves why local equality $A_{i,j} = A_{i-1, j-1}$ implies global Toeplitz structure via transitive induction, and derives $O(M \cdot N)$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ matrix:
Determine if it is a **Toeplitz matrix** (every diagonal from top-left to bottom-right has identical elements).

```text
matrix:
  1 2 3 4
  5 1 2 3
  9 5 1 2

Diagonals:
  [1, 1, 1] -> identical
  [2, 2, 2] -> identical
  [3, 3]    -> identical
  [4]       -> identical
  [5, 5]    -> identical
  [9]       -> identical

All diagonals are uniform!
Result: true
```

### The Invariant of the Top-Left Neighbor
- Along any diagonal, each element $(i, j)$ is the direct successor of $(i-1, j-1)$.
- A matrix is Toeplitz if and only if **every cell equals its top-left neighbor**: $matrix[i][j] == matrix[i-1][j-1]$.
- A single nested loop over $i \in [1, m-1], j \in [1, n-1]$ verifies this in $O(M \cdot N)$ time.

---

## 2. Conceptual Foundation & Invariants

### 1. Diagonal Index Relation:
$$
\text{Cell } (i, j) \text{ lies on diagonal } d \iff i - j = d
$$

### 2. Local Differential Predicate:
$$
\text{isToeplitz}(A) \iff \forall i \in [1, m - 1], \; \forall j \in [1, n - 1]: \quad A[i][j] = A[i - 1][j - 1]
$$

> **Toeplitz Operator Shift Invariance.** A linear operator matrix $T \in \mathbb{R}^{m \times n}$ is Toeplitz if and only if $T_{i, j} = a_{i - j}$ for some sequence $a$, which is completely characterized by the commutation relation with shift operators $[S_m, T] = 0$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Row 1
- $(1, 1) = 1 == (0, 0) = 1$ (Match).
- $(1, 2) = 2 == (0, 1) = 2$ (Match).
- $(1, 3) = 3 == (0, 2) = 3$ (Match).

---

### Step 2: Row 2
- $(2, 1) = 5 == (1, 0) = 5$ (Match).
- $(2, 2) = 1 == (1, 1) = 1$ (Match).
- $(2, 3) = 2 == (1, 2) = 2$ (Match).

---

### Step 3: Output
$$
\mathbf{true}
$$

---

## 4. Complete Execution Trace

| Row $i$ | Col $j$ | Current Cell $matrix[i][j]$ | Predecessor Cell $matrix[i-1][j-1]$ | Equality Verified? |
|:---:|:---:|:---:|:---:|:---:|
| $1$ | $1$ | $1$ | $1$ | Yes |
| $1$ | $2$ | $2$ | $2$ | Yes |
| $1$ | $3$ | $3$ | $3$ | Yes |
| $2$ | $1$ | $5$ | $5$ | Yes |
| $2$ | $2$ | $1$ | $1$ | Yes |
| **$2$** | **$3$** | **$2$** | **$2$** | **Yes** |
| **Final** | — | — | — | **Result: `true`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Row Matrix ($1 \times N$):** No cells with $i \ge 1 \implies$ trivially returns `true`.
- **Single Column Matrix ($M \times 1$):** No cells with $j \ge 1 \implies$ trivially returns `true`.
- **Single Element ($1 \times 1$):** Returns `true`.
- **Immediate Mismatch:** Return `false` on the very first mismatch without examining further cells.

---

## 6. Traps & Common Anti-Patterns

- **Collecting and Checking Diagonals with Hash Maps:** Grouping elements by key $i - j$ works but uses $O(M \cdot N)$ extra memory. Comparing each element directly with its top-left predecessor uses strictly $O(1)$ extra space.
- **Checking Bottom-Right and Exceeding Bounds:** Checking `matrix[i][j] == matrix[i+1][j+1]` requires stopping at $m-2$ and $n-2$. Checking backwards `matrix[i][j] == matrix[i-1][j-1]` from $1$ to $m-1$ is cleaner and avoids boundary errors.
- **Large Matrices Loaded in Memory (Follow-Up):** For memory-constrained environments, you only need to keep the previous row in memory and compare the current row against it.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Double loop over $(M - 1) \times (N - 1)$ cells: $\mathcal{O}(M \cdot N)$.
  - Each check is an $\mathcal{O}(1)$ value comparison.
  - Total Time: strictly linear in matrix size $\mathcal{O}(M \cdot N)$. Completes in $< 0.1$ ms for $M, N \le 20$.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (no extra arrays or hash sets).
