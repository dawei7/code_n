# Guided Example: The Number of Passengers in Each Bus II

We analyze and execute the sequential capacity-constrained queuing recurrence on a representative database instance, establishing how recursive state transitions track spillover passenger accumulation across temporal intervals.

- **Input:**
  - `Buses`: `[(1, 2, 1), (2, 4, 10), (3, 7, 2)]` (columns: `bus_id`, `arrival_time`, `capacity`)
  - `Passengers`: `[(11, 1), (12, 1), (13, 5), (14, 6), (15, 7)]` (columns: `passenger_id`, `arrival_time`)
- **Output:**
  - `[(1, 1), (2, 1), (3, 2)]` (columns: `bus_id`, `passengers_cnt`)

This instance illustrates FIFO waiting queue aggregation, capacity threshold clamping, carry-forward passenger spillover, and recursive chronological propagation.

---

## 1. Problem Overview & Representative Instance

The transport system consists of two tables:
1. `Buses`: Each bus has a unique `bus_id`, distinct chronological `arrival_time`, and a maximum passenger `capacity`.
2. `Passengers`: Each passenger has a unique `passenger_id` and records an `arrival_time`.

The boarding policy follows sequential capacity-constrained queuing:
- At bus arrival time $t_b$, all passengers who arrived at $t_p \le t_b$ and have not boarded an earlier bus are waiting at the station.
- Bus $b$ boards at most $\text{capacity}_b$ passengers from this waiting pool.
- If the number of waiting passengers exceeds $\text{capacity}_b$, the excess passengers remain at the station, eligible to board later buses.
- Any bus arriving to an empty queue departs with $0$ passengers.

The task is to report `bus_id` and `passengers_cnt` for every bus, ordered by `bus_id` ascending.

In our representative instance:
- Bus 1: Arrives at $t = 2$, capacity $= 1$.
- Bus 2: Arrives at $t = 4$, capacity $= 10$.
- Bus 3: Arrives at $t = 7$, capacity $= 2$.
- Five passengers arrive across times $1, 1, 5, 6,$ and $7$.

Unlike the unconstrained case where each bus operates on an independent interval, finite capacity creates a sequential dependency: leftover passengers from Bus 1 carry over to Bus 2.

---

## 2. Mathematical & Algorithmic Principles

### Interval Decomposition & New Arrivals

Order all $m$ buses chronologically:
$$t_{b,1} < t_{b,2} < \dots < t_{b,m}$$

For each bus $i \in \{1, \dots, m\}$, define the temporal window of newly arrived passengers:
$$I_i = (t_{b, i-1}, \, t_{b, i}] \quad \text{with } t_{b,0} = 0$$

The count of newly arriving passengers during this interval is:
$$N_i = \sum_{p} \mathbf{1}_{\{t_{b,i-1} < t_p \le t_{b,i}\}}$$

### Recursive State Machine for Spillover Queue

Let:
- $W_i$: The number of waiting passengers remaining at the station *after* bus $i$ departs (with base boundary $W_0 = 0$).
- $Q_i$: The total queue of waiting passengers when bus $i$ arrives.
- $C_i$: The passenger capacity of bus $i$.
- $B_i$: The actual number of passengers who board bus $i$.

The system evolves according to the recurrence:
1. **Queue Accumulation:**
   $$Q_i = W_{i-1} + N_i$$
2. **Capacity Clamping (Boarding):**
   $$B_i = \min(Q_i, C_i)$$
3. **Leftover Spillover (Queue Retention):**
   $$W_i = Q_i - B_i = \max(0, \, Q_i - C_i)$$

Because $Q_i$ explicitly depends on $W_{i-1}$, the calculation cannot be parallelized using independent group-by queries; it requires sequential evaluation (or a recursive Common Table Expression in SQL).

