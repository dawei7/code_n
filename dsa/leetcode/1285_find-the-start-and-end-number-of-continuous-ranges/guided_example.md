# Guided Example: Find the Start and End Number of Continuous Ranges

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Logs": {"columns": ["log_id"], "rows": []}}}`
- **Required output:** `{"columns": ["start_id", "end_id"], "rows": []}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Logs`

The objective is to compute `{"columns": ["start_id", "end_id"], "rows": []}` from `{"tables": {"Logs": {"columns": ["log_id"], "rows": []}}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Detect where a new continuous range begins

Because `log_id` values are unique, sorting them reveals maximal runs of consecutive integers. A row continues the previous range exactly when its identifier is one greater than the preceding identifier.

The innermost query uses `LAG(log_id) OVER (ORDER BY log_id)` to retrieve the preceding sorted value. It computes `delta` as zero when the difference equals one and one otherwise:

`IF((log_id - LAG(...)) = 1, 0, 1)`.

For the first sorted row, `LAG` returns `NULL`. Arithmetic and comparison with `NULL` produce `NULL`, and MySQL's `IF` treats that condition as not true, selecting one. Therefore the first row correctly starts range number one.

For identifiers `1,2,3,7,8,10`, delta values are `1,0,0,1,0,1`. A one marks each gap boundary.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Logs": {"columns": ["log_id"], "rows": []}}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Turn boundary markers into a stable group identifier

The next query level computes the running sum

`SUM(delta) OVER (ORDER BY log_id) AS pid`.

Within consecutive rows, delta is zero, so the cumulative value stays unchanged. At a gap, delta one increments it. All identifiers in one maximal continuous range therefore share one `pid`, while different ranges have different values.

The window operations are separated into nested queries because the cumulative sum consumes the result of `LAG`; SQL window functions generally cannot be nested directly in one expression at the same query level.

For the example, cumulative identifiers are `1,1,1,2,2,3`, assigning the expected three groups.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The next query level computes the running sum

`SUM(delta) O... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Collapse each group to its endpoints

The outer query groups by `pid`. Since every group contains a sorted consecutive run, its smallest `log_id` is the range start and its largest is the range end. `MIN(log_id) AS start_id` and `MAX(log_id) AS end_id` produce exactly those endpoints.

A one-element range has identical minimum and maximum, correctly returning the same start and end.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["start_id", "end_id"], "rows": []}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Logs": {"columns": ["log_id"], "rows": []}}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["start_id", "end_id"], "rows": []}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`log_id - ROW_NUMBER()` grouping:** For consec:** - **`log_id - ROW_NUMBER()` grouping:** For consecutive values, subtracting their sorted row number remains constant. Grouping by that difference is a compact islands-and-gaps technique.
- **Recursive range construction:** It is more complex and unnecessary when window functions are available.
- **Single identifier:** Delta starts at one, one group forms, and start equals end.
- **All identifiers consecutive:** The cumulative group identifier never changes after the first row, producing one range.
- **Every pair separated:** Every delta is one, so each identifier becomes a singleton range.
- **Negative or nonstarting identifiers:** Only differences matter; the logic does not require IDs to start at one.
- **Unique-value guarantee:** Duplicate identifiers would produce difference zero and require a clarified meaning, but the schema excludes them.
- **First-row null:** MySQL `IF` selects the else branch for the null comparison, correctly marking a new group.
- **Missing final ordering:** Add `ORDER BY start_id` for a result whose required order is guaranteed rather than incidental.
- **Window sort reuse:** An optimizer may reuse ordering between window stages, affecting constants but not the worst-case bound.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the number of log rows. Both window functions require `log_id` order. Without a supporting execution order, sorting costs $O(n\log n)$ time. Window scans and final aggregation are linear after ordering, so total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
