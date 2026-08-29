# Guided Example: Find Nearest Point That Has the Same X or Y Coordinate

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"x": 3, "y": 4, "points": [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integers, `x` and `y`, which represent your current location on a Cartesian grid: `(x, y)`. You are also given an array `points` where each $\text{points}[i] = [a_{i}, b_{i}]$ represents that a point exists at $(a_{i}, b_{i})$. A point is **valid** if it shares the same x-coordinate or the same y-coordinate as your location.

The objective is to compute `2` from `{"x": 3, "y": 4, "points": [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Filter by the validity rule before comparing distance

A point `(a, b)` is valid when it lies on the same vertical line or horizontal line as `(x, y)`. The exact condition is:

`a == x or b == y`.

Only valid points compete for the answer. An invalid point may be geometrically close, but it must be ignored completely.

The exact solution scans points in original index order and keeps the best valid distance found so far.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"x": 3, "y": 4, "points": [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compute Manhattan distance

For each valid point, the source calculates:

`abs(a - x) + abs(b - y)`.

This is the stated Manhattan distance. Because a valid point shares at least one coordinate, one term is zero, but using the full formula is clear and works even when both coordinates match.

A point at the exact current location has distance zero and is valid through both equalities. Zero is the smallest possible distance.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Maintain the best index and distance

`ans` begins at minus one, meaning no valid point has been seen. `mi` begins at positive infinity, so the first valid finite distance is always accepted.

For each valid point at index `i`, the source updates only when:

`mi > d`.

The strict inequality means a genuinely smaller distance replaces the current best. It assigns both `ans = i` and `mi = d` together.

If the new distance equals `mi`, no update occurs. Since indices are visited from zero upward, the stored point is already the smallest index among all points at that distance. This implements the tie rule without an explicit index comparison.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"x": 3, "y": 4, "points": [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort valid candidates:** Sorting by `(distance, index)` is correct but costs $O(n\log n)$ time and extra storage.
- **Build a filtered list:** It makes validity explicit but uses $O(n)$ space that a streaming minimum avoids.
- **Check same x only:** It would miss valid points sharing y.
- **Check same y only:** It would miss valid points sharing x.
- **Use AND instead of OR:** It would accept only the identical location, which is too restrictive.
- **No valid points:** `ans` never changes and minus one is returned.
- **Exact same location:** Distance zero is valid and cannot be beaten.
- **Several zero-distance duplicates:** The earliest index remains because updates are strict.
- **Equal nearest distances:** Scan order plus strict comparison keeps the smallest index.
- **Later smaller distance:** It replaces the earlier farther point even though its index is larger.
- **Valid vertical point:** `a == x` and distance reduces to `abs(b-y)`.
- **Valid horizontal point:** `b == y` and distance reduces to `abs(a-x)`.
- **Point sharing both coordinates:** Both validity clauses are true, but it is still processed once.
- **Positive coordinate bounds:** They are irrelevant to the logic; only differences matter.
- **Input preservation:** Enumeration reads points in their original order, which is essential for implicit tie handling.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of points. The loop visits each point once and performs a constant number of integer comparisons, subtractions, absolute values, and assignments. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
