# Guided Example: Reshape the Matrix

We trace the step-by-step capacity compatibility verification ($m \cdot n == r \cdot c$), fallback identity preservation, 1D virtual flattening mapping ($i \in [0, m \cdot n - 1]$), quotient-remainder row/column coordinate projection ($i // c, i \pmod c$), and row-major matrix reconstruction on representative grid instances:

- **Input:**
  $$
  mat = \begin{bmatrix}
  1 & 2 \\
  3 & 4
  \end{bmatrix}, \quad r = 1, \quad c = 4
  $$
- **Required output:**
  $$
  ans = \begin{bmatrix} 1 & 2 & 3 & 4 \end{bmatrix}
  $$
  - Problem contract:
    - Input dimensions: $m = 2$ rows, $n = 2$ columns. Total elements: $m \cdot n = 4$.
    - Desired dimensions: $r = 1$ row, $c = 4$ columns. Total requested capacity: $r \cdot c = 4$.
    - Rule: The elements must be transferred in **row-major order** (left to right, row by row).
    - If $m \cdot n \ne r \cdot c$, the operation is invalid and the **original matrix** must be returned unmodified.
- **Bijective Index Projection Trace:**
  - **Step 1: Check Capacity Compatibility:**
    $$
    m \cdot n = 2 \times 2 = 4
    $$
    $$
    r \cdot c = 1 \times 4 = 4
    $$
    Since $4 == 4$, the reshape is valid!
  - **Step 2: Initialize Reshaped Matrix of Size $r \times c = 1 \times 4$:**
    $$
    ans = \begin{bmatrix} 0 & 0 & 0 & 0 \end{bmatrix}
    $$
  - **Step 3: Map Each 1D Linear Index $i \in [0, 3]$:**
    - Any flattened index $i$ corresponds to:
      - Source cell: $(\lfloor i / n \rfloor, \; i \pmod n) = (\lfloor i / 2 \rfloor, \; i \pmod 2)$
      - Target cell: $(\lfloor i / c \rfloor, \; i \pmod c) = (\lfloor i / 4 \rfloor, \; i \pmod 4)$
    - **Linear Index $i = 0$:**
      - Source: $(\lfloor 0 / 2 \rfloor, 0 \pmod 2) = (0, 0) \implies mat[0][0] = \mathbf{1}$.
      - Target: $(\lfloor 0 / 4 \rfloor, 0 \pmod 4) = (0, 0)$.
      - Assignment: $ans[0][0] \leftarrow 1$.
    - **Linear Index $i = 1$:**
      - Source: $(\lfloor 1 / 2 \rfloor, 1 \pmod 2) = (0, 1) \implies mat[0][1] = \mathbf{2}$.
      - Target: $(\lfloor 1 / 4 \rfloor, 1 \pmod 4) = (0, 1)$.
      - Assignment: $ans[0][1] \leftarrow 2$.
    - **Linear Index $i = 2$:**
      - Source: $(\lfloor 2 / 2 \rfloor, 2 \pmod 2) = (1, 0) \implies mat[1][0] = \mathbf{3}$.
      - Target: $(\lfloor 2 / 4 \rfloor, 2 \pmod 4) = (0, 2)$.
      - Assignment: $ans[0][2] \leftarrow 3$.
    - **Linear Index $i = 3$:**
      - Source: $(\lfloor 3 / 2 \rfloor, 3 \pmod 2) = (1, 1) \implies mat[1][1] = \mathbf{4}$.
      - Target: $(\lfloor 3 / 4 \rfloor, 3 \pmod 4) = (0, 3)$.
      - Assignment: $ans[0][3] \leftarrow 4$.
  - All 4 elements transferred in exact order.
  - Final reshaped matrix:
    $$
    ans = \begin{bmatrix} 1 & 2 & 3 & 4 \end{bmatrix}
    $$
- **Incompatible Shape Instance ($mat = [[1, 2], [3, 4]], r = 2, c = 4$):**
  - Original size: $2 \times 2 = 4$.
  - Requested size: $2 \times 4 = 8$.
  - $4 \ne 8 \implies$ Reshape impossible $\implies$ returns original $mat = [[1, 2], [3, 4]]$ directly!
- **Column Vector Reshape ($r = 4, c = 1$):**
  - Reshapes into a vertical column: $[[1], [2], [3], [4]]$.

This instance demonstrates Euclidean division coordinate transformations on multidimensional tensors, mathematically proves why quotient and remainder operations preserve row-major traversal invariants, and derives $O(M \cdot N)$ runtime and $O(M \cdot N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ matrix $mat$ and target dimensions $r, c$:
Reshape the matrix to size $r \times c$ while preserving **row-major order**.
If the reshape is impossible ($m \cdot n \ne r \cdot c$), return the original matrix.

```text
Original Matrix (2 x 2):
  [ 1,  2 ]
  [ 3,  4 ]
Flattened: [ 1,  2,  3,  4 ]

Target Shape (1 x 4):
  [ 1,  2,  3,  4 ]
```

### The Invariant of Euclidean Index Mapping
- Instead of physically flattening the matrix into a temporary 1D list and then slicing it into rows:
  We can perform direct mathematical projection in $O(1)$ auxiliary space per element!
- For any index $i \in [0, \text{Total} - 1]$:
  $$
  \text{Row} = \lfloor i / \text{Cols} \rfloor, \quad \text{Col} = i \pmod{\text{Cols}}
  $$
- This maps the 1D rank to 2D coordinates seamlessly for any arbitrary dimension pair.

---

## 2. Conceptual Foundation & Invariants

### 1. Validity Check:
$$
\text{Valid} \iff m \cdot n == r \cdot c
$$
If false, return $mat$ immediately.

### 2. Dual Coordinate Projection Formula:
For linear index $i \in [0, m \cdot n - 1]$:
$$
ans[\lfloor i / c \rfloor][i \pmod c] = mat[\lfloor i / n \rfloor][i \pmod n]
$$

> **Bijective Ordering Invariant.** Because $\lfloor i / k \rfloor \cdot k + (i \pmod k) = i$ is an exact bijection from $\mathbb{Z}_{mn} \to \mathbb{Z}_m \times \mathbb{Z}_n$, traversing $i$ monotonically preserves the row-major ordering across arbitrary tensor geometries.

---

## 3. Step-by-Step Worked Execution

We trace $mat = [[1, 2], [3, 4]]$ with $r = 1, c = 4$:

---

### Step 1: Validate
- $m = 2, n = 2 \implies m \cdot n = 4$.
- $r = 1, c = 4 \implies r \cdot c = 4$.
- $4 == 4 \implies$ Valid.

---

### Step 2: Allocate Target Grid
$$
ans = [[0, 0, 0, 0]]
$$

---

### Step 3: Loop $i \in [0, 3]$
- $i = 0$:
  - $mat[0 // 2][0 \% 2] = mat[0][0] = 1$
  - $ans[0 // 4][0 \% 4] = ans[0][0] \leftarrow 1$
- $i = 1$:
  - $mat[1 // 2][1 \% 2] = mat[0][1] = 2$
  - $ans[1 // 4][1 \% 4] = ans[0][1] \leftarrow 2$
- $i = 2$:
  - $mat[2 // 2][2 \% 2] = mat[1][0] = 3$
  - $ans[2 // 4][2 \% 4] = ans[0][2] \leftarrow 3$
- $i = 3$:
  - $mat[3 // 2][3 \% 2] = mat[1][1] = 4$
  - $ans[3 // 4][3 \% 4] = ans[0][3] \leftarrow 4$

---

### Step 4: Final Output
$$
ans = [[1, 2, 3, 4]]
$$

---

## 4. Complete Execution Trace

| 1D Index $i$ | Source Coordinates $(\lfloor i/2 \rfloor, i \% 2)$ | Value $mat$ | Target Coordinates $(\lfloor i/4 \rfloor, i \% 4)$ | Target Grid Row 0 |
|:---:|:---:|:---:|:---:|:---:|
| $0$ | $(0, 0)$ | **$1$** | $(0, 0)$ | `[1, 0, 0, 0]` |
| $1$ | $(0, 1)$ | **$2$** | $(0, 1)$ | `[1, 2, 0, 0]` |
| $2$ | $(1, 0)$ | **$3$** | $(0, 2)$ | `[1, 2, 3, 0]` |
| $3$ | $(1, 1)$ | **$4$** | $(0, 3)$ | **`[1, 2, 3, 4]`** |
| **Result** | — | — | — | **`[[1, 2, 3, 4]]`** |

---

## 5. Boundary Cases & Failure Modes

- **Incompatible Capacity ($2 \times 2 \to 2 \times 4$):** $4 \ne 8 \implies$ early exit returns original `mat`.
- **Identity Reshape ($r = m, c = n$):** Copies elements to identical positions without error.
- **Flatten to Single Row ($1 \times (m \cdot n)$):** Creates a single row vector.
- **Reshape to Single Column ($(m \cdot n) \times 1$):** Creates a vertical list of 1-element rows.

---

## 6. Traps & Common Anti-Patterns

- **Returning an Empty Matrix on Mismatch:** When $m \cdot n \ne r \cdot c$, the requirement is to return the **original matrix `mat`**, not `[]` or `None`.
- **Dividing by Target Rows Instead of Columns:** In coordinate projection, the column count determines stride and wrap-around. Dividing by $r$ instead of $c$ transposes the coordinates.
- **Using Column-Major (Fortran) Order:** The problem specifies row-major (C-style) traversal.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Checking dimensions takes $\mathcal{O}(1)$ time.
  - Transferring $M \cdot N$ elements takes $\mathcal{O}(M \cdot N)$ operations.
  - Total Time: strictly linear $\mathcal{O}(M \cdot N)$. For $10^4$ elements, completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ space to store the output reshaped matrix.
