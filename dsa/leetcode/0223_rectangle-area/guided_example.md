# Guided Example: Rectangle Area

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"ax1": -3, "ay1": 0, "ax2": 3, "ay2": 4, "bx1": 0, "by1": -1, "bx2": 9, "by2": 2}`
- **Required output:** `45`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given the coordinates of two **rectilinear** rectangles in a 2D plane, return *the total area covered by the two rectangles*.

The objective is to compute `45` from `{"ax1": -3, "ay1": 0, "ax2": 3, "ay2": 4, "bx1": 0, "by1": -1, "bx2": 9, "by2": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Start with inclusion-exclusion

The area of rectangle A is its horizontal side length times its vertical side
length:

$$
A = (\texttt{ax2}-\texttt{ax1})(\texttt{ay2}-\texttt{ay1}).
$$

Rectangle B has the analogous area

$$
B = (\texttt{bx2}-\texttt{bx1})(\texttt{by2}-\texttt{by1}).
$$

Adding $A+B$ counts every point covered by either rectangle, but a point in
their intersection is included once in $A$ and once in $B$. The union area
therefore follows the two-set inclusion-exclusion formula:

$$
\operatorname{area}(A\cup B)
= A+B-\operatorname{area}(A\cap B).
$$

The only nontrivial part is finding the intersection area. Because both
rectangles are axis-aligned, their two-dimensional intersection is determined
independently by the overlap of their x-intervals and y-intervals.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"ax1": -3, "ay1": 0, "ax2": 3, "ay2": 4, "bx1": 0, "by1": -1, "bx2": 9, "by2": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find the horizontal interval shared by both rectangles

Rectangle A spans horizontally from `ax1` to `ax2`, while B spans from `bx1`
to `bx2`. Any shared interval must begin at the later left edge,
`max(ax1, bx1)`, because points before that coordinate are outside whichever
rectangle starts later. It must end at the earlier right edge,
`min(ax2, bx2)`, because points after that coordinate are outside whichever
rectangle ends earlier.

The candidate overlap width is therefore

$$
\texttt{width}
= \min(\texttt{ax2},\texttt{bx2})
- \max(\texttt{ax1},\texttt{bx1}).
$$

If this value is positive, it is the length of the shared horizontal segment.
If it is zero, the projections only touch at an edge, which has zero area. If
it is negative, there is a horizontal gap and no intersection. The expression
`max(width, 0)` converts all non-overlap cases to zero while retaining a real
overlap length unchanged.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Rectangle A spans horizontally from `ax1` to `ax2`, while B ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Apply the same reasoning vertically

The shared vertical interval begins at the higher bottom edge,
`max(ay1, by1)`, and ends at the lower top edge,
`min(ay2, by2)`. Its candidate height is

$$
\texttt{height}
= \min(\texttt{ay2},\texttt{by2})
- \max(\texttt{ay1},\texttt{by1}).
$$

Again, `max(height, 0)` is the actual nonnegative overlap length.

Two rectangles have positive intersection area only when their projections
overlap positively on both axes. Since the intersection, when present, is
itself an axis-aligned rectangle, its area is
`max(height, 0) * max(width, 0)`.

Clamping each dimension separately is important. Using
`max(width * height, 0)` would be wrong: if the rectangles are separated both
horizontally and vertically, both candidate lengths can be negative, and their
product would be spuriously positive even though the rectangles do not meet.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `45` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"ax1": -3, "ay1": 0, "ax2": 3, "ay2": 4, "bx1": 0, "by1": -1, "bx2": 9, "by2": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `45` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit overlap branch:** Test whether `width:** - **Explicit overlap branch:** Test whether `width > 0 and height > 0`, set overlap to their product only then, and otherwise use zero. It is equivalent to separately clamping both dimensions but needs more control flow.
- **Plane partitioning:** Split the plane at all rectangle edges and sum covered cells. It can work but is unnecessary for only two rectangles and introduces much more machinery than inclusion-exclusion.
- **No overlap on one axis:** A horizontal or vertical gap makes one clamped dimension zero, so the intersection area is zero regardless of the other dimension.
- **Touching edges:** Candidate width or height is exactly zero. A shared boundary line has zero area, so subtracting zero is correct.
- **Touching at one corner:** Both overlap dimensions are zero; the single shared point has zero area.
- **One rectangle inside the other:** Both overlap intervals equal the inner rectangle's intervals. Subtracting the inner area from the sum leaves exactly the outer area.
- **Identical rectangles:** The overlap equals either full rectangle, preventing the same area from being counted twice.
- **Degenerate rectangles:** The constraints permit equal left and right coordinates or equal bottom and top coordinates. Such a rectangle has zero area, and the same formulas still produce the correct union.
- **Negative coordinates:** Side lengths use differences between ordered endpoints, so crossing or lying left/below the origin changes no reasoning.
- **Large coordinate products:** Python has arbitrary-precision integers. In a fixed-width language, an adequately wide integer type should be used for multiplication.
- **Axis mix-up:** Horizontal overlap must use only x-coordinates and vertical overlap only y-coordinates. Combining an x endpoint with a y endpoint has no geometric meaning.
- **Input preservation:** All coordinates are immutable numbers, and the method computes derived values without changing any input object.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The method performs a fixed number of subtractions, multiplications, `min`
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
