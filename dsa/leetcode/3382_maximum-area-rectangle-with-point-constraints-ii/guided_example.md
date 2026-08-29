# Guided Example: Maximum Area Rectangle With Point Constraints II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"xCoord": [1, 1, 3, 3], "yCoord": [1, 3, 1, 3]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are n points on an infinite plane. You are given two integer arrays `xCoord` and `yCoord` where $(\text{xCoord}[i], \text{yCoord}[i])$ represents the coordinates of the $i^{\text{th}}$ point.

The objective is to compute `4` from `{"xCoord": [1, 1, 3, 3], "yCoord": [1, 3, 1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

**A valid vertical side must join consecutive points in its column.** Group all points by `x` in `columns` and sort each column's `y` values. Suppose a rectangle uses lower and upper corners at the same $x$. If another point in that column had a $y$ strictly between them, it would lie on the rectangle's vertical border and invalidate the rectangle.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"xCoord": [1, 1, 3, 3], "yCoord": [1, 3, 1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Therefore the two corner heights must be adjacent in that column's sorted list. The source records every consecutive pair `(lower,upper)` and appends the column coordinate to `segment_columns[lower,upper]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

This preprocessing creates only $O(n)$ vertical segments: a column with $p$ points contributes $p-1$ adjacent pairs.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"xCoord": [1, 1, 3, 3], "yCoord": [1, 3, 1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Cubic scan from version I:** It is simple for ten points but impossible for $2\cdot10^5$.
- **2D prefix grid:** Raw coordinates are too large and sparse.
- **2D range tree:** It can answer rectangle counts but is more complex than the offline x sweep.
- **Nonconsecutive vertical corners:** A point between them lies on the side, so they cannot form a valid rectangle.
- **Nonconsecutive matching columns:** An intermediate matching segment supplies forbidden border points.
- **Interior point:** Inclusive count becomes greater than four.
- **Horizontal-border point:** It is included by the closed y range and also raises the count.
- **Vertical-border point:** Consecutive-y filtering often prevents the candidate; inclusive counting provides final protection.
- **Duplicate coordinates:** The contract forbids them, which makes four counted points equal four distinct corners.
- **One point or one column:** No candidate exists and the answer is `-1`.
- **`left = 0`:** Negative prefix limit correctly sees no points.
- **Coordinate compression:** It preserves ordering and inclusive range semantics, not geometric distances; area still uses raw coordinates.
- **Fenwick one-based indexing:** Rank zero is never used.
- **Same x event limits:** Points are inserted once and all events receive the complete prefix.
- **Count below four:** It is rejected even though candidate construction should prevent it.
- **Generated source status:** With no local editorial, this derivation follows the exact segment generation, events, and Fenwick queries in `solution.py`.
- **Input preservation:** New zipped points and dictionaries are built without altering coordinate arrays.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the number of points. Sorting y-values within columns costs at most $O(n\log n)$ in aggregate. There are $O(n)$ adjacent vertical segments and therefore $O(n)$ candidate pairs across all segment groups. Sorting their x-lists is also $O(n\log n)$ aggregate work.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
