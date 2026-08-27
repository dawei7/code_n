# Guided Example: Get the Second Most Recent Activity

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"UserActivity": [{"username": "Alice", "activity": "Travel", "startDate": "2020-02-12", "endDate": "2020-02-20"}, {"username": "Alice", "activity": "Dancing", "startDate": "2020-02-21", "endDate": "2020-02-23"}, {"username": "Alice", "activity": "Travel", "startDate": "2020-02-24", "endDate": "2020-02-28"}, {"username": "Bob", "activity": "Travel", "startDate": "2020-02-11", "endDate": "2020-02-18"}]}}`
- **Required output:** `{"columns": ["username", "activity", "startDate", "endDate"], "rows": [["Alice", "Dancing", "2020-02-21", "2020-02-23"], ["Bob", "Travel", "2020-02-11", "2020-02-18"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `UserActivity`

The objective is to compute `{"columns": ["username", "activity", "startDate", "endDate"], "rows": [["Alice", "Dancing", "2020-02-21", "2020-02-23"], ["Bob", "Travel", "2020-02-11", "2020-02-18"]]}` from `{"tables": {"UserActivity": [{"username": "Alice", "activity": "Travel", "startDate": "2020-02-12", "endDate": "2020-02-20"}, {"username": "Alice", "activity": "Dancing", "startDate": "2020-02-21", "endDate": "2020-02-23"}, {"username": "Alice", "activity": "Travel", "startDate": "2020-02-24", "endDate": "2020-02-28"}, {"username": "Bob", "activity": "Travel", "startDate": "2020-02-11", "endDate": "2020-02-18"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Rank each user's rows independently

The desired row depends on chronology within one user, not on the global order of all activities. The inner query therefore uses window functions with `PARTITION BY username`. A partition is the collection of rows belonging to one username. Calculations restart independently for every partition while preserving every original row for later selection.

Two window values are attached to each row:

- `RANK() OVER (PARTITION BY username ORDER BY startdate DESC) AS rk` assigns chronological rank, with the newest start date ranked one and the next start date ranked two.
- `COUNT(username) OVER (PARTITION BY username) AS cnt` records how many stored rows belong to that user.

Unlike `GROUP BY`, window functions do not collapse a user's history into one row. Each activity retains its `activity`, `startdate`, and `enddate` while gaining the information needed to decide whether it is the requested row.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"UserActivity": [{"username": "Alice", "activity": "Travel", "startDate": "2020-02-12", "endDate": "2020-02-20"}, {"username": "Alice", "activity": "Dancing", "startDate": "2020-02-21", "endDate": "2020-02-23"}, {"username": "Alice", "activity": "Travel", "startDate": "2020-02-24", "endDate": "2020-02-28"}, {"username": "Bob", "activity": "Travel", "startDate": "2020-02-11", "endDate": "2020-02-18"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why descending order makes rank two the answer

`ORDER BY startdate DESC` places later starting activities before earlier ones. Under the guarantee that one user cannot perform overlapping activities and under the intended one-row-per-activity data, the most recent activity has `rk = 1` and the immediately preceding activity has `rk = 2`.

For Alice's three sample periods, the February 24 activity ranks one, the February 21 activity ranks two, and the February 12 activity ranks three. The outer predicate keeps only the Dancing row with rank two.

The use of `RANK` deserves precision. Rows with equal `startdate` receive the same rank, and the next rank is skipped. This behavior is useful only if equal starts should be treated as tied. The non-overlap rule normally prevents distinct simultaneous activities, so distinct logical periods should have distinct chronological positions.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `ORDER BY startdate DESC` places later starting activities b... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why single-activity users need a separate condition

A partition containing one row has rank one and no rank-two row. The requirement says to return that sole activity rather than return nothing. `COUNT(username)` equals one for that row, so `a.cnt = 1` selects it.

The final condition is `a.rk = 2 OR a.cnt = 1`. A multi-row user contributes the second-ranked row. A single-row user contributes its only row. The conditions cannot accidentally select the most recent row of an ordinary multi-row user because its count is greater than one.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["username", "activity", "startDate", "endDate"], "rows": [["Alice", "Dancing", "2020-02-21", "2020-02-23"], ["Bob", "Travel", "2020-02-11", "2020-02-18"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"UserActivity": [{"username": "Alice", "activity": "Travel", "startDate": "2020-02-12", "endDate": "2020-02-20"}, {"username": "Alice", "activity": "Dancing", "startDate": "2020-02-21", "endDate": "2020-02-23"}, {"username": "Alice", "activity": "Travel", "startDate": "2020-02-24", "endDate": "2020-02-28"}, {"username": "Bob", "activity": "Travel", "startDate": "2020-02-11", "endDate": "2020-02-18"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["username", "activity", "startDate", "endDate"], "rows": [["Alice", "Dancing", "2020-02-21", "2020-02-23"], ["Bob", "Travel", "2020-02-11", "2020-02-18"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Deduplicate before ranking:** Apply `SELECT DI:** - **Deduplicate before ranking:** Apply `SELECT DISTINCT` to the four logical activity columns, then compute both windows. This is required to honor the local duplicate-row semantics exactly, at the cost of an additional distinct operation.
- **`ROW_NUMBER`:** It guarantees one sequential row number even when dates tie, but without a complete tie breaker it arbitrarily chooses among tied rows and does not solve logical duplicates by itself.
- **Correlated subquery:** Count how many later activities exist for each row. It avoids window syntax but is usually harder to read and can be quadratic without effective indexing.
- **Self-join and aggregation:** Join each activity to later activities and select those with exactly one later period. This can work but tends to create a large intermediate result.
- **One activity:** Its `rk` is one and its `cnt` is one, so the second disjunct preserves it.
- **Two distinct activities:** The older row ranks two and is returned; the newer row ranks one and is excluded.
- **More than two activities:** Only chronological rank two survives, regardless of how old the remaining rows are.
- **Equal start dates:** `RANK` gives ties the same rank and skips later rank numbers. The non-overlap guarantee should rule out distinct simultaneous activities, while duplicate rows still require explicit deduplication.
- **Duplicate rows:** The exact code treats them as multiple stored activities for `COUNT` and tied ranking. A distinct-input layer is necessary when duplicates are genuinely legal.
- **Result order:** Any order is accepted. The absence of an outer `ORDER BY` is intentional.
- **Column-name casing:** MySQL treats the referenced `startdate` and `enddate` names case-insensitively in the usual setup, corresponding to the Reference's `startDate` and `endDate`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(A)$. Let $A$ be the number of input rows. The database must organize rows by username and descending `startdate` for the ranking window. A general sort-based execution costs $O(A\log A)$ time. Computing rank and count over the arranged partitions and applying the outer filter are linear passes, so sorting remains dominant. This matches the manifest.
- **Auxiliary Space Complexity:** $O(A)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
