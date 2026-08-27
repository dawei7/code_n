# Guided Example: Trips and Users

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Trips": [{"id": 1, "client_id": 1, "driver_id": 10, "city_id": 1, "status": "completed", "request_at": "2013-10-01"}, {"id": 2, "client_id": 2, "driver_id": 11, "city_id": 1, "status": "cancelled_by_driver", "request_at": "2013-10-01"}, {"id": 3, "client_id": 3, "driver_id": 10, "city_id": 1, "status": "completed", "request_at": "2013-10-02"}, {"id": 4, "client_id": 1, "driver_id": 11, "city_id": 1, "status": "cancelled_by_client", "request_at": "2013-10-03"}], "Users": [{"users_id": 1, "banned": "No", "role": "client"}, {"users_id": 2, "banned": "No", "role": "client"}, {"users_id": 3, "banned": "No", "role": "client"}, {"users_id": 10, "banned": "No", "role": "driver"}, {"users_id": 11, "banned": "No", "role": "driver"}]}}`
- **Required output:** `{"columns": ["Day", "Cancellation Rate"], "rows": [["2013-10-01", 0.5], ["2013-10-02", 0.0], ["2013-10-03", 1.0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Trips`

The objective is to compute `{"columns": ["Day", "Cancellation Rate"], "rows": [["2013-10-01", 0.5], ["2013-10-02", 0.0], ["2013-10-03", 1.0]]}` from `{"tables": {"Trips": [{"id": 1, "client_id": 1, "driver_id": 10, "city_id": 1, "status": "completed", "request_at": "2013-10-01"}, {"id": 2, "client_id": 2, "driver_id": 11, "city_id": 1, "status": "cancelled_by_driver", "request_at": "2013-10-01"}, {"id": 3, "client_id": 3, "driver_id": 10, "city_id": 1, "status": "completed", "request_at": "2013-10-02"}, {"id": 4, "client_id": 1, "driver_id": 11, "city_id": 1, "status": "cancelled_by_client", "request_at": "2013-10-03"}], "Users": [{"users_id": 1, "banned": "No", "role": "client"}, {"users_id": 2, "banned": "No", "role": "client"}, {"users_id": 3, "banned": "No", "role": "client"}, {"users_id": 10, "banned": "No", "role": "driver"}, {"users_id": 11, "banned": "No", "role": "driver"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Join `Users` twice because the roles are different references

One trip contains two foreign keys into the same `Users` table: `client_id` and `driver_id`. A single join cannot independently inspect both referenced users. The query therefore gives the table two aliases:



The first join condition is



and the second is



Both are inner `JOIN`s. A trip survives the joined result only if it finds an unbanned client row **and** an unbanned driver row. If either participant is banned, that join has no qualifying match and the trip disappears before aggregation.

Putting each ban predicate in its corresponding `ON` clause keeps the relationship and eligibility rule together. With inner joins, placing the same predicates in `WHERE` would produce the same final rows, but the current placement makes the purpose of each alias explicit.

The query does not need to test `role = 'client'` or `role = 'driver'`. The trip columns already specify which user ID occupies each relationship, and the source schema declares them as foreign keys to the unique `users_id`. The requested eligibility depends on `banned`, not on adding a redundant role check.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Trips": [{"id": 1, "client_id": 1, "driver_id": 10, "city_id": 1, "status": "completed", "request_at": "2013-10-01"}, {"id": 2, "client_id": 2, "driver_id": 11, "city_id": 1, "status": "cancelled_by_driver", "request_at": "2013-10-01"}, {"id": 3, "client_id": 3, "driver_id": 10, "city_id": 1, "status": "completed", "request_at": "2013-10-02"}, {"id": 4, "client_id": 1, "driver_id": 11, "city_id": 1, "status": "cancelled_by_client", "request_at": "2013-10-03"}], "Users": [{"users_id": 1, "banned": "No", "role": "client"}, {"users_id": 2, "banned": "No", "role": "client"}, {"users_id": 3, "banned": "No", "role": "client"}, {"users_id": 10, "banned": "No", "role": "driver"}, {"users_id": 11, "banned": "No", "role": "driver"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Restrict the inclusive three-day window

The condition



is inclusive at both ends. Because the stored strings use fixed-width ISO `YYYY-MM-DD` form, their lexical ordering agrees with chronological date ordering. Trips on October 1, 2, and 3 remain; dates before or after are removed.

Using the unqualified name `request_at` is unambiguous here because only `Trips` has that column among the joined tables. Qualifying it as `t.request_at` would be equally valid and potentially clearer in a larger query.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The condition



is inclusive at both ends.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Turn each status into a numeric indicator

MySQL evaluates the Boolean expression



as `0` when the trip completed and `1` when it did not. The only other allowed status values are `cancelled_by_driver` and `cancelled_by_client`, so “not completed” is exactly equivalent to “canceled by either participant.”

For a day with status indicators such as `[0, 1, 0]`, the average is

$$
\frac{0+1+0}{3}=\frac13,
$$

which is the number of canceled eligible trips divided by the total number of eligible trips. `AVG` performs both the summation and division directly; a separate `SUM(...) / COUNT(*)` expression is unnecessary.

The query applies `ROUND(..., 2)` after taking the average, producing the required two-decimal cancellation rate.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["Day", "Cancellation Rate"], "rows": [["2013-10-01", 0.5], ["2013-10-02", 0.0], ["2013-10-03", 1.0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Trips": [{"id": 1, "client_id": 1, "driver_id": 10, "city_id": 1, "status": "completed", "request_at": "2013-10-01"}, {"id": 2, "client_id": 2, "driver_id": 11, "city_id": 1, "status": "cancelled_by_driver", "request_at": "2013-10-01"}, {"id": 3, "client_id": 3, "driver_id": 10, "city_id": 1, "status": "completed", "request_at": "2013-10-02"}, {"id": 4, "client_id": 1, "driver_id": 11, "city_id": 1, "status": "cancelled_by_client", "request_at": "2013-10-03"}], "Users": [{"users_id": 1, "banned": "No", "role": "client"}, {"users_id": 2, "banned": "No", "role": "client"}, {"users_id": 3, "banned": "No", "role": "client"}, {"users_id": 10, "banned": "No", "role": "driver"}, {"users_id": 11, "banned": "No", "role": "driver"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["Day", "Cancellation Rate"], "rows": [["2013-10-01", 0.5], ["2013-10-02", 0.0], ["2013-10-03", 1.0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Conditional sum divided by count:** `SUM(statu:** - **Conditional sum divided by count:** `SUM(status != 'completed') / COUNT(*)` expresses the same rate explicitly. `AVG` is shorter because a Boolean indicator already represents one canceled trip or zero.
- **Exclude banned IDs with subqueries:** Filter both foreign keys using `NOT IN` or `NOT EXISTS`. It can be correct, but two joins make the client and driver requirements direct and avoid `NOT IN` null semantics.
- **Common table expression:** First select eligible rows and a `cancelled` indicator, then group the CTE. This may improve readability for a longer pipeline but is unnecessary for the compact query.
- **Banned client:** The first join eliminates the trip entirely, regardless of driver status or trip outcome.
- **Banned driver:** The second join likewise eliminates the trip, even when the client is unbanned.
- **Both participants banned:** Failure of either required join is sufficient; the row cannot be duplicated or partially counted.
- **Completed trip:** The Boolean expression contributes zero to the numerator while still contributing one row to `AVG`'s denominator.
- **Either cancellation status:** Both values differ from `completed`, so each contributes one.
- **Boundary dates:** `BETWEEN` includes both `2013-10-01` and `2013-10-03`.
- **No eligible rows on a date:** No group is produced, which satisfies the “at least one trip” requirement.
- **Missing referenced user outside the schema contract:** Inner joins would exclude the trip. The declared foreign keys normally guarantee that both user rows exist.
- **Duplicate user rows:** `users_id` is a primary key, so each join has at most one matching user and cannot multiply trip rows.
- **Result ordering:** Without `ORDER BY`, the engine may return dates in any order, which the contract explicitly allows.
- **Null status outside the declared enum contract:** `status != 'completed'` would evaluate to `NULL`, and `AVG` ignores nulls. If null statuses were possible, an explicit `CASE` expression would be safer; the source schema supplies only the stated enum outcomes.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(t \log u)$. Let $t$ be the number of `Trips` rows considered and $u$ the number of `Users` rows. Physical SQL complexity depends on indexes, statistics, join order, and the optimizer's chosen plan rather than solely on query text.
- **Auxiliary Space Complexity:** $O(u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
