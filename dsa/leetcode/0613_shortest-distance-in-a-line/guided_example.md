# Guided Example: Shortest Distance in a Line

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Point": [{"x": -1}, {"x": 0}, {"x": 2}]}}`
- **Required output:** `{"columns": ["shortest"], "rows": [[1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Point`

The objective is to compute `{"columns": ["shortest"], "rows": [[1]]}` from `{"tables": {"Point": [{"x": -1}, {"x": 0}, {"x": 2}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Turn the geometric wording into a numerical operation.** Every row stores one integer coordinate on the x-axis. For two coordinates `a` and `b`, their distance is $\lvert a-b\rvert$. The task therefore has two parts: consider every valid pair of different points, and keep the smallest distance produced by any pair. The exact query expresses both parts inside one aggregate query.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Point": [{"x": -1}, {"x": 0}, {"x": 2}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Why the self-join is needed.** A row contains only one point, whereas a distance needs two points. Giving the table two aliases, `p1` and `p2`, lets one output row represent a pair. A completely unrestricted self-join would also pair every point with itself. Such a pair has distance zero, which would always become the minimum and would be invalid because the problem asks for two distinct points. It would also produce both orientations of every genuine pair: `(a, b)` and `(b, a)`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The join condition `p1.x < p2.x` solves all three concerns at once:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["shortest"], "rows": [[1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Point": [{"x": -1}, {"x": 0}, {"x": 2}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["shortest"], "rows": [[1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort and compare adjacent points:** After coordinates are ordered, the globally closest pair must be adjacent; any coordinate between two nonadjacent endpoints would create an equal or smaller neighboring gap. This gives the manifest's intended $O(P\log P)$ bound and is the preferable large-input algorithm.
- **Already ordered input:** If ascending order is guaranteed by an index scan or another explicit ordering contract, use a previous-row operation such as `LAG(x)` and minimize `x - previous_x`. The scan is linear after the ordered access.
- **Unrestricted self-join plus `ABS`:** Joining on `p1.x != p2.x` is correct, but it emits both orientations of every pair. The strict `<` condition performs half as much pair work and removes the need for `ABS`.
- **Self-pairs:** Omitting the inequality condition makes every row pair with itself, forcing the minimum to zero. The primary key does not prevent that mistake because the two aliases may refer to the same row.
- **Negative coordinates:** They require no special case. Once `p1.x < p2.x`, the subtraction `p2.x - p1.x` is positive even when one or both coordinates are negative.
- **Exactly two rows:** The join produces one candidate, so that sole distance is returned.
- **Fewer than two rows:** The official contract excludes this case. If it occurred, the aggregate would still return one row, but its `shortest` value would be `NULL`.
- **Duplicate coordinates:** The primary key forbids them. If duplicates were allowed, two distinct rows at the same coordinate would have distance zero, but the strict `<` condition would omit that valid pair; the query relies on uniqueness.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P^2)$. Let $P$ be the number of rows in `Point`.
- **Auxiliary Space Complexity:** $O(P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
