# Guided Example: Queens That Can Attack the King

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"queens": [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], "king": [0, 0]}`
- **Required output:** `[[1, 0], [0, 1], [3, 3]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

On a **0-indexed** `8 x 8` chessboard, there can be multiple black queens and one white king.

The objective is to compute `[[1, 0], [0, 1], [3, 3]]` from `{"queens": [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], "king": [0, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Look outward from the king, not inward from every queen

A chess queen attacks along its row, column, and two diagonals. From the king’s square, these lines form exactly eight rays: up, down, left, right, and four diagonals. On any one ray, only the nearest queen can attack the king directly. If another queen lies farther along the same ray, the nearer queen blocks it.

This observation changes the problem from “analyze every queen’s line” into “scan the first occupied square in each of eight directions.” It automatically handles blocking and produces at most one answer per direction.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"queens": [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], "king": [0, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Constant-time occupancy checks

The comprehension `s = {(i, j) for i, j in queens}` converts the input coordinates into a set of tuples. A list membership test would scan queens one by one, but a hash set supports expected \(O(1)\) membership. The input uses lists, which are mutable and cannot be hashed; converting each coordinate to tuple `(i, j)` creates the hashable representation used during searches.

The board size is fixed by `n = 8`. The output list `ans` starts empty.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The comprehension `s = {(i, j) for i, j in queens}` converts... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How the eight directions are generated

The nested loops choose `a` and `b` independently from \(-1,0,1\). These values describe a row change and column change:

- one coordinate zero and the other nonzero gives a horizontal or vertical direction;
- both coordinates nonzero gives a diagonal direction;
- both zero would mean no movement.

The condition `if a or b` skips only `(0, 0)`, leaving exactly eight direction pairs. In Python, zero is false and \(-1\) and 1 are true, so the condition means “at least one change is nonzero.”

For each direction, `x, y = king` begins at the king’s coordinate. The loop condition checks the next square, `x + a, y + b`, before moving. This ensures the scan never steps outside indices zero through seven.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 0], [0, 1], [3, 3]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"queens": [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], "king": [0, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 0], [0, 1], [3, 3]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Examine every queen:** Test whether each queen:** - **Examine every queen:** Test whether each queen is aligned with the king and retain the nearest queen for each normalized direction. This also takes \(O(q)\) expected time and can avoid scanning empty squares, but direction normalization and distance comparison are more involved.
- **Boolean board:** Fill an \(8\)-by-\(8\) occupancy matrix and scan the same rays. Because the board is fixed, it uses constant space, though the set directly represents only occupied cells.
- **Continue after finding a queen:** This is incorrect because any farther queen on the same ray is blocked. The `break` expresses direct visibility.
- **King on an edge or corner:** Several directions have no in-bounds next square. The while condition rejects them safely without special cases.
- **Adjacent queen:** The first step finds it immediately, and with no intervening square it attacks directly.
- **Multiple queens on one ray:** Only the nearest is returned; all farther queens are blocked.
- **Queens on different rays:** Up to eight queens can attack simultaneously, one from each direction.
- **No attacking queen:** Every ray reaches an edge without a set hit, and the method returns an empty list.
- **Unique positions:** The statement guarantees no duplicate queens and no queen on the king. The set would silently deduplicate repeated coordinates, but such input is outside the contract.
- **Coordinate interpretation:** The method treats the first coordinate as the row and the second as the column. Swapping this convention consistently would preserve geometry, but mixing conventions would scan incorrect squares.
- **Any answer order:** Sorting is unnecessary and would add work solely for presentation. Tests must compare according to the contract’s order-insensitive requirement.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(q)$. Let \(q\) be `len(queens)`. Constructing the set takes expected \(O(q)\) time and \(O(q)\) space. The eight rays inspect at most seven squares each on an \(8\)-by-\(8\) board, a fixed maximum of 56 membership checks, so that portion is \(O(1)\). Total expected time is \(O(q)\), matching the manifest.
- **Auxiliary Space Complexity:** $O(q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
