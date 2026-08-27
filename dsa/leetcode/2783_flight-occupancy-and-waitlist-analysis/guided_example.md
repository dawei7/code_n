# Guided Example: Flight Occupancy and Waitlist Analysis

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Flights": [{"flight_id": 1, "capacity": 2}, {"flight_id": 2, "capacity": 2}, {"flight_id": 3, "capacity": 1}], "Passengers": [{"passenger_id": 101, "flight_id": 1}, {"passenger_id": 102, "flight_id": 1}, {"passenger_id": 103, "flight_id": 1}, {"passenger_id": 104, "flight_id": 2}, {"passenger_id": 105, "flight_id": 2}, {"passenger_id": 106, "flight_id": 3}, {"passenger_id": 107, "flight_id": 3}]}}`
- **Required output:** `{"columns": ["flight_id", "booked_cnt", "waitlist_cnt"], "rows": [[1, 2, 1], [2, 2, 0], [3, 1, 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Flights`

The objective is to compute `{"columns": ["flight_id", "booked_cnt", "waitlist_cnt"], "rows": [[1, 2, 1], [2, 2, 0], [3, 1, 1]]}` from `{"tables": {"Flights": [{"flight_id": 1, "capacity": 2}, {"flight_id": 2, "capacity": 2}, {"flight_id": 3, "capacity": 1}], "Passengers": [{"passenger_id": 101, "flight_id": 1}, {"passenger_id": 102, "flight_id": 1}, {"passenger_id": 103, "flight_id": 1}, {"passenger_id": 104, "flight_id": 2}, {"passenger_id": 105, "flight_id": 2}, {"passenger_id": 106, "flight_id": 3}, {"passenger_id": 107, "flight_id": 3}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Begin from flights because every flight needs a row

The output is one aggregate row per flight, including a flight with no passenger requests. The exact query therefore uses `Flights` as the left side of a `LEFT JOIN` and attaches matching `Passengers` rows through the shared `flight_id` column:

`Flights LEFT JOIN Passengers USING (flight_id)`.

An inner join would remove flights that have no passengers. A left join preserves them by producing one joined row whose passenger columns are null.

`USING (flight_id)` is shorthand for equality of the same-named columns and exposes one merged `flight_id` column rather than two qualified copies.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Flights": [{"flight_id": 1, "capacity": 2}, {"flight_id": 2, "capacity": 2}, {"flight_id": 3, "capacity": 1}], "Passengers": [{"passenger_id": 101, "flight_id": 1}, {"passenger_id": 102, "flight_id": 1}, {"passenger_id": 103, "flight_id": 1}, {"passenger_id": 104, "flight_id": 2}, {"passenger_id": 105, "flight_id": 2}, {"passenger_id": 106, "flight_id": 3}, {"passenger_id": 107, "flight_id": 3}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Aggregate demand once per flight

`GROUP BY 1` groups by the first selected expression, which is `flight_id`. Every joined passenger row for one flight enters the same group.

The request count is `COUNT(passenger_id)`. SQL `COUNT(column)` counts only non-null values. This distinction is essential for an empty flight: its left-join placeholder has `passenger_id = NULL`, so the count is zero. `COUNT(*)` would count that placeholder as one and incorrectly invent a booking.

The schema says `passenger_id` is unique, so counting rows and counting distinct passenger IDs are equivalent for real matches. No `DISTINCT` is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `GROUP BY 1` groups by the first selected expression, which ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Clamp confirmed bookings to capacity

For one flight, let `P` be `COUNT(passenger_id)` and `C` be `capacity`. The number of passengers receiving seats is:

$$
\min(P,C).
$$

The SQL expression `LEAST(COUNT(passenger_id), capacity)` computes that minimum and aliases it `booked_cnt`.

If demand is below capacity, all `P` passengers are confirmed. If demand equals or exceeds capacity, only `C` seats can be assigned. The calculation does not need passenger booking order because this problem asks only for totals, not which individuals received the seats.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["flight_id", "booked_cnt", "waitlist_cnt"], "rows": [[1, 2, 1], [2, 2, 0], [3, 1, 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Flights": [{"flight_id": 1, "capacity": 2}, {"flight_id": 2, "capacity": 2}, {"flight_id": 3, "capacity": 1}], "Passengers": [{"passenger_id": 101, "flight_id": 1}, {"passenger_id": 102, "flight_id": 1}, {"passenger_id": 103, "flight_id": 1}, {"passenger_id": 104, "flight_id": 2}, {"passenger_id": 105, "flight_id": 2}, {"passenger_id": 106, "flight_id": 3}, {"passenger_id": 107, "flight_id": 3}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["flight_id", "booked_cnt", "waitlist_cnt"], "rows": [[1, 2, 1], [2, 2, 0], [3, 1, 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Pre-aggregate passengers in a subquery:** Coun:** - **Pre-aggregate passengers in a subquery:** Count requests by flight first, then left-join those counts to Flights and replace null with zero. It is equivalent but more verbose.
- **Inner join:** It incorrectly omits flights with no passengers.
- **`COUNT(*)`:** It counts the left-join placeholder and reports one passenger for an empty flight.
- **`COUNT(DISTINCT passenger_id)`:** It is unnecessary because passenger IDs are unique, though it would produce the same logical count.
- **Demand below capacity:** `booked_cnt` equals demand and `waitlist_cnt` is zero.
- **Demand equals capacity:** Every passenger is confirmed and no one waits.
- **Demand exceeds capacity:** Confirmed count is capped at capacity and the exact excess is waitlisted.
- **No passengers:** Both counts are zero while the flight row remains present.
- **Flight ID ordering:** Ascending is the default for `ORDER BY 1`.
- **Functional dependency:** Unique `flight_id` determines one capacity; stricter SQL dialects may still require capacity in the group list.
- **Individual booking order:** It is irrelevant when reporting counts only. The later passenger-status problem requires chronological ranking, but this query does not.
- **Physical indexes:** They affect execution cost without changing the relational reasoning or result.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(F + P)$. Let `F` be the number of flight rows and `P` the number of passenger rows. With a hash join or an index on `Passengers.flight_id` plus hash aggregation, joining and grouping require `O(F + P)` expected processing. The final ordering of `F` grouped rows can cost `O(F log F)` unless the database can produce groups in flight-ID order from an index or ordered plan.
- **Auxiliary Space Complexity:** $O(F)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
