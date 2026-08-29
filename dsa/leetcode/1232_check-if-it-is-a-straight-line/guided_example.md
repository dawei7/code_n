# Guided Example: Check If It Is a Straight Line

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"coordinates": [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `coordinates`, $\text{coordinates}[i] = [x, y]$, where `[x, y]` represents the coordinate of a point. Check if these points make a straight line in the XY plane.

The objective is to compute `true` from `{"coordinates": [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the first two points to define the candidate line

The input contains at least two distinct points. Exactly one straight line passes through the first two, so there is no need to compare every pair of points. The solution stores the first point as `(x1, y1)` and the second as `(x2, y2)`. Every remaining point must lie on that same line.

A familiar test would compare slopes:

\[
\frac{y-y_1}{x-x_1}
=
\frac{y_2-y_1}{x_2-x_1}.
\]

Direct division is inconvenient. A vertical line has a zero horizontal difference, causing division by zero, and floating-point division can introduce rounding error. Cross multiplication removes both problems:

\[
(x-x_1)(y_2-y_1)
=
(y-y_1)(x_2-x_1).
\]

The exact code checks this equality for each point after the first two. If any point fails, it returns `false` immediately. If all pass, it returns `true`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"coordinates": [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Geometric meaning of the cross product

The vectors from the first point to the second and from the first point to the current point are

\[
\mathbf{u}=(x_2-x_1,y_2-y_1),
\qquad
\mathbf{v}=(x-x_1,y-y_1).
\]

Their two-dimensional cross product is

\[
u_xv_y-u_yv_x.
\]

It equals zero exactly when the vectors are parallel. Rearranging that zero condition gives the equality used by the code. Because both vectors begin at the same point, parallel vectors mean all three points are collinear.

This view covers horizontal, vertical, increasing, and decreasing lines uniformly.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a single anchor point is enough

Suppose every point has zero cross product with the fixed vector from point zero to point one. Every vector from point zero to another point is parallel to that fixed nonzero vector. Therefore, every point belongs to the unique line through the first two points.

Comparing consecutive slopes instead would also work, but it is unnecessary and can make correctness reasoning more complicated. A fixed anchor provides one unchanging reference throughout the scan.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"coordinates": [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Index-based cross-product loop:** Iterate indices from two onward instead of slicing. It keeps the same \(O(n)\) time and reduces auxiliary space to \(O(1)\).
- **Floating-point slope comparison:** It is shorter mathematically but requires vertical-line handling and risks precision errors.
- **Reduced rational slopes:** Normalize each \((\Delta x,\Delta y)\) by its greatest common divisor. This remains exact but does more work than one cross multiplication.
- **Exactly two points:** The slice is empty and the loop finds no contradiction. Any two distinct points form a straight line, so the method returns true.
- **Vertical line:** Cross multiplication handles zero horizontal difference without division.
- **Horizontal line:** Zero vertical difference is handled by the same equality.
- **Negative coordinates and slopes:** Subtraction and signed multiplication work unchanged.
- **Early off-line point:** The method returns false immediately because one counterexample is enough.
- **Duplicate anchor points:** The contract excludes duplicates. If the first two were identical, they could not define the reference direction.
- **Integer overflow outside Python:** Use a wide enough product type in languages with fixed-width integers.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let \(n=\lvert\texttt{coordinates}\rvert\). The loop checks \(n-2\) points with constant arithmetic per point, so running time is \(O(n)\). An early mismatch can stop sooner, but the worst case examines them all.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
