# Guided Example: Sudoku Solver

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"board": [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]}`
- **Required output:** `[["5", "3", "4", "6", "7", "8", "9", "1", "2"], ["6", "7", "2", "1", "9", "5", "3", "4", "8"], ["1", "9", "8", "3", "4", "2", "5", "6", "7"], ["8", "5", "9", "7", "6", "1", "4", "2", "3"], ["4", "2", "6", "8", "5", "3", "7", "9", "1"], ["7", "1", "3", "9", "2", "4", "8", "5", "6"], ["9", "6", "1", "5", "3", "7", "2", "8", "4"], ["2", "8", "7", "4", "1", "9", "6", "3", "5"], ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a program to solve a Sudoku puzzle by filling the empty cells.

The objective is to compute `[["5", "3", "4", "6", "7", "8", "9", "1", "2"], ["6", "7", "2", "1", "9", "5", "3", "4", "8"], ["1", "9", "8", "3", "4", "2", "5", "6", "7"], ["8", "5", "9", "7", "6", "1", "4", "2", "3"], ["4", "2", "6", "8", "5", "3", "7", "9", "1"], ["7", "1", "3", "9", "2", "4", "8", "5", "6"], ["9", "6", "1", "5", "3", "7", "2", "8", "4"], ["2", "8", "7", "4", "1", "9", "6", "3", "5"], ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]` from `{"board": [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: What the solver is actually deciding

The board already contains fixed clues, and every `'.'` marks a decision that is still unknown. A legal completed board must satisfy three restrictions at the same time: a digit may appear only once in its row, only once in its column, and only once in its $3 \times 3$ sub-box. Checking only one or two of those restrictions is insufficient. For example, a `5` may be absent from a cell's row but already present in its column, so placing it would still be illegal.

There is an important difference between a **legal next placement** and a **placement that belongs to the solution**. A digit can obey all three restrictions now and nevertheless create a dead end several cells later. No local test can always recognize that future failure. The algorithm therefore combines fast legality checks with backtracking: make one legal choice, recursively try to finish the rest of the puzzle, and undo the choice's bookkeeping if that branch cannot be completed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"board": [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Representing the three restrictions

The solution builds three occupancy structures before searching:

- `row[i][v]` says whether row `i` already contains digit `v + 1`.
- `col[j][v]` says whether column `j` already contains digit `v + 1`.
- `block[i // 3][j // 3][v]` says whether the sub-box containing `(i, j)` already contains digit `v + 1`.

Digits are stored at indices `0` through `8`, so digit `1` corresponds to `v = 0` and digit `9` corresponds to `v = 8`. This conversion explains both `int(board[i][j]) - 1` during initialization and `str(v + 1)` during placement.

Integer division locates a cell's box. Rows `0`, `1`, and `2` all have `i // 3 == 0`; rows `3`, `4`, and `5` have value `1`; and rows `6`, `7`, and `8` have value `2`. Columns behave the same way. Thus `(i // 3, j // 3)` identifies one of the nine boxes without a special-case table.

The chained test `row[i][v] == col[j][v] == block[i // 3][j // 3][v] == false` is true only when all three flags are false. Consequently, each candidate check takes constant time. The solver does not have to rescan nine cells in the row, nine in the column, and nine in the box for every tentative digit.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Separating clues from decisions

One pass over the board records every fixed clue in the occupancy structures. Empty positions are appended, in row-major order, to `t`. This list matters because recursion can work with a single integer `k`: `t[k]` is the next cell to fill. Fixed cells never enter `t`, so the search can neither overwrite nor accidentally erase an original clue.

The input guarantee allows initialization to trust the clues. This implementation does not reject a malformed starting board containing duplicate fixed digits; that validation is unnecessary under the stated contract.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[["5", "3", "4", "6", "7", "8", "9", "1", "2"], ["6", "7", "2", "1", "9", "5", "3", "4", "8"], ["1", "9", "8", "3", "4", "2", "5", "6", "7"], ["8", "5", "9", "7", "6", "1", "4", "2", "3"], ["4", "2", "6", "8", "5", "3", "7", "9", "1"], ["7", "1", "3", "9", "2", "4", "8", "5", "6"], ["9", "6", "1", "5", "3", "7", "2", "8", "4"], ["2", "8", "7", "4", "1", "9", "6", "3", "5"], ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"board": [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[["5", "3", "4", "6", "7", "8", "9", "1", "2"], ["6", "7", "2", "1", "9", "5", "3", "4", "8"], ["1", "9", "8", "3", "4", "2", "5", "6", "7"], ["8", "5", "9", "7", "6", "1", "4", "2", "3"], ["4", "2", "6", "8", "5", "3", "7", "9", "1"], ["7", "1", "3", "9", "2", "4", "8", "5", "6"], ["9", "6", "1", "5", "3", "7", "2", "8", "4"], ["2", "8", "7", "4", "1", "9", "6", "3", "5"], ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Rescan the row, column, and box for every candidate:** This removes the occupancy tables and is easy to derive, but every tentative placement performs repeated work. It remains a valid backtracking strategy on a $9 \times 9$ board, though the constant factor is worse.
- **Bit masks instead of Boolean tables:** Nine-bit integers can represent the digits used by each row, column, and box. Availability then becomes a few bitwise operations. This is compact and fast, but Boolean arrays make the digit-to-constraint relationship easier to inspect for a beginner.
- **Choose the most constrained empty cell first:** Rather than preserve row-major order in `t`, each level can select the unfilled cell with the fewest legal candidates. This minimum-remaining-values heuristic often shrinks the search tree dramatically, at the cost of extra selection logic and more complicated state management.
- **Copy the whole board at each recursive call:** Copies make rollback conceptually simple, but they allocate and copy 81 cells per branch. Updating one cell and three flags, then undoing those flags, is substantially cheaper.
- **Already solved board:** Then `t` is empty, so `dfs(0)` immediately sets `ok`. No clue is changed, and the method correctly returns `null` after leaving the board as it was.
- **A cell with no legal digit:** Its candidate loop makes no recursive call. The frame returns, causing its parent to undo the preceding choice and try another digit. This is the normal dead-end signal, not an exceptional condition.
- **Several locally legal digits:** The solver deliberately cannot commit based only on local validity. It explores one candidate to completion and backtracks if later constraints expose the mistake.
- **Stale characters after a failed branch:** Descendant cells can temporarily retain digits in `board`, but the occupancy tables—not those characters—govern candidate legality, and a descendant is overwritten before reuse. On the guaranteed-solvable input, the successful branch ultimately overwrites every position in `t` with its final digit.
- **Invalid or unsatisfiable input:** The official contract guarantees one solution. This source has no explicit failure return and does not restore every empty cell to `'.'` after total failure, so callers should not treat it as a validator for boards outside that contract.
- **In-place result:** The required outcome is the mutation of `board`. The absence of a returned grid is intentional; callers inspect the same nested list they passed in.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(9^E)$. Let $E$ be the number of empty cells in the input board. At each recursive level, at most nine digits are tried, so a direct worst-case upper bound is $O(9^E)$. Sudoku restrictions prune most branches much earlier: a cell often has only a few available digits, and an impossible partial board stops when some later cell has no candidate. That pruning is crucial in practice, but it does not change the conservative exponential worst-case bound recorded in the variant manifest.
- **Auxiliary Space Complexity:** $O(E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