| Queue State Variable | Formal Expression | Operational Role in System |
|---|---|---|
| Interval Arrivals $N_i$ | Count of $t_p \in (t_{b,i-1}, t_{b,i}]$ | Passengers arriving since previous bus departure |
| Prior Carry-Over $W_{i-1}$ | Remainder from bus $i-1$ | Stranded passengers waiting for next available bus |
| Total Waiting Queue $Q_i$ | $W_{i-1} + N_i$ | Total pool competing for seats on bus $i$ |
| Boarded Count $B_i$ | $\min(Q_i, C_i)$ | Final reported passenger count for bus $i$ |
| New Spillover $W_i$ | $Q_i - B_i$ | Excess passengers forwarded to bus $i+1$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace the chronological execution over the three buses:
- Buses: Bus 1 ($t=2, C=1$), Bus 2 ($t=4, C=10$), Bus 3 ($t=7, C=2$).
- Passengers: P11 ($t=1$), P12 ($t=1$), P13 ($t=5$), P14 ($t=6$), P15 ($t=7$).

```
Timeline:
t = 0      1      2      3      4      5      6      7
Pass:   P11,P12                        P13    P14    P15
Bus 1: (cap 1) -> picks 1, leaves 1
Bus 2: (cap 10) -> picks 1 leftover, leaves 0
Bus 3: (cap 2) -> picks 2 of 3 waiting, leaves 1
```

### Step 1: Base Initialization
- Initial waiting queue before any bus arrives: $W_0 = 0$.

### Step 2: Process Bus 1 ($t_b = 2$, Capacity $C_1 = 1$)
- Interval: $(0, 2]$.
- Passengers arriving in $(0, 2]$:
  - P11 ($t = 1$), P12 ($t = 1$).
  - New arrivals count: $N_1 = 2$.
- Total waiting queue:
  $$Q_1 = W_0 + N_1 = 0 + 2 = 2$$
- Boarding decision:
  $$B_1 = \min(Q_1, C_1) = \min(2, 1) = 1$$
- Leftover spillover:
  $$W_1 = Q_1 - B_1 = 2 - 1 = 1$$
- Record: Bus 1 departs with $1$ passenger; $1$ passenger remains waiting.

### Step 3: Process Bus 2 ($t_b = 4$, Capacity $C_2 = 10$)
- Interval: $(2, 4]$.
- Passengers arriving in $(2, 4]$: None.
  - New arrivals count: $N_2 = 0$.
- Total waiting queue:
  $$Q_2 = W_1 + N_2 = 1 + 0 = 1$$
- Boarding decision:
  $$B_2 = \min(Q_2, C_2) = \min(1, 10) = 1$$
- Leftover spillover:
  $$W_2 = Q_2 - B_2 = 1 - 1 = 0$$
- Record: Bus 2 departs with $1$ passenger (the leftover from Bus 1); $0$ passengers remain waiting.

### Step 4: Process Bus 3 ($t_b = 7$, Capacity $C_3 = 2$)
- Interval: $(4, 7]$.
- Passengers arriving in $(4, 7]$:
  - P13 ($t = 5$), P14 ($t = 6$), P15 ($t = 7$).
  - New arrivals count: $N_3 = 3$.
- Total waiting queue:
  $$Q_3 = W_2 + N_3 = 0 + 3 = 3$$
- Boarding decision:
  $$B_3 = \min(Q_3, C_3) = \min(3, 2) = 2$$
- Leftover spillover:
  $$W_3 = Q_3 - B_3 = 3 - 2 = 1$$
- Record: Bus 3 departs with $2$ passengers; $1$ passenger remains stranded.

### Step 5: Final Result Ordering
Order output rows by `bus_id` ascending:
- Bus 1: $1$ passenger.
- Bus 2: $1$ passenger.
- Bus 3: $2$ passengers.

Output table: `[(1, 1), (2, 1), (3, 2)]`.

---

## 4. Comprehensive State Trace

The table below catalogs every chronological step, detailing queue evolution, boarding counts, and residual spillover:

