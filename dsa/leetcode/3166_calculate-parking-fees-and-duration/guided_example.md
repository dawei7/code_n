# Guided Example: Calculate Parking Fees and Duration

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"ParkingTransactions": [{"lot_id": 1, "car_id": 1001, "entry_time": "2023-06-01 08:00:00", "exit_time": "2023-06-01 10:30:00", "fee_paid": 5}, {"lot_id": 1, "car_id": 1001, "entry_time": "2023-06-02 11:00:00", "exit_time": "2023-06-02 12:45:00", "fee_paid": 3}, {"lot_id": 2, "car_id": 1001, "entry_time": "2023-06-01 10:45:00", "exit_time": "2023-06-01 12:00:00", "fee_paid": 6}, {"lot_id": 2, "car_id": 1002, "entry_time": "2023-06-01 09:00:00", "exit_time": "2023-06-01 11:30:00", "fee_paid": 4}, {"lot_id": 3, "car_id": 1001, "entry_time": "2023-06-03 07:00:00", "exit_time": "2023-06-03 09:00:00", "fee_paid": 4}, {"lot_id": 3, "car_id": 1002, "entry_time": "2023-06-02 12:00:00", "exit_time": "2023-06-02 14:00:00", "fee_paid": 2}]}}`
- **Required output:** `{"columns": ["car_id", "total_fee_paid", "avg_hourly_fee", "most_time_lot"], "rows": [[1001, 18, 2.4, 1], [1002, 6, 1.33, 2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `ParkingTransactions`

The objective is to compute `{"columns": ["car_id", "total_fee_paid", "avg_hourly_fee", "most_time_lot"], "rows": [[1001, 18, 2.4, 1], [1002, 6, 1.33, 2]]}` from `{"tables": {"ParkingTransactions": [{"lot_id": 1, "car_id": 1001, "entry_time": "2023-06-01 08:00:00", "exit_time": "2023-06-01 10:30:00", "fee_paid": 5}, {"lot_id": 1, "car_id": 1001, "entry_time": "2023-06-02 11:00:00", "exit_time": "2023-06-02 12:45:00", "fee_paid": 3}, {"lot_id": 2, "car_id": 1001, "entry_time": "2023-06-01 10:45:00", "exit_time": "2023-06-01 12:00:00", "fee_paid": 6}, {"lot_id": 2, "car_id": 1002, "entry_time": "2023-06-01 09:00:00", "exit_time": "2023-06-01 11:30:00", "fee_paid": 4}, {"lot_id": 3, "car_id": 1001, "entry_time": "2023-06-03 07:00:00", "exit_time": "2023-06-03 09:00:00", "fee_paid": 4}, {"lot_id": 3, "car_id": 1002, "entry_time": "2023-06-02 12:00:00", "exit_time": "2023-06-02 14:00:00", "fee_paid": 2}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Aggregate time per car and lot

CTE `T` groups transactions by `car_id` and `lot_id`. For each group,

`SUM(TIMESTAMPDIFF(SECOND, entry_time, exit_time))`

adds all visits in seconds. This produces the total time that one car spent in one lot.

CTE `P` ranks those lot totals separately for each car, ordering `duration DESC`. A row with `rk = 1` has a maximum duration for its car.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"ParkingTransactions": [{"lot_id": 1, "car_id": 1001, "entry_time": "2023-06-01 08:00:00", "exit_time": "2023-06-01 10:30:00", "fee_paid": 5}, {"lot_id": 1, "car_id": 1001, "entry_time": "2023-06-02 11:00:00", "exit_time": "2023-06-02 12:45:00", "fee_paid": 3}, {"lot_id": 2, "car_id": 1001, "entry_time": "2023-06-01 10:45:00", "exit_time": "2023-06-01 12:00:00", "fee_paid": 6}, {"lot_id": 2, "car_id": 1002, "entry_time": "2023-06-01 09:00:00", "exit_time": "2023-06-01 11:30:00", "fee_paid": 4}, {"lot_id": 3, "car_id": 1001, "entry_time": "2023-06-03 07:00:00", "exit_time": "2023-06-03 09:00:00", "fee_paid": 4}, {"lot_id": 3, "car_id": 1002, "entry_time": "2023-06-02 12:00:00", "exit_time": "2023-06-02 14:00:00", "fee_paid": 2}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Join the chosen lot to per-car totals

The outer query starts from original transactions `t1` because total fee and average hourly fee must use every visit across every lot.

The left join matches rows from `P` with the same car and rank one. For the intended unique-winner case, every transaction of a car receives the same winning `lot_id`.

Grouping by car then computes:

- `SUM(fee_paid)`, total paid across all visits;
- total parked seconds through another `SUM(TIMESTAMPDIFF(...))`;
- total fee divided by total hours, rounded to two decimal places;
- the joined lot identifier as `most_time_lot`.

Using total fee divided by total duration is a weighted hourly average. It is not the ordinary average of per-transaction rates, which would give short visits the same influence as long visits.

`ORDER BY 1` sorts by selected `car_id` ascending.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Example

If a car spends 4.25 hours in lot 1, 1.25 hours in lot 2, and 2 hours in lot 3, `T` produces those three totals and `P` ranks lot 1 first.

If total fee is 18 and total duration is 7.5 hours, average hourly fee is $18/7.5=2.4$, rendered as 2.40 after rounding.


`T` contains exact car-lot duration totals. Descending rank makes the unique largest duration rank one. The join attaches that lot to all of the car's raw visits without filtering any visit. The outer aggregates therefore compute exact total fee and seconds, and division produces the exact overall hourly rate. One grouped row per car contains all requested values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["car_id", "total_fee_paid", "avg_hourly_fee", "most_time_lot"], "rows": [[1001, 18, 2.4, 1], [1002, 6, 1.33, 2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"ParkingTransactions": [{"lot_id": 1, "car_id": 1001, "entry_time": "2023-06-01 08:00:00", "exit_time": "2023-06-01 10:30:00", "fee_paid": 5}, {"lot_id": 1, "car_id": 1001, "entry_time": "2023-06-02 11:00:00", "exit_time": "2023-06-02 12:45:00", "fee_paid": 3}, {"lot_id": 2, "car_id": 1001, "entry_time": "2023-06-01 10:45:00", "exit_time": "2023-06-01 12:00:00", "fee_paid": 6}, {"lot_id": 2, "car_id": 1002, "entry_time": "2023-06-01 09:00:00", "exit_time": "2023-06-01 11:30:00", "fee_paid": 4}, {"lot_id": 3, "car_id": 1001, "entry_time": "2023-06-03 07:00:00", "exit_time": "2023-06-03 09:00:00", "fee_paid": 4}, {"lot_id": 3, "car_id": 1002, "entry_time": "2023-06-02 12:00:00", "exit_time": "2023-06-02 14:00:00", "fee_paid": 2}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["car_id", "total_fee_paid", "avg_hourly_fee", "most_time_lot"], "rows": [[1001, 18, 2.4, 1], [1002, 6, 1.33, 2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`ROW_NUMBER` with lot tie-breaker:** Order by duration descending and lot ID ascending to select one deterministic winner and prevent join multiplication.
- **Aggregate car totals separately:** Compute fee and duration per car in one CTE, winner lots in another, then join one row to one row.
- **Return all tied lots:** If that were the intended policy, totals must be aggregated before joining so they are not duplicated.
- **Average transaction rates:** Incorrect; overall hourly fee is total fee divided by total hours.
- **Several visits to one lot:** `T` correctly combines their durations before ranking.
- **Fractional hours:** Seconds are divided by 3600 before the final ratio and rounded only at the end.
- **Unique maximum:** The query behaves as intended and returns exact totals.
- **Tied maximum:** The exact query duplicates aggregates and has nondeterministic or invalid grouping behavior.
- **One transaction:** Its lot wins, total fee is that fee, and its hourly rate is direct.
- **Zero-duration transaction:** It could cause division by zero if all duration is zero; the statement implicitly expects valid positive parking intervals.
- **Car independence:** Both grouping and ranking partition by car.
- **Final ordering:** `ORDER BY 1` means ascending car ID.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r log r)$. Let $r$ be the transaction count.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
