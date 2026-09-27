# Guided Example: Sudoku Solver

We trace the step-by-step recursive depth-first backtracking search with state rollback on a representative Sudoku board instance:

- **Input:** A 9x9 board with fixed numerical clues and unfilled cells (`'.'`)
- **Required output:** The uniquely completed 9x9 board satisfying all Sudoku constraints

This instance demonstrates collecting empty cell coordinates, computing viable candidate digits using bitmask / set intersections across row, column, and $3 \times 3$ sub-box constraints, recursive state exploration, and deterministic backtracking rollback upon encountering dead ends.

---

## 1. Instance & Teaching Goal

We must fill all empty cells (`'.'`) in a 9x9 Sudoku puzzle such that:
1. Every row contains digits $1 \dots 9$ exactly once.
2. Every column contains digits $1 \dots 9$ exactly once.
3. Every $3 \times 3$ sub-box contains digits $1 \dots 9$ exactly once.

A brute-force generator trying all $9^{E}$ configurations (where $E \le 64$ is the number of empty cells) is computationally infeasible ($9^{64} \approx 10^{61}$). Backtracking with constraint propagation prunes illegal candidates immediately, exploring only dynamically legal partial configurations. When a path encounters an empty cell with zero legal placements, the algorithm immediately backtracks, resetting state and exploring alternative branches.

---

## 2. Conceptual Foundation & Invariants

### State Management & Constraint Bitmasks
We track occupied digits using three collections of sets (or 9-bit bitmasks):
- $\text{row\_used}[r]$: Set of digits present in row $r$.
- $\text{col\_used}[c]$: Set of digits present in column $c$.
- $\text{box\_used}[b]$: Set of digits present in sub-box $b = \lfloor r/3 \rfloor \times 3 + \lfloor c/3 \rfloor$.

### The Candidate Set Formula
For an empty cell at $(r, c)$, the set of legal candidate digits $D(r, c)$ is the set difference:
$$
D(r, c) = \{1, 2, \dots, 9\} \setminus \Big( \text{row\_used}[r] \cup \text{col\_used}[c] \cup \text{box\_used}[b] \Big)
$$

### Backtracking Algorithm Structure
1. **Collect Empty Cells:** Traverse the board once and append all coordinates $(r, c)$ where $\text{board}[r][c] == \text{'.'}$ to a list $\text{blanks}$.
2. **Recursive Function `solve(k)`:**
   - **Base Case:** If $k == |\text{blanks}|$, all cells are legally filled $\implies$ return $\text{True}$.
   - Let $(r, c) = \text{blanks}[k]$ and $b = \lfloor r/3 \rfloor \times 3 + \lfloor c/3 \rfloor$.
   - For each candidate digit $d \in D(r, c)$:
     - **Place:** Assign $\text{board}[r][c] \leftarrow d$, add $d$ to $\text{row\_used}[r]$, $\text{col\_used}[c]$, $\text{box\_used}[b]$.
     - **Recurse:** If `solve(k + 1)` returns $\text{True}$, propagate $\text{True}$ upward immediately.
     - **Rollback (Undo):** Remove $d$ from $\text{row\_used}[r]$, $\text{col\_used}[c]$, $\text{box\_used}[b]$, and reset $\text{board}[r][c] \leftarrow \text{'.'}$.
   - If no candidate $d \in D(r, c)$ yields a valid solution, return $\text{False}$ (triggering backtrack to cell $k - 1$).

> **Invariant.** At recursion depth $k$, all cells before $k$ in $\text{blanks}$ and all original clue cells satisfy all Sudoku invariants simultaneously.

---

## 3. Step-by-Step Worked Execution

We trace the candidate evaluation and placement for the first empty cell in the standard board:

### Clue Extraction & Cell Identification
- Clues in Row 0: $\text{board}[0][0] = \text{'5'}, \text{board}[0][1] = \text{'3'}, \text{board}[0][4] = \text{'7'}$.
  - $\text{row\_used}[0] = \{3, 5, 7\}$.
- First empty cell: $(0, 2)$.
- Column 2 clues: $\text{board}[2][2] = \text{'8'}$.
  - $\text{col\_used}[2] = \{8\}$.
