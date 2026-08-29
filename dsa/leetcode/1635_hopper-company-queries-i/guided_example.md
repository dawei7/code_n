# Guided Example: Hopper Company Queries I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Drivers": [{"driver_id": 10, "join_date": "2019-12-10"}, {"driver_id": 8, "join_date": "2020-01-13"}, {"driver_id": 5, "join_date": "2020-02-16"}, {"driver_id": 7, "join_date": "2020-03-08"}, {"driver_id": 4, "join_date": "2020-05-17"}, {"driver_id": 1, "join_date": "2020-10-24"}, {"driver_id": 6, "join_date": "2021-01-05"}], "Rides": [{"ride_id": 6, "user_id": 75, "requested_at": "2019-12-09"}, {"ride_id": 1, "user_id": 54, "requested_at": "2020-02-09"}, {"ride_id": 10, "user_id": 63, "requested_at": "2020-03-04"}, {"ride_id": 19, "user_id": 39, "requested_at": "2020-04-06"}, {"ride_id": 3, "user_id": 41, "requested_at": "2020-06-03"}, {"ride_id": 13, "user_id": 52, "requested_at": "2020-06-22"}, {"ride_id": 7, "user_id": 69, "requested_at": "2020-07-16"}, {"ride_id": 17, "user_id": 70, "requested_at": "2020-08-25"}, {"ride_id": 20, "user_id": 81, "requested_at": "2020-11-02"}, {"ride_id": 5, "user_id": 57, "requested_at": "2020-11-09"}, {"ride_id": 2, "user_id": 42, "requested_at": "2020-12-09"}, {"ride_id": 11, "user_id": 68, "requested_at": "2021-01-11"}, {"ride_id": 15, "user_id": 32, "requested_at": "2021-01-17"}, {"ride_id": 12, "user_id": 11, "requested_at": "2021-01-19"}, {"ride_id": 14, "user_id": 18, "requested_at": "2021-01-27"}], "AcceptedRides": [{"ride_id": 10, "driver_id": 10, "ride_distance": 63, "ride_duration": 38}, {"ride_id": 13, "driver_id": 10, "ride_distance": 73, "ride_duration": 96}, {"ride_id": 7, "driver_id": 8, "ride_distance": 100, "ride_duration": 28}, {"ride_id": 17, "driver_id": 7, "ride_distance": 119, "ride_duration": 68}, {"ride_id": 20, "driver_id": 1, "ride_distance": 121, "ride_duration": 92}, {"ride_id": 5, "driver_id": 7, "ride_distance": 42, "ride_duration": 101}, {"ride_id": 2, "driver_id": 4, "ride_distance": 6, "ride_duration": 38}, {"ride_id": 11, "driver_id": 8, "ride_distance": 37, "ride_duration": 43}, {"ride_id": 15, "driver_id": 8, "ride_distance": 108, "ride_duration": 82}, {"ride_id": 12, "driver_id": 8, "ride_distance": 38, "ride_duration": 34}, {"ride_id": 14, "driver_id": 1, "ride_distance": 90, "ride_duration": 74}]}}`
- **Required output:** `{"columns": ["month", "active_drivers", "accepted_rides"], "rows": [[1, 2, 0], [2, 3, 0], [3, 4, 1], [4, 4, 0], [5, 5, 0], [6, 5, 1], [7, 5, 1], [8, 5, 1], [9, 5, 0], [10, 6, 0], [11, 6, 2], [12, 6, 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Drivers`

