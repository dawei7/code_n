# Guided Example: N-Queens

We trace the step-by-step recursive depth-first backtracking search on the canonical 4-Queens chessboard instance:

- **Input:** $n = 4$
- **Required output:** `[[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]`

This instance demonstrates row-by-row queen placement, constant-time threat detection using column and diagonal index formulas ($c$, $r + c$, $r - c$), pruning blocked subtrees, and board reconstruction upon reaching depth $n$.

---

## 1. Instance & Teaching Goal

On an $n \times n$ chessboard with $n = 4$, place $4$ queens such that no two queens attack each other. A queen attacks any cell in the same row, column, or diagonal.

A brute-force search over all $\binom{16}{4} = 1820$ cell configurations is slow and examines mostly invalid boards.
By observing that each row must contain **exactly one** queen, we formulate the problem as assigning a unique column $c \in [0, 3]$ to each row $r \in [0, 3]$. This reduces the search space to at most $4! = 24$ permutations. Backtracking with diagonal constraint tracking prunes invalid branches early, discovering both valid solutions in only a few recursive steps.

---

## 2. Conceptual Foundation & Invariants

### Coordinate Threat Formulas
For a queen placed at row $r$ and column $c$:
1. **Vertical Column Threat:** All cells sharing the same column $c$. Tracked via set or bitmask $\text{cols}$.
2. **Anti-Diagonal Threat ($/$):** All cells along top-right to bottom-left diagonals share constant $r + c \in [0, 2n - 2]$. Tracked via set $\text{diag1}$.
3. **Main Diagonal Threat ($\setminus$):** All cells along top-left to bottom-right diagonals share constant $r - c \in [-(n - 1), n - 1]$. Tracked via set $\text{diag2}$.

```text
Anti-diagonals (r + c):       Main diagonals (r - c):
   0   1   2   3                 0  -1  -2  -3
   1   2   3   4                 1   0  -1  -2
   2   3   4   5                 2   1   0  -1
   3   4   5   6                 3   2   1   0
```

### Backtracking Transitions
Function `place_queen(row)`:
- If $\text{row} == n$: All $n$ queens are placed safely! Convert the placement history into a string board representation and record it.
- For each column $c \in [0, n - 1]$:
  - If $c \notin \text{cols}$ and $(r + c) \notin \text{diag1}$ and $(r - c) \notin \text{diag2}$:
    - Mark $c, r + c, r - c$ as occupied.
    - Record column: $\text{queens}[r] = c$.
    - Recurse: `place_queen(row + 1)`.
    - Unmark $c, r + c, r - c$ (Rollback).

> **Invariant.** At recursion depth $r$, exactly $r$ queens have been safely placed in rows $0 \dots r - 1$ without any mutual row, column, or diagonal conflicts.

---

## 3. Step-by-Step Worked Execution

We trace the search tree for $n = 4$:

### Subtree 1: Anchor at $(0, 0)$ (Row 0, Col 0)
- Place Queen at $(0, 0)$: $\text{cols}=\{0\}, \text{diag1}=\{0\}, \text{diag2}=\{0\}$.
- **Row 1:**
  - $c = 0$: Conflict with col 0.
  - $c = 1$: Conflict on diag2 ($1 - 1 = 0$).
  - $c = 2$: Safe! Place at $(1, 2)$.
    - $\text{cols}=\{0, 2\}, \text{diag1}=\{0, 3\}, \text{diag2}=\{0, -1\}$.
    - **Row 2:**
      - $c = 0$: Col 0 conflict.
      - $c = 1$: Diag1 conflict ($2 + 1 = 3$).
      - $c = 2$: Col 2 conflict.
      - $c = 3$: Diag2 conflict ($2 - 3 = -1$).
      - *All columns blocked! Dead end at Row 2. Backtrack.*
  - $c = 3$: Safe! Place at $(1, 3)$.
    - $\text{cols}=\{0, 3\}, \text{diag1}=\{0, 4\}, \text{diag2}=\{0, -2\}$.
    - **Row 2:**
      - $c = 1$: Safe! Place at $(2, 1)$.
        - $\text{cols}=\{0, 3, 1\}, \text{diag1}=\{0, 4, 3\}, \text{diag2}=\{0, -2, 1\}$.
        - **Row 3:**
          - $c = 0, 1, 3$: Col conflicts.
          - $c = 2$: Diag2 conflict ($3 - 2 = 1$).
          - *All columns blocked! Backtrack.*
