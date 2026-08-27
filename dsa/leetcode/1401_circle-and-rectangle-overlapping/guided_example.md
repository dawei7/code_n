# Guided Example: Circle and Rectangle Overlapping

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"radius": 1, "xCenter": 0, "yCenter": 0, "x1": 1, "y1": -1, "x2": 3, "y2": 1}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a circle represented as `(radius, xCenter, yCenter)` and an axis-aligned rectangle represented as `(x1, y1, x2, y2)`, where `(x1, y1)` are the coordinates of the bottom-left corner, and `(x2, y2)` are the coordinates of the top-right corner of the rectangle.

The objective is to compute `true` from `{"radius": 1, "xCenter": 0, "yCenter": 0, "x1": 1, "y1": -1, "x2": 3, "y2": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Find the rectangle point closest to the circle center

A circle and rectangle overlap exactly when some rectangle point lies within or on the circle. Among all rectangle points, the easiest one to test is the point closest to the circle center. If even that closest point is farther than the radius, every other rectangle point is farther too. If it is within the radius, it belongs to both shapes.

Because the rectangle is axis-aligned, the horizontal and vertical distances to it can be computed independently.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"radius": 1, "xCenter": 0, "yCenter": 0, "x1": 1, "y1": -1, "x2": 3, "y2": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Distance from one coordinate to an interval

The helper `f(i, j, k)` returns the distance from coordinate `k` to closed interval `[i,j]`:

- If `i <= k <= j`, the coordinate already lies within the interval, so distance is zero.
- If `k < i`, the nearest interval endpoint is `i`, so distance is `i - k`.
- If `k > j`, the nearest endpoint is `j`, so distance is `k - j`.

For the x-axis, `a = f(x1, x2, xCenter)` is the horizontal gap from the circle center to the rectangle. For the y-axis, `b = f(y1, y2, yCenter)` is the vertical gap.

These components identify the closest rectangle point implicitly. Its x-coordinate is the center's x clamped into `[x1,x2]`, and its y-coordinate is the center's y clamped into `[y1,y2]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The helper `f(i, j, k)` returns the distance from coordinate... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The four geometric positions

If the center lies inside the rectangle on both axes, $a=b=0$. The center itself belongs to both shapes, so overlap is immediate.

If the center aligns with the rectangle horizontally but lies above or below it, $a=0$ and $b$ is the vertical distance to the nearest horizontal edge.

If it aligns vertically but lies left or right, $b=0$ and $a$ is the distance to the nearest vertical edge.

If it lies diagonally beyond a corner, both components are positive, and the closest rectangle point is that corner.

The same formula handles all cases without separate edge and corner logic.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"radius": 1, "xCenter": 0, "yCenter": 0, "x1": 1, "y1": -1, "x2": 3, "y2": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit clamping:** Compute `closest_x = max(:** - **Explicit clamping:** Compute `closest_x = max(x1, min(xCenter, x2))` and similarly for y, then test squared distance. It is equivalent and often visually intuitive.
- **Separate edge and corner cases:** This works but creates many branches and makes it easy to miss a geometric position.
- **Rectangle-center projection:** Comparing only rectangle and circle centers is insufficient because rectangle dimensions matter.
- **Circle center inside rectangle:** Both gaps are zero, so overlap is true.
- **Rectangle inside circle:** Its closest point is certainly within the radius, so the method returns true.
- **Edge tangency:** One component is zero and the other equals the radius; non-strict comparison returns true.
- **Corner tangency:** $a^2+b^2=r^2$ also returns true.
- **Clearly separated shapes:** Minimum squared distance exceeds $r^2$, producing false.
- **Negative coordinates:** Interval distance uses ordinary ordering and works unchanged.
- **Large coordinates:** Squared comparison avoids floating-point square roots.
- **Axis alignment:** Independent coordinate clamping relies on the rectangle being axis-aligned, as guaranteed.
- **No mutation:** The method computes from scalar inputs and changes no shape representation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The algorithm performs a fixed number of comparisons, subtractions, multiplications, and additions, independent of coordinate magnitude. Time is $O(1)$ and auxiliary space is $O(1)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
