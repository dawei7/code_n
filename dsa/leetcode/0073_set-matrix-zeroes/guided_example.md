# Guided Example: Set Matrix Zeroes

We trace the step-by-step in-place $O(1)$ auxiliary space matrix zeroing algorithm on a representative 2D matrix:

- **Input:** $\text{matrix} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 1 \end{pmatrix}$
- **Required output:** $\begin{pmatrix} 1 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 1 \end{pmatrix}$

This instance demonstrates reusing the matrix's first row and first column as internal zero-marker registers, protecting the $(0, 0)$ intersection via separate boundary flags, zeroing interior cells, and finalizing outer boundaries in strictly $O(1)$ extra space.

---

## 1. Instance & Teaching Goal

Given an $M \times N$ integer matrix ($M = 3, N = 3$), if any cell contains `0`, set its entire row and column to `0`'s. The operation must be performed **in place**.

For the input:
$$
\begin{pmatrix}
1 & 1 & 1 \\
1 & \mathbf{0} & 1 \\
1 & 1 & 1
\end{pmatrix}
$$
Because cell $(1, 1)$ is `0`, all elements in Row 1 and Column 1 must become `0`.

A naive algorithm that zeroes rows and columns immediately upon seeing a zero triggers a runaway cascade, turning the entire matrix into zeros.
Allocating separate row and column boolean arrays requires $O(M + N)$ auxiliary memory.
The optimal algorithm stores zero markers directly inside $\text{matrix}[r][0]$ and $\text{matrix}[0][c]$ (the first column and first row), requiring only two boolean flags for $O(1)$ extra space.

---

## 2. Conceptual Foundation & Invariants

### In-Place Header Marker Protocol
The top-left cell $(0, 0)$ belongs to both the first row and first column. To resolve this collision:
- Use a boolean flag `first_row_zero` to track if Row 0 originally contained any zeros.
- Use a boolean flag `first_col_zero` to track if Column 0 originally contained any zeros.
- Use $\text{matrix}[r][0]$ to indicate whether interior row $r \ge 1$ should be zeroed.
- Use $\text{matrix}[0][c]$ to indicate whether interior column $c \ge 1$ should be zeroed.

### 4-Phase Algorithm
1. **Initial Boundary Scan:**
   - Check if any cell in Row 0 is 0: `first_row_zero = any(matrix[0][c] == 0)`.
   - Check if any cell in Col 0 is 0: `first_col_zero = any(matrix[r][0] == 0)`.
2. **Interior Flagging:**
   For each $r \in [1, M - 1]$ and $c \in [1, N - 1]$:
   - If $\text{matrix}[r][c] == 0$:
     $$
     \text{matrix}[r][0] \leftarrow 0, \quad \text{matrix}[0][c] \leftarrow 0
     $$
3. **Interior Zeroing:**
   For each $r \in [1, M - 1]$ and $c \in [1, N - 1]$:
   - If $\text{matrix}[r][0] == 0$ or $\text{matrix}[0][c] == 0$:
     $$
     \text{matrix}[r][c] \leftarrow 0
     $$
4. **Header Line Zeroing:**
   - If `first_row_zero`: set $\text{matrix}[0][c] \leftarrow 0$ for all $c \in [0, N - 1]$.
   - If `first_col_zero`: set $\text{matrix}[r][0] \leftarrow 0$ for all $r \in [0, M - 1]$.

> **Invariant.** After Phase 2, $\text{matrix}[r][0] == 0 \iff$ original row $r$ had a zero, and $\text{matrix}[0][c] == 0 \iff$ original column $c$ had a zero.

---

## 3. Step-by-Step Worked Execution

We trace the $3 \times 3$ matrix:

### Phase 1: Boundary Flags
- Row 0: `[1, 1, 1]` $\implies \text{first\_row\_zero} = \text{False}$.
- Col 0: `[1, 1, 1]` $\implies \text{first\_col\_zero} = \text{False}$.

---

### Phase 2: Interior Scan ($r \in [1, 2], c \in [1, 2]$)
- Cell $(1, 1)$: Value is `0`!
  - Record zero in row marker: $\text{matrix}[1][0] \leftarrow 0$.
  - Record zero in col marker: $\text{matrix}[0][1] \leftarrow 0$.
- Cell $(1, 2)$: Value is `1`.
- Cell $(2, 1)$: Value is `1`.
- Cell $(2, 2)$: Value is `1`.

Matrix after Phase 2 (Markers in Row 0 and Col 0):
$$
\begin{pmatrix}
1 & \mathbf{0} & 1 \\
\mathbf{0} & 0 & 1 \\
1 & 1 & 1
\end{pmatrix}
$$

---

### Phase 3: Interior Zeroing ($r \in [1, 2], c \in [1, 2]$)
- Cell $(1, 1)$: Row marker $\text{matrix}[1][0] == 0 \implies \text{matrix}[1][1] = 0$.
- Cell $(1, 2)$: Row marker $\text{matrix}[1][0] == 0 \implies \text{matrix}[1][2] = 0$.
- Cell $(2, 1)$: Col marker $\text{matrix}[0][1] == 0 \implies \text{matrix}[2][1] = 0$.
- Cell $(2, 2)$: Row marker $\text{matrix}[2][0] == 1$ and col marker $\text{matrix}[0][2] == 1 \implies$ unchanged (`1`).

Matrix after Phase 3:
$$
\begin{pmatrix}
1 & 0 & 1 \\
0 & 0 & 0 \\
1 & 0 & 1
\end{pmatrix}
$$

