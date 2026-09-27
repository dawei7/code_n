# Guided Example: Sparse Matrix Multiplication

We trace the step-by-step sparse matrix product evaluation, inner product dimension matching ($M \times K$ by $K \times N \to M \times N$), zero-skipping computational savings, and cell accumulator aggregation on representative sparse matrix instances:

- **Input:**
  $$
  \text{mat1} = \begin{bmatrix}
  1 & 0 & 0 \\
  -1 & 0 & 3
  \end{bmatrix}, \quad
  \text{mat2} = \begin{bmatrix}
  7 & 0 & 0 \\
  0 & 0 & 0 \\
  0 & 0 & 1
  \end{bmatrix}
  $$
- **Required output:**
  $$
  \text{ans} = \begin{bmatrix}
  7 & 0 & 0 \\
  -7 & 0 & 3
  \end{bmatrix}
  $$
  - Cell $(0, 0)$: $1 \times 7 + 0 \times 0 + 0 \times 0 = 7$
  - Cell $(1, 0)$: $(-1) \times 7 + 0 \times 0 + 3 \times 0 = -7$
  - Cell $(1, 2)$: $(-1) \times 0 + 0 \times 0 + 3 \times 1 = 3$
  - All other cells evaluate to $0$
- **All-Zero Matrix Multiplication:** Multiplying by a zero matrix immediately produces an $M \times N$ zero matrix
- **Identity Matrix Multiplier:** Multiplying by an identity matrix preserves the original matrix values exactly
- **Negative Sign Cancellation:** Opposing products cancel to $0$ without violating arithmetic soundness

This instance demonstrates matrix dot-product accumulation, proves how the inner dimension $K$ aligns row slices with column vectors, contrasts naive $O(M N K)$ multiplication against sparse index skipping, and operates in $O(M N)$ output auxiliary space.

---

## 1. Instance & Teaching Goal

Given two matrices:
- $\text{mat1}$ of dimensions $M \times K = 2 \times 3$
- $\text{mat2}$ of dimensions $K \times N = 3 \times 3$

Compute the matrix product $\text{ans} = \text{mat1} \times \text{mat2}$ of dimensions $M \times N = 2 \times 3$:
$$
\text{ans}[i][j] = \sum_{k=0}^{K-1} \text{mat1}[i][k] \times \text{mat2}[k][j]
$$

```text
mat1 (2x3):             mat2 (3x3):
[ 1, 0, 0 ]             [ 7, 0, 0 ]
[-1, 0, 3 ]             [ 0, 0, 0 ]
                        [ 0, 0, 1 ]

Computation for ans[0][0]:
Row 0 of mat1: [1, 0, 0]
Col 0 of mat2: [7, 0, 0]
Dot product: 1*7 + 0*0 + 0*0 = 7

Computation for ans[1][0]:
Row 1 of mat1: [-1, 0, 3]
Col 0 of mat2: [7,  0, 0]
Dot product: (-1)*7 + 0*0 + 3*0 = -7

Computation for ans[1][2]:
Row 1 of mat1: [-1, 0, 3]
Col 2 of mat2: [0,  0, 1]
Dot product: (-1)*0 + 0*0 + 3*1 = 3
```

### Exploiting Sparsity in Matrix Multiplication
In standard matrix multiplication, $M \times N \times K$ multiplications and additions are performed.
When matrices are **sparse** (most elements are $0$):
- If $\text{mat1}[i][k] == 0$, the entire product $\text{mat1}[i][k] \times \text{mat2}[k][j]$ is $0$ for all $j \in [0, N - 1]$.
- Reordering loops as $i \to k \to j$ allows testing `if mat1[i][k] != 0` before the inner column loop, bypassing thousands of redundant arithmetic operations!

---

## 2. Conceptual Foundation & Invariants

### Output Matrix Dimensions:
- Let $M = \text{len}(\text{mat1})$ (Number of rows in result).
- Let $N = \text{len}(\text{mat2}[0])$ (Number of columns in result).
- Let $K = \text{len}(\text{mat2}) = \text{len}(\text{mat1}[0])$ (Shared inner dimension).
- Initialize $\text{ans}$ as an $M \times N$ matrix of zeros: `[[0] * n for _ in range(m)]`.

### Triple Loop Multiplication Protocol:
For each row $i \in [0, M - 1]$:
  For each shared index $k \in [0, K - 1]$:
    If $\text{mat1}[i][k] \ne 0$:
      For each column $j \in [0, N - 1]$:
        If $\text{mat2}[k][j] \ne 0$:
          $$
          \text{ans}[i][j] \leftarrow \text{ans}[i][j] + \text{mat1}[i][k] \times \text{mat2}[k][j]
          $$

> **Invariant.** At the end of the iterations, $\text{ans}[i][j]$ is the exact inner product of row $i$ of $\text{mat1}$ and column $j$ of $\text{mat2}$.

---

## 3. Step-by-Step Worked Execution

We trace the matrix multiplication on $\text{mat1} \; (2 \times 3)$ and $\text{mat2} \; (3 \times 3)$:
Output grid size: $2 \times 3$, initialized to all zeros.

---

### Row $i = 0$: $\text{mat1}[0] = [1, 0, 0]$
- **$k = 0$ ($\text{mat1}[0][0] = 1 \ne 0$):**
  Inspect Row $k = 0$ of $\text{mat2}$: $[7, 0, 0]$.
  - $j = 0$: $\text{mat2}[0][0] = 7 \implies \text{ans}[0][0] \mathrel{+}= 1 \times 7 = \mathbf{7}$.
  - $j = 1$: $\text{mat2}[0][1] = 0 \implies \text{No-op}$.
  - $j = 2$: $\text{mat2}[0][2] = 0 \implies \text{No-op}$.
