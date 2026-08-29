# Guided Example: Biggest Window Between Visits

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"UserVisits": [{"user_id": 1, "visit_date": "2020-11-28"}, {"user_id": 1, "visit_date": "2020-10-20"}, {"user_id": 1, "visit_date": "2020-12-03"}, {"user_id": 2, "visit_date": "2020-10-05"}, {"user_id": 2, "visit_date": "2020-12-09"}, {"user_id": 3, "visit_date": "2020-11-11"}]}}`
- **Required output:** `{"columns": ["user_id", "biggest_window"], "rows": [[1, 39], [2, 65], [3, 51]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `UserVisits`

The objective is to compute `{"columns": ["user_id", "biggest_window"], "rows": [[1, 39], [2, 65], [3, 51]]}` from `{"tables": {"UserVisits": [{"user_id": 1, "visit_date": "2020-11-28"}, {"user_id": 1, "visit_date": "2020-10-20"}, {"user_id": 1, "visit_date": "2020-12-03"}, {"user_id": 2, "visit_date": "2020-10-05"}, {"user_id": 2, "visit_date": "2020-12-09"}, {"user_id": 3, "visit_date": "2020-11-11"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn each visit into a gap to its successor

For one user, place visit dates in ascending order. Every visit begins one candidate window: it ends at that user's next visit, except that the final visit ends at the fixed date `'2021-1-1'`.

The query first computes all such windows in common table expression `T`, then takes the maximum for each user. Separating row-level window calculation from group-level maximum aggregation keeps the two meanings clear.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"UserVisits": [{"user_id": 1, "visit_date": "2020-11-28"}, {"user_id": 1, "visit_date": "2020-10-20"}, {"user_id": 1, "visit_date": "2020-12-03"}, {"user_id": 2, "visit_date": "2020-10-05"}, {"user_id": 2, "visit_date": "2020-12-09"}, {"user_id": 3, "visit_date": "2020-11-11"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Keep users isolated with a window partition

`LEAD(visit_date, 1, '2021-1-1') OVER (...)` asks for the `visit_date` one row ahead. Its window specification is

`PARTITION BY user_id ORDER BY visit_date`.

`PARTITION BY` gives each user an independent ordered sequence. A row for one user can never take a next date from another user. `ORDER BY visit_date` defines “next” chronologically rather than by arbitrary table storage order.

The offset argument one means immediate successor, not the second or any later visit.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Supply today for the last visit

On the final ordered row in a user's partition, no next row exists. The third `LEAD` argument is the default returned in that case, so the expression yields `'2021-1-1'`.

This integrates the special last-visit rule into the same expression used for ordinary consecutive visits. A user with only one visit still gets one meaningful interval—from that visit to today—instead of a null.

The literal's non-zero-padded month and day are accepted as the intended MySQL date value. `DATEDIFF` applies date semantics rather than string subtraction.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id", "biggest_window"], "rows": [[1, 39], [2, 65], [3, 51]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"UserVisits": [{"user_id": 1, "visit_date": "2020-11-28"}, {"user_id": 1, "visit_date": "2020-10-20"}, {"user_id": 1, "visit_date": "2020-12-03"}, {"user_id": 2, "visit_date": "2020-10-05"}, {"user_id": 2, "visit_date": "2020-12-09"}, {"user_id": 3, "visit_date": "2020-11-11"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id", "biggest_window"], "rows": [[1, 39], [2, 65], [3, 51]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Self-join on ranked dates:** Assign row numbers and join each visit to rank plus one. It works but is more verbose than `LEAD`.
- **Append today then use `LAG`:** Add one today row per user and compute backward differences. This is equivalent but requires a union and careful deduplication.
- **Correlated next-date subquery:** Find the minimum later date for each visit. Without strong indexing, repeated searches can be much slower.
- **Single visit:** The default date creates the sole window from that visit to today.
- **Duplicate visit dates:** They introduce zero-length gaps but do not inflate the maximum; the successor after the duplicate run remains represented.
- **Several users:** Partitioning prevents a user's last visit from leading into the next user's first visit.
- **Last visit:** The three-argument `LEAD` supplies today directly, avoiding null arithmetic.
- **Date argument order:** `DATEDIFF(next, current)` is required for positive window lengths.
- **Explicit output order:** `ORDER BY 1` guarantees ascending user IDs; `GROUP BY` alone would not.
- **Ordinal clauses:** Both `GROUP BY 1` and `ORDER BY 1` depend on `user_id` remaining the first select expression.
- **Visits on today in generalized data:** The last gap is zero and competes normally with earlier gaps.
- **Fixed today literal:** The solution intentionally uses `2021-01-01` rather than the database server's current date.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let $R$ be the number of visit rows. Once rows are ordered by user and date, computing `LEAD` and scanning the CTE for grouped maxima are linear in $R$. A hash aggregation needs up to one state per user, bounded by $O(R)$ space.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
