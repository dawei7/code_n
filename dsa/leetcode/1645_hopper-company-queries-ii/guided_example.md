# Guided Example: Hopper Company Queries II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Drivers": [{"driver_id": 1, "join_date": "2019-12-31"}], "Rides": [{"ride_id": 10, "user_id": 7, "requested_at": "2020-01-15"}], "AcceptedRides": [{"ride_id": 10, "driver_id": 1, "ride_distance": 5, "ride_duration": 8}]}}`
- **Required output:** `{"columns": ["month", "working_percentage"], "rows": [[1, 100.0], [2, 0.0], [3, 0.0], [4, 0.0], [5, 0.0], [6, 0.0], [7, 0.0], [8, 0.0], [9, 0.0], [10, 0.0], [11, 0.0], [12, 0.0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Drivers`

The objective is to compute `{"columns": ["month", "working_percentage"], "rows": [[1, 100.0], [2, 0.0], [3, 0.0], [4, 0.0], [5, 0.0], [6, 0.0], [7, 0.0], [8, 0.0], [9, 0.0], [10, 0.0], [11, 0.0], [12, 0.0]]}` from `{"tables": {"Drivers": [{"driver_id": 1, "join_date": "2019-12-31"}], "Rides": [{"ride_id": 10, "user_id": 7, "requested_at": "2020-01-15"}], "AcceptedRides": [{"ride_id": 10, "driver_id": 1, "ride_distance": 5, "ride_duration": 8}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build a complete month calendar

The recursive `Month` CTE generates integers 1 through 12. It begins with 1 and repeatedly adds one while the current value is below 12. Starting from this calendar ensures months with no active or working drivers still appear.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Drivers": [{"driver_id": 1, "join_date": "2019-12-31"}], "Rides": [{"ride_id": 10, "user_id": 7, "requested_at": "2020-01-15"}], "AcceptedRides": [{"ride_id": 10, "driver_id": 1, "ride_distance": 5, "ride_duration": 8}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Expand drivers into their active months

CTE `S` left joins each month to Drivers. A driver matches when the join year is before 2020, or when it is 2020 and the join month is no later than the reporting month.

Thus, a pre-2020 driver appears in all twelve month rows. A driver joining in March 2020 appears from month 3 through 12. A post-2020 driver appears nowhere. Because there is no departure date, membership remains active after joining.

The left join preserves a month even if no driver matches, producing a row with null driver data. This is essential for the required zero percentage.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | CTE `S` left joins each month to Drivers.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Identify accepted rides during 2020

CTE `T` joins Rides to AcceptedRides using their shared `ride_id` and filters request dates to year 2020. Requested but unaccepted rides have no join match and disappear.

`T` keeps `driver_id` and `requested_at`. It does not aggregate yet because the final numerator needs the number of distinct drivers who worked, not the number of accepted rides.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["month", "working_percentage"], "rows": [[1, 100.0], [2, 0.0], [3, 0.0], [4, 0.0], [5, 0.0], [6, 0.0], [7, 0.0], [8, 0.0], [9, 0.0], [10, 0.0], [11, 0.0], [12, 0.0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Drivers": [{"driver_id": 1, "join_date": "2019-12-31"}], "Rides": [{"ride_id": 10, "user_id": 7, "requested_at": "2020-01-15"}], "AcceptedRides": [{"ride_id": 10, "driver_id": 1, "ride_distance": 5, "ride_duration": 8}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["month", "working_percentage"], "rows": [[1, 100.0], [2, 0.0], [3, 0.0], [4, 0.0], [5, 0.0], [6, 0.0], [7, 0.0], [8, 0.0], [9, 0.0], [10, 0.0], [11, 0.0], [12, 0.0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Aggregate one row per working driver and month:** - **Aggregate one row per working driver and month in `T`:** Grouping there can reduce duplicate ride rows before the final join.
- **Monthly driver counts plus window sums:** Aggregate joiners and use a cumulative window function for active counts, then join monthly working-driver counts.
- **Correlated subqueries per month:** They are readable but may rescan base tables twelve times.
- **Several rides by one driver:** `COUNT(DISTINCT)` counts one working driver, not several rides.
- **Ride before join date in the same month:** The explicit date comparison excludes it.
- **No active drivers:** Division produces null and `COALESCE` returns zero.
- **No accepted rides:** The left join gives no non-null `t.driver_id`, so the numerator is zero.
- **Pre-2020 driver:** Included in every reporting month.
- **Post-2020 driver:** Excluded from every reporting month.
- **Requested but unaccepted ride:** Excluded by the inner join in `T`.
- **Missing ordering:** The exact query has no `ORDER BY`, so row order is not guaranteed despite the contract's ascending requirement.
- **Recursive CTE uses `UNION`:** The generated month values are unique, so duplicate elimination does not change the twelve-row result.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d+r+a)$. Let $d$, $r$, and $a$ be row counts for Drivers, Rides, and AcceptedRides. Month generation is constant work. With primary-key indexes, building `T` is logically $O(r+a)$. Expanding Drivers across twelve fixed months is $O(d)$ because twelve is constant.
- **Auxiliary Space Complexity:** $O(a)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
