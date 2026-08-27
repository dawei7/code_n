# Guided Example: Spiral Matrix

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}`
- **Required output:** `[1, 2, 3, 6, 9, 8, 7, 4, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an `m x n` `matrix`, return *all elements of the* `matrix` *in spiral order*.

The objective is to compute `[1, 2, 3, 6, 9, 8, 7, 4, 5]` from `{"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Simulate the path a person would draw

The spiral begins at the top-left cell, moves right, turns down when blocked, then turns left, then up, and repeats. A cell is blocked if it lies outside the matrix or has already been visited. The selected solution models exactly that movement rather than explicitly maintaining shrinking rectangle boundaries.

It performs exactly $mn$ iterations, where $m$ and $n$ are the matrix dimensions. Each iteration appends one current cell and marks it visited. Because the loop count equals the number of cells, the main correctness obligation is to show that the movement never revisits a cell before all cells have been emitted.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Encode four directions in one compact tuple

`dirs = (0, 1, 0, -1, 0)` stores overlapping row/column deltas. For direction index `k`, the pair `(dirs[k], dirs[k + 1])` means:

- `k = 0`: `(0, 1)`, move right;
- `k = 1`: `(1, 0)`, move down;
- `k = 2`: `(0, -1)`, move left;
- `k = 3`: `(-1, 0)`, move up.

The repeated zero at the end allows the up pair to use indices 3 and 4 without a special case. Updating `k = (k + 1) % 4` rotates clockwise and wraps from up back to right.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `dirs = (0, 1, 0, -1, 0)` stores overlapping row/column delt... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Mark before choosing the next position

At the current coordinate `(i, j)`, the algorithm first appends `matrix[i][j]` and sets `vis[i][j] = true`. It then computes tentative next coordinates `(x, y)` using the current direction.

Marking before this check is essential. When the path eventually returns beside an earlier portion of the spiral, `vis[x][y]` detects that entering it would duplicate output and trigger the inward turn. If marking happened afterward, an immediately adjacent earlier cell might incorrectly appear unvisited during the decision.

The boundary conditions reject negative row or column coordinates and coordinates at or beyond `m` or `n`. These checks occur before `vis[x][y]` is evaluated because Python's `or` short-circuits left to right. An out-of-range proposal therefore never indexes the visited grid.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 3, 6, 9, 8, 7, 4, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 3, 6, 9, 8, 7, 4, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Four shrinking boundaries:** Track top, bottom:** - **Four shrinking boundaries:** Track top, bottom, left, and right bounds and traverse one perimeter at a time. It achieves the same $O(mn)$ time with genuine $O(1)$ auxiliary space.
- **Destructively mark the matrix:** Replace visited elements with a sentinel. This removes `vis` but mutates input and is unsafe if the sentinel may be a legitimate value.
- **Layer index formulas:** Compute each ring's coordinates directly. It avoids a visited grid but is more vulnerable to duplicate center-row or center-column handling.
- **Single row:** The walker moves right through all cells; only the irrelevant post-final update points outside.
- **Single column:** The first blocked right move turns downward, and all cells are visited once.
- **One cell:** It is appended and marked; any invalid next coordinate is never read because the loop ends.
- **Rectangular rather than square:** Boundary tests use independent `m` and `n`, so either dimension may be larger.
- **Repeated values:** Visitation is coordinate-based, not value-based. Equal integers in different cells are all returned.
- **Input preservation:** The matrix is only read. The separate Boolean grid holds traversal state.
- **Post-final coordinate:** It may be invalid or visited, but no subsequent iteration dereferences it, so it cannot affect the returned answer.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. The `for` loop runs exactly $mn$ times. Every iteration performs constant-time append, mark, boundary checks, at most one turn, and one coordinate update. Time is $O(mn)$.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