- Conclude: No solutions exist starting with Queen at $(0, 0)$.

---

### Subtree 2: Anchor at $(0, 1)$ (Row 0, Col 1)
- Place Queen at $(0, 1)$: $\text{cols}=\{1\}, \text{diag1}=\{1\}, \text{diag2}=\{-1\}$.
- **Row 1:**
  - $c = 0, 1, 2$: Blocked by threats.
  - $c = 3$: Safe! Place at $(1, 3)$.
    - Occupied: $\text{cols}=\{1, 3\}, \text{diag1}=\{1, 4\}, \text{diag2}=\{-1, -2\}$.
- **Row 2:**
  - $c = 0$: Safe! Place at $(2, 0)$.
    - Occupied: $\text{cols}=\{1, 3, 0\}, \text{diag1}=\{1, 4, 2\}, \text{diag2}=\{-1, -2, 2\}$.
- **Row 3:**
  - $c = 0, 1$: Blocked.
  - $c = 2$: Safe! ($2 \notin \text{cols}, 3+2=5 \notin \text{diag1}, 3-2=1 \notin \text{diag2}$).
    - Place at $(3, 2)$!
- **Depth Reached ($r = 4$):**
  - All 4 queens placed: Columns are $[1, 3, 0, 2]$.
  - **Record Solution 1:**
    ```text
    . Q . .
    . . . Q
    Q . . .
    . . Q .
    ```

---

### Subtree 3: Anchor at $(0, 2)$ (Row 0, Col 2)
By horizontal symmetry with Subtree 2:
- Row 0: Col 2 $\to (0, 2)$.
- Row 1: Col 0 $\to (1, 0)$.
- Row 2: Col 3 $\to (2, 3)$.
- Row 3: Col 1 $\to (3, 1)$.
- All 4 queens placed: Columns are $[2, 0, 3, 1]$.
- **Record Solution 2:**
  ```text
  . . Q .
  Q . . .
  . . . Q
  . Q . .
  ```

---

### Subtree 4: Anchor at $(0, 3)$ (Row 0, Col 3)
Symmetrical to Subtree 1: Dead ends on all branches.

Search finishes. Exactly 2 valid configurations found.

---

## 4. Complete Execution Trace

| DFS State ($r$) | Queen Placed at $(r, c)$ | Columns In Use | Anti-Diags ($r+c$) | Main Diags ($r-c$) | Subtree Outcome |
|:---:|:---:|:---:|:---:|:---:|:---|
| Row 0 | $(0, 0)$ | $\{0\}$ | $\{0\}$ | $\{0\}$ | Dead end at Row 2 / Row 3 |
| Row 0 | **$(0, 1)$** | $\{1\}$ | $\{1\}$ | $\{-1\}$ | Continues |
| Row 1 | $(1, 3)$ | $\{1, 3\}$ | $\{1, 4\}$ | $\{-1, -2\}$ | Continues |
| Row 2 | $(2, 0)$ | $\{1, 3, 0\}$ | $\{1, 4, 2\}$ | $\{-1, -2, 2\}$ | Continues |
| Row 3 | $(3, 2)$ | $\{1, 3, 0, 2\}$ | $\{1, 4, 2, 5\}$ | $\{-1, -2, 2, 1\}$ | **Emits Solution 1 (`[1, 3, 0, 2]`)** |
| Row 0 | **$(0, 2)$** | $\{2\}$ | $\{2\}$ | $\{-2\}$ | Continues |
| Row 1 | $(1, 0)$ | $\{2, 0\}$ | $\{2, 1\}$ | $\{-2, 1\}$ | Continues |
| Row 2 | $(2, 3)$ | $\{2, 0, 3\}$ | $\{2, 1, 5\}$ | $\{-2, 1, -1\}$ | Continues |
| Row 3 | $(3, 1)$ | $\{2, 0, 3, 1\}$ | $\{2, 1, 5, 4\}$ | $\{-2, 1, -1, 2\}$ | **Emits Solution 2 (`[2, 0, 3, 1]`)** |
| Row 0 | $(0, 3)$ | $\{3\}$ | $\{3\}$ | $\{-3\}$ | Dead end (Symmetric to $(0, 0)$) |

