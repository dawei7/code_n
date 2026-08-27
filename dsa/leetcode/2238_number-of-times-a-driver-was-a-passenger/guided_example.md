# Guided Example: Number of Times a Driver Was a Passenger

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Rides": [{"ride_id": 1, "driver_id": 7, "passenger_id": 1}, {"ride_id": 2, "driver_id": 7, "passenger_id": 2}, {"ride_id": 3, "driver_id": 11, "passenger_id": 1}, {"ride_id": 4, "driver_id": 11, "passenger_id": 7}, {"ride_id": 5, "driver_id": 11, "passenger_id": 7}, {"ride_id": 6, "driver_id": 11, "passenger_id": 3}]}}`
- **Required output:** `{"columns": ["driver_id", "cnt"], "rows": [[7, 2], [11, 0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Rides`

The objective is to compute `{"columns": ["driver_id", "cnt"], "rows": [[7, 2], [11, 0]]}` from `{"tables": {"Rides": [{"ride_id": 1, "driver_id": 7, "passenger_id": 1}, {"ride_id": 2, "driver_id": 7, "passenger_id": 2}, {"ride_id": 3, "driver_id": 11, "passenger_id": 1}, {"ride_id": 4, "driver_id": 11, "passenger_id": 7}, {"ride_id": 5, "driver_id": 11, "passenger_id": 7}, {"ride_id": 6, "driver_id": 11, "passenger_id": 3}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The output population is the distinct set of drivers

The result needs one row for every ID that appears as a `driver_id` in at least one ride. A driver who was never a passenger must still appear with count zero.

The common table expression

`WITH T AS (SELECT DISTINCT driver_id FROM Rides)`

creates exactly that output population. `DISTINCT` ensures a driver with many driven rides appears once in `T`.

Starting from this driver set is important. If the query grouped only passenger rows, drivers who never rode as passengers would be absent rather than reported with zero.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Rides": [{"ride_id": 1, "driver_id": 7, "passenger_id": 1}, {"ride_id": 2, "driver_id": 7, "passenger_id": 2}, {"ride_id": 3, "driver_id": 11, "passenger_id": 1}, {"ride_id": 4, "driver_id": 11, "passenger_id": 7}, {"ride_id": 5, "driver_id": 11, "passenger_id": 7}, {"ride_id": 6, "driver_id": 11, "passenger_id": 3}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Match driver IDs to passenger occurrences

The query left-joins the original rides:

`LEFT JOIN Rides AS r ON t.driver_id = r.passenger_id`.

For a driver `d`, every ride where `passenger_id = d` produces one joined row. The ride's actual `driver_id` does not matter for this count; the question asks how often `d` occupied the passenger role.

If `d` never appears as a passenger, the left join still emits one row for `t` with all columns from `r` set to `NULL`. This preservation behavior is the reason for using `LEFT JOIN` rather than an inner join.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The query left-joins the original rides:

`LEFT JOIN Rides A... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count matched passenger values, not joined rows

The selected count is

`COUNT(passenger_id) AS cnt`.

SQL's `COUNT(column)` counts non-null values only. For a driver with matching passenger rides, each matched row supplies a non-null `passenger_id` and contributes one. For a never-passenger driver, the placeholder row from the left join has a null right-side passenger value and contributes zero.

Using `COUNT(*)` would be wrong for the zero-match case because it would count the preserved placeholder row and report one instead of zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["driver_id", "cnt"], "rows": [[7, 2], [11, 0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Rides": [{"ride_id": 1, "driver_id": 7, "passenger_id": 1}, {"ride_id": 2, "driver_id": 7, "passenger_id": 2}, {"ride_id": 3, "driver_id": 11, "passenger_id": 1}, {"ride_id": 4, "driver_id": 11, "passenger_id": 7}, {"ride_id": 5, "driver_id": 11, "passenger_id": 7}, {"ride_id": 6, "driver_id": 11, "passenger_id": 3}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["driver_id", "cnt"], "rows": [[7, 2], [11, 0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Inner join:** It counts passenger occurrences :** - **Inner join:** It counts passenger occurrences but entirely drops drivers who were never passengers, violating the required zero rows.
- **Correlated subquery:** For each distinct driver, count matching passenger rows. It is correct, but can repeat scans without suitable indexing.
- **Pre-aggregate passengers then left join:** Group `Rides` by `passenger_id` first and join those counts to distinct drivers with `COALESCE`. This is also valid but uses an additional aggregation subquery.
- **Use `COUNT(*)`:** An unmatched left-join row would count as one. Counting a nullable right-side column is essential.
- **Driver never a passenger:** The left join preserves the driver and the count is zero.
- **Driver is a passenger many times:** Every matching ride row contributes one.
- **Passenger-only ID:** It is not a driver and correctly does not appear.
- **Driver appears in many driven rides:** `DISTINCT` places it once in the output population.
- **Same ID in both roles on different rides:** Those passenger occurrences are counted normally.
- **Self-ride prohibition:** The schema guarantees a ride's driver and passenger differ, but the query does not need this fact for cross-ride counting.
- **Any output order:** No `ORDER BY` is required.
- **Group-by ordinal:** `GROUP BY 1` refers to `t.driver_id`, the first selected expression; writing the column explicitly would be equivalent and sometimes clearer.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r log r)$. Let `r` be the number of ride rows. Producing distinct drivers, joining, and grouping can be implemented with hashing in expected `O(r)` time, but a general database plan may sort for distinctness or grouping. The manifest uses the conservative `O(r \log r)` bound.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
