# Guided Example: Hopper Company Queries III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Drivers": [{"driver_id": 1, "join_date": "2019-01-01"}], "Rides": [{"ride_id": 1, "user_id": 10, "requested_at": "2020-01-15"}], "AcceptedRides": [{"ride_id": 1, "driver_id": 1, "ride_distance": 30, "ride_duration": 60}]}}`
- **Required output:** `{"columns": ["month", "average_ride_distance", "average_ride_duration"], "rows": [[1, 10.0, 20.0], [2, 0.0, 0.0], [3, 0.0, 0.0], [4, 0.0, 0.0], [5, 0.0, 0.0], [6, 0.0, 0.0], [7, 0.0, 0.0], [8, 0.0, 0.0], [9, 0.0, 0.0], [10, 0.0, 0.0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Drivers`

The objective is to compute `{"columns": ["month", "average_ride_distance", "average_ride_duration"], "rows": [[1, 10.0, 20.0], [2, 0.0, 0.0], [3, 0.0, 0.0], [4, 0.0, 0.0], [5, 0.0, 0.0], [6, 0.0, 0.0], [7, 0.0, 0.0], [8, 0.0, 0.0], [9, 0.0, 0.0], [10, 0.0, 0.0]]}` from `{"tables": {"Drivers": [{"driver_id": 1, "join_date": "2019-01-01"}], "Rides": [{"ride_id": 1, "user_id": 10, "requested_at": "2020-01-15"}], "AcceptedRides": [{"ride_id": 1, "driver_id": 1, "ride_distance": 30, "ride_duration": 60}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Create one row for every month of 2020

The recursive `Months` CTE generates month numbers 1 through 12. It begins at 1 and repeatedly adds one while the current value is below 12.

This calendar is the left side of the monthly aggregation so that months with no rides still exist. Without it, an empty month would vanish and three-month windows would no longer line up with calendar months.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Drivers": [{"driver_id": 1, "join_date": "2019-01-01"}], "Rides": [{"ride_id": 1, "user_id": 10, "requested_at": "2020-01-15"}], "AcceptedRides": [{"ride_id": 1, "driver_id": 1, "ride_distance": 30, "ride_duration": 60}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Aggregate accepted distance and duration by request month

The `Ride` CTE left joins each generated month to `Rides` when the requested date has that month and year 2020. Placing the year condition in the join preserves calendar rows with no matching 2020 request.

It then left joins `AcceptedRides` by `ride_id`. An unaccepted request has null accepted fields. `COALESCE(ride_distance, 0)` and the corresponding duration expression make that request contribute zero.

Grouping by month produces exactly one row per calendar month. `ride_distance` is the sum of accepted-ride distances requested in that month, and `ride_duration` is the analogous duration total.

The Drivers table is irrelevant to this question because accepted-ride records already contain the measurements being averaged; the result does not filter or group by driver membership.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The `Ride` CTE left joins each generated month to `Rides` wh... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The required average is over monthly totals

For a window starting at month $m$, the problem defines

$$
\frac{D_m+D_{m+1}+D_{m+2}}{3},
$$

where $D_k$ is total accepted ride distance in month $k$. It is not the average distance of individual rides. A month with no accepted rides contributes zero as one of the three monthly terms.

The source applies `AVG(ride_distance)` over a three-row window and similarly for duration, then rounds each result to two decimals.

`LIMIT 10` keeps only ten output rows, corresponding conceptually to starting months January through October. Starts 11 and 12 do not have two following months within 2020 and must be omitted.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["month", "average_ride_distance", "average_ride_duration"], "rows": [[1, 10.0, 20.0], [2, 0.0, 0.0], [3, 0.0, 0.0], [4, 0.0, 0.0], [5, 0.0, 0.0], [6, 0.0, 0.0], [7, 0.0, 0.0], [8, 0.0, 0.0], [9, 0.0, 0.0], [10, 0.0, 0.0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Drivers": [{"driver_id": 1, "join_date": "2019-01-01"}], "Rides": [{"ride_id": 1, "user_id": 10, "requested_at": "2020-01-15"}], "AcceptedRides": [{"ride_id": 1, "driver_id": 1, "ride_distance": 30, "ride_duration": 60}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["month", "average_ride_distance", "average_ride_duration"], "rows": [[1, 10.0, 20.0], [2, 0.0, 0.0], [3, 0.0, 0.0], [4, 0.0, 0.0], [5, 0.0, 0.0], [6, 0.0, 0.0], [7, 0.0, 0.0], [8, 0.0, 0.0], [9, 0.0, 0.0], [10, 0.0, 0.0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Correctly ordered forward window:** Add `ORDER:** - **Correctly ordered forward window:** Add `ORDER BY month` inside each `OVER` clause. This is the smallest change needed for deterministic three-calendar-month frames.
- **Self-join monthly totals:** Join each start month to totals whose month lies from start through start+2, then divide their sum by three. It is more verbose but makes the window membership explicit.
- **Use `SUM(...) / 3` instead of `AVG`:** With all twelve zero-filled months present, both are equivalent for valid three-row frames.
- **Month with no requests:** The calendar left join preserves it and monthly sums become zero.
- **Requested but unaccepted ride:** Its accepted fields are null and contribute zero.
- **Several accepted rides in one month:** Their distances and durations are summed before the window average.
- **Starting month 10:** Its ordered frame must contain months 10, 11, and 12.
- **Starting months 11 and 12:** They are removed by `LIMIT 10` after final month ordering.
- **Outer ordering is insufficient:** It controls presentation only, not the order used to evaluate an unordered window frame.
- **Rounding:** The source rounds the three-month average, not each monthly total.
- **Drivers table unused:** No driver property is needed to compute totals from accepted rides.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r+a)$. Let $r$ and $a$ be the numbers of Rides and AcceptedRides rows. Generating 12 months is constant work. With indexes on `ride_id` and date access supported by the optimizer, joining and aggregating the relevant rows is logically $O(r+a)$.
- **Auxiliary Space Complexity:** $O(a)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
