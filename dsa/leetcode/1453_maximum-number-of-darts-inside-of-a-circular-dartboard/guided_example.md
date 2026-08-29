# Guided Example: Maximum Number of Darts Inside of a Circular Dartboard

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"darts": [[-2, 0], [2, 0], [0, 2], [0, -2]], "r": 2}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Alice is throwing `n` darts on a very large wall. You are given an array `darts` where $\text{darts}[i] = [x_{i}, y_{i}]$ is the position of the $i^{\text{th}}$ dart that Alice threw on the wall.

The objective is to compute `4` from `{"darts": [[-2, 0], [2, 0], [0, 2], [0, -2]], "r": 2}` while avoiding redundant calculations and unnecessary overhead.

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

**Use pairs of boundary darts to generate candidate circles.** The dartboard radius is fixed. If two darts are farther than `2r` apart, no radius-`r` circle can contain both because the diameter is the greatest possible distance between two points in such a circle. If their distance is at most `2r`, there are one or two circle centers whose boundary passes through both points.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"darts": [[-2, 0], [2, 0], [0, 2], [0, -2]], "r": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The helper `possibleCenters(x1, y1, x2, y2)` computes those centers. Let the vector from the first dart to the second be `(dx, dy)` and its length be `d`. The center of any circle through both points must be equally distant from them, so it lies on their perpendicular bisector.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The midpoint `(mid_x, mid_y)` is the base point on that bisector. Drawing a segment from a candidate center to either dart forms a right triangle. Its hypotenuse is `r`, one leg from the midpoint to a dart has length `d / 2`, and the other leg from the midpoint to the center has length
`sqrt(r*r - (d/2)*(d/2))`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"darts": [[-2, 0], [2, 0], [0, 2], [0, -2]], "r": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Angular sweep around each anchor:** For each dart, compute the angular interval of centers at distance `r` that would also contain every other reachable dart, sort interval events, and find maximum overlap. This achieves the manifest's `O(n^2 log n)` time and `O(n)` space but requires careful wraparound and event ordering.
- **Pair centers with squared-distance counting:** Compare squared distances with `r*r` to avoid a square root for every counted dart. Center coordinates are still floating-point, but this improves constants without changing the cubic bound.
- **Try centers at dart positions only:** This is incorrect. An optimal circle's center need not coincide with any dart.
- **Generate only one center per pair:** This can miss a better placement on the other side of the chord. Both perpendicular signs matter.
- **Single dart:** No pair loop runs, and the initialized answer one is correct.
- **Pair farther than the diameter:** No fixed-radius circle contains both, so it generates no centers.
- **Pair exactly one diameter apart:** The two formulas coincide at the midpoint. Duplicate evaluation does not change the maximum.
- **Very close distinct darts:** The division by `d` is valid because points are unique, though floating-point care is important when `d` is small.
- **Dart on the boundary:** It counts as inside. The small epsilon protects this inclusive rule from rounding error.
- **All darts fit one circle:** Some pair-derived extremal center reaches all of them, and counting returns `n`.
- **Collinear darts:** The same chord geometry applies. Feasible pair centers lie on perpendicular lines, and the maximum is still found.
- **Negative coordinates:** Distances use coordinate differences and squares, so signs require no special handling.
- **Duplicate darts outside the contract:** `d = 0` would cause division by zero in `possibleCenters`. The uniqueness guarantee is essential to this exact implementation.
- **Floating comparison at d versus 2r:** The early rejection has no epsilon. Integer-coordinate distance calculations are usually stable here, but a defensive geometric implementation may compare squared distances with a tolerance.
- **Tolerance too large:** A generous epsilon could count points truly outside the board. The selected `1e-7` is intended only for floating rounding.
- **Complexity reporting:** Report `O(n^3)` time and `O(1)` auxiliary space for this exact source. Reserve `O(n^2 log n)` and `O(n)` for an implemented angular sweep.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of darts. There are `n(n - 1) / 2` unordered pairs. Each pair produces at most two centers using constant-time arithmetic. For each center, `countDarts` scans all `n` points. The exact implementation therefore takes `O(n^3)` time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
