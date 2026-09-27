# Guided Example: Rotate Image

We trace the step-by-step execution of in-place 2D matrix clockwise rotation on a representative grid instance:

- **Input:** $\text{matrix} = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$
- **Required output:** $\begin{pmatrix} 7 & 4 & 1 \\ 8 & 5 & 2 \\ 9 & 6 & 3 \end{pmatrix}$

This instance demonstrates in-place $O(1)$-space coordinate rotation, factoring 90-degree clockwise rotation into matrix transposition followed by horizontal row reversal, and the equivalent 4-element concentric ring cycle permutation.

---

## 1. Instance & Teaching Goal

Given an $N \times N$ 2D matrix representing an image where $N = 3$, rotate the image by 90 degrees clockwise in place. The modification must be performed directly on the input array without allocating a second matrix.

In an $N \times N$ matrix, a $90^\circ$ clockwise rotation maps coordinate $(r, c)$ to:
$$
(r, c) \longmapsto (c, N - 1 - r)
$$
Directly assigning $\text{matrix}[c][N - 1 - r] = \text{matrix}[r][c]$ would overwrite elements before their original values can be moved. The optimal in-place method decomposes the rotation into two elementary geometric reflections:
1. **Transpose:** Reflect across the main diagonal: $(r, c) \mapsto (c, r)$.
2. **Reflect Horizontally:** Reverse each row from left to right: $(c, r) \mapsto (c, N - 1 - r)$.

Both steps operate strictly in place using scalar element swaps.

---

## 2. Conceptual Foundation & Invariants

### Mathematical Decomposition
Let $T$ be matrix transposition and $R$ be horizontal reflection:
$$
\text{Rotation}_{90^\circ} = R \circ T
$$

1. **Step 1: Transposition ($A \mapsto A^T$):**
   For all $r \in [0, N-1]$ and $c \in [r + 1, N-1]$:
   $$
   \text{Swap}(\text{matrix}[r][c], \, \text{matrix}[c][r])
   $$
   *(Only elements strictly above the main diagonal are swapped with their symmetrical counterparts below to avoid swapping back).*

2. **Step 2: Horizontal Row Inversion:**
   For each row $r \in [0, N-1]$ and column $c \in [0, \lfloor N/2 \rfloor - 1]$:
   $$
   \text{Swap}(\text{matrix}[r][c], \, \text{matrix}[r][N - 1 - c])
   $$

### Alternative: 4-Way Concentric Ring Permutation
Each coordinate belongs to a 4-cycle of elements rotating into each other:
$$
(r, c) \to (c, N - 1 - r) \to (N - 1 - r, N - 1 - c) \to (N - 1 - c, r) \to (r, c)
$$
Saving one temporary variable allows rotating all 4 corners simultaneously.

> **Invariant.** After transposition, rows and columns are swapped. After row reversal, columns appear in reverse order, achieving an exact $90^\circ$ clockwise orientation.

---

## 3. Step-by-Step Worked Execution

We rotate the $3 \times 3$ matrix:
$$
\text{Initial} = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}
$$

### Phase 1: Transposition (Swap Across Main Diagonal)
Elements on the diagonal ($\text{matrix}[0][0]=1, \text{matrix}[1][1]=5, \text{matrix}[2][2]=9$) remain invariant.

- **Cell $(0, 1) \leftrightarrow (1, 0)$:** Swap value $2$ with value $4$.
  - Matrix becomes:
    $$
    \begin{pmatrix} 1 & \mathbf{4} & 3 \\ \mathbf{2} & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}
    $$
- **Cell $(0, 2) \leftrightarrow (2, 0)$:** Swap value $3$ with value $7$.
  - Matrix becomes:
    $$
    \begin{pmatrix} 1 & 4 & \mathbf{7} \\ 2 & 5 & 6 \\ \mathbf{3} & 8 & 9 \end{pmatrix}
    $$
- **Cell $(1, 2) \leftrightarrow (2, 1)$:** Swap value $6$ with value $8$.
  - Matrix becomes:
    $$
    A^T = \begin{pmatrix} 1 & 4 & 7 \\ 2 & 5 & 8 \\ 3 & 6 & 9 \end{pmatrix}
    $$

Transposition complete. Notice that original rows $[1, 2, 3], [4, 5, 6], [7, 8, 9]$ are now columns!