### Candidate Audit at Row 2

The trace records what happened to each row-1 child, but the interesting step is row 2, where the two live branches meet opposite fates. At row 2 the threat sets are frozen by the two queens already placed, so every column can be tested against all three constraints at once.

| Row-1 state | Columns in use | Anti-diagonals $r+c$ | Main diagonals $r-c$ | Candidate $c$ | Column clash? | Anti-diagonal clash $2 + c$? | Main-diagonal clash $2 - c$? | Verdict |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| $(0,0), (1,2)$ | $\{0, 2\}$ | $\{0, 3\}$ | $\{0, -1\}$ | 0 | Yes, $0 \in \{0, 2\}$ | No ($2$) | No ($2$) | Rejected |
| $(0,0), (1,2)$ | $\{0, 2\}$ | $\{0, 3\}$ | $\{0, -1\}$ | 1 | No | Yes, $3 \in \{0, 3\}$ | No ($1$) | Rejected |
| $(0,0), (1,2)$ | $\{0, 2\}$ | $\{0, 3\}$ | $\{0, -1\}$ | 2 | Yes, $2 \in \{0, 2\}$ | No ($4$) | Yes, $0 \in \{0, -1\}$ | Rejected |
| $(0,0), (1,2)$ | $\{0, 2\}$ | $\{0, 3\}$ | $\{0, -1\}$ | 3 | No | No ($5$) | Yes, $-1 \in \{0, -1\}$ | Rejected |
| $(0,1), (1,3)$ | $\{1, 3\}$ | $\{1, 4\}$ | $\{-1, -2\}$ | 0 | No | No ($2$) | No ($2$) | **Accepted, queen at $(2, 0)$** |
| $(0,1), (1,3)$ | $\{1, 3\}$ | $\{1, 4\}$ | $\{-1, -2\}$ | 1 | Yes, $1 \in \{1, 3\}$ | No ($3$) | No ($1$) | Rejected |
| $(0,1), (1,3)$ | $\{1, 3\}$ | $\{1, 4\}$ | $\{-1, -2\}$ | 2 | No | Yes, $4 \in \{1, 4\}$ | No ($0$) | Rejected |
| $(0,1), (1,3)$ | $\{1, 3\}$ | $\{1, 4\}$ | $\{-1, -2\}$ | 3 | Yes, $3 \in \{1, 3\}$ | No ($5$) | Yes, $-1 \in \{-1, -2\}$ | Rejected |

The left block is the clearest illustration of why exhaustive checking at each row pays for itself: the four candidates are rejected for three distinct reasons — a column clash at $c = 0$, an anti-diagonal clash at $c = 1$, a column clash *and* a main-diagonal clash together at $c = 2$, and a main-diagonal clash at $c = 3$. A pruning rule that tracked only columns would have accepted $c = 1$ and $c = 3$ and then discovered the conflict one row too late. The right block shows the same audit producing a single survivor, and that survivor is the queen at $(2, 0)$ that leads to the first recorded board.

---

## 5. Algorithmic Correctness

**Soundness.** A cell $(r, c)$ is occupied only when no prior queen shares its row (enforced by placing one queen per recursive step), column ($c \notin \text{cols}$), or either diagonal ($r+c \notin \text{diag1}$, $r-c \notin \text{diag2}$). Reaching row $n$ guarantees that all $n$ queens are mutually non-attacking.

