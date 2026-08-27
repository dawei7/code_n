# Guided Example: Count Lattice Points Inside a Circle

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"circles": [[2, 2, 1]]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a 2D integer array `circles` where $\text{circles}[i] = [x_{i}, y_{i}, r_{i}]$ represents the center $(x_{i}, y_{i})$ and radius $r_{i}$ of the $$i^{\text{th}}$$ circle drawn on a grid, return *the **number of lattice points** **that are present inside **at least one** circle*.

The objective is to compute `5` from `{"circles": [[2, 2, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Search every lattice point that could possibly be covered

A lattice point has integer coordinates. For circle center `(x,y)` and radius `r`, a point `(i,j)` is inside or on the circle exactly when

$$
(i-x)^2 + (j-y)^2 \le r^2.
$$

The solution enumerates candidate integer coordinates and checks this squared-distance condition. Squared values avoid floating-point square roots and include the circumference through `<=`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"circles": [[2, 2, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find global upper coordinate bounds

No circle extends right of `x + r` or above `y + r`. The code computes

`mx = max(x + r for x, _, r in circles)`

and the analogous `my`. Every covered point must have horizontal coordinate at most `mx` and vertical coordinate at most `my`.

The loops begin at zero. This is sufficient because the constraints state `r <= min(x, y)`, so every circle's leftmost coordinate `x-r` and lowest coordinate `y-r` are nonnegative. There are no covered negative-coordinate lattice points to examine.

Thus, the rectangle `[0,mx] \times [0,my]` contains the union of all circles.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | No circle extends right of `x + r` or above `y + r`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Test one point against circles

For each integer pair `(i,j)` in the bounding rectangle, the innermost loop visits circles. It calculates `dx = i - x` and `dy = j - y`, then checks

`dx * dx + dy * dy <= r * r`.

On the first circle that contains the point, `ans` is incremented and `break` exits the circle loop.

The break is essential for union counting. A point inside three overlapping circles is still one lattice point and must be counted once, not three times.

If no circle passes, the loop finishes without changing `ans`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"circles": [[2, 2, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Per-circle enumeration with a set:** Visit eac:** - **Per-circle enumeration with a set:** Visit each circle's bounding square and insert covered coordinates into a set. This matches the manifest and can avoid testing distant points against every circle, but uses space proportional to the union.
- **Scan only each circle's horizontal slices:** For each integer row, derive the covered x interval. Merging intervals can be more efficient but is more complex.
- **Use Euclidean square roots:** Floating-point calculations are unnecessary and can create boundary precision issues; squared distances are exact.
- **Overlapping circles:** A point is counted once because its coordinate is visited once and the circle loop breaks.
- **Point on circumference:** Equality is included.
- **One circle:** The same global scan checks its exact disk.
- **Radius one:** The center and four axis neighbors are the only lattice points.
- **Disjoint circles:** Points from both regions are visited and counted independently.
- **Nonnegative lower bound:** Starting loops at zero relies on `r <= x` and `r <= y`.
- **Maximum coordinates:** Global bounds include `x+r` and `y+r` through the `+1` range endpoints.
- **No set allocation:** Duplicate avoidance comes from visiting each coordinate once.
- **Input preservation:** Circle definitions are only read.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(XYC)$. Let `C` be the number of circles, `X = mx + 1`, and `Y = my + 1`. The code visits `XY` candidate points and may test all `C` circles for each. Worst-case time is `O(XYC)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