---

### Phase 2: Horizontal Row Reversal
Reverse each of the 3 rows ($c$ from $0$ to $\lfloor 3/2 \rfloor - 1 = 0$):

- **Row 0 ($[1, 4, 7]$):** Swap $\text{matrix}[0][0]=1$ with $\text{matrix}[0][2]=7$.
  - Row 0 becomes: $[7, 4, 1]$.
- **Row 1 ($[2, 5, 8]$):** Swap $\text{matrix}[1][0]=2$ with $\text{matrix}[1][2]=8$.
  - Row 1 becomes: $[8, 5, 2]$.
- **Row 2 ($[3, 6, 9]$):** Swap $\text{matrix}[2][0]=3$ with $\text{matrix}[2][2]=9$.
  - Row 2 becomes: $[9, 6, 3]$.

Final matrix:
$$
\begin{pmatrix} 7 & 4 & 1 \\ 8 & 5 & 2 \\ 9 & 6 & 3 \end{pmatrix}
$$

Rotation complete in place.

---

## 4. Complete Execution Trace

| Phase | Operation | Coordinates Swapped | Values Exchanged | Resulting Matrix State |
|:---:|:---|:---:|:---:|:---|
| Start | Initial State | - | - | `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` |
| Transpose | Upper/Lower Swap | $(0, 1) \leftrightarrow (1, 0)$ | $2 \leftrightarrow 4$ | `[[1, 4, 3], [2, 5, 6], [7, 8, 9]]` |
| Transpose | Upper/Lower Swap | $(0, 2) \leftrightarrow (2, 0)$ | $3 \leftrightarrow 7$ | `[[1, 4, 7], [2, 5, 6], [3, 8, 9]]` |
| Transpose | Upper/Lower Swap | $(1, 2) \leftrightarrow (2, 1)$ | $6 \leftrightarrow 8$ | `[[1, 4, 7], [2, 5, 8], [3, 6, 9]]` ($A^T$) |
| Reversal | Row 0 Reverse | $(0, 0) \leftrightarrow (0, 2)$ | $1 \leftrightarrow 7$ | Row 0: `[7, 4, 1]` |
| Reversal | Row 1 Reverse | $(1, 0) \leftrightarrow (1, 2)$ | $2 \leftrightarrow 8$ | Row 1: `[8, 5, 2]` |
| Reversal | Row 2 Reverse | $(2, 0) \leftrightarrow (2, 2)$ | $3 \leftrightarrow 9$ | **Final: `[[7, 4, 1], [8, 5, 2], [9, 6, 3]]`** |

---

## 5. Algorithmic Correctness

**Soundness.** Let an arbitrary entry have initial position $(r, c)$.
1. Transpose maps $(r, c) \mapsto (c, r)$.
2. Row reversal on the transposed matrix maps row $c$, column $r$ to row $c$, column $N - 1 - r$.
The composition yields $(r, c) \mapsto (c, N - 1 - r)$, which is the exact mathematical definition of a $90^\circ$ clockwise rotation.

**Completeness.** Swapping $r < c$ ensures every off-diagonal element is transposed exactly once without undoing earlier swaps. Reversing $c < \lfloor N/2 \rfloor$ ensures each row is inverted without double-reversal.

---

## 6. Traps This Instance Exposes

- **Double Transposition:** Looping over all $r \in [0, N-1]$ and all $c \in [0, N-1]$ swaps elements twice, restoring the original matrix. The inner loop must restrict $c \ge r + 1$.
- **Clockwise vs Counter-Clockwise:** Transposing then reversing rows yields $90^\circ$ **clockwise**. Reversing rows first then transposing yields $90^\circ$ **counter-clockwise**.
- **Extra Memory Allocation:** Creating a new matrix `rotated[c][N - 1 - r] = matrix[r][c]` violates the problem's strict in-place modification requirement.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$, where $N$ is the matrix dimension. Transposition performs $N(N - 1) / 2$ swaps. Row reversal performs $N \times \lfloor N / 2 \rfloor$ swaps. Total operations $\approx N^2 = O(N^2)$, visiting each element a constant number of times.
- **Auxiliary Space Complexity:** $O(1)$. All swaps occur strictly in place using scalar temporary variables.
