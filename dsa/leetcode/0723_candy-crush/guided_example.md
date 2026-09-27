# Guided Example: Candy Crush

We trace the step-by-step simultaneous match detection ($|\text{run}| \ge 3$), in-place negative sign tagging ($board[i][j] \leftarrow -|val|$), simultaneous horizontal and vertical triplet intersection preservation, bottom-up column gravity compaction, empty cell zero-padding, and cascade round iteration until board stabilization on representative game grids:

- **Input:**
  $$
  board = \begin{bmatrix}
  1 & 1 & 1 \\
  2 & 3 & 4 \\
  5 & 6 & 7
  \end{bmatrix}
  $$
- **Required output:**
  $$
  \begin{bmatrix}
  0 & 0 & 0 \\
  2 & 3 & 4 \\
  5 & 6 & 7
  \end{bmatrix}
  $$
  - Game mechanics:
    - Positive integers represent distinct candy colors; $0$ represents empty space.
    - A contiguous horizontal or vertical run of **3 or more identical candies** must be crushed.
    - **Simultaneous Crushing:** All qualifying runs must crush concurrently. A candy participating in both a horizontal and vertical run must be cleared in the same step.
    - **Gravity Drop:** After crushing, surviving candies fall straight down to fill empty voids below them. Empty spaces at the top are filled with $0$.
    - **Cascade Loop:** If dropping candies creates new crushable runs, the cycle repeats until the board reaches a static equilibrium.
- **Negative In-Place Tagging & Gravity Compaction Invariant:**
  - **The Simultaneous Crushing Dilemma:**
    - If matching candies were immediately overwritten with $0$, a candy shared between a horizontal run and a vertical run would be wiped out before the vertical scan detects the second run!
  - **In-Place Negative Sign Tagging:**
    - To preserve candy color while marking it for destruction, negate its value:
      $$
      board[i][j] \leftarrow -|board[i][j]|
      $$
    - During scanning, inspect absolute values:
      $$
      |board[i][j]| == |board[i][j-1]| == |board[i][j-2]|
      $$
    - Any candy marked negative still reveals its original color to subsequent overlapping checks.
  - **Column-by-Column Gravity Compaction:**
    - For each column $j$, iterate from the bottom row ($m - 1$) upward to row $0$:
      - Maintain write pointer $k = m - 1$.
      - If $board[i][j] > 0$ (a surviving candy that was never crushed):
        $$
        board[k][j] \leftarrow board[i][j], \quad k \leftarrow k - 1
        $$
      - Crushed candies (negative values) are bypassed.
    - Once all surviving candies have settled, fill all remaining upper cells ($k \ge 0$) with $0$:
      $$
      board[k][j] \leftarrow 0 \quad (\text{while } k \ge 0)
      $$
  - **Stability Halting Condition:**
    - If an entire round completes without tagging any candies (`run == false`), the board is completely stable $\implies$ halt and return $board$.
- **Step-by-Step Worked Execution Trace on the $3 \times 3$ Board:**
  - Board dimensions: $m = 3, n = 3$.
  - **Round 1:**
    - Initialize round flag: $run = \text{false}$.
    - **Phase 1: Horizontal Triplet Scan:**
      - Row 0 ($[1, 1, 1]$):
        - Check triplet at $j = 2$:
          $$
          |board[0][2]| == |board[0][1]| == |board[0][0]| \iff |1| == |1| == |1| \quad \mathbf{(Match!)}
          $$
        - Tag all 3 candies as crushed:
          $$
          board[0][0] = board[0][1] = board[0][2] \leftarrow -1
          $$
        - Activate round flag: $run \leftarrow \mathbf{true}$.
      - Row 1 ($[2, 3, 4]$): All distinct.
      - Row 2 ($[5, 6, 7]$): All distinct.
    - **Phase 2: Vertical Triplet Scan:**
      - Col 0 ($[-1, 2, 5]$): Distinct.
      - Col 1 ($[-1, 3, 6]$): Distinct.
      - Col 2 ($[-1, 4, 7]$): Distinct.
    - Board state after Tagging:
      $$
      \begin{bmatrix}
      \mathbf{-1} & \mathbf{-1} & \mathbf{-1} \\
      2 & 3 & 4 \\
      5 & 6 & 7
      \end{bmatrix}
      $$
    - **Phase 3: Gravity Compaction (Column by Column):**
      - **Column 0:**
        - Read from bottom:
          - $i = 2$: $board[2][0] = 5 > 0 \implies board[2][0] \leftarrow 5, \; k = 1$.
          - $i = 1$: $board[1][0] = 2 > 0 \implies board[1][0] \leftarrow 2, \; k = 0$.
          - $i = 0$: $board[0][0] = -1 < 0 \implies$ Bypassed!
        - Fill remaining cells with 0:
          - $k = 0 \implies board[0][0] \leftarrow \mathbf{0}$.
        - Col 0 becomes: $[0, 2, 5]^T$.
      - **Column 1:**
        - Surviving candies: $7 \to 6 \to 3$.
        - Crushed candy: $-1$ bypassed.
        - $board[0][1] \leftarrow \mathbf{0}, board[1][1] \leftarrow 3, board[2][1] \leftarrow 6$.
        - Col 1 becomes: $[0, 3, 6]^T$.
      - **Column 2:**
        - Surviving candies: $7, 4$.
        - Crushed candy: $-1$ bypassed.
        - Col 2 becomes: $[0, 4, 7]^T$.
    - Board state after Gravity:
      $$
      \begin{bmatrix}
      \mathbf{0} & \mathbf{0} & \mathbf{0} \\
      2 & 3 & 4 \\
      5 & 6 & 7
      \end{bmatrix}
      $$
  - **Round 2 (Equilibrium Check):**
    - Scan horizontal triplets: None found.
    - Scan vertical triplets: None found.
    - $run == \text{false} \implies \mathbf{Board\ is\ Stable!}$
    - Cascade terminates.
  - **Step 4: Output Final Board:**
    $$
    ans = \begin{bmatrix}
    0 & 0 & 0 \\
    2 & 3 & 4 \\
    5 & 6 & 7
    \end{bmatrix}
    $$
