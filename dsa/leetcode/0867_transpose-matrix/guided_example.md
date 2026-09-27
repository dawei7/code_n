# Guided Example: Transpose Matrix

We trace the step-by-step linear algebraic matrix reflection across the main diagonal, dimension swapping from $m \times n$ to $n \times m$, coordinate mapping $(i, j) \mapsto (j, i)$, and row-column element relocation on representative rectangular grids:

- **Input:**
  $$
  matrix = \begin{bmatrix}
  1 & 2 & 3 \\
  4 & 5 & 6
  \end{bmatrix}
  $$
- **Required output:**
  $$
  \begin{bmatrix}
  1 & 4 \\
  2 & 5 \\
  3 & 6
  \end{bmatrix}
  $$
  - Transposition rules:
    - Input matrix dimensions: $m = 2$ rows, $n = 3$ columns.
    - The transpose of a matrix $A$ is denoted $A^T$.
    - The rows of the original matrix become the columns of the transposed matrix, and the columns of the original matrix become the rows of the transposed matrix.
    - The dimensions swap: from $m \times n$ ($2 \times 3$) to $n \times m$ ($3 \times 2$).
    - Each cell at row $i$ and column $j$ moves to row $j$ and column $i$:
      $$
      A^T[j][i] = A[i][j]
      $$
- **The Coordinate Transposition Invariant:**
  - **Main Diagonal Invariance:**
    - Cells where $i = j$ ($matrix[0][0]=1$, $matrix[1][1]=5$) remain on the main diagonal ($A^T[0][0]=1$, $A^T[1][1]=5$).
  - **Dimension Inversion for Rectangles:**
    - In non-square matrices ($m \ne n$), in-place transposition is impossible within the same 2D array without completely rewriting the memory layout.
    - We allocate a fresh destination matrix with $n$ rows and $m$ columns.
    - Iterating over all $i \in [0, m - 1]$ and $j \in [0, n - 1]$, each element $matrix[i][j]$ is placed into $result[j][i]$.

---

## 1. Instance & Teaching Goal

Given the $2 \times 3$ matrix:
$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
$$
Derive the step-by-step population of the $3 \times 2$ transposed matrix.

```text
Original Matrix (2x3):
Row 0: [1, 2, 3]  -> becomes Column 0 of Transpose
Row 1: [4, 5, 6]  -> becomes Column 1 of Transpose

Transposed Matrix (3x2):
Row 0: [1, 4]  (Original Column 0)
Row 1: [2, 5]  (Original Column 1)
Row 2: [3, 6]  (Original Column 2)
```

The teaching goal is to show the bijection $(i, j) \longleftrightarrow (j, i)$ across rectangular memory layouts.

---

## 2. Conceptual Foundation & Invariants

### 1. Mathematical Definition:
For an $m \times n$ matrix $A \in \mathbb{R}^{m \times n}$:
$$
A^T \in \mathbb{R}^{n \times m}, \quad (A^T)_{j, i} = A_{i, j} \quad \forall 0 \le i < m, \; 0 \le j < n
$$

### 2. Dual-Loop Iteration Order:
Whether looping outer-row ($i$) and inner-column ($j$) or vice-versa, the mapping is identical:
$$
\text{Write } A^T[j][i] \leftarrow A[i][j]
$$

---

## 3. Step-by-Step Worked Execution

Input dimensions: $m = 2$ rows, $n = 3$ columns.
Initialize result matrix $T$ of dimensions $3 \times 2$:
$$
T = \begin{bmatrix}
\cdot & \cdot \\
\cdot & \cdot \\
\cdot & \cdot
\end{bmatrix}
$$

---

### Step 1: Process Row 0 ($i = 0$)
- **Element $(0, 0) = 1$:**
  - Destination: $T[0][0] \leftarrow 1$.
- **Element $(0, 1) = 2$:**
  - Destination: $T[1][0] \leftarrow 2$.
- **Element $(0, 2) = 3$:**
  - Destination: $T[2][0] \leftarrow 3$.

State of $T$ after Row 0:
$$
\begin{bmatrix}
1 & \cdot \\
2 & \cdot \\
3 & \cdot
\end{bmatrix}
$$

---

### Step 2: Process Row 1 ($i = 1$)
- **Element $(1, 0) = 4$:**
  - Destination: $T[0][1] \leftarrow 4$.
- **Element $(1, 1) = 5$:**
  - Destination: $T[1][1] \leftarrow 5$.
- **Element $(1, 2) = 6$:**
  - Destination: $T[2][1] \leftarrow 6$.

Final Transposed Matrix $T$:
$$
\begin{bmatrix}
1 & 4 \\
2 & 5 \\
3 & 6
\end{bmatrix}
$$

---

## 4. Complete Execution Trace

| Source Row $i$ | Source Column $j$ | Element Value | Target Row $j$ | Target Column $i$ | Target Coordinate |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $0$ | $1$ | $0$ | $0$ | $T[0][0] = 1$ |
| $0$ | $1$ | $2$ | $1$ | $0$ | $T[1][0] = 2$ |
| $0$ | $2$ | $3$ | $2$ | $0$ | $T[2][0] = 3$ |
| $1$ | $0$ | $4$ | $0$ | $1$ | $T[0][1] = 4$ |
| $1$ | $1$ | $5$ | $1$ | $1$ | $T[1][1] = 5$ |
| **$1$** | **$2$** | **$6$** | **$2$** | **$1$** | **$T[2][1] = 6$** |

---

## 5. Boundary Cases & Failure Modes

- **Square Matrix ($m = n$, e.g. $3 \times 3$):** Dimensions remain $3 \times 3$; off-diagonal pairs $(i, j)$ and $(j, i)$ swap.
- **Single Row ($1 \times n$):** Transposes into a column vector of dimension $n \times 1$.
- **Single Column ($m \times 1$):** Transposes into a single row matrix of dimension $1 \times m$.
- **$1 \times 1$ Matrix (`[[x]]`):** Unchanged, returns `[[x]]`.

---

## 6. Traps & Common Anti-Patterns

- **Assuming Square Input:** Attempting in-place swapping (`matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]`) immediately causes an `IndexError` when $m \ne n$ because row lengths differ from column heights.
- **Shallow Copy of Row Lists:** Reusing row references causes mutations across multiple rows. Always instantiate fresh rows for the destination matrix.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Every element of the $m \times n$ matrix is read and written exactly once: $\mathcal{O}(m \cdot n)$.
  - Total Time: strictly $\mathcal{O}(m \cdot n)$, executing in $< 2$ ms for $m, n \le 1000$.
- **Auxiliary Space Complexity:**
  - Storing the output transposed matrix of size $n \times m$: $\mathcal{O}(m \cdot n)$ space.
