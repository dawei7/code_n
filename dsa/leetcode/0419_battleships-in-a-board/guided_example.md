# Guided Example: Battleships in a Board

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"board": [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an `m x n` matrix `board` where each cell is a battleship `'X'` or empty `'.'`, return *the number of the **battleships** on* `board`.

The objective is to compute `2` from `{"board": [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count one canonical cell per ship

A battleship may occupy many `'X'` cells, so counting every `'X'` would count its length rather than the number of ships. Flood-filling each ship would work, but the placement rules provide a simpler one-pass signature.

Every valid horizontal or vertical ship has exactly one beginning cell when the board is read from top to bottom and left to right:

- a horizontal ship's beginning is its leftmost `'X'`; and
- a vertical ship's beginning is its topmost `'X'`.

A one-cell ship is both its leftmost and topmost cell. The algorithm counts an `'X'` only when there is no `'X'` immediately above it and no `'X'` immediately to its left. That condition identifies exactly these beginning cells.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"board": [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Scan every board coordinate once

The nested loops visit rows `0` through `m-1` and columns `0` through `n-1`. If `board[i][j] == '.'`, the cell is empty and cannot represent a ship, so the code immediately continues.

For an `'X'`, the test

`i > 0 and board[i - 1][j] == 'X'`

asks whether the ship continues from the cell above. If so, the current cell is not the top of a vertical ship and has already been represented by an earlier cell in that ship.

The next test

`j > 0 and board[i][j - 1] == 'X'`

asks whether the ship continues from the left. If so, the current cell is not the left end of a horizontal ship.

Only an occupied cell with neither predecessor increments `ans`.

The boundary checks `i > 0` and `j > 0` must precede neighbor access. A cell in the top row has no above neighbor, and a cell in the leftmost column has no left neighbor. In Python, using index `-1` without these guards would wrap around to the opposite edge and could falsely connect unrelated ships.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every ship contributes at least once

Take a horizontal ship. Its leftmost cell has no `'X'` to its left by definition. The separation guarantee also prevents an unrelated vertical ship from placing an `'X'` immediately above it; adjacent ships are not allowed. Because the ship itself extends only horizontally, this beginning cell has no same-ship cell above. It passes both predecessor tests and is counted.

Take a vertical ship. Its topmost cell similarly has no `'X'` above. It has no same-ship cell to the left, and the separation rule prevents another ship there. It is counted.

A single-cell ship has no occupied predecessor in either direction and is counted as well. Thus no valid battleship is missed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"board": [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Flood fill each unvisited ship:** Start DFS or BFS at an unvisited `'X'`, mark its connected cells, and increment once. This is $O(rc)$ time but needs $O(rc)$ visited space in the worst case or modifies the board, both unnecessary under the placement guarantees.
- **Erase ships in place:** On finding an `'X'`, walk through and replace its cells with `'.'`. It uses little auxiliary space but violates the follow-up's requirement not to modify `board`.
- **Count transitions along rows and columns separately:** This can work but risks double-counting single-cell ships and needs careful orientation logic. The no-above-and-no-left signature treats all lengths uniformly.
- **Count all occupied cells:** This is incorrect whenever a ship has length greater than one because it counts cells rather than connected straight segments.
- **Top-row ship:** The guarded above check treats the missing neighbor as empty; only a left continuation can suppress counting.
- **Left-column ship:** The guarded left check similarly leaves the above neighbor to determine whether it is a continuation.
- **Single-cell board containing `'.'`:** The cell is skipped and the result is zero.
- **Single-cell board containing `'X'`:** It has no predecessor and contributes exactly one.
- **One long horizontal ship:** Only its first column is counted; every later cell sees the previous `'X'`.
- **One long vertical ship:** Only its first row is counted; every later cell sees the above `'X'`.
- **Several separated ships:** The required empty separation ensures each beginning cell is not rejected because of an unrelated adjacent ship.
- **Invalid touching or L-shaped arrangements:** The proof relies on the contract's straight, separated placement. If arbitrary connected `'X'` shapes were permitted, a graph traversal and an explicit definition of a ship would be necessary.
- **Python negative indexing:** Omitting `i > 0` or `j > 0` would read the last row or column from a first-edge cell. The explicit guards are correctness conditions, not merely optimizations.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(rc)$. Let $r=m$ be the number of rows and $c=n$ the number of columns. The nested loops inspect all $rc$ cells. Each occupied cell triggers at most two constant-time neighbor checks. Total time is $O(rc)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
