# Guided Example: Status of Flight Tickets

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Flights": [{"flight_id": 1, "capacity": 2}, {"flight_id": 2, "capacity": 2}, {"flight_id": 3, "capacity": 1}], "Passengers": [{"passenger_id": 101, "flight_id": 1, "booking_time": "2023-07-10 16:30:00"}, {"passenger_id": 102, "flight_id": 1, "booking_time": "2023-07-10 17:45:00"}, {"passenger_id": 103, "flight_id": 1, "booking_time": "2023-07-10 12:00:00"}, {"passenger_id": 104, "flight_id": 2, "booking_time": "2023-07-05 13:23:00"}, {"passenger_id": 105, "flight_id": 2, "booking_time": "2023-07-05 09:00:00"}, {"passenger_id": 106, "flight_id": 3, "booking_time": "2023-07-08 11:10:00"}, {"passenger_id": 107, "flight_id": 3, "booking_time": "2023-07-08 09:10:00"}]}}`
- **Required output:** `{"columns": ["passenger_id", "Status"], "rows": [[101, "Confirmed"], [102, "Waitlist"], [103, "Confirmed"], [104, "Confirmed"], [105, "Confirmed"], [106, "Waitlist"], [107, "Confirmed"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Flights`

The objective is to compute `{"columns": ["passenger_id", "Status"], "rows": [[101, "Confirmed"], [102, "Waitlist"], [103, "Confirmed"], [104, "Confirmed"], [105, "Confirmed"], [106, "Waitlist"], [107, "Confirmed"]]}` from `{"tables": {"Flights": [{"flight_id": 1, "capacity": 2}, {"flight_id": 2, "capacity": 2}, {"flight_id": 3, "capacity": 1}], "Passengers": [{"passenger_id": 101, "flight_id": 1, "booking_time": "2023-07-10 16:30:00"}, {"passenger_id": 102, "flight_id": 1, "booking_time": "2023-07-10 17:45:00"}, {"passenger_id": 103, "flight_id": 1, "booking_time": "2023-07-10 12:00:00"}, {"passenger_id": 104, "flight_id": 2, "booking_time": "2023-07-05 13:23:00"}, {"passenger_id": 105, "flight_id": 2, "booking_time": "2023-07-05 09:00:00"}, {"passenger_id": 106, "flight_id": 3, "booking_time": "2023-07-08 11:10:00"}, {"passenger_id": 107, "flight_id": 3, "booking_time": "2023-07-08 09:10:00"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A passenger's status depends on booking order within one flight

Each flight has its own independent seat capacity. A passenger is confirmed when their chronological position among bookings for that same flight is at most the capacity. Everyone later is waitlisted.

The exact query combines passenger rows with their flight capacities, assigns each booking a within-flight chronological rank, converts that rank to a status, and finally sorts the report by passenger ID.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Flights": [{"flight_id": 1, "capacity": 2}, {"flight_id": 2, "capacity": 2}, {"flight_id": 3, "capacity": 1}], "Passengers": [{"passenger_id": 101, "flight_id": 1, "booking_time": "2023-07-10 16:30:00"}, {"passenger_id": 102, "flight_id": 1, "booking_time": "2023-07-10 17:45:00"}, {"passenger_id": 103, "flight_id": 1, "booking_time": "2023-07-10 12:00:00"}, {"passenger_id": 104, "flight_id": 2, "booking_time": "2023-07-05 13:23:00"}, {"passenger_id": 105, "flight_id": 2, "booking_time": "2023-07-05 09:00:00"}, {"passenger_id": 106, "flight_id": 3, "booking_time": "2023-07-08 11:10:00"}, {"passenger_id": 107, "flight_id": 3, "booking_time": "2023-07-08 09:10:00"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Join capacity onto each passenger

`Passengers JOIN Flights USING (flight_id)` performs an inner join on the common flight-ID column. Every passenger row receives the corresponding `capacity`.

The result is passenger-oriented: the problem asks for one status row per passenger, not one row per flight. Therefore flights without passenger bookings do not need output rows. Starting from Passengers and using an inner join matches that shape.

The data model implies each booking references its flight. If orphan passenger rows were possible, an inner join would omit them, but no meaningful status could be calculated without capacity; such rows are outside the intended contract.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Rank separately inside every flight

The window expression is:

`RANK() OVER (PARTITION BY flight_id ORDER BY booking_time)`.

`PARTITION BY flight_id` restarts ranking for each flight. A first booking on flight 2 receives rank one regardless of how many earlier bookings exist on flight 1.

`ORDER BY booking_time` gives earlier requests smaller ranks. The schema guarantees booking times are distinct, so each partition has ranks `1, 2, 3, ...` without ties or gaps. Under this guarantee, `RANK`, `DENSE_RANK`, and `ROW_NUMBER` would yield the same numbers.

The distinct-time guarantee is important. If two passengers could share a booking time, `RANK` would give both the same position and could confirm more passengers than capacity at the boundary. The exact code relies on the stated uniqueness.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["passenger_id", "Status"], "rows": [[101, "Confirmed"], [102, "Waitlist"], [103, "Confirmed"], [104, "Confirmed"], [105, "Confirmed"], [106, "Waitlist"], [107, "Confirmed"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Flights": [{"flight_id": 1, "capacity": 2}, {"flight_id": 2, "capacity": 2}, {"flight_id": 3, "capacity": 1}], "Passengers": [{"passenger_id": 101, "flight_id": 1, "booking_time": "2023-07-10 16:30:00"}, {"passenger_id": 102, "flight_id": 1, "booking_time": "2023-07-10 17:45:00"}, {"passenger_id": 103, "flight_id": 1, "booking_time": "2023-07-10 12:00:00"}, {"passenger_id": 104, "flight_id": 2, "booking_time": "2023-07-05 13:23:00"}, {"passenger_id": 105, "flight_id": 2, "booking_time": "2023-07-05 09:00:00"}, {"passenger_id": 106, "flight_id": 3, "booking_time": "2023-07-08 11:10:00"}, {"passenger_id": 107, "flight_id": 3, "booking_time": "2023-07-08 09:10:00"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["passenger_id", "Status"], "rows": [[101, "Confirmed"], [102, "Waitlist"], [103, "Confirmed"], [104, "Confirmed"], [105, "Confirmed"], [106, "Waitlist"], [107, "Confirmed"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`ROW_NUMBER` instead of `RANK`:** It is the clearest exact seat position and gives the same result because booking times are distinct.
- **Correlated count of earlier bookings:** Count passengers on the same flight with earlier times for every row. It is logically valid but can be quadratic without strong indexing.
- **Group by flight:** It loses individual passenger rows and solves the occupancy totals problem instead.
- **Capacity exactly equals booking count:** Every rank is within capacity, so all passengers are Confirmed.
- **More bookings than seats:** Ranks above capacity become Waitlist.
- **Flight with no passengers:** It contributes no row because output is per passenger.
- **Capacity one:** Only the earliest booking in that partition is confirmed.
- **Distinct booking times:** They prevent ties; without this guarantee, `RANK` could assign the same seat position to multiple passengers.
- **Separate orderings:** Booking time controls status; passenger ID controls final display.
- **Passenger IDs unrelated to time:** A smaller ID can have a later booking and still be waitlisted.
- **Inner join:** It assumes every passenger references an existing flight, as the problem data model intends.
- **Database indexes:** Indexes on flight ID, booking time, and passenger ID can reduce physical sorting or lookup work without changing query semantics.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P log P + F)$. Let `P` be the number of passengers and `F` the number of flights. With indexes or hashing, joining costs about `O(P + F)`. The window function must order passengers within flight partitions. Across all partitions, comparison sorting is bounded by `O(P log P)`.
- **Auxiliary Space Complexity:** $O(F)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
