# Guided Example: Find Drivers with Improved Fuel Efficiency

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"drivers": [{"driver_id": 1, "driver_name": "Alice Johnson"}, {"driver_id": 2, "driver_name": "Bob Smith"}, {"driver_id": 3, "driver_name": "Carol Davis"}, {"driver_id": 4, "driver_name": "David Wilson"}, {"driver_id": 5, "driver_name": "Emma Brown"}], "trips": [{"trip_id": 1, "driver_id": 1, "trip_date": "2023-02-15", "distance_km": 120.5, "fuel_consumed": 10.2}, {"trip_id": 2, "driver_id": 1, "trip_date": "2023-03-20", "distance_km": 200.0, "fuel_consumed": 16.5}, {"trip_id": 3, "driver_id": 1, "trip_date": "2023-08-10", "distance_km": 150.0, "fuel_consumed": 11.0}, {"trip_id": 4, "driver_id": 1, "trip_date": "2023-09-25", "distance_km": 180.0, "fuel_consumed": 12.5}, {"trip_id": 5, "driver_id": 2, "trip_date": "2023-01-10", "distance_km": 100.0, "fuel_consumed": 9.0}, {"trip_id": 6, "driver_id": 2, "trip_date": "2023-04-15", "distance_km": 250.0, "fuel_consumed": 22.0}, {"trip_id": 7, "driver_id": 2, "trip_date": "2023-10-05", "distance_km": 200.0, "fuel_consumed": 15.0}, {"trip_id": 8, "driver_id": 3, "trip_date": "2023-03-12", "distance_km": 80.0, "fuel_consumed": 8.5}, {"trip_id": 9, "driver_id": 3, "trip_date": "2023-05-18", "distance_km": 90.0, "fuel_consumed": 9.2}, {"trip_id": 10, "driver_id": 4, "trip_date": "2023-07-22", "distance_km": 160.0, "fuel_consumed": 12.8}, {"trip_id": 11, "driver_id": 4, "trip_date": "2023-11-30", "distance_km": 140.0, "fuel_consumed": 11.0}, {"trip_id": 12, "driver_id": 5, "trip_date": "2023-02-28", "distance_km": 110.0, "fuel_consumed": 11.5}]}}`
- **Required output:** `{"columns": ["driver_id", "driver_name", "first_half_avg", "second_half_avg", "efficiency_improvement"], "rows": [[2, "Bob Smith", 11.24, 13.33, 2.1], [1, "Alice Johnson", 11.97, 14.02, 2.05]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `drivers`

The objective is to compute `{"columns": ["driver_id", "driver_name", "first_half_avg", "second_half_avg", "efficiency_improvement"], "rows": [[2, "Bob Smith", 11.24, 13.33, 2.1], [1, "Alice Johnson", 11.97, 14.02, 2.05]]}` from `{"tables": {"drivers": [{"driver_id": 1, "driver_name": "Alice Johnson"}, {"driver_id": 2, "driver_name": "Bob Smith"}, {"driver_id": 3, "driver_name": "Carol Davis"}, {"driver_id": 4, "driver_name": "David Wilson"}, {"driver_id": 5, "driver_name": "Emma Brown"}], "trips": [{"trip_id": 1, "driver_id": 1, "trip_date": "2023-02-15", "distance_km": 120.5, "fuel_consumed": 10.2}, {"trip_id": 2, "driver_id": 1, "trip_date": "2023-03-20", "distance_km": 200.0, "fuel_consumed": 16.5}, {"trip_id": 3, "driver_id": 1, "trip_date": "2023-08-10", "distance_km": 150.0, "fuel_consumed": 11.0}, {"trip_id": 4, "driver_id": 1, "trip_date": "2023-09-25", "distance_km": 180.0, "fuel_consumed": 12.5}, {"trip_id": 5, "driver_id": 2, "trip_date": "2023-01-10", "distance_km": 100.0, "fuel_consumed": 9.0}, {"trip_id": 6, "driver_id": 2, "trip_date": "2023-04-15", "distance_km": 250.0, "fuel_consumed": 22.0}, {"trip_id": 7, "driver_id": 2, "trip_date": "2023-10-05", "distance_km": 200.0, "fuel_consumed": 15.0}, {"trip_id": 8, "driver_id": 3, "trip_date": "2023-03-12", "distance_km": 80.0, "fuel_consumed": 8.5}, {"trip_id": 9, "driver_id": 3, "trip_date": "2023-05-18", "distance_km": 90.0, "fuel_consumed": 9.2}, {"trip_id": 10, "driver_id": 4, "trip_date": "2023-07-22", "distance_km": 160.0, "fuel_consumed": 12.8}, {"trip_id": 11, "driver_id": 4, "trip_date": "2023-11-30", "distance_km": 140.0, "fuel_consumed": 11.0}, {"trip_id": 12, "driver_id": 5, "trip_date": "2023-02-28", "distance_km": 110.0, "fuel_consumed": 11.5}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Fuel efficiency is computed per trip

For one trip, efficiency is:

$$
\frac{\text{distance\_km}}{\text{fuel\_consumed}}.
$$

The CTE applies `AVG` directly to `distance_km / fuel_consumed`. This detail matters. It computes an unweighted arithmetic mean of the individual trip efficiencies. It does not compute `SUM(distance_km) / SUM(fuel_consumed)`. Those formulas can produce different values because trips with different fuel consumption would receive different effective weights in the ratio-of-sums formula.

For example, suppose one trip travels 100 km on 10 units of fuel and another travels 100 km on 20 units. Their per-trip efficiencies are 10 and 5, so the query's average is 7.5. The combined-distance ratio would be `200 / 30`, approximately 6.67. The problem explicitly asks for efficiency for each trip and then its average, so the query uses the first interpretation.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"drivers": [{"driver_id": 1, "driver_name": "Alice Johnson"}, {"driver_id": 2, "driver_name": "Bob Smith"}, {"driver_id": 3, "driver_name": "Carol Davis"}, {"driver_id": 4, "driver_name": "David Wilson"}, {"driver_id": 5, "driver_name": "Emma Brown"}], "trips": [{"trip_id": 1, "driver_id": 1, "trip_date": "2023-02-15", "distance_km": 120.5, "fuel_consumed": 10.2}, {"trip_id": 2, "driver_id": 1, "trip_date": "2023-03-20", "distance_km": 200.0, "fuel_consumed": 16.5}, {"trip_id": 3, "driver_id": 1, "trip_date": "2023-08-10", "distance_km": 150.0, "fuel_consumed": 11.0}, {"trip_id": 4, "driver_id": 1, "trip_date": "2023-09-25", "distance_km": 180.0, "fuel_consumed": 12.5}, {"trip_id": 5, "driver_id": 2, "trip_date": "2023-01-10", "distance_km": 100.0, "fuel_consumed": 9.0}, {"trip_id": 6, "driver_id": 2, "trip_date": "2023-04-15", "distance_km": 250.0, "fuel_consumed": 22.0}, {"trip_id": 7, "driver_id": 2, "trip_date": "2023-10-05", "distance_km": 200.0, "fuel_consumed": 15.0}, {"trip_id": 8, "driver_id": 3, "trip_date": "2023-03-12", "distance_km": 80.0, "fuel_consumed": 8.5}, {"trip_id": 9, "driver_id": 3, "trip_date": "2023-05-18", "distance_km": 90.0, "fuel_consumed": 9.2}, {"trip_id": 10, "driver_id": 4, "trip_date": "2023-07-22", "distance_km": 160.0, "fuel_consumed": 12.8}, {"trip_id": 11, "driver_id": 4, "trip_date": "2023-11-30", "distance_km": 140.0, "fuel_consumed": 11.0}, {"trip_id": 12, "driver_id": 5, "trip_date": "2023-02-28", "distance_km": 110.0, "fuel_consumed": 11.5}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Assigning each trip to a half

`MONTH(trip_date)` returns a month number from 1 through 12. The `CASE` expression maps months 1 through 6 to `half = 1` and months 7 through 12 to `half = 2`:

- January through June belong to the first half;
- July through December belong to the second half.

The CTE groups by `driver_id` and this computed `half`. Therefore, a driver can contribute at most two rows to `T`: one first-half row and one second-half row. Each row contains the driver's unrounded `half_avg`.

The exact query does not group by year and does not filter to a particular year. If `trips` contains several calendar years, all January-to-June trips for a driver are combined into one first-half average, and all July-to-December trips are combined into one second-half average. Under the intended one-year dataset this distinction has no effect, but it is important when describing the exact SQL rather than assuming an unexpressed year condition.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `MONTH(trip_date)` returns a month number from 1 through 12.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Pairing the two halves

The outer query reads `T` twice, naming the copies `t1` and `t2`. Their join requires:

`t1.driver_id = t2.driver_id`

so both rows belong to the same driver. It also requires:

`t1.half < t2.half`.

Because `half` can only be 1 or 2, this inequality has exactly one possible match: `t1` is half 1 and `t2` is half 2. It cannot reverse the halves, and it cannot pair a row with itself.

This inner self-join automatically enforces the requirement that a driver have trips in both halves. A driver represented by only one CTE row has no matching row from the other half and disappears from the result without needing a separate `HAVING` condition.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["driver_id", "driver_name", "first_half_avg", "second_half_avg", "efficiency_improvement"], "rows": [[2, "Bob Smith", 11.24, 13.33, 2.1], [1, "Alice Johnson", 11.97, 14.02, 2.05]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"drivers": [{"driver_id": 1, "driver_name": "Alice Johnson"}, {"driver_id": 2, "driver_name": "Bob Smith"}, {"driver_id": 3, "driver_name": "Carol Davis"}, {"driver_id": 4, "driver_name": "David Wilson"}, {"driver_id": 5, "driver_name": "Emma Brown"}], "trips": [{"trip_id": 1, "driver_id": 1, "trip_date": "2023-02-15", "distance_km": 120.5, "fuel_consumed": 10.2}, {"trip_id": 2, "driver_id": 1, "trip_date": "2023-03-20", "distance_km": 200.0, "fuel_consumed": 16.5}, {"trip_id": 3, "driver_id": 1, "trip_date": "2023-08-10", "distance_km": 150.0, "fuel_consumed": 11.0}, {"trip_id": 4, "driver_id": 1, "trip_date": "2023-09-25", "distance_km": 180.0, "fuel_consumed": 12.5}, {"trip_id": 5, "driver_id": 2, "trip_date": "2023-01-10", "distance_km": 100.0, "fuel_consumed": 9.0}, {"trip_id": 6, "driver_id": 2, "trip_date": "2023-04-15", "distance_km": 250.0, "fuel_consumed": 22.0}, {"trip_id": 7, "driver_id": 2, "trip_date": "2023-10-05", "distance_km": 200.0, "fuel_consumed": 15.0}, {"trip_id": 8, "driver_id": 3, "trip_date": "2023-03-12", "distance_km": 80.0, "fuel_consumed": 8.5}, {"trip_id": 9, "driver_id": 3, "trip_date": "2023-05-18", "distance_km": 90.0, "fuel_consumed": 9.2}, {"trip_id": 10, "driver_id": 4, "trip_date": "2023-07-22", "distance_km": 160.0, "fuel_consumed": 12.8}, {"trip_id": 11, "driver_id": 4, "trip_date": "2023-11-30", "distance_km": 140.0, "fuel_consumed": 11.0}, {"trip_id": 12, "driver_id": 5, "trip_date": "2023-02-28", "distance_km": 110.0, "fuel_consumed": 11.5}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["driver_id", "driver_name", "first_half_avg", "second_half_avg", "efficiency_improvement"], "rows": [[2, "Bob Smith", 11.24, 13.33, 2.1], [1, "Alice Johnson", 11.97, 14.02, 2.05]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Conditional aggregation in one driver row:** C:** - **Conditional aggregation in one driver row:** Compute first- and second-half averages with `AVG(CASE WHEN ... THEN ... END)`, use `HAVING` to require both, and compare them. This avoids the CTE self-join but must repeat or carefully alias the aggregate expressions.
- **Ratio of total distance to total fuel:** `SUM(distance_km) / SUM(fuel_consumed)` weights trips by fuel consumed and does not match the requested average of per-trip efficiencies.
- **Round before comparing:** This could discard a real but small improvement or manufacture equality. The source correctly compares raw averages.
- **Subtract rounded averages:** It can disagree with rounding the raw difference; the source calculates the difference first.
- **Driver with trips only in the first half:** No `t2` row exists, so the inner self-join excludes the driver.
- **Driver with trips only in the second half:** No `t1` row exists, so the driver is also excluded.
- **Equal half averages:** The strict `<` condition rejects the driver because unchanged efficiency is not improvement.
- **Tiny positive improvement:** The driver qualifies on raw values even if the displayed improvement is `0.00`.
- **Multiple trips in one half:** Every trip contributes one efficiency value with equal weight to that half's `AVG`.
- **Boundary months:** June has `MONTH(...) = 6` and is first-half; July has value 7 and is second-half.
- **Several calendar years:** The exact query pools the same halves across all years because year is absent from grouping and filtering.
- **Duplicate driver names:** Ordering may leave their relative order unspecified when both rounded improvement and name tie; `driver_id` could be added as a deterministic final key if required.
- **Ordering precision:** The alias in `ORDER BY` is rounded, so name breaks ties at displayed precision rather than raw precision.
- **Zero fuel consumption:** Division by zero is not a meaningful efficiency and may yield `NULL` or an error depending on SQL mode. The solution relies on valid problem data with usable fuel values.
- **NULL measurements:** In MySQL, a NULL division result is ignored by `AVG`. The stated table semantics are expected to provide valid measurements; otherwise explicit data-quality rules would be needed.
- **Missing driver row:** The inner join to `drivers` excludes a trip aggregate whose `driver_id` has no matching driver, though the intended relational data should maintain that relationship.
- **Input preservation:** The query reads and aggregates the tables; it performs no `INSERT`, `UPDATE`, or `DELETE` operation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(T\log T)$. Let `T` denote the number of rows in `trips` and `D` the number of rows in `drivers`. The CTE must inspect all `T` trips. A database engine may implement `GROUP BY` with hashing in expected `O(T)` time or with sorting in `O(T\log T)` time. The grouped CTE contains at most two rows per driver appearing in `trips`.
- **Auxiliary Space Complexity:** $O(T + D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
