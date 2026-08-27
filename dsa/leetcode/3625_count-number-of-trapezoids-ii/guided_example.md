# Guided Example: Count Number of Trapezoids II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"points": [[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D integer array `points` where $\text{points}[i] = [x_{i}, y_{i}]$ represents the coordinates of the $$i^{\text{th}}$$ point on the Cartesian plane.

The objective is to compute `2` from `{"points": [[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Representing one segment's line

For endpoints `(x1,y1)` and `(x2,y2)`, the source computes `dx=x2-x1` and `dy=y2-y1`.

For a nonvertical segment:

`k = dy/dx`

is its slope. The expression:

`b = (y1*dx - x1*dy)/dx`

equals `y1-k*x1`, the y-intercept. Segments have the same slope and intercept exactly when they lie on the same infinite supporting line.

For a vertical segment, ordinary slope is undefined. The source uses sentinel `k=1e9` and uses `b=x1` to distinguish vertical supporting lines by x-coordinate. Actual finite slopes are at most 2000 in magnitude under the coordinate limits, so the sentinel does not overlap them.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"points": [[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: First grouping: slope to supporting-line counts

`cnt1[k][b]` counts how many point-pair segments lie on supporting line `b` with slope `k`.

For one slope group, let the counts on distinct lines be `t1,t2,...`. Choosing one segment from line A and one from different parallel line B gives four distinct endpoints:

- different parallel lines cannot share a point;
- the two segments form opposite parallel sides;
- connecting their endpoints in boundary order creates a convex trapezoid.

The source combines line groups with a running total `s`. For current count `t`, `s*t` counts choices with every earlier supporting line. This sums:

$$
\sum_{a<b}t_at_b.
$$

Pairs from the same supporting line are deliberately excluded because four collinear endpoints do not form a quadrilateral.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `cnt1[k][b]` counts how many point-pair segments lie on supp... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why parallelograms are counted twice

A trapezoid with exactly one pair of parallel opposite sides appears in exactly one slope group.

A parallelogram has two pairs of parallel opposite sides. Its four vertices therefore generate:

- one segment pair for one side slope;
- another segment pair for the other side slope.

The first phase counts the same four-point parallelogram twice, while the problem wants each unique quadrilateral once. One duplicate contribution per parallelogram must be subtracted.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"points": [[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Exact normalized slope:** Divide `(dy,dx)` by :** - **Exact normalized slope:** Divide `(dy,dx)` by their gcd and normalize sign, avoiding float-key concerns.
- **Tuple midpoint key:** Use `(x1+x2,y1+y2)` directly, eliminating the base-4000 collision.
- **Base 4001 encoding:** It also distinguishes every legal offset pair, though a tuple is clearer.
- **Only one parallel-side pair:** The quadrilateral is counted once in `cnt1` and not subtracted.
- **Parallelogram:** It is counted twice by side slopes and once by diagonal midpoint, leaving one.
- **Rectangle or rhombus:** Both are parallelograms and follow the same correction.
- **Four collinear points:** Same-line segment pairs are not combined because the intercept group is not paired with itself.
- **Vertical sides:** Sentinel slope and x-coordinate line key group them separately.
- **Segments sharing an endpoint:** Parallel segments on different lines cannot share an endpoint, so first-phase selections use four distinct points.
- **Same-midpoint collinear segments:** Equal slopes are not paired in `cnt2`, avoiding degenerate subtraction.
- **Boundary coordinate sums:** They expose the exact source's midpoint encoding collision.
- **No parallel segments:** The first phase contributes zero, so the answer is zero.
- **Duplicate points:** The constraints exclude them; zero-length segments need no handling.
- **Missing imports:** Standalone use must provide `defaultdict` and `List`.
- **Input preservation:** The algorithm only reads `points` and stores derived segment statistics.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let `n` be the number of points and `q=n(n-1)/2=O(n^2)` the number of segments.
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
