# Guided Example: The Number of Passengers in Each Bus II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Buses": [{"bus_id": 1, "arrival_time": 2, "capacity": 1}, {"bus_id": 2, "arrival_time": 4, "capacity": 10}, {"bus_id": 3, "arrival_time": 7, "capacity": 2}], "Passengers": [{"passenger_id": 11, "arrival_time": 1}, {"passenger_id": 12, "arrival_time": 1}, {"passenger_id": 13, "arrival_time": 5}, {"passenger_id": 14, "arrival_time": 6}, {"passenger_id": 15, "arrival_time": 7}]}}`
- **Required output:** `{"columns": ["bus_id", "passengers_cnt"], "rows": [[1, 1], [2, 1], [3, 2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Buses`

The objective is to compute `{"columns": ["bus_id", "passengers_cnt"], "rows": [[1, 1], [2, 1], [3, 2]]}` from `{"tables": {"Buses": [{"bus_id": 1, "arrival_time": 2, "capacity": 1}, {"bus_id": 2, "arrival_time": 4, "capacity": 10}, {"bus_id": 3, "arrival_time": 7, "capacity": 2}], "Passengers": [{"passenger_id": 11, "arrival_time": 1}, {"passenger_id": 12, "arrival_time": 1}, {"passenger_id": 13, "arrival_time": 5}, {"passenger_id": 14, "arrival_time": 6}, {"passenger_id": 15, "arrival_time": 7}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Encode both kinds of event in the same columns

The derived table `a` is built with `UNION ALL`:

- a bus becomes `(bus_id, arrival_time AS dt, capacity AS cnt)`;
- a passenger becomes `(-1, arrival_time AS dt, -1 AS cnt)`.

A positive `bus_id` identifies a bus. The sentinel ID `-1` identifies a passenger. Bus `cnt` is positive capacity, while passenger `cnt` is negative one.

`UNION ALL` is necessary because every passenger event matters, including passengers sharing an arrival time. Removing duplicates would undercount waiting people.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Buses": [{"bus_id": 1, "arrival_time": 2, "capacity": 1}, {"bus_id": 2, "arrival_time": 4, "capacity": 10}, {"bus_id": 3, "arrival_time": 7, "capacity": 2}], "Passengers": [{"passenger_id": 11, "arrival_time": 1}, {"passenger_id": 12, "arrival_time": 1}, {"passenger_id": 13, "arrival_time": 5}, {"passenger_id": 14, "arrival_time": 6}, {"passenger_id": 15, "arrival_time": 7}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Order passengers before a bus at the same time

The window expression `SUM(cnt) OVER (ORDER BY dt, bus_id)` establishes the intended chronological key. At equal `dt`, passenger events have `bus_id = -1` and therefore precede positive bus IDs. This matches the inclusive rule that a passenger arriving at the same time as a bus may board it.

The cumulative value is named `cur`. It is selected into the CTE even though the outer query does not use it directly.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Interpret the user variable t

The single-row derived table `(SELECT @t := 0 AS x)` initializes the MySQL session variable `@t`. The expression

`IF(@t > 0, @t := cnt, @t := @t + cnt)`

produces `cur_sum` for each intended event.

The sign of `@t` carries state:

- `@t <= 0` means `-@t` passengers are waiting;
- `@t > 0` means the previous bus had unused capacity.

Unused capacity cannot carry forward to another bus. Therefore, when the previous state is positive, the next event resets `@t` to its own `cnt`. If the next event is a passenger, the state becomes `-1`, beginning a new waiting count. If it is another bus with no intervening passenger, the state becomes that bus’s positive capacity.

When `@t <= 0`, adding passenger `cnt = -1` increases the waiting count by one. Adding a bus’s positive capacity offsets the negative waiting amount.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["bus_id", "passengers_cnt"], "rows": [[1, 1], [2, 1], [3, 2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Buses": [{"bus_id": 1, "arrival_time": 2, "capacity": 1}, {"bus_id": 2, "arrival_time": 4, "capacity": 10}, {"bus_id": 3, "arrival_time": 7, "capacity": 2}], "Passengers": [{"passenger_id": 11, "arrival_time": 1}, {"passenger_id": 12, "arrival_time": 1}, {"passenger_id": 13, "arrival_time": 5}, {"passenger_id": 14, "arrival_time": 6}, {"passenger_id": 15, "arrival_time": 7}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["bus_id", "passengers_cnt"], "rows": [[1, 1], [2, 1], [3, 2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recursive chronological CTE:** Assign each bus a sequence number, count arrivals between consecutive buses, and carry waiting passengers explicitly. This is deterministic and directly models capacity.
- **Procedural or pandas simulation:** Sort buses, advance through sorted passengers, and maintain a waiting count. This is conceptually simple outside pure SQL.
- **Cumulative eligible counts alone:** Unlike Bus I, subtracting consecutive cumulative arrivals is insufficient because passengers left behind by a full bus must carry forward.
- **Use `UNION` instead of `UNION ALL`:** This could collapse identical passenger event rows and lose people; every event must remain.
- **Passenger at bus time:** The sentinel ID `-1` sorts before positive bus IDs at equal `dt`, making that passenger available.
- **More waiting passengers than capacity:** `cur_sum` remains nonpositive, the bus boards its full capacity, and the negative remainder carries waiting passengers.
- **Fewer waiting passengers than capacity:** `cur_sum` becomes positive, and subtracting unused seats from capacity yields the waiting count.
- **No passengers before a bus:** The state is positive after the bus, so its passenger count is zero.
- **Consecutive empty buses:** Positive state is reset to each new capacity rather than accumulated, because unused seats do not transfer.
- **Passengers after unused capacity:** The first new passenger resets positive state to minus one, correctly discarding the departed bus’s empty seats.
- **Several passengers share a time:** `UNION ALL` retains one negative event per passenger.
- **Bus IDs out of arrival order:** Boarding logic intends chronological event order; final output alone is sorted by ID.
- **Positive capacities:** The sign-based interpretation depends on every bus capacity being greater than zero, as guaranteed.
- **User-variable order:** Without a guaranteed event evaluation order, results may be optimizer-dependent; an explicit recursive solution avoids this reliance.
- **Session state:** The joined initialization subquery resets `@t` for this statement, preventing a previous session value from being used initially.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N log N)$. Let $N=B+P$ be the total number of bus and passenger events. Constructing the event stream is $O(N)$. Ordering it for the window calculation and final processing generally costs $O(N\log N)$, and the per-event arithmetic is linear. The final sort of the $B$ bus rows by ID costs $O(B\log B)$ and is covered by the same worst-case bound.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
