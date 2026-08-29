# Guided Example: N-Queens

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4}`
- **Required output:** `[[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

The objective is to compute `[[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]` from `{"n": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Place exactly one queen in each row

A queen attacks along its row, column, and both diagonal directions. The recursion assigns rows in increasing order, and each call `dfs(i)` chooses the queen's column for row `i`. Because the algorithm makes exactly one choice before recursing to the next row, two queens can never share a row. No row-occupancy structure is needed.

The remaining work is to reject a column if an earlier queen attacks it vertically or diagonally. Once one queen has been placed in every row without those conflicts, the board is a complete solution.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How diagonal coordinates become array indices

Cells on a diagonal running from top-right to bottom-left have the same row-plus-column value. Thus `i + j` identifies that diagonal. Its range is 0 through $2n-2$, so `dg[i + j]` can record whether it already contains a queen.

Cells on a diagonal running from top-left to bottom-right have the same column-minus-row value `j - i`. That value may be negative, so the code adds `n` and indexes `udg[n - i + j]`. The possible indices range from 1 through $2n-1$. The arrays have length `2 * n`; every used index is valid, although index 0 of `udg` is unused.

`col[j]` records vertical occupancy. Each entry in all three arrays is either zero or one. The expression

`col[j] + dg[i + j] + udg[n - i + j] == 0`

is true precisely when all three relevant lines are unoccupied. If any one contains a queen, the sum is positive and the candidate is skipped.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The recursive state invariant

At entry to `dfs(i)`, rows 0 through `i - 1` contain exactly one queen each, rows `i` through `n - 1` contain only dots, and the three occupancy arrays describe exactly the queens in the filled prefix. Those queens do not attack one another.

The initial call `dfs(0)` satisfies the invariant: the grid is all dots and every occupancy entry is zero. For a safe column `j`, the algorithm writes `"Q"` into `g[i][j]` and marks the corresponding column and two diagonals. These updates happen before recursion so deeper rows see the new queen as an obstacle.

Since the safety test ruled out every attack with an earlier queen, the child state remains non-attacking. The child also moves to `i + 1`, so its filled prefix is one row longer and the invariant is preserved.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Column path plus sets:** Store one column per row and three occupied sets. This reduces the active board representation, but Python sets still need linear state and board strings must be created at each solution.
- **Boolean arrays with no full grid:** Keep the same conflict checks but store only `curr[row] = column`. It achieves $O(n)$ auxiliary search space and constructs the board only at leaves.
- **Bit-mask backtracking:** Represent columns and diagonals as integers, derive all available positions with bit operations, and recurse on set bits. It is compact and fast but less beginner-friendly.
- **Check the grid by scanning:** Testing an entire column and two diagonals for every tentative queen avoids marker arrays but increases each safety check to $O(n)$.
- **`n = 1`:** The only cell is safe, the leaf serializes `["Q"]`, and one solution is returned.
- **Rows with no safe column:** The empty remainder of the loop is the dead-end signal; ordinary return triggers rollback in the parent.
- **Odd and even dimensions:** No special geometric case is needed. Diagonal formulas cover every square uniformly.
- **Negative diagonal differences:** The `n` offset prevents negative indexing from being used as a different Python list position.
- **Input mutation:** The only input is integer `n`; all board state is internal.
- **Answer order:** Depth-first increasing-column order determines presentation, but the contract accepts any order.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n!)$. Column uniqueness alone reduces full placement orders to at most $n!$, and diagonal checks prune many of them. Let $S$ be the number of valid solutions and let $V$ be the number of partial states visited. Each state scans up to $n$ columns, so search work is $O(nV)$, with $V=O(n!)$ as a conventional coarse bound.
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