---

### Phase 4: Header Finalization
- `first_row_zero` is False: Row 0 remains `[1, 0, 1]`.
- `first_col_zero` is False: Column 0 remains `[1, 0, 1]`.

Output matrix:
$$
\begin{pmatrix}
1 & 0 & 1 \\
0 & 0 & 0 \\
1 & 0 & 1
\end{pmatrix}
$$

---

### Corner Collision Trace: A Zero at $(0, 0)$

The instance above never exercises the boundary flags, so the collision at the shared corner deserves its own trace. Take the $2 \times 2$ input $\begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$, where the single zero sits exactly on $(0, 0)$ — the cell that both a row marker and a column marker would want to occupy.

| Phase | Boundary flags | Interior markers $\text{matrix}[1][0]$, $\text{matrix}[0][1]$ | Matrix after the phase |
|:---:|:---|:---:|:---:|
| 1 | `first_row_zero = True`, `first_col_zero = True` | Not yet written; both still `1` | $\begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$ |
| 2 | Unchanged | Cell $(1, 1) = 1$ is non-zero, so both markers stay `1` | $\begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$ |
| 3 | Unchanged | Consulted for $(1, 1)$; neither marker equals `0`, so the interior cell keeps `1` | $\begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$ |
| 4 | Both True | Header lines are overwritten by the two flags | $\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ |

The final matrix is correct because the zero at $(0, 0)$ means Row 0 must be cleared and Column 0 must be cleared, while cell $(1, 1)$ lies in neither of those lines and survives as `1`. The corner cell alone cannot express that, since reading it as a row marker and reading it as a column marker return the same bit; the two scalars are what keep the two facts separate and prevent the algorithm from inventing a zero in a row or column that never had one.

---

## 4. Complete Execution Trace

| Phase | Affected Indices | Condition / Value | Action Taken | Matrix Configuration |
|:---:|:---:|:---:|:---|:---:|
| 1 | Row 0, Col 0 | No zeroes present | Set both boundary flags = False | Initial matrix |
| 2 | Cell $(1, 1)$ | Original zero found | Set $\text{matrix}[1][0] = 0$, $\text{matrix}[0][1] = 0$ | $\begin{pmatrix} 1 & 0 & 1 \\ 0 & 0 & 1 \\ 1 & 1 & 1 \end{pmatrix}$ |
| 3 | Cells $(1, 1), (1, 2)$ | Row marker 1 is 0 | Set row 1 interior cells to 0 | - |
| 3 | Cell $(2, 1)$ | Col marker 1 is 0 | Set col 1 interior cells to 0 | $\begin{pmatrix} 1 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 1 \end{pmatrix}$ |
| 4 | Boundary headers | Flags are False | Keep headers intact | **Final Output** |

---

## 5. Algorithmic Correctness

**Soundness.** Because Phase 2 only updates Row 0 and Column 0, and Phase 3 reads markers strictly from Row 0 and Column 0 without writing to them, no false secondary zero markers can ever be generated.

**Completeness.** Every interior cell $(r, c)$ is zeroed if and only if either its row marker or its column marker was set in Phase 2. The boundary flags independently preserve the initial state of Row 0 and Column 0.

---

## 6. Traps This Instance Exposes

- **Cascade Zeroing (Premature Writes):** If you overwrite elements as you discover zeros, a newly written zero will subsequently cause its entire row and column to be zeroed, rapidly turning valid non-zero rows into zeros.
- **Header Order Inversion:** Phase 4 must execute **after** Phase 3. If Row 0 or Column 0 is zeroed first, all interior row/column markers would become 0, causing Phase 3 to mistakenly zero out the entire matrix.
- **Matrix Dimensions $1 \times 1$:** When $M = 1$ or $N = 1$, the interior loops execute zero times, and the boundary flags handle the single row/column safely.

---

## 7. Complexity Derivation

### Variant Comparison

Every variant below makes the same final decision — clear a row or column exactly when the original matrix put a zero in it — and differs only in where the evidence is stored.

| Approach | Where the zero evidence lives | Time | Auxiliary space | Failure mode |
|:---|:---|:---|:---|:---|
| Immediate zeroing during the scan | Nowhere; the matrix is mutated on sight | $O(M \cdot N \cdot (M + N))$ | $O(1)$ | Each freshly written zero becomes new evidence, so the matrix cascades to all zeros |
| Boolean row and column arrays | Two separate vectors of length $M$ and $N$ | $O(M \cdot N)$ | $O(M + N)$ | Correct, but the extra vectors breach a strict in-place contract |
| Recorded zero coordinates | A list of $(r, c)$ pairs | $O(M \cdot N)$ | $O(M \cdot N)$ in the worst case | Every cell of an all-zero matrix is stored, so memory scales with the number of zeros |
| First row and first column as markers (used here) | The matrix headers themselves, plus two scalars for the $(0, 0)$ collision | $O(M \cdot N)$ | $O(1)$ | Phase 4 must run strictly after Phase 3, and the corner facts must ride in the flags rather than in $\text{matrix}[0][0]$ |

- **Time Complexity:** $O(M \cdot N)$, where $M$ is the number of rows and $N$ is the number of columns. Exactly two passes over the matrix are performed.
- **Auxiliary Space Complexity:** $O(1)$. All markings are stored in place using the matrix itself, using two boolean scalar flags for boundary headers.
