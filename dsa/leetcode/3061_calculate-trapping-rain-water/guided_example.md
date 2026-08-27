# Guided Example: Calculate Trapping Rain Water

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Heights": [{"id": 1, "height": 0}, {"id": 2, "height": 1}, {"id": 3, "height": 0}, {"id": 4, "height": 2}, {"id": 5, "height": 1}, {"id": 6, "height": 0}, {"id": 7, "height": 1}, {"id": 8, "height": 3}, {"id": 9, "height": 2}, {"id": 10, "height": 1}, {"id": 11, "height": 2}, {"id": 12, "height": 1}]}}`
- **Required output:** `{"columns": ["total_trapped_water"], "rows": [[6]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: Heights

The objective is to compute `{"columns": ["total_trapped_water"], "rows": [[6]]}` from `{"tables": {"Heights": [{"id": 1, "height": 0}, {"id": 2, "height": 1}, {"id": 3, "height": 0}, {"id": 4, "height": 2}, {"id": 5, "height": 1}, {"id": 6, "height": 0}, {"id": 7, "height": 1}, {"id": 8, "height": 3}, {"id": 9, "height": 2}, {"id": 10, "height": 1}, {"id": 11, "height": 2}, {"id": 12, "height": 1}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Water above a bar is limited from both sides.** At position $i$, define:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Heights": [{"id": 1, "height": 0}, {"id": 2, "height": 1}, {"id": 3, "height": 0}, {"id": 4, "height": 2}, {"id": 5, "height": 1}, {"id": 6, "height": 0}, {"id": 7, "height": 1}, {"id": 8, "height": 3}, {"id": 9, "height": 2}, {"id": 10, "height": 1}, {"id": 11, "height": 2}, {"id": 12, "height": 1}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

$$
L_i=\max_{j\le i}\texttt{height}[j],
\qquad
R_i=\max_{j\ge i}\texttt{height}[j].
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | $$
L_i=\max_{j\le i}\texttt{height}[j],
\qquad
R_i=\max_{j\g... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The water surface cannot exceed the tallest boundary available on the left or the tallest boundary on the right. Therefore its height is $\min(L_i,R_i)$, and water stored above the current bar is

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["total_trapped_water"], "rows": [[6]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Heights": [{"id": 1, "height": 0}, {"id": 2, "height": 1}, {"id": 3, "height": 0}, {"id": 4, "height": 2}, {"id": 5, "height": 1}, {"id": 6, "height": 0}, {"id": 7, "height": 1}, {"id": 8, "height": 3}, {"id": 9, "height": 2}, {"id": 10, "height": 1}, {"id": 11, "height": 2}, {"id": 12, "height": 1}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["total_trapped_water"], "rows": [[6]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Correlated subqueries for each side maximum:**:** - **Correlated subqueries for each side maximum:** They express the formula directly but may rescan large portions of the table for every bar, causing quadratic work.
- **Self joins and grouping:** Joining all left and right candidates creates large intermediate relations; window maxima are much cleaner.
- **Two-pointer algorithm outside SQL:** In an imperative language it reaches $O(N)$ time and $O(1)$ space, but relational SQL naturally favors windows.
- **Monotonically increasing heights:** Right boundaries never create a basin, so every contribution is zero.
- **Monotonically decreasing heights:** The symmetric result is also zero.
- **Flat plateau:** Both maxima equal the bar height and no water is stored.
- **Interior zero height:** It can hold water up to the smaller surrounding maximum.
- **Current bar included in maxima:** This guarantees nonnegative contributions automatically.
- **Sequential IDs:** Their ordering defines adjacent unit-width bars; the formula relies on it.
- **Empty table:** The exact aggregate returns null, not zero.
- **Width-one assumption:** Each row represents exactly one horizontal unit, so no multiplication by an interval width is needed. Nonuniform or missing positions would require using coordinate differences.
- **Boundary bars:** At the global tallest bar, both directional maxima equal its own height and contribution is zero. Exterior endpoints likewise cannot trap water beyond the landscape.
- **Multiple equal maxima:** Window functions retain the same boundary height across the plateau; basins between equal peaks are handled without selecting a unique wall.
- **No negative correction required:** Since both running maxima include the current row, `LEAST(l,r)` is always at least `height`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. For $N$ bars, the two window functions require ordering by `id` in opposite directions. A typical database plan costs $O(N\log N)$ time and $O(N)$ temporary space. A clustered or indexed `id` may help one direction, though the reverse window or engine materialization can still require work.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