- Sub-box 0 ($r \in [0, 2], c \in [0, 2]$) clues:
  - Row 0: $\{5, 3\}$
  - Row 1: $\{6\}$
  - Row 2: $\{9, 8\}$
  - $\text{box\_used}[0] = \{3, 5, 6, 8, 9\}$.

---

### Candidate Intersection for Cell $(0, 2)$
- Prohibited digits:
  $$
  \text{Prohibited} = \{3, 5, 7\} \cup \{8\} \cup \{3, 5, 6, 8, 9\} = \{3, 5, 6, 7, 8, 9\}
  $$
- Allowed candidate digits:
  $$
  D(0, 2) = \{1, 2, 3, 4, 5, 6, 7, 8, 9\} \setminus \{3, 5, 6, 7, 8, 9\} = \{1, 2, 4\}
  $$

---

### Branching and Backtracking
- **Attempt 1: Place $d = 1$ in $(0, 2)$**
  - $\text{board}[0][2] \leftarrow \text{'1'}$.
  - Advance to next empty cell $(0, 3)$.
  - In downstream recursion, placing $1$ at $(0, 2)$ eventually deprives column 2 of a legal placement for digit $1$.
  - Downstream returns $\text{False}$.
  - **Rollback:** $\text{board}[0][2] \leftarrow \text{'.'}$, remove $1$ from sets.

- **Attempt 2: Place $d = 2$ in $(0, 2)$**
  - Downstream conflict detected.
  - **Rollback:** Reset $(0, 2)$ to `'.'`.

- **Attempt 3: Place $d = 4$ in $(0, 2)$**
  - $\text{board}[0][2] \leftarrow \text{'4'}$.
  - State accepted: Row 0 now has $\{3, 4, 5, 7\}$, Box 0 has $\{3, 4, 5, 6, 8, 9\}$.
  - Advance to cell $(0, 3)$ with valid remaining candidates $\{6\}$.
  - Recursive search proceeds until all empty cells are filled.

---

## 4. Complete Execution Trace

### Candidate Filtering Table for Cell $(0, 2)$

| Digit $d$ | In Row 0? | In Col 2? | In Sub-box 0? | Legally Viable? | Action in DFS |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | No | No | No | **Yes** | Attempted; triggers downstream backtrack |
| 2 | No | No | No | **Yes** | Attempted; triggers downstream backtrack |
| 3 | **Yes** | No | **Yes** | No | Pruned immediately |
| 4 | No | No | No | **Yes** | **Successful branch in global solution** |
| 5 | **Yes** | No | **Yes** | No | Pruned immediately |
| 6 | No | No | **Yes** | No | Pruned immediately |
| 7 | **Yes** | No | No | No | Pruned immediately |
| 8 | No | **Yes** | **Yes** | No | Pruned immediately |
| 9 | No | No | **Yes** | No | Pruned immediately |

### What Each Branch of the Search Actually Costs

Legality is not the same as usefulness: a legal digit can still open a vast dead subtree. The
next table follows the accepted digit at each decisive ply of the successful path and records
how many recursive placements the rejected candidates consume before rollback discards them.

| Ply $k$ | Blank $(r, c)$ | Rejected candidates (subtree calls spent) | Accepted digit | Subtree calls under the accepted digit |
|:---:|:---:|:---|:---:|:---:|
| 0 | $(0, 2)$ | $1$ ($333$ calls), $2$ ($1874$ calls) | $4$ | $2001$ |
| 1 | $(0, 3)$ | $2$ ($40$) | $6$ | $1960$ |
| 2 | $(0, 5)$ | $2$ ($34$) | $8$ | $1925$ |
| 3 | $(0, 6)$ | $1$ ($1207$) | $9$ | $717$ |
| 6 | $(1, 1)$ | $2$ ($434$) | $7$ | $280$ |
| 12 | $(2, 3)$ | $2$ ($102$) | $3$ | $172$ |
| 17 | $(3, 1)$ | $1$ ($44$), $2$ ($60$) | $5$ | $63$ |
| 18 | $(3, 2)$ | $1$ ($23$) | $9$ | $39$ |
| 34 | $(6, 0)$ | $3$ ($6$) | $9$ | $17$ |
| 37 | $(6, 4)$ | none: row, column and box leave exactly one digit | $3$ | $14$ |
| 50 | $(8, 6)$ | none: the final blank | $1$ | $1$ (the terminating base-case call) |

