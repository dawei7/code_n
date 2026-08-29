# Guided Example: Find Top Performing Driver

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Drivers": [{"driver_id": 1, "name": "Alice", "age": 34, "experience": 10, "accidents": 1}, {"driver_id": 2, "name": "Bob", "age": 45, "experience": 20, "accidents": 3}, {"driver_id": 3, "name": "Charlie", "age": 28, "experience": 5, "accidents": 0}], "Vehicles": [{"vehicle_id": 100, "driver_id": 1, "model": "Sedan", "fuel_type": "Gasoline", "mileage": 20000}, {"vehicle_id": 101, "driver_id": 2, "model": "SUV", "fuel_type": "Electric", "mileage": 30000}, {"vehicle_id": 102, "driver_id": 3, "model": "Coupe", "fuel_type": "Gasoline", "mileage": 15000}], "Trips": [{"trip_id": 201, "vehicle_id": 100, "distance": 50, "duration": 30, "rating": 5}, {"trip_id": 202, "vehicle_id": 100, "distance": 30, "duration": 20, "rating": 4}, {"trip_id": 203, "vehicle_id": 101, "distance": 100, "duration": 60, "rating": 4}, {"trip_id": 204, "vehicle_id": 101, "distance": 80, "duration": 50, "rating": 5}, {"trip_id": 205, "vehicle_id": 102, "distance": 40, "duration": 30, "rating": 5}, {"trip_id": 206, "vehicle_id": 102, "distance": 60, "duration": 40, "rating": 5}]}}`
- **Required output:** `{"columns": ["fuel_type", "driver_id", "rating", "distance"], "rows": [["Electric", 2, 4.5, 180], ["Gasoline", 3, 5.0, 100]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Drivers`

