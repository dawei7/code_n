# Guided Example: The Number of Passengers in Each Bus I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Buses": [{"bus_id": 1, "arrival_time": 2}, {"bus_id": 2, "arrival_time": 4}, {"bus_id": 3, "arrival_time": 7}], "Passengers": [{"passenger_id": 11, "arrival_time": 1}, {"passenger_id": 12, "arrival_time": 5}, {"passenger_id": 13, "arrival_time": 6}, {"passenger_id": 14, "arrival_time": 7}]}}`
- **Required output:** `{"columns": ["bus_id", "passengers_cnt"], "rows": [[1, 1], [2, 0], [3, 3]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Buses`

The objective is to compute `{"columns": ["bus_id", "passengers_cnt"], "rows": [[1, 1], [2, 0], [3, 3]]}` from `{"tables": {"Buses": [{"bus_id": 1, "arrival_time": 2}, {"bus_id": 2, "arrival_time": 4}, {"bus_id": 3, "arrival_time": 7}], "Passengers": [{"passenger_id": 11, "arrival_time": 1}, {"passenger_id": 12, "arrival_time": 5}, {"passenger_id": 13, "arrival_time": 6}, {"passenger_id": 14, "arrival_time": 7}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build the cumulative eligible set for every bus

The join condition is

`p.arrival_time <= b.arrival_time`.

For one bus row `b`, this matches every passenger who has arrived by that bus’s time. This includes passengers who actually boarded an earlier bus, so the joined set is cumulative rather than the final per-bus group.

The join is a `LEFT JOIN`, not an inner join. Consequently, every bus remains in the result even if no passenger has arrived by its time. In that case, passenger columns in the joined row are `NULL`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Buses": [{"bus_id": 1, "arrival_time": 2}, {"bus_id": 2, "arrival_time": 4}, {"bus_id": 3, "arrival_time": 7}], "Passengers": [{"passenger_id": 11, "arrival_time": 1}, {"passenger_id": 12, "arrival_time": 5}, {"passenger_id": 13, "arrival_time": 6}, {"passenger_id": 14, "arrival_time": 7}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count passengers without counting the synthetic null row

After the join, `GROUP BY 1` groups by the first selected expression, `bus_id`. Since `bus_id` is unique, each group corresponds to exactly one bus.

The aggregate `COUNT(passenger_id)` counts non-null passenger IDs. It does not count the null placeholder produced by the left join. Therefore it yields zero for a bus with no eligible passenger and otherwise yields the number of passengers whose arrival time is at most that bus’s arrival time.

Let this cumulative count for the bus at arrival time $t_i$ be $C_i$. Because later buses have later arrival times, their eligible passenger sets contain the earlier sets, so $C_i$ is non-decreasing in bus arrival order.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | After the join, `GROUP BY 1` groups by the first selected ex... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Subtract the previous cumulative count

The window expression

`LAG(COUNT(passenger_id), 1, 0) OVER (ORDER BY b.arrival_time)`

retrieves the preceding bus’s cumulative count when buses are ordered by arrival time. The offset `1` means one preceding row. The default `0` is used for the first arriving bus because it has no predecessor.

The selected result is

`COUNT(passenger_id) - previous cumulative count`.

For the first bus, this is $C_1-0$, so every passenger who arrived by that time boards it. For each later bus, $C_i-C_{i-1}$ counts passengers whose arrival time is after the previous bus and at or before the current bus. Those are exactly the passengers who have waited since the preceding departure and have not caught any earlier bus.

In the sample, cumulative counts in bus-arrival order are one, one, and four. Their differences are one, zero, and three, matching the required passenger counts.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["bus_id", "passengers_cnt"], "rows": [[1, 1], [2, 0], [3, 3]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Buses": [{"bus_id": 1, "arrival_time": 2}, {"bus_id": 2, "arrival_time": 4}, {"bus_id": 3, "arrival_time": 7}], "Passengers": [{"passenger_id": 11, "arrival_time": 1}, {"passenger_id": 12, "arrival_time": 5}, {"passenger_id": 13, "arrival_time": 6}, {"passenger_id": 14, "arrival_time": 7}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["bus_id", "passengers_cnt"], "rows": [[1, 1], [2, 0], [3, 3]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Event sweep:** Combine bus and passenger arriv:** - **Event sweep:** Combine bus and passenger arrival events, order them once, maintain a waiting count, and reset it at each bus. This can realize the manifest’s near-$O(N\log N)$ strategy but is not the exact stored query.
- **Correlated count per bus:** Count passengers up to the current bus and subtract a previous threshold. This is conceptually similar but may repeat range work and makes the prior-bus boundary more cumbersome.
- **Assign each passenger with a minimum bus time:** Join passengers to qualifying buses, choose the earliest bus per passenger, then count assignments. This is direct but also creates an inequality join and needs an extra grouping stage.
- **Bus with no passengers ever arrived:** The left join preserves it, `COUNT(passenger_id)` is zero, and the cumulative difference is zero.
- **Bus after an empty interval:** If no passenger arrives between consecutive buses, their cumulative counts are equal and subtraction returns zero.
- **Passenger arrives at bus time:** The inclusive `<=` condition assigns that passenger to the current bus.
- **Passenger arrives after the last bus:** That passenger matches no bus and contributes to no count, which is correct because no bus carries them.
- **Several passengers share an arrival time:** Their unique IDs create separate non-null joined rows, so each is counted.
- **No two bus times equal:** This guarantee makes the chronological predecessor unambiguous for `LAG`.
- **Bus IDs out of time order:** Calculations still use arrival time; only final display uses bus ID.
- **First bus:** The third `LAG` argument supplies zero, preventing a null passenger count.
- **COUNT choice:** `COUNT(*)` would incorrectly count the left-join placeholder for an empty bus. Counting `passenger_id` deliberately ignores it.
- **GROUP BY ordinal:** `GROUP BY 1` means the first selected expression, `bus_id`. An explicit `GROUP BY b.bus_id` would be clearer but equivalent here.
- **Final ordering:** `ORDER BY 1` returns ascending `bus_id` as required, independently of the internal chronological window.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N log N)$. Let $B$ be the number of buses, $P$ the number of passengers, and $J$ the number of rows produced by the inequality join. In the worst case, every passenger arrives before every bus, so $J=BP$. The exact written query may therefore require $O(BP)$ join-row processing, followed by grouping and window work. Sorting the $B$ grouped bus rows for the window and final output costs up to $O(B\log B)$.
- **Auxiliary Space Complexity:** $O(J)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
