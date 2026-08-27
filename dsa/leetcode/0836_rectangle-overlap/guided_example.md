# Guided Example: Rectangle Overlap

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"rec1": [0, 0, 2, 2], "rec2": [1, 1, 3, 3]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An axis-aligned rectangle is represented as a list `[x1, y1, x2, y2]`, where `(x1, y1)` is the coordinate of its bottom-left corner, and `(x2, y2)` is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

The objective is to compute `true` from `{"rec1": [0, 0, 2, 2], "rec2": [1, 1, 3, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Positive-area overlap must exist on both axes

Because the rectangles are axis-aligned, each rectangle is the Cartesian product of:

- an open-width interval along the x-axis;
- an open-height interval along the y-axis.

The two rectangles have a positive-area intersection exactly when their x-intervals overlap with positive length and their y-intervals overlap with positive length.

The source tests the opposite condition: it lists every way the rectangles can be separated on at least one axis, then negates that disjunction.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"rec1": [0, 0, 2, 2], "rec2": [1, 1, 3, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Name the boundaries

For `rec1 = [x1,y1,x2,y2]`:

- `x1` is its left edge and `x2` its right edge;
- `y1` is its bottom edge and `y2` its top edge.

For `rec2 = [x3,y3,x4,y4]`, the analogous boundaries are left `x3`, bottom `y3`, right `x4`, and top `y4`.

Validity guarantees each left edge is strictly left of its right edge and each bottom edge is strictly below its top edge.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For `rec1 = [x1,y1,x2,y2]`:

- `x1` is its left edge and `x2... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The four separating cases

The rectangles do not overlap with positive area if any one of these is true:

1. `y3 >= y2`: rectangle 2's bottom is at or above rectangle 1's top.
2. `y4 <= y1`: rectangle 2's top is at or below rectangle 1's bottom.
3. `x3 >= x2`: rectangle 2's left edge is at or to the right of rectangle 1's right edge.
4. `x4 <= x1`: rectangle 2's right edge is at or to the left of rectangle 1's left edge.

The exact return is the negation of these cases:

`not (y3 >= y2 or y4 <= y1 or x3 >= x2 or x4 <= x1)`.

If none is true, neither rectangle is entirely above, below, left, or right of the other. Their projections overlap positively on both axes, so their intersection has positive width and height.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"rec1": [0, 0, 2, 2], "rec2": [1, 1, 3, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Compute intersection width and height:** Check:** - **Compute intersection width and height:** Check `min(rights) > max(lefts)` and `min(tops) > max(bottoms)`. This is equally constant-time and directly expresses positive dimensions.
- **- **Multiply intersection dimensions:** Multiplica:** - **Multiply intersection dimensions:** Multiplication is unnecessary and can be misleading if one or both dimensions are negative. Check both dimensions separately.
- **- **Edge contact:** Equality on one separating bou:** - **Edge contact:** Equality on one separating boundary returns false because shared area is zero.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The algorithm unpacks eight coordinates and performs four comparisons, three Boolean `or` operations, and one negation. The amount of work does not depend on coordinate magnitudes or any input collection size, so time complexity is `O(1)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