The objective is to compute `{"columns": ["month", "active_drivers", "accepted_rides"], "rows": [[1, 2, 0], [2, 3, 0], [3, 4, 1], [4, 4, 0], [5, 5, 0], [6, 5, 1], [7, 5, 1], [8, 5, 1], [9, 5, 0], [10, 6, 0], [11, 6, 2], [12, 6, 1]]}` from `{"tables": {"Drivers": [{"driver_id": 10, "join_date": "2019-12-10"}, {"driver_id": 8, "join_date": "2020-01-13"}, {"driver_id": 5, "join_date": "2020-02-16"}, {"driver_id": 7, "join_date": "2020-03-08"}, {"driver_id": 4, "join_date": "2020-05-17"}, {"driver_id": 1, "join_date": "2020-10-24"}, {"driver_id": 6, "join_date": "2021-01-05"}], "Rides": [{"ride_id": 6, "user_id": 75, "requested_at": "2019-12-09"}, {"ride_id": 1, "user_id": 54, "requested_at": "2020-02-09"}, {"ride_id": 10, "user_id": 63, "requested_at": "2020-03-04"}, {"ride_id": 19, "user_id": 39, "requested_at": "2020-04-06"}, {"ride_id": 3, "user_id": 41, "requested_at": "2020-06-03"}, {"ride_id": 13, "user_id": 52, "requested_at": "2020-06-22"}, {"ride_id": 7, "user_id": 69, "requested_at": "2020-07-16"}, {"ride_id": 17, "user_id": 70, "requested_at": "2020-08-25"}, {"ride_id": 20, "user_id": 81, "requested_at": "2020-11-02"}, {"ride_id": 5, "user_id": 57, "requested_at": "2020-11-09"}, {"ride_id": 2, "user_id": 42, "requested_at": "2020-12-09"}, {"ride_id": 11, "user_id": 68, "requested_at": "2021-01-11"}, {"ride_id": 15, "user_id": 32, "requested_at": "2021-01-17"}, {"ride_id": 12, "user_id": 11, "requested_at": "2021-01-19"}, {"ride_id": 14, "user_id": 18, "requested_at": "2021-01-27"}], "AcceptedRides": [{"ride_id": 10, "driver_id": 10, "ride_distance": 63, "ride_duration": 38}, {"ride_id": 13, "driver_id": 10, "ride_distance": 73, "ride_duration": 96}, {"ride_id": 7, "driver_id": 8, "ride_distance": 100, "ride_duration": 28}, {"ride_id": 17, "driver_id": 7, "ride_distance": 119, "ride_duration": 68}, {"ride_id": 20, "driver_id": 1, "ride_distance": 121, "ride_duration": 92}, {"ride_id": 5, "driver_id": 7, "ride_distance": 42, "ride_duration": 101}, {"ride_id": 2, "driver_id": 4, "ride_distance": 6, "ride_duration": 38}, {"ride_id": 11, "driver_id": 8, "ride_distance": 37, "ride_duration": 43}, {"ride_id": 15, "driver_id": 8, "ride_distance": 108, "ride_duration": 82}, {"ride_id": 12, "driver_id": 8, "ride_distance": 38, "ride_duration": 34}, {"ride_id": 14, "driver_id": 1, "ride_distance": 90, "ride_duration": 74}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Generate all twelve reporting months first

Months with no drivers joining and no accepted rides must still appear. The recursive `Months` common table expression starts with row 1, then repeatedly selects `month + 1` while the current month is below 12. `UNION ALL` preserves every generated row, producing exactly integers 1 through 12.

Using this complete calendar as the left side of later joins guarantees one reporting group per month. Starting from activity tables instead would omit inactive months.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Drivers": [{"driver_id": 10, "join_date": "2019-12-10"}, {"driver_id": 8, "join_date": "2020-01-13"}, {"driver_id": 5, "join_date": "2020-02-16"}, {"driver_id": 7, "join_date": "2020-03-08"}, {"driver_id": 4, "join_date": "2020-05-17"}, {"driver_id": 1, "join_date": "2020-10-24"}, {"driver_id": 6, "join_date": "2021-01-05"}], "Rides": [{"ride_id": 6, "user_id": 75, "requested_at": "2019-12-09"}, {"ride_id": 1, "user_id": 54, "requested_at": "2020-02-09"}, {"ride_id": 10, "user_id": 63, "requested_at": "2020-03-04"}, {"ride_id": 19, "user_id": 39, "requested_at": "2020-04-06"}, {"ride_id": 3, "user_id": 41, "requested_at": "2020-06-03"}, {"ride_id": 13, "user_id": 52, "requested_at": "2020-06-22"}, {"ride_id": 7, "user_id": 69, "requested_at": "2020-07-16"}, {"ride_id": 17, "user_id": 70, "requested_at": "2020-08-25"}, {"ride_id": 20, "user_id": 81, "requested_at": "2020-11-02"}, {"ride_id": 5, "user_id": 57, "requested_at": "2020-11-09"}, {"ride_id": 2, "user_id": 42, "requested_at": "2020-12-09"}, {"ride_id": 11, "user_id": 68, "requested_at": "2021-01-11"}, {"ride_id": 15, "user_id": 32, "requested_at": "2021-01-17"}, {"ride_id": 12, "user_id": 11, "requested_at": "2021-01-19"}, {"ride_id": 14, "user_id": 18, "requested_at": "2021-01-27"}], "AcceptedRides": [{"ride_id": 10, "driver_id": 10, "ride_distance": 63, "ride_duration": 38}, {"ride_id": 13, "driver_id": 10, "ride_distance": 73, "ride_duration": 96}, {"ride_id": 7, "driver_id": 8, "ride_distance": 100, "ride_duration": 28}, {"ride_id": 17, "driver_id": 7, "ride_distance": 119, "ride_duration": 68}, {"ride_id": 20, "driver_id": 1, "ride_distance": 121, "ride_duration": 92}, {"ride_id": 5, "driver_id": 7, "ride_distance": 42, "ride_duration": 101}, {"ride_id": 2, "driver_id": 4, "ride_distance": 6, "ride_duration": 38}, {"ride_id": 11, "driver_id": 8, "ride_distance": 37, "ride_duration": 43}, {"ride_id": 15, "driver_id": 8, "ride_distance": 108, "ride_duration": 82}, {"ride_id": 12, "driver_id": 8, "ride_distance": 38, "ride_duration": 34}, {"ride_id": 14, "driver_id": 1, "ride_distance": 90, "ride_duration": 74}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Aggregate accepted rides before joining them to drivers

The `Ride` CTE joins `Rides AS r` to `AcceptedRides AS a` by equal `ride_id`. This inner join retains only requested rides that have an accepted-ride record. The additional condition `YEAR(requested_at) = 2020` restricts them to the reporting year.

The condition is written in the `ON` clause. Because this is an inner join, placing it in `WHERE` would have the same filtering effect.

`MONTH(requested_at) AS month` converts each accepted request date into its 1-through-12 reporting month. `GROUP BY month` then creates one row per month having accepted rides, and `COUNT(1) AS cnt` counts those rides. `ride_id` is unique in both relevant tables, so the join produces at most one row per accepted ride.

Pre-aggregating rides is important. The final query also joins multiple drivers to each month. If raw ride rows and driver rows were joined together before counting, every ride could be repeated once per active driver and both counts could be inflated. Reducing Ride to one count row per month prevents that multiplication.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Join each driver to every month when that driver is active

The left join from `Months AS m` to `Drivers AS d` uses this condition:

`(m.month >= MONTH(d.join_date) AND YEAR(d.join_date) = 2020) OR YEAR(d.join_date) < 2020`.

A driver who joined during 2020 is matched to their join month and every later month because `m.month` must be at least the join month. A driver who joined before 2020 matches every month, since they are already active in January. A driver who joined after 2020 satisfies neither branch and is excluded from all 2020 groups.

The schema contains no departure date, so once a driver joins, the driver remains active for every later reporting month. The predicate models “currently with the company by the end of the month” as cumulative membership.

Because this is a left join, a month with no matching active driver still remains as a row with null driver columns. `COUNT(driver_id)` counts only non-null IDs, producing zero for such a month rather than counting the preserved calendar row itself.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["month", "active_drivers", "accepted_rides"], "rows": [[1, 2, 0], [2, 3, 0], [3, 4, 1], [4, 4, 0], [5, 5, 0], [6, 5, 1], [7, 5, 1], [8, 5, 1], [9, 5, 0], [10, 6, 0], [11, 6, 2], [12, 6, 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Drivers": [{"driver_id": 10, "join_date": "2019-12-10"}, {"driver_id": 8, "join_date": "2020-01-13"}, {"driver_id": 5, "join_date": "2020-02-16"}, {"driver_id": 7, "join_date": "2020-03-08"}, {"driver_id": 4, "join_date": "2020-05-17"}, {"driver_id": 1, "join_date": "2020-10-24"}, {"driver_id": 6, "join_date": "2021-01-05"}], "Rides": [{"ride_id": 6, "user_id": 75, "requested_at": "2019-12-09"}, {"ride_id": 1, "user_id": 54, "requested_at": "2020-02-09"}, {"ride_id": 10, "user_id": 63, "requested_at": "2020-03-04"}, {"ride_id": 19, "user_id": 39, "requested_at": "2020-04-06"}, {"ride_id": 3, "user_id": 41, "requested_at": "2020-06-03"}, {"ride_id": 13, "user_id": 52, "requested_at": "2020-06-22"}, {"ride_id": 7, "user_id": 69, "requested_at": "2020-07-16"}, {"ride_id": 17, "user_id": 70, "requested_at": "2020-08-25"}, {"ride_id": 20, "user_id": 81, "requested_at": "2020-11-02"}, {"ride_id": 5, "user_id": 57, "requested_at": "2020-11-09"}, {"ride_id": 2, "user_id": 42, "requested_at": "2020-12-09"}, {"ride_id": 11, "user_id": 68, "requested_at": "2021-01-11"}, {"ride_id": 15, "user_id": 32, "requested_at": "2021-01-17"}, {"ride_id": 12, "user_id": 11, "requested_at": "2021-01-19"}, {"ride_id": 14, "user_id": 18, "requested_at": "2021-01-27"}], "AcceptedRides": [{"ride_id": 10, "driver_id": 10, "ride_distance": 63, "ride_duration": 38}, {"ride_id": 13, "driver_id": 10, "ride_distance": 73, "ride_duration": 96}, {"ride_id": 7, "driver_id": 8, "ride_distance": 100, "ride_duration": 28}, {"ride_id": 17, "driver_id": 7, "ride_distance": 119, "ride_duration": 68}, {"ride_id": 20, "driver_id": 1, "ride_distance": 121, "ride_duration": 92}, {"ride_id": 5, "driver_id": 7, "ride_distance": 42, "ride_duration": 101}, {"ride_id": 2, "driver_id": 4, "ride_distance": 6, "ride_duration": 38}, {"ride_id": 11, "driver_id": 8, "ride_distance": 37, "ride_duration": 43}, {"ride_id": 15, "driver_id": 8, "ride_distance": 108, "ride_duration": 82}, {"ride_id": 12, "driver_id": 8, "ride_distance": 38, "ride_duration": 34}, {"ride_id": 14, "driver_id": 1, "ride_distance": 90, "ride_duration": 74}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["month", "active_drivers", "accepted_rides"], "rows": [[1, 2, 0], [2, 3, 0], [3, 4, 1], [4, 4, 0], [5, 5, 0], [6, 5, 1], [7, 5, 1], [8, 5, 1], [9, 5, 0], [10, 6, 0], [11, 6, 2], [12, 6, 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Hard-code twelve rows with `UNION ALL`:** This avoids recursion but is verbose. The recursive CTE expresses the calendar range compactly.
- **Aggregate drivers by join month and use a cumulative window sum:** Count pre-2020 drivers into January, count 2020 joiners by month, fill missing months, and run `SUM(...) OVER (ORDER BY month)`. This avoids the range join.
- **Correlated count subqueries per month:** For each of twelve months, count eligible drivers and accepted rides. It is readable but may rescan base tables repeatedly.
- **Join raw rides and raw drivers together:** This creates a many-to-many multiplication within each month and makes simple counts wrong. Pre-aggregating Ride avoids it.
- **Driver joined before 2020:** The OR branch includes that driver in all twelve months.
- **Driver joined during 2020:** The month comparison includes the join month itself because statistics are measured by month end.
- **Driver joined after 2020:** Neither predicate branch matches, so the driver is excluded.
- **Ride requested outside 2020:** The Ride CTE filters it out even if it was accepted.
- **Requested but not accepted:** It has no AcceptedRides match and is excluded by the inner join.
- **Month with no accepted rides:** The left join yields null and `COALESCE` returns zero.
- **Month with no active drivers:** `COUNT(driver_id)` ignores the null from the calendar-preserving left join and returns zero.
- **Ordering requirement:** The exact source lacks `ORDER BY`, so ascending presentation is not guaranteed. Grouping alone must not be relied upon as an ordering contract.
- **Grouping name resolution:** The source writes `GROUP BY month` rather than `GROUP BY m.month`. In this select scope the intended key is the output month; qualifying it would make the intent more robust.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d+r+a)$. Let $d$, $r$, and $a$ be the row counts of Drivers, Rides, and AcceptedRides. Months always has 12 rows, so its recursive generation is constant work.
- **Auxiliary Space Complexity:** $O(a)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
