# Guided Example: Projection Area of 3D Shapes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 2], [3, 4]]}`
- **Required output:** `17`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `n x n` `grid` where we place some `1 x 1 x 1` cubes that are axis-aligned with the `x`, `y`, and `z` axes.

The objective is to compute `17` from `{"grid": [[1, 2], [3, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

Each grid cell $(i,j)$ holds a vertical tower of `grid[i][j]` unit cubes. A projection collapses one spatial axis, so overlapping cubes hide one another. The three viewing directions therefore require three different summaries:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 2], [3, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- From above onto the $xy$ plane, only whether a tower exists matters.
- From one side onto the $yz$ plane, only the tallest tower in each row matters.
- From the perpendicular side onto the $zx$ plane, only the tallest tower in each column matters.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The solution calculates these three areas independently and adds them.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `17` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 2], [3, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `17` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **One explicit nested loop:** Track positive cells, row maxima, and column maxima manually. This has the same time bound and uses an $O(n)$ column-maximum array.
- **Build a transposed matrix:** Then take row maxima of both orientations. It works but allocates $O(n^2)$ data unnecessarily.
- **Model every unit cube:** Expanding towers takes time proportional to the sum of all heights, even though only occupancy and maxima matter.
- **Sum tower heights for side views:** This double-counts overlapping shadow levels along the viewing direction.
- **All zeros:** Every positive test is false and every row and column maximum is zero, so total projection area is zero.
- **One cell of height `v`:** Top area is 1 when $v>0$, and each side area is $v$, giving $1+2v$. For `v=2`, the result is 5.
- **Sparse diagonal towers:** Each positive cell contributes separately to the top, while row and column maxima capture the separated side positions.
- **Several towers in one row:** Only the tallest affects that row's side projection.
- **Several towers in one column:** Only the tallest affects that column's perpendicular projection.
- **Equal maxima:** Equal-height towers aligned in one viewing line still create one shadow of that height, not multiple copies.
- **Square-grid guarantee:** Every row is nonempty and has equal length, so `max(row)` and `zip(*grid)` are safe.
- **Value magnitude:** Heights affect maxima but not the number of grid positions traversed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the side length of the square grid. Each of the three calculations examines all $n^2$ values once overall up to a constant factor.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
