# Guided Example: Transform to Chessboard

We trace the step-by-step 2D chessboard rank-1 binary matrix invariants, dual row/column pattern complementarity ($R \text{ and } \overline{R}$), population balance conditions ($|n - 2 \cdot ones| \le 1$), row and column swap orthogonality, alternating pattern Hamming distance minimization, and minimal swap calculation on representative binary grids:

- **Input:**
  $$
  board = \begin{bmatrix}
  0 & 1 & 1 & 0 \\
  0 & 1 & 1 & 0 \\
  1 & 0 & 0 & 1 \\
  1 & 0 & 0 & 1
  \end{bmatrix}
  $$
- **Required output:** `2`
  - Chessboard rules & transformation constraints:
    - In an $n \times n$ chessboard, alternating symbols (`0` and `1`) must tile every row and column such that no two adjacent cells share the same value:
      $$
      board[r][c] \ne board[r \pm 1][c] \quad \text{and} \quad board[r][c] \ne board[r][c \pm 1]
      $$
    - Permissible moves:
      1. Swap any two entire rows.
      2. Swap any two entire columns.
    - Objective: Find the **minimum number of total moves** (row swaps + column swaps) to transform the grid into a valid chessboard, or return `-1` if impossible.
    - For the input matrix ($n = 4$):
      - Swapping row 1 and row 2:
        $$
        \begin{bmatrix}
        0 & 1 & 1 & 0 \\
        1 & 0 & 0 & 1 \\
        0 & 1 & 1 & 0 \\
        1 & 0 & 0 & 1
        \end{bmatrix}
        $$
      - Swapping column 1 and column 2:
        $$
        \begin{bmatrix}
        0 & 1 & 0 & 1 \\
        1 & 0 & 1 & 0 \\
        0 & 1 & 0 & 1 \\
        1 & 0 & 1 & 0
        \end{bmatrix}
        $$
      - Valid chessboard achieved in 1 row swap + 1 column swap = **2 moves**.
- **Orthogonality & Two-Pattern Invariant:**
  - **The Rank-2 Binary Vector Space Invariant:**
    - A valid chessboard has only **two types of rows**: an alternating pattern $P$ (e.g. `0101...`) and its exact bitwise complement $\overline{P}$ (e.g. `1010...`).
    - Row swaps can reorder rows, but they **cannot change the relative values within any row**.
    - Therefore, in the initial matrix:
      1. Every single row must be either **identically equal to row 0** ($R_0$) or **the exact bitwise inverse of row 0** ($\overline{R_0}$).
      2. Exactly the same condition must hold for columns: every column must equal $C_0$ or $\overline{C_0}$.
      3. If any row or column differs from both the prototype and its inverse, return `-1` immediately.
  - **Population Parity Invariant:**
    - The count of `1`s and `0`s in row 0 must be balanced:
      - If $n$ is even: $ones = n / 2$.
      - If $n$ is odd: $|n - 2 \cdot ones| == 1$.
    - The count of rows matching $R_0$ vs $\overline{R_0}$ must also be balanced ($|n - 2 \cdot sameRow| \le 1$).
  - **Independent 1D Row and Column Decomposition:**
    - Because row swaps never alter column contents and column swaps never alter row contents, the problem splits into two independent 1D problems:
      $$
      \text{Total Moves} = \text{moves}(rowMask) + \text{moves}(colMask)
      $$
    - Each single swap corrects **two misplaced elements** at once. Thus:
      $$
      moves = \frac{\text{misplaced positions}}{2}
      $$