The objective is to compute `{"columns": ["fuel_type", "driver_id", "rating", "distance"], "rows": [["Electric", 2, 4.5, 180], ["Gasoline", 3, 5.0, 100]]}` from `{"tables": {"Drivers": [{"driver_id": 1, "name": "Alice", "age": 34, "experience": 10, "accidents": 1}, {"driver_id": 2, "name": "Bob", "age": 45, "experience": 20, "accidents": 3}, {"driver_id": 3, "name": "Charlie", "age": 28, "experience": 5, "accidents": 0}], "Vehicles": [{"vehicle_id": 100, "driver_id": 1, "model": "Sedan", "fuel_type": "Gasoline", "mileage": 20000}, {"vehicle_id": 101, "driver_id": 2, "model": "SUV", "fuel_type": "Electric", "mileage": 30000}, {"vehicle_id": 102, "driver_id": 3, "model": "Coupe", "fuel_type": "Gasoline", "mileage": 15000}], "Trips": [{"trip_id": 201, "vehicle_id": 100, "distance": 50, "duration": 30, "rating": 5}, {"trip_id": 202, "vehicle_id": 100, "distance": 30, "duration": 20, "rating": 4}, {"trip_id": 203, "vehicle_id": 101, "distance": 100, "duration": 60, "rating": 4}, {"trip_id": 204, "vehicle_id": 101, "distance": 80, "duration": 50, "rating": 5}, {"trip_id": 205, "vehicle_id": 102, "distance": 40, "duration": 30, "rating": 5}, {"trip_id": 206, "vehicle_id": 102, "distance": 60, "duration": 40, "rating": 5}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Build one performance row per driver and fuel type.** The first common table expression, `T`, joins `Drivers` to `Vehicles` through `driver_id` and then joins `Trips` through `vehicle_id`. Each joined row represents a trip associated with a driver and a vehicle fuel type. Grouping by `fuel_type, driver_id` gathers all such trips for one driver's activity within one fuel category.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Drivers": [{"driver_id": 1, "name": "Alice", "age": 34, "experience": 10, "accidents": 1}, {"driver_id": 2, "name": "Bob", "age": 45, "experience": 20, "accidents": 3}, {"driver_id": 3, "name": "Charlie", "age": 28, "experience": 5, "accidents": 0}], "Vehicles": [{"vehicle_id": 100, "driver_id": 1, "model": "Sedan", "fuel_type": "Gasoline", "mileage": 20000}, {"vehicle_id": 101, "driver_id": 2, "model": "SUV", "fuel_type": "Electric", "mileage": 30000}, {"vehicle_id": 102, "driver_id": 3, "model": "Coupe", "fuel_type": "Gasoline", "mileage": 15000}], "Trips": [{"trip_id": 201, "vehicle_id": 100, "distance": 50, "duration": 30, "rating": 5}, {"trip_id": 202, "vehicle_id": 100, "distance": 30, "duration": 20, "rating": 4}, {"trip_id": 203, "vehicle_id": 101, "distance": 100, "duration": 60, "rating": 4}, {"trip_id": 204, "vehicle_id": 101, "distance": 80, "duration": 50, "rating": 5}, {"trip_id": 205, "vehicle_id": 102, "distance": 40, "duration": 30, "rating": 5}, {"trip_id": 206, "vehicle_id": 102, "distance": 60, "duration": 40, "rating": 5}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Within each group, `AVG(rating)` calculates the trip-average rating, and `ROUND(..., 2)` produces the required two-decimal value. `SUM(distance)` calculates the total miles traveled by that driver using that fuel type. These are the first two ranking criteria.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The joins are inner joins. A driver without a vehicle, a vehicle without a trip, or a fuel type with no trips contributes no performance group. That matches the idea of ranking based on actual trips rather than inventing a rating for missing activity.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["fuel_type", "driver_id", "rating", "distance"], "rows": [["Electric", 2, 4.5, 180], ["Gasoline", 3, 5.0, 100]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Drivers": [{"driver_id": 1, "name": "Alice", "age": 34, "experience": 10, "accidents": 1}, {"driver_id": 2, "name": "Bob", "age": 45, "experience": 20, "accidents": 3}, {"driver_id": 3, "name": "Charlie", "age": 28, "experience": 5, "accidents": 0}], "Vehicles": [{"vehicle_id": 100, "driver_id": 1, "model": "Sedan", "fuel_type": "Gasoline", "mileage": 20000}, {"vehicle_id": 101, "driver_id": 2, "model": "SUV", "fuel_type": "Electric", "mileage": 30000}, {"vehicle_id": 102, "driver_id": 3, "model": "Coupe", "fuel_type": "Gasoline", "mileage": 15000}], "Trips": [{"trip_id": 201, "vehicle_id": 100, "distance": 50, "duration": 30, "rating": 5}, {"trip_id": 202, "vehicle_id": 100, "distance": 30, "duration": 20, "rating": 4}, {"trip_id": 203, "vehicle_id": 101, "distance": 100, "duration": 60, "rating": 4}, {"trip_id": 204, "vehicle_id": 101, "distance": 80, "duration": 50, "rating": 5}, {"trip_id": 205, "vehicle_id": 102, "distance": 40, "duration": 30, "rating": 5}, {"trip_id": 206, "vehicle_id": 102, "distance": 60, "duration": 40, "rating": 5}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["fuel_type", "driver_id", "rating", "distance"], "rows": [["Electric", 2, 4.5, 180], ["Gasoline", 3, 5.0, 100]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Correct the accident metric:** Use `MAX(accidents) accidents` or `MIN(accidents) accidents` in CTE `T`. Because the driver value is repeated across joined trips, either returns the actual count.
- **Use `ROW_NUMBER` with a fourth tie-break:** Adding `driver_id ASC` and filtering row number one guarantees exactly one deterministic driver when all stated metrics tie.
- **Correlated subqueries per fuel type:** They can retrieve a top row but repeat aggregation work and are harder to read than grouped CTEs plus a window function.
- **Driver with several vehicles of one fuel type:** Grouping combines all of that driver's trips within the fuel type, which is appropriate for a driver/fuel performance row.
- **Driver with vehicles of several fuel types:** Separate partitions and group keys produce independent performance statistics in each category.
- **No trips:** Inner joins exclude the driver or vehicle from ranking because no rating or distance exists.
- **Rounded-rating tie:** Distance becomes the next criterion even if the unrounded averages differ slightly.
- **Complete metric tie:** `RANK` returns multiple rows with `rk = 1`; whether that is acceptable depends on an unstated final tie policy.
- **Accident count zero:** The intended ascending tie-break favors it, but `SUM` still remains zero regardless of trip count.
- **Trip-count distortion:** A driver-level accident value is multiplied by joined trip count, making the exact query potentially incorrect.
- **Vehicle-ID uniqueness:** Joining Trips on `vehicle_id` alone assumes that identifier uniquely determines a vehicle row despite the documented composite key.
- **Final ordering:** `ORDER BY 1` is valid but positional. `ORDER BY fuel_type ASC` is clearer if projection order later changes.
- **SQL dialect:** The leading `#` comment, CTEs, `USING`, window functions, and alias syntax target a modern MySQL environment.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the size of the joined trip-level relation. Physical cost depends on indexes and MySQL's chosen plan. Hashing or indexing joins and grouping can take expected $O(N)$ work, while grouping and window partition ordering may require $O(N\log N)$ sorting in a general plan. The manifest's $O(N\log N)$ time and $O(N)$ working-space summary is a reasonable database-plan upper-bound characterization.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
