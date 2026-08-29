# Guided Example: Rectangle Area II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"rectangles": [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D array of axis-aligned `rectangles`. Each $\text{rectangle}[i] = [x_{i1}, y_{i1}, x_{i2}, y_{i2}]$ denotes the $i^{\text{th}}$ rectangle where $(x_{i1}, y_{i1})$ are the coordinates of the **bottom-left corner**, and $(x_{i2}, y_{i2})$ are the coordinates of the **top-right corner**.

The objective is to compute `6` from `{"rectangles": [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sweep across x and maintain the union of active y-intervals

Imagine moving a vertical line from left to right. Between two consecutive rectangle x-boundaries, the set of rectangles intersected by the sweep line is constant. If their combined covered height is `H` and the horizontal distance to the next boundary is `\Delta x`, that vertical strip contributes:

$$
H\Delta x
$$

to the union area.

The challenge is maintaining `H` while rectangles begin and end, without double-counting overlapping y-ranges. A coordinate-compressed segment tree maintains the total length covered by at least one active rectangle.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"rectangles": [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create two x-events per rectangle

For rectangle `[x1,y1,x2,y2]`:

- event `(x1,y1,y2,+1)` adds its y-interval when the sweep enters the rectangle;
- event `(x2,y1,y2,-1)` removes it when the sweep leaves.

All events are stored in `segs` and sorted by x. The set `alls` collects every y-boundary `y1` and `y2` for coordinate compression.

Only boundaries matter because coverage changes nowhere between consecutive boundary values.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Compress coordinates into elementary intervals

After sorting distinct y-values:

`alls = [Y0,Y1,\ldots,Yp]`.

The segment tree does not represent the coordinate points themselves. Leaf index `r` represents the elementary half-open interval:

$$
[Y_r,Y_{r+1}).
$$

There are `len(alls)-1` such intervals.

Dictionary `m` maps each original y-coordinate to its compressed boundary index. Rectangle interval `[y1,y2)` covers elementary interval indices:

`m[y1]` through `m[y2]-1` inclusive.

That is why `modify` receives those endpoints.

Coordinate compression preserves exact physical lengths because tree nodes calculate length from original values in `nums`, not from compressed index differences.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"rectangles": [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Coordinate-compressed 2D cells:** Mark every rectangle over compressed x-y cells and sum covered cells. With up to `O(n^2)` cells, it is simpler but uses and processes quadratic space.
- **Sweep with a sorted list of active intervals:** Recompute merged y-length at each x event in `O(n)`, giving `O(n^2)` worst-case time.
- **Inclusion-exclusion over rectangle subsets:** Exponential and impractical.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let `n` be the number of rectangles. There are `2n` events and at most `2n` distinct y-coordinates.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