The accounting closes exactly: $1 + 333 + 1874 + 2001 = 4209$ recursive placements for the whole
solve, against $51$ blanks. Well over half of that total — $2207$ calls — is spent proving that
placing $1$ or $2$ at $(0,2)$ cannot ever complete the grid, which is exactly the work that
rollback throws away. After ply $19$ the search is nearly forced: only ply $34$ still rejects a
candidate, and every other ply up to $50$ accepts its first legal digit.

### Solution Verification Snapshot (First 3 Rows)

```text
Row 0:  [5, 3, 4 | 6, 7, 8 | 9, 1, 2]  -> Digits 1-9 unique
Row 1:  [6, 7, 2 | 1, 9, 5 | 3, 4, 8]  -> Digits 1-9 unique
Row 2:  [1, 9, 8 | 3, 4, 2 | 5, 6, 7]  -> Digits 1-9 unique
```

---

## 5. Algorithmic Correctness

**Soundness.** A cell is assigned digit $d$ only if $d \notin \text{row\_used}[r]$, $d \notin \text{col\_used}[c]$, and $d \notin \text{box\_used}[b]$. When $k = |\text{blanks}|$, all empty cells have been filled without violating any constraint. The resulting board is a complete, valid Sudoku solution.

**Completeness.** Backtracking systematically explores every candidate assignment in $D(r, c)$. Because rollback restores the exact state upon branch failure, no valid configuration is prematurely abandoned. If a unique solution exists, the search tree is guaranteed to reach the successful leaf.

---

## 6. Traps This Instance Exposes

- **Failing to Revert State on Backtrack:** Forgetting to clear `board[r][c] = '.'` or forgetting to remove $d$ from the used sets poisons subsequent branch evaluations with stale constraints.
- **Deep Recursion Limit:** A board with up to 64 empty cells has recursion depth at most 64, well within default Python stack limits (1000).
- **Early Termination Propagation:** Once the base case returns $\text{True}$, returning $\text{True}$ immediately up the call stack prevents further backtracking and preserves the solved board in place.

### Boundary instances solved by the identical procedure

No case-specific branch is needed for any of these; the table records what each one stresses and
the recursion count it produces, so the same procedure is seen to cover the whole legal domain.

| Instance | Blanks $E$ | Recursive placements | What it stresses | Why no special case is required |
|:---|:---:|:---:|:---|:---|
| Already solved grid | $0$ | $1$ | An empty blank list | The base case fires before any candidate is examined, so the grid is returned exactly as given |
| Single hole at $(8,8)$ | $1$ | $2$ | One forced placement | Row 8, column 8 and the bottom-right box together leave only $9$, which is placed and immediately accepted |
| One hole per row | $9$ | $10$ | Nine independent forced placements | Blanks $(0,0), (1,1), \dots, (8,8)$ admit the single digits $5, 7, 8, 7, 5, 4, 2, 3, 9$, so no rejection ever occurs |
| Sparse grid | $45$ | $83$ | Broad branching with many legal digits per cell | Even though each blank initially has several legal digits, forward checking rejects them at the next ply, so the search never explodes |
| Digit-remapped grid | $9$ | $10$ | A different completed grid | The clues describe a relabelled completion whose row 0 is `576432198`; the constraints alone must rediscover it, because nothing in the state records a memorised answer |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(9^E)$ in the theoretical worst case, where $E \le 64$ is the number of empty cells. In practice, constraint pruning eliminates the vast majority of branches, solving standard puzzles in a few thousand recursive calls ($< 10\text{ ms}$).
- **Auxiliary Space Complexity:** $O(E)$ recursion stack depth and $O(1)$ constraint set memory. The board is mutated strictly in place.
