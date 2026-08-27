# Guided Example: Surrounded Regions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"board": [["X"]]}`
- **Required output:** `[["X"]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` matrix `board` containing **letters** `'X'` and `'O'`, **capture regions** that are **surrounded**:

The objective is to compute `[["X"]]` from `{"board": [["X"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn “surrounded” into the easier opposite question

The board contains only `X` and `O`. A region is a group of `O` cells joined through horizontal or vertical moves. An `O` must remain unchanged exactly when its region can reach an edge of the board. Therefore, instead of examining every region and trying to prove that it is enclosed, the solution starts from the edge and marks every `O` that is known to be safe.

This reversal is the central idea. A region may have an irregular shape, so directly checking whether `X` surrounds it requires exploring the whole region and remembering whether any visited cell touches the edge. Starting at the edge removes that uncertainty: every `O` reached from a border `O` is automatically part of a non-surrounded region.

The solution temporarily changes every safe cell from `O` to `.`. The placeholder is unambiguous because the contract says that the original board contains only `X` and `O`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"board": [["X"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What the nested depth-first search means

For coordinates `(i, j)`, `dfs(i, j)` has one job: if this position is an unmarked `O` inside the board, mark it safe and continue to all four orthogonal neighbors.

The guard rejects three kinds of calls:

- coordinates outside the matrix;
- an original `X`, which blocks connectivity;
- a cell already changed to `.`, which has already been discovered.

Rejecting an already marked cell is essential. Adjacent cells can point back to one another, so an unrestricted recursive search would revisit the same positions indefinitely. Marking before making recursive calls establishes the visited state immediately and ensures that every real `O` is processed at most once.

The expression `pairwise((-1, 0, 1, 0, -1))` produces the four direction pairs `(-1, 0)`, `(0, 1)`, `(1, 0)`, and `(0, -1)`. These are precisely up, right, down, and left. Diagonal cells are intentionally absent because the problem defines connectivity only horizontally and vertically.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For coordinates `(i, j)`, `dfs(i, j)` has one job: if this p... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why all four borders are search origins

The first pair of loops invokes the search on column `0` and column `n - 1` for every row. The second pair invokes it on row `0` and row `m - 1` for every column. Together, these calls cover every border position.

Corners are passed to `dfs` more than once, and a one-row or one-column board causes still more overlap. That does not affect correctness. The first successful visit changes an `O` to `.`, and every later visit immediately returns because that cell is no longer `O`. Avoiding duplicate border calls could save a few constant-time checks, but it would complicate otherwise direct loops without changing the asymptotic cost.

After all border searches finish, the board has a useful classification:

- `X` is an original blocking cell;
- `.` is an original `O` connected to at least one border;
- `O` is an original `O` not connected to any border.

There cannot be an unmarked `O` that belongs to a border-connected region. If such a cell existed, there would be a horizontal-or-vertical path of `O` cells from a searched border cell to it. The depth-first search follows every such edge, so it would have reached and marked that cell.

Conversely, every `.` is safe. The search can create a `.` only while walking from a border origin through original `O` cells, so its region has a path to the edge and is not surrounded.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[["X"]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"board": [["X"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[["X"]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Breadth-first search from the border:** Use a :** - **Breadth-first search from the border:** Use a queue of safe `O` cells and mark each cell when it is enqueued. It proves the same reachability fact without recursive calls, but the queue can require $O(mn)$ memory.
- **Explicit depth-first stack:** Replacing recursion with a stack preserves depth-first traversal while avoiding Python’s recursion-depth limit. It still has $O(mn)$ worst-case auxiliary space.
- **Region-by-region search:** One can start from every unvisited `O`, collect its complete component, and record whether the component touches a border. This works, but it needs component storage and solves a harder classification problem than the border-first method.
- **Union-find:** Treat each `O` as a vertex and union adjacent `O` cells, with a virtual vertex representing the border. This is valid but needs $O(mn)$ parent/rank storage and is more machinery than a single traversal.
- **Single row or single column:** Every cell lies on the border, so every `O` must survive. Duplicate border calls are harmless because marked cells are rejected.
- **All `X`:** Every DFS call returns immediately, and the final sweep leaves the board unchanged.
- **All `O`:** Every cell is connected to a border and becomes `.`, then every cell is restored to `O`; nothing is captured.
- **Diagonal contact:** An interior `O` touching a border `O` only diagonally is not connected to it. The four direction pairs correctly exclude that diagonal move.
- **Temporary-character safety:** Using `.` is correct only because the input alphabet is restricted to `X` and `O`. With a broader alphabet, the marker would need to be chosen or tracked differently.
- **Runtime dependencies:** The selected source refers to `List` and `pairwise` without importing them. A standalone Python file needs `from typing import List` and `from itertools import pairwise`; `pairwise` also requires a sufficiently recent Python version.
- **Recursion depth:** Although the algorithm is mathematically correct for boards up to $200 \times 200$, a large connected component can exceed Python’s default recursion limit. An iterative queue or stack is safer when the execution environment does not raise that limit.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let $m$ be the number of rows and $n$ be the number of columns.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