- **$k = 1$ ($\text{mat1}[0][1] = 0$):**
  Zero multiplier! Entire loop over $j$ skipped.
- **$k = 2$ ($\text{mat1}[0][2] = 0$):**
  Zero multiplier! Skipped.

Row 0 result: $\text{ans}[0] = [7, 0, 0]$.

---

### Row $i = 1$: $\text{mat1}[1] = [-1, 0, 3]$
- **$k = 0$ ($\text{mat1}[1][0] = -1 \ne 0$):**
  Inspect Row $k = 0$ of $\text{mat2}$: $[7, 0, 0]$.
  - $j = 0$: $\text{mat2}[0][0] = 7 \implies \text{ans}[1][0] \mathrel{+}= (-1) \times 7 = \mathbf{-7}$.
  - $j = 1$: $\text{mat2}[0][1] = 0 \implies \text{No-op}$.
  - $j = 2$: $\text{mat2}[0][2] = 0 \implies \text{No-op}$.
- **$k = 1$ ($\text{mat1}[1][1] = 0$):**
  Zero multiplier! Skipped.
- **$k = 2$ ($\text{mat1}[1][2] = 3 \ne 0$):**
  Inspect Row $k = 2$ of $\text{mat2}$: $[0, 0, 1]$.
  - $j = 0$: $\text{mat2}[2][0] = 0 \implies \text{No-op}$.
  - $j = 1$: $\text{mat2}[2][1] = 0 \implies \text{No-op}$.
  - $j = 2$: $\text{mat2}[2][2] = 1 \implies \text{ans}[1][2] \mathrel{+}= 3 \times 1 = \mathbf{3}$.

Row 1 result: $\text{ans}[1] = [-7, 0, 3]$.

---

### Completed Multiplication
Output matrix:
$$
\mathbf{\begin{bmatrix}
7 & 0 & 0 \\
-7 & 0 & 3
\end{bmatrix}}
$$

---

## 4. Complete Execution Trace

```text
mat1: [[1, 0, 0], [-1, 0, 3]]
mat2: [[7, 0, 0], [0, 0, 0], [0, 0, 1]]

i = 0:
  k = 0 (val = 1):  j = 0 -> ans[0][0] += 1 * 7 = 7
  k = 1 (val = 0):  skipped
  k = 2 (val = 0):  skipped
i = 1:
  k = 0 (val = -1): j = 0 -> ans[1][0] += -1 * 7 = -7
  k = 1 (val = 0):  skipped
  k = 2 (val = 3):  j = 2 -> ans[1][2] += 3 * 1 = 3

Final Result:
[[7, 0, 0],
 [-7, 0, 3]]
```

| Output Cell $(i, j)$ | Row Vector of $\text{mat1}$ | Column Vector of $\text{mat2}$ | Non-Zero Multiplications | Computed Cell Value |
|:---:|:---:|:---:|:---|:---:|
| **$(0, 0)$** | $[1, 0, 0]$ | $[7, 0, 0]^T$ | $1 \times 7 = 7$ | **7** |
| $(0, 1)$ | $[1, 0, 0]$ | $[0, 0, 0]^T$ | None | **0** |
| $(0, 2)$ | $[1, 0, 0]$ | $[0, 0, 1]^T$ | None | **0** |
| **$(1, 0)$** | $[-1, 0, 3]$ | $[7, 0, 0]^T$ | $(-1) \times 7 = -7$ | **-7** |
| $(1, 1)$ | $[-1, 0, 3]$ | $[0, 0, 0]^T$ | None | **0** |
| **$(1, 2)$** | $[-1, 0, 3]$ | $[0, 0, 1]^T$ | $3 \times 1 = 3$ | **3** |

---

## 5. Algorithmic Correctness

**Soundness.** Linear algebra defines the matrix product entry $(i, j)$ as the scalar dot product of row $i$ of the first matrix and column $j$ of the second matrix. The triple loop computes $\sum_{k=0}^{K-1} \text{mat1}[i][k] \times \text{mat2}[k][j]$. Skipping indices where either factor is zero leaves the summation mathematically identical because $0 \times x = 0$.

**Completeness.** Every pair of rows $i \in [0, M-1]$ and columns $j \in [0, N-1]$ is evaluated across all shared indices $k \in [0, K-1]$. No non-zero component is omitted, guaranteeing the product matrix is completely and accurately formed.

---

## 6. Traps This Instance Exposes

- **Memory Aliasing in Python:** Initializing a 2D matrix with `[[0] * n] * m` creates $m$ references to the **same** underlying list, causing an update to `ans[0][0]` to overwrite all rows simultaneously. Independent rows must be instantiated via list comprehension: `[[0] * n for _ in range(m)]`.
- **Inefficient Loop Ordering:** The classical $i \to j \to k$ loop order prevents skipping row zeros effectively because $j$ changes on the second loop. Ordering as $i \to k \to j$ allows testing $\text{mat1}[i][k] \ne 0$ once and skipping the entire $N$-element inner loop.
- **Negative Sign Arithmetic:** Multiplying negative values (e.g. $-1 \times 7 = -7$) and adding terms of opposite signs must preserve exact signed arithmetic.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot N \cdot K)$ in the worst-case dense setting. With sparsity skipping ($i \to k \to j$), runtime is bounded by $O(M \cdot K + \text{nnz}(\text{mat1}) \cdot N)$ where $\text{nnz}$ is the number of non-zero entries. If $\text{mat1}$ has density $\rho_1 \ll 1$, operations drop by a factor of $\rho_1$.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary memory (excluding the required $M \times N$ output matrix `ans`).
