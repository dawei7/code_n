# Guided Example: Find Maximum Area of a Triangle

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"coords": [[1, 1], [1, 2], [3, 2], [3, 3]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D array `coords` of size `n x 2`, representing the coordinates of `n` points in an infinite Cartesian plane.

The objective is to compute `2` from `{"coords": [[1, 1], [1, 2], [3, 2], [3, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Best base on one vertical line

For every x-coordinate, dictionaries `f` and `g` store the minimum and maximum y-coordinates seen on that line.

Any vertical base on line `x` has length at most:

`g[x]-f[x]`.

Using the extreme endpoints is always optimal for any fixed third-point height because it maximizes the base independently.

If only one point exists on that line, the difference is zero and no positive-area triangle can use it as a vertical base.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"coords": [[1, 1], [1, 2], [3, 2], [3, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Best perpendicular height

`mn` and `mx` are the smallest and largest x-coordinates among all points. For a base on line `x`, the farthest possible horizontal distance is:

`max(mx-x, x-mn)`.

No interior x-coordinate can be farther than both global extremes. The y-coordinate of the third point does not affect perpendicular height to a vertical line, so any point at the chosen extreme x works.

The candidate doubled area is therefore:

`(g[x]-f[x]) * max(mx-x, x-mn)`.

The helper maximizes this product over every line containing points.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why base and height choices combine

The two base endpoints are chosen from points sharing `x`. The third point is chosen at an extreme different x-coordinate. These selections are independent: changing the third point’s y does not change horizontal height, and changing base endpoints within the same line does not change that height.

If height is zero, all points lie on the same vertical line and any triangle is degenerate. If base is zero, the line has fewer than two distinct points. Only a positive product forms a valid triangle.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"coords": [[1, 1], [1, 2], [3, 2], [3, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Group both axes separately:** Build extrema maps for equal x and equal y without mutating coordinates. This uses similar `O(n)` time and space with clearer input preservation.
- **Enumerate triples:** Testing every three points costs `O(n^3)` and is unnecessary because only line extrema matter.
- **Enumerate bases and third points:** Even grouping axis-parallel pairs can become quadratic; line and global extrema collapse both choices.
- **All points on one line:** Perpendicular height is zero, so the answer is `-1`.
- **Axis-parallel pair but no off-line point:** The product remains zero and cannot form a triangle.
- **Several points on one line:** Only minimum and maximum perpendicular coordinates are needed for the widest base.
- **Third point vertically between base endpoints:** Its parallel coordinate is irrelevant; perpendicular distance alone determines area.
- **Unique coordinates:** Base endpoints are distinct whenever their stored extrema differ.
- **One or two points:** No positive-area triangle exists, and zero maximum maps to `-1`.
- **Horizontal-only optimum:** It is discovered after transposition.
- **Vertical-only optimum:** It is discovered by the first call.
- **Equal best orientations:** Either produces the same stored maximum.
- **Positive coordinate constraint:** Initial `mx=0` is safe because every coordinate is at least one; generalized negative coordinates would require `-inf`.
- **Mutated argument:** After the method, every input point is `[old_y,old_x]`; this should be documented or repaired in reusable code.
- **Why twice-area is integral:** Coordinate differences are integers, so `base*height` is an integer even when the geometric area itself is a half-integer. Returning the product exactly matches the requested doubled quantity.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Each `calc` call scans all `n` points and then all distinct line keys, taking `O(n)` expected time with hash dictionaries. Two calls plus the transpose pass remain `O(n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
