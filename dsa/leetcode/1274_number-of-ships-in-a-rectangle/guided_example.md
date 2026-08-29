# Guided Example: Number of Ships in a Rectangle

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"sea": {"ships": [], "max_queries": 400}, "topRight": [7, 9], "bottomLeft": [2, 4]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

*(This problem is an **interactive problem**.)*

The objective is to compute `0` from `{"sea": {"ships": [], "max_queries": 400}, "topRight": [7, 9], "bottomLeft": [2, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the API to discard large empty regions

Checking every integer coordinate would exceed the four-hundred-call limit. The API is powerful because one call answers whether an entire inclusive rectangle contains at least one ship. The solution recursively divides only rectangles known to contain ships, while empty rectangles stop immediately.

Function `dfs(topRight, bottomLeft)` first extracts inclusive bounds `x1, y1, x2, y2`. Some quadrants of a thin rectangle can be invalid, so `x1 > x2 or y1 > y2` returns zero before calling the API. This ordering avoids unauthorized or meaningless queries with reversed corners.

For a valid rectangle, `sea.hasShips` is called. A false result proves the count is zero and prunes every coordinate inside. If the rectangle is one point and the API has returned true, that point contains exactly one ship because the contract allows at most one per integer point.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"sea": {"ships": [], "max_queries": 400}, "topRight": [7, 9], "bottomLeft": [2, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Partition an inclusive rectangle without gaps or overlaps

For a nonempty rectangle containing more than one point, midpoint coordinates are floor averages. The four recursive rectangles are:

- northeast: from `(midx + 1, midy + 1)` to the original top right;
- northwest: from `(x1, midy + 1)` to `(midx, y2)`;
- southwest: from the original bottom left to `(midx, midy)`;
- southeast: from `(midx + 1, y1)` to `(x2, midy)`.

The `+1` boundaries are essential for inclusive coordinates. Every x-coordinate belongs either to the left half through `midx` or the right half starting at `midx + 1`, and the same holds for y. Combining those choices creates four disjoint quadrants whose union is the original rectangle.

When one dimension has length one, two quadrant descriptions become invalid. The initial bound check returns zero for them without consuming API calls, while the valid halves still cover the rectangle.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why summing recursive answers is correct

An empty rectangle returns zero by authoritative API evidence. A nonempty single point returns one. Otherwise, every ship belongs to exactly one of the four disjoint quadrants. By recursively counting each quadrant and summing `a + b + c + d`, the algorithm counts every ship once and none twice.

The recursion eventually terminates because every valid child is strictly smaller in at least one non-single dimension. Repeated halving reaches individual points.

The method never tries to inspect hidden ship coordinates directly. `Point` objects only describe query corners, and `hasShips` is the sole observation of the sea, respecting the interactive contract.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"sea": {"ships": [], "max_queries": 400}, "topRight": [7, 9], "bottomLeft": [2, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Check every coordinate:** It is exact but may require about a million API calls and violates the limit.
- **Split into two rectangles:** Binary partitioning is also possible; four-way splitting halves both dimensions together and matches the sparse two-dimensional geometry well.
- **Call API before validating bounds:** This can send reversed rectangles created by thin quadrants and must be avoided.
- **Empty target rectangle:** Public corners are ordered, but recursive empty quadrants correctly return zero without an API call.
- **No ships:** The initial `hasShips` call is false, so the answer is zero immediately.
- **Single-point recursive region:** A true API result means exactly one ship; further subdivision is unnecessary.
- **Ship on a midpoint boundary:** Inclusive half definitions assign it to exactly one side because the other begins at midpoint plus one.
- **One-row or one-column region:** Invalid quadrants vanish, and valid halves continue reducing the remaining dimension.
- **Ships on outer boundaries:** `hasShips` includes rectangle boundaries, and the partition covers them.
- **API call limit:** Pruning empty regions is essential; recursion without the initial existence query would still explore every point.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1+s\log C)$. Let $s$ be the number of ships and let $C$ be the larger inclusive side length. Empty input still causes one API query. In general, only branches containing ships continue for $O(\log C)$ levels, with a constant number of empty siblings per continuing branch. Time and API calls are $O(1+s\log C)$, commonly written $O(s\log C)$ when $s>0$.
- **Auxiliary Space Complexity:** $O(\log C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