| Chronological Order | `bus_id` | Arrival Time $t_b$ | Capacity $C_i$ | Prior Spillover $W_{i-1}$ | New Arrivals $N_i$ | Total Waiting $Q_i$ | Boarded Count $B_i$ | Remaining Spillover $W_i$ |
|---|---|---|---|---|---|---|---|---|
| Initial | - | - | - | - | - | - | - | $0$ |
| 1 | $1$ | $2$ | $1$ | $0$ | $2$ (P11, P12) | $2$ | $\min(2, 1) = \mathbf{1}$ | $1$ |
| 2 | $2$ | $4$ | $10$ | $1$ | $0$ (None) | $1$ | $\min(1, 10) = \mathbf{1}$ | $0$ |
| 3 | $3$ | $7$ | $2$ | $0$ | $3$ (P13, P14, P15) | $3$ | $\min(3, 2) = \mathbf{2}$ | $1$ |

### Comparison with Unconstrained Problem I

- In Part I (infinite capacity), Bus 2 picked up $0$ passengers because nobody arrived in $(2, 4]$.
- In Part II, Bus 2 picks up $1$ passenger because Bus 1 lacked the capacity to board both arrivals from $(0, 2]$, pushing the stranded passenger forward into Bus 2.
- Finite capacities directly link subsequent bus loads through queue state memory.

---

## 5. Algorithmic Correctness & Soundness

### Queue Conservation Invariant
At each step $i$, total passengers accounted for must satisfy the conservation law:
$$\sum_{j=1}^i B_j + W_i = \sum_{j=1}^i N_j$$
- For $i = 1$: $B_1 + W_1 = 1 + 1 = 2 = N_1$.
- For $i = 2$: $(B_1 + B_2) + W_2 = (1 + 1) + 0 = 2 = N_1 + N_2$.
- For $i = 3$: $(B_1 + B_2 + B_3) + W_3 = (1 + 1 + 2) + 1 = 5 = N_1 + N_2 + N_3$.

All passenger arrivals are either boarded or accurately accounted for in the final leftover queue, proving zero loss or phantom duplicate creation.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Massive Capacity Exceeds Total Queue:** If $C_i \ge Q_i$, the bus takes all waiting passengers ($B_i = Q_i$) and resets spillover to $W_i = 0$.
2. **Zero Capacity or Zero Arrivals:** Capacities are strictly positive ($C_i \ge 1$). When $N_i = 0$ and $W_{i-1} = 0$, $Q_i = 0$ and the bus departs with $0$ passengers.
3. **Continuous Capacity Overload:** If every bus has $C_i = 1$ and $10$ passengers arrive each minute, spillover $W_i$ monotonically grows by $9$ each step.
4. **All Passengers Arrive After All Buses:** Passengers with $t_p > \max(t_b)$ never enter any $N_i$ and are excluded from all boarding counts.

### Common Anti-Patterns
- **Non-Recursive Window Aggregate:** Assuming cumulative passengers boarded can be solved with static window sums (`SUM(capacity)`) fails whenever a bus arrives to an under-capacity queue ($C_i > Q_i$), as unused capacity cannot be stored for future passengers.
- **Ignoring Leftover Waiters:** Counting only $N_i$ for each bus ignores passengers stranded by earlier full buses.
- **Sorting by Bus ID Early:** Evaluating the queuing recurrence by `bus_id` rather than `arrival_time` violates physical causality, as passengers must board buses in chronological order of bus arrival.

---

## 7. Complexity Analysis

### Time Complexity
- **Sorting Buses:** Sorting $m$ buses by `arrival_time` takes $O(m \log m)$.
- **Binning Passenger Arrivals:** Assigning $p$ passengers to the $m$ bus intervals takes $O(p \log m)$ using binary search, or $O(p + m \log m)$ via two-pointer merge.
- **Sequential Queue Recurrence:** The recurrence $W_i = \max(0, W_{i-1} + N_i - C_i)$ takes $O(1)$ operations per bus, running in $O(m)$ time across all buses.
- **Final Result Sort:** Sorting output by `bus_id` takes $O(m \log m)$.
- Total time complexity is $O(m \log m + p \log m)$.

### Auxiliary Space Complexity
- Storing sorted bus interval arrival counts requires $O(m)$ space.
- The recursive queue state machine requires $O(1)$ auxiliary scalar state ($W$).
- Total auxiliary space complexity is $O(m)$ for query execution tables.
