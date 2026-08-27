# Guided Example: Count Number of Trapezoids I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"points": [[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D integer array `points`, where $\text{points}[i] = [x_{i}, y_{i}]$ represents the coordinates of the $$i^{\text{th}}$$ point on the Cartesian plane.

The objective is to compute `3` from `{"points": [[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count points by height

`Counter(p[1] for p in points)` maps each y-coordinate to the number of input points lying on that horizontal line.

All points are distinct. At one height, distinct points cannot share both x and y, so any pair has different x-coordinates and forms a nonzero horizontal segment.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"points": [[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count horizontal segments at one height

If a height contains `v` points, the number of unordered endpoint pairs is:

$$
\binom{v}{2}=\frac{v(v-1)}2.
$$

The source stores this count in `t`. Heights containing zero or one point produce `t=0` and cannot supply a trapezoid side.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If a height contains `v` points, the number of unordered end... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Combine sides from different heights

Choosing one horizontal segment at height `y_1` and another at different height `y_2` determines four distinct points. Ordering the lower segment's endpoints and upper segment's endpoints around their boundary forms a convex quadrilateral with those two horizontal sides parallel.

Thus every pair of segments from two different height groups creates one horizontal trapezoid.

The source avoids a quadratic loop over all pairs of heights. `s` stores the total number of horizontal segments seen at earlier heights. For the current height with `t` segments:

`s * t`

counts every choice of one earlier segment and one current segment.

After adding that contribution, `s += t` makes the current segments available to later heights.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"points": [[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Double loop over heights:** Compute each segme:** - **Double loop over heights:** Compute each segment count, then multiply every pair. It is correct but can take `O(h^2)` time.
- **Prefix sum of segment counts:** This is exactly the role of scalar `s`; no prefix array is necessary.
- **Enumerate all four-point subsets:** It costs `O(n^4)` and repeats geometry checks.
- **One point at a height:** It creates no horizontal side and contributes zero.
- **Two points at a height:** They create exactly one possible side.
- **All points at one height:** There is no second parallel supporting line, so the answer is zero.
- **Every point at a distinct height:** Every `t` is zero and the answer is zero.
- **Negative y-coordinates:** Counter keys handle them exactly like positive heights.
- **Negative or unordered x-coordinates:** Only equality of y matters for choosing a horizontal segment.
- **Parallelogram:** It is a trapezoid under “at least one pair” and is counted once by its two horizontal sides.
- **Modulo:** Only the returned count is reduced; geometric uniqueness is counted over ordinary integers first.
- **Counter iteration order:** It affects which height is “earlier” but not the total over unordered height pairs.
- **Input preservation:** The source reads coordinates and never sorts or mutates `points`.
- **Missing imports:** Standalone use must provide `Counter` and `List`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of points and `h` the number of distinct y-coordinates.
- **Auxiliary Space Complexity:** $O(h)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