- **Step-by-Step Worked Execution Trace on the $4 \times 4$ Matrix:**
  - Board dimension: $n = 4$ (even).
  - Row 0: `[0, 1, 1, 0]`. Bitmask: $rowMask = (0110)_2 = 6$.
  - Bitwise inverse: $\overline{rowMask} = 15 - 6 = 9 = (1001)_2$.
  - Column 0: `[0, 0, 1, 1]`. Bitmask: $colMask = (1100)_2 = 12$.
  - **Phase 0: Structural Verification Across All Rows & Columns:**
    - Row 0: `0110` (matches $rowMask$)
    - Row 1: `0110` (matches $rowMask$)
    - Row 2: `1001` (matches $\overline{rowMask}$)
    - Row 3: `1001` (matches $\overline{rowMask}$)
    - All rows valid! $sameRow = 2$, which equals $n / 2 = 2$.
    - Number of ones in row 0: $2 == n / 2 \implies \mathbf{Valid!}$
    - Column checks symmetrically pass with $sameCol = 2$.
  - **Phase 1: Calculate Row Swaps ($n = 4$):**
    - The column vector sequence of rows is: $[0, 0, 1, 1]$ (indicating $R_0, R_0, \overline{R_0}, \overline{R_0}$).
    - We want to transform $[0, 0, 1, 1]$ into an alternating sequence:
      - Candidate Target 1: `0 1 0 1`
        - Misplaced indices: index 1 has `0` (should be `1`), index 2 has `1` (should be `0`).
        - Total misplaced: 2 positions $\implies 2 / 2 = \mathbf{1} \text{ swap}$.
      - Candidate Target 2: `1 0 1 0`
        - Misplaced indices: all 4 indices differ $\implies 4 / 2 = 2 \text{ swaps}$.
      - Minimal row swaps:
        $$
        \text{row\_moves} = \min(1, 2) = \mathbf{1}
        $$
  - **Phase 2: Calculate Column Swaps ($n = 4$):**
    - Row 0 vector is: $[0, 1, 1, 0]$.
    - We want to transform $[0, 1, 1, 0]$ into an alternating sequence:
      - Candidate Target 1: `0 1 0 1`
        - Misplaced: index 2 has `1` (should be `0`), index 3 has `0` (should be `1`).
        - Misplaced: 2 positions $\implies 2 / 2 = \mathbf{1} \text{ swap}$.
      - Candidate Target 2: `1 0 1 0`
        - Misplaced: 2 positions $\implies 2 / 2 = \mathbf{1} \text{ swap}$.
      - Minimal column swaps:
        $$
        \text{col\_moves} = \min(1, 1) = \mathbf{1}
        $$
  - **Phase 3: Total Execution Cost:**
    $$
    ans = \text{row\_moves} + \text{col\_moves} = 1 + 1 = \mathbf{2}
    $$
- **Impossible Grid Configuration Trace ($board = [[0, 1], [1, 0]]$):**
  - Row 0 is `01`, Row 1 is `10` (already a chessboard!).
  - $0$ swaps required $\implies ans = \mathbf{0}$.
- **Unbalanced Population Trace ($board = [[1, 1], [1, 1]]$):**
  - Row 0 has 2 ones, but $n / 2 = 1$.
  - Cannot form an alternating chessboard $\implies$ returns **`-1`**.
- **Odd Dimension Anchor ($n = 3$):**
  - For odd $n$, the dominant symbol (having $(n + 1) / 2$ occurrences) must occupy the even indices $0, 2, \dots$ in the alternating pattern.
  - There is only 1 valid alternating target, removing the $\min(cnt_0, cnt_1)$ choice.

This instance demonstrates rank-1 tensor product factorization over $\mathbb{F}_2$ and orthogonal coordinate projection, mathematically proves why row and column permutations commute and decouple into 1D Hamming alignment problems, and derives $O(N^2)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an $n \times n$ binary grid:
Find the **minimum swaps** of rows and columns to transform into a chessboard, or return `-1` if impossible.

```text
board:
  0 1 1 0
  0 1 1 0
  1 0 0 1
  1 0 0 1

1. Valid structure check:
   Every row is either identical to row 0 or its exact inverse!
   Rows: [ 0110, 0110, 1001, 1001 ] -> All valid!

2. Row swaps:
   Row pattern is 0, 0, 1, 1.
   To make 0, 1, 0, 1 -> 1 swap!

3. Col swaps:
   Col pattern is 0, 1, 1, 0.
   To make 0, 1, 0, 1 -> 1 swap!

Total moves = 1 + 1 = 2
Result: 2
```