- **Cross/Intersection Match Trace (T-Shape of 3s):**
  - A horizontal run of three 3s shares its center with a vertical run of three 3s.
  - Negating the horizontal triplet marks the center as $-3$.
  - The vertical scan checks $|-3| == |3| == |3|$ and successfully tags the vertical branch!
  - All 5 candies crush simultaneously into 0.
- **Already Stable Board ($[[1, 2, 3], [4, 5, 6], [7, 8, 9]]$):**
  - No triplets in either dimension $\implies$ returns identical board in 1 round.

This instance demonstrates cellular automata simulation and concurrent multi-directional pattern matching, mathematically proves why signed magnitude tagging preserves state history during concurrent rewrite phases, and derives $O(R \cdot M \cdot N)$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ Candy Crush grid:
1. Crush all horizontal and vertical runs of $\ge 3$ adjacent identical candies **simultaneously**.
2. Apply **gravity** so surviving candies drop down to the bottom.
3. Repeat until no more candies can be crushed (stable board).

```text
board:
  1 1 1  <- 3 matching candies in a row!
  2 3 4
  5 6 7

Crush row 0: tag with -1
  -1 -1 -1
   2  3  4
   5  6  7

Apply gravity (drop down, fill top with 0):
   0  0  0
   2  3  4
   5  6  7

Stable! (No more matches)
```

### The Invariant of Negative Value Tagging
- Tagging crushed candies as `-abs(val)` allows other checks in the same round to still see the candy's original color via `abs(...)`.
- This ensures horizontal and vertical intersecting crosses are both detected and crushed simultaneously.

---

## 2. Conceptual Foundation & Invariants

### 1. Triplet Tagging Predicate:
Horizontal:
$$
|board[i][j]| == |board[i][j-1]| == |board[i][j-2]| \ne 0 \implies \text{tag all three as } -|val|
$$
Vertical:
$$
|board[i][j]| == |board[i-1][j]| == |board[i-2][j]| \ne 0 \implies \text{tag all three as } -|val|
$$

### 2. In-Place Column Compaction:
For each column $j$:
$$
\text{Read } i = m-1 \dots 0: \quad \text{if } board[i][j] > 0 \implies board[k][j] \leftarrow board[i][j], \; k \leftarrow k - 1
$$
$$
\text{Pad zeros: } \quad board[k][j] \leftarrow 0 \quad \forall k \ge 0
$$

> **Synchronous Cellular Rewrite Invariant.** The rewrite rule $\mathcal{R}: \mathbb{Z}^{m \times n} \to \mathbb{Z}^{m \times n}$ decomposes into a simultaneous marking phase followed by a strictly monotonic vertical compaction operator, ensuring finite termination on any discrete bounded lattice.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Scan
- Row 0 has triplet `[1, 1, 1]`.
- Tag row 0 as `[-1, -1, -1]`.
- $run = \text{True}$.

---

### Step 2: Gravity
- Column 0: 5 at row 2, 2 at row 1, 0 at row 0.
- Column 1: 6 at row 2, 3 at row 1, 0 at row 0.
- Column 2: 7 at row 2, 4 at row 1, 0 at row 0.

---

### Step 3: Check Next Round
- No runs $\ge 3 \implies$ Stable.

---

### Step 4: Output
$$
\begin{bmatrix}
0 & 0 & 0 \\
2 & 3 & 4 \\
5 & 6 & 7
\end{bmatrix}
$$

---

## 4. Complete Execution Trace

| Round | Candidate Cell $(i, j)$ | Neighbor Match Checked | Value Tagged | Column Affected | Compaction Profile | Stable? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $(0, 2)$ | $(0, 0), (0, 1), (0, 2) \to 1$ | `-1` | Rows $0 \dots 2$ | Tagged as $-1$ | No |
| $1$ | Gravity Drop | — | — | All Columns | $[0, 2, 5], [0, 3, 6], [0, 4, 7]$ | Yes |
| **$2$** | **Verification** | **No triplets found** | — | — | **Unchanged** | **Halt** |

---

## 5. Boundary Cases & Failure Modes

- **Already Stable Board:** 0 runs tagged $\implies$ terminates in 1 iteration.
- **Cascading Collapses:** When dropping candies forms a new run of $\ge 3$, the loop automatically runs again.
- **Minimum Grid Size ($3 \times 3$):** Correctly handles smallest dimensions that can support a triplet.
- **Multiple Intersecting Runs (Cross/T-shape):** Simultaneous negative tagging ensures all arms of the cross crush together.

---

## 6. Traps & Common Anti-Patterns

- **Setting Cells to 0 Immediately:** Overwriting cells with 0 during the horizontal scan destroys vertical runs that share the same candy. Using negative signs `-abs(val)` preserves color information.
- **Top-Down Compaction:** Compacting from top to bottom overwrites candies before they can drop. Always read and write from the **bottom up** ($m - 1 \to 0$).
- **Single Direction Only:** Check both horizontal triplets AND vertical triplets in every round.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - In each round, scans all $M \times N$ cells horizontally, vertically, and during compaction: $\mathcal{O}(M \cdot N)$.
  - In the worst case, each cascade round eliminates at least 3 candies, bounding rounds $R \le (M \cdot N) / 3$.
  - Total Time: $\mathcal{O}(R \cdot M \cdot N)$. For $M = N = 50$, executes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (in-place tagging on the existing board).