**Completeness.** Backtracking tests every available column for row $r$. Rollback guarantees that unwinding a failed branch leaves no lingering constraints, ensuring the entire legal solution space is explored.

---

## 6. Traps This Instance Exposes

- **String Board Reconstruction:** Creating the list of strings `["." * c + "Q" + "." * (n - 1 - c)]` only upon reaching depth $n$ is far faster than maintaining a 2D char array across all backtracking steps.
- **Negative Diagonal Indices:** $r - c$ ranges from $-(n - 1)$ to $n - 1$. While Python sets naturally handle negative keys, fixed arrays require adding an offset $n$ (`diag[r - c + n]`).
- **Bitmask Acceleration:** For $n \le 16$, the three conflict sets can be represented as integer bitmasks, with threat testing and bit flipping performed via fast bitwise operations (`cols | (1 << c)`).

### Board Sizes and Their Solution Counts

| Board size $n$ | Required output | Why that many |
|:---:|:---|:---|
| 1 | `[["Q"]]` — one board | A single queen shares a row, column, and diagonal with nobody, so the only configuration is immediately accepted. |
| 2 | `[]` — no boards | Rows 0 and 1 must take distinct columns, leaving only the assignments $[0, 1]$ and $[1, 0]$; the first puts both queens on the main diagonal $r - c = 0$ and the second puts both on the anti-diagonal $r + c = 1$. |
| 3 | `[]` — no boards | All $3! = 6$ column assignments are rejected, so the impossibility is total rather than a matter of missing a corner case. |
| 4 | 2 boards | The two surviving assignments are column lists $[1, 3, 0, 2]$ and $[2, 0, 3, 1]$, exactly the two boards this lesson's search records. |
| 6 | 4 boards | The $6! = 720$ column assignments prune down to four complete boards, all listed in the package cases. |
| 9 | 352 boards | The largest board the constraints permit still yields $352$ distinct configurations, which is why the answer is returned as a list of boards rather than a count. |

The jump from $n = 2$ and $n = 3$ (impossible) to $n = 4$ (two boards) is the reason the search cannot be replaced by a formula: existence is not monotone in $n$, and the counting sequence for this puzzle has no closed form, so enumeration with pruning is the method the constraints demand.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n!)$. Row 0 has $n$ choices, Row 1 has at most $n-1$, Row 2 has at most $n-2$. Diagonal constraints prune the tree much faster than $n!$. For $n=4$, only 8 leaf states are examined.
- **Auxiliary Space Complexity:** $O(n)$ to store the recursion stack and conflict sets of size $O(n)$.

### Alternative Formulations

| Approach | Conflict state | Time | Auxiliary space | Behaviour on $n = 4$ |
|:---|:---|:---|:---|:---|
| Column and diagonal sets (this lesson) | Three hash sets keyed by $c$, $r + c$, and $r - c$ | $O(n!)$ node visits before pruning | $O(n)$ for the sets plus the recursion | Walks the tree in section 3, rejecting row-2 candidate 1 by the anti-diagonal test and candidate 3 by the main-diagonal test. |
| Three boolean arrays | Offset indices, with $r - c + n$ used for the main diagonals | $O(n!)$ node visits before pruning | $O(n)$ | Identical tree; the main-diagonal values $\{0, -1\}$ in the left block above are stored at array slots $4$ and $3$. |
| Three integer bitmasks | One bit per column, per anti-diagonal, and per main diagonal | $O(n!)$ node visits before pruning | $O(1)$ beyond the recursion | Identical tree using a 4-bit column mask and two 7-bit diagonal masks, with a single combined test replacing three membership queries. |
| Mutable board rescanned at every step | The partial board itself | $O(n! \cdot n^2)$ before pruning, since each trial placement rescans earlier rows | $O(n^2)$ for the board | Still finds both boards, but re-derives conflicts that the sets and masks already hold, and the reconstruction cost is paid at every node rather than once at depth $n$. |