### The Invariant of the Independent 1D Row/Col Projection
- Row swaps do not affect column contents; column swaps do not affect row contents.
- Every row must be $R_0$ or $\overline{R_0}$; every column must be $C_0$ or $\overline{C_0}$.
- Each swap corrects 2 misplaced positions $\implies$ swaps = misplaced / 2.

---

## 2. Conceptual Foundation & Invariants

### 1. Structural Complementarity Condition:
$$
\forall i \in [0, n - 1]: \quad Row_i \in \{Row_0, \; \overline{Row_0}\} \quad \text{and} \quad Col_i \in \{Col_0, \; \overline{Col_0}\}
$$

### 2. 1D Alternating Minimization:
For even $n$:
$$
moves = \min\left(\frac{\text{mismatches}(mask, 0xAA)}{2}, \; \frac{\text{mismatches}(mask, 0x55)}{2}\right)
$$
$$
Total = moves(Row) + moves(Col)
$$

> **Kronecker Tensor Rank Invariant.** A matrix $M \in \{0, 1\}^{n \times n}$ can be permuted into a chessboard if and only if $M = u \otimes v$ over $\mathbb{F}_2$ (rank 1 over the affine field), where $u, v \in \{0, 1\}^n$ are balanced vectors whose orbit under permutation contains the alternating word $(01)^{\lfloor n/2 \rfloor}$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Validate Board
- Row 0: `0110` (2 ones, 2 zeros).
- Rows 0, 1 are `0110`; Rows 2, 3 are `1001` (exact inverse).
- Matches $\implies$ Valid!

---

### Step 2: Row Sequence $[0, 0, 1, 1]$
- Target `0, 1, 0, 1`: 2 misplaced $\implies 2 / 2 = 1$ swap.

---

### Step 3: Col Sequence $[0, 1, 1, 0]$
- Target `0, 1, 0, 1`: 2 misplaced $\implies 2 / 2 = 1$ swap.

---

### Step 4: Total
- $1 + 1 = \mathbf{2}$.

---

## 4. Complete Execution Trace

| Dimension | Pattern Analyzed | Target Sequence | Misplaced Elements | Required Swaps |
|:---:|:---:|:---:|:---:|:---:|
| Rows | $[0, 0, 1, 1]$ | `0 1 0 1` | $2$ (indices 1, 2) | **$1$** |
| Columns | $[0, 1, 1, 0]$ | `0 1 0 1` | $2$ (indices 2, 3) | **$1$** |
| **Combined** | — | — | — | **Total: `2`** |

---

## 5. Boundary Cases & Failure Modes

- **Already a Chessboard ($[[0, 1], [1, 0]]$):** 0 mismatches $\implies$ returns 0.
- **Unbalanced Population ($[[1, 1], [1, 1]]$):** All 1s cannot alternate $\implies$ returns -1.
- **Row Not Equal to $R_0$ or $\overline{R_0}$:** 3rd pattern exists $\implies$ returns -1.
- **Odd Dimension ($n = 5$):** The majority character must occupy even indices; only 1 target pattern is legal.

---

## 6. Traps & Common Anti-Patterns

- **Trying 2D BFS / Search:** A grid of size $30 \times 30$ has $(30!)^2$ states. 2D search is completely impossible. The problem must be solved analytically via 1D projections.
- **Forgetting Odd vs Even Discrepancy:** For even $n$, both `0101...` and `1010...` are valid targets ($\min$). For odd $n$, only the pattern whose parity matches the majority symbol is valid.
- **Bit Shift Endianness:** When building bitmasks, ensure coordinate mapping is consistent across rows and columns.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Reading the $N \times N$ matrix to build bitmasks and verify complementary patterns: $\mathcal{O}(N^2)$.
  - Calculating 1D swap distance: $\mathcal{O}(1)$ via bit operations.
  - Total Time: strictly $\mathcal{O}(N^2)$ where $N \le 30 \implies \le 900$ operations. Completes in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space beyond input grid.
