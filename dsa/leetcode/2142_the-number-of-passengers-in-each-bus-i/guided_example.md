# Guided Example: The Number of Passengers in Each Bus I

We analyze and execute the relational interval partitioning and cumulative aggregation logic on a representative database instance, demonstrating how temporal boundaries map waiting passengers to unique buses without capacity limits.

- **Input:**
  - `Buses`: `[(1, 2), (2, 4), (3, 7)]` (columns: `bus_id`, `arrival_time`)
  - `Passengers`: `[(11, 1), (12, 5), (13, 6), (14, 7)]` (columns: `passenger_id`, `arrival_time`)
- **Output:**
  - `[(1, 1), (2, 0), (3, 3)]` (columns: `bus_id`, `passengers_cnt`)

This instance illustrates temporal disjoint interval partitioning, empty bus zero-count retention, and exact arrival time boundary inclusion.

---

## 1. Problem Overview & Representative Instance

The database system tracks two entities:
1. `Buses`: Each bus has a distinct `bus_id` and arrives at a unique `arrival_time`.
2. `Passengers`: Each passenger has a distinct `passenger_id` and arrives at a recorded `arrival_time`.

The boarding policy follows strict chronological dispatch:
- A bus arriving at time $t_b$ collects all waiting passengers who arrived at or before $t_b$ ($t_p \le t_b$) and have not already boarded an earlier bus.
- Since buses have infinite capacity, every passenger waiting at the station boards the first bus to arrive at or after their arrival time.
- Any bus that arrives when no eligible passengers are waiting departs with $0$ passengers.
- Passengers who arrive strictly after the last bus departs are never picked up.

In our representative instance:
- Three buses arrive at times $2, 4,$ and $7$.
- Four passengers arrive at times $1, 5, 6,$ and $7$.

We must determine the exact passenger count for each bus and present the result ordered by `bus_id` ascending.

---

## 2. Mathematical & Algorithmic Principles

### Temporal Interval Partitioning

Because all buses have unlimited capacity and every passenger boards the earliest possible bus:
- Each bus $k$ (ordered chronologically by arrival time $t_{b,k}$) services a disjoint half-open temporal interval of passenger arrival times.
- Let $t_{b,0} = -\infty$ (or $0$ if arrival times are strictly positive).
- Bus $k$ collects all passengers whose arrival time $t_p$ satisfies:
$$t_{b,k-1} < t_p \le t_{b,k}$$

This formulation guarantees:
1. **Mutual Exclusivity:** Every passenger arrival time belongs to at most one bus interval.
2. **Exhaustive Routing:** Every passenger arriving before the final bus belongs to exactly one bus interval.

### Interval Construction via Window Functions

In relational terms, each bus can be associated with its predecessor's arrival time using the window lag operator:
$$\text{prev\_arrival\_time} = \text{LAG}(t_{b}, 1, 0) \text{ OVER (ORDER BY } t_b\text{)}$$

Then, joining `Buses` with `Passengers` on:
$$P.\text{arrival\_time} > B.\text{prev\_arrival\_time} \quad \text{AND} \quad P.\text{arrival\_time} \le B.\text{arrival\_time}$$
associates every passenger with their exact bus.

### Outer Join Retention for Zero-Count Buses

A standard inner join would discard any bus whose interval contains zero passenger arrivals (such as Bus 2 arriving at time $4$). To preserve all buses and report `passengers_cnt = 0`:
- We perform a `LEFT JOIN` from `Buses` to `Passengers`.
- We compute `COUNT(P.passenger_id)` rather than `COUNT(*)`, because `COUNT(column)` evaluates to $0$ when the joined passenger columns are `NULL`.

| Bus Parameter | Relational Expression | Concrete Instance Role |
|---|---|---|
| Current Arrival $t_b$ | `Buses.arrival_time` | Upper boundary of passenger collection interval (inclusive) |
| Prior Arrival $t_{b-1}$ | `LAG(arrival_time, 1, 0)` | Lower boundary of passenger collection interval (exclusive) |
| Boarding Condition | $t_{b-1} < t_p \le t_b$ | Relational join predicate for passenger assignment |
| Aggregate Count | `COUNT(passenger_id)` | Null-safe count preserving zero-passenger buses |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace the relational processing across the instance:
- Buses: Bus 1 ($t=2$), Bus 2 ($t=4$), Bus 3 ($t=7$).
- Passengers: Passenger 11 ($t=1$), Passenger 12 ($t=5$), Passenger 13 ($t=6$), Passenger 14 ($t=7$).

```
Timeline:
t = 0      1      2      3      4      5      6      7
Pass:     P11                         P12    P13    P14
Buses:           B1                   B2                   B3
Intervals: (0, 2]                      (2, 4]               (4, 7]
Boarding:  P11 -> B1                  None -> B2           P12, P13, P14 -> B3
```

### Step 1: Establish Temporal Intervals for Each Bus
Sort buses chronologically and establish preceding arrival boundaries:
- **Bus 1 (arrival 2):** First bus. Preceding boundary is $0$. Eligible passenger arrival window is $(0, 2]$.
- **Bus 2 (arrival 4):** Preceding bus arrived at $2$. Eligible passenger arrival window is $(2, 4]$.
- **Bus 3 (arrival 7):** Preceding bus arrived at $4$. Eligible passenger arrival window is $(4, 7]$.

### Step 2: Match Passengers to Bus Intervals
Evaluate each passenger against the established windows:
- **Passenger 11 ($t_p = 1$):**
  - Check interval $(0, 2]$: $0 < 1 \le 2$ holds true.
  - Assigned to Bus 1.
- **Passenger 12 ($t_p = 5$):**
  - Check interval $(0, 2]$: $5 > 2$ (missed).
  - Check interval $(2, 4]$: $5 > 4$ (missed).
  - Check interval $(4, 7]$: $4 < 5 \le 7$ holds true.
  - Assigned to Bus 3.
- **Passenger 13 ($t_p = 6$):**
  - Check interval $(4, 7]$: $4 < 6 \le 7$ holds true.
  - Assigned to Bus 3.
- **Passenger 14 ($t_p = 7$):**
  - Check interval $(4, 7]$: $4 < 7 \le 7$ holds true (exact arrival time match).
  - Assigned to Bus 3.

### Step 3: Aggregate Passenger Counts per Bus
- **Bus 1:** Passenger 11 matched. Count $= 1$.
- **Bus 2:** No passengers matched (window $(2, 4]$ was empty). Passenger field is `NULL`. Null-safe count $= 0$.
- **Bus 3:** Passengers 12, 13, and 14 matched. Count $= 3$.

### Step 4: Format and Order Final Result
Order by `bus_id` ascending:
- Bus 1: Count $= 1$.
- Bus 2: Count $= 0$.
- Bus 3: Count $= 3$.

Output table matches required result: `[(1, 1), (2, 0), (3, 3)]`.

---

## 4. Comprehensive State Trace

The table below catalogs each bus, its active arrival window, matched passengers, and aggregated passenger count:

| `bus_id` | `arrival_time` | Prior Window Bound | Active Window $(t_{\text{prev}}, t_{\text{curr}}]$ | Matched Passenger IDs | Matched Arrivals | Passenger Count |
|---|---|---|---|---|---|---|
| $1$ | $2$ | $0$ | $(0, 2]$ | $[11]$ | $[1]$ | $1$ |
| $2$ | $4$ | $2$ | $(2, 4]$ | None (`NULL`) | None | $0$ |
| $3$ | $7$ | $4$ | $(4, 7]$ | $[12, 13, 14]$ | $[5, 6, 7]$ | $3$ |

### Cumulative Arrival Alternative Verification

Another valid formulation uses cumulative passenger totals:
- At time $2$: Total cumulative passengers arrived $\le 2$ is $1$ (P11).
  - Passengers boarding Bus 1: $1 - 0 = 1$.
- At time $4$: Total cumulative passengers arrived $\le 4$ is $1$ (P11).
  - Passengers boarding Bus 2: $1 - 1 = 0$.
- At time $7$: Total cumulative passengers arrived $\le 7$ is $4$ (P11, P12, P13, P14).
  - Passengers boarding Bus 3: $4 - 1 = 3$.

Both perspectives confirm identical per-bus counts: $1, 0, 3$.

---

## 5. Algorithmic Correctness & Soundness

### Disjoint Partitioning Theorem
Let $\mathcal{B} = \{t_{b,1} < t_{b,2} < \dots < t_{b,m}\}$ be the strictly sorted set of bus arrival times. The sets:
$$I_k = \{t_p \mid t_{b,k-1} < t_p \le t_{b,k}\}$$
form a pairwise disjoint partition of $(0, t_{b,m}]$.
- If $t_p \le t_{b,k-1}$, the passenger arrived prior to bus $k-1$ and must have boarded bus $k-1$ or earlier by induction.
- If $t_p > t_{b,k}$, the passenger arrived after bus $k$ departed and cannot board bus $k$.
- Therefore, passenger $p$ boards bus $k$ if and only if $t_p \in I_k$.

### Null Preservation
Because a `LEFT JOIN` retains all rows of `Buses`, every `bus_id` appears in the output. `COUNT(P.passenger_id)` evaluates to $0$ on rows with no joined passenger records, ensuring that buses with zero passengers are neither dropped nor assigned non-zero values.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Bus with Zero Passengers:** Handled by `LEFT JOIN` and `COUNT(passenger_id)`, emitting count $0$.
2. **Multiple Passengers Arriving Simultaneously:** Multiple passengers sharing the exact same $t_p$ within an interval are all counted individually by `COUNT(P.passenger_id)`.
3. **Passenger Arriving Exactly at Bus Arrival Time:** Handled by the inclusive upper bound ($\le t_{b,k}$). Passenger 14 arriving at $7$ successfully boards Bus 3 arriving at $7$.
4. **Passengers Arriving After All Buses:** Passengers with $t_p > \max(t_b)$ do not satisfy the join condition for any bus and are excluded from all counts.
5. **No Passengers in the Station:** If `Passengers` is completely empty, every bus receives count $0$.

### Common Anti-Patterns
- **Using `COUNT(*)` with `LEFT JOIN`:** `COUNT(*)` counts the preserved bus row even when no passenger matched, falsely turning $0$ into $1$. Using `COUNT(P.passenger_id)` correctly yields $0$ when joined fields are `NULL`.
- **Inner Join:** An `INNER JOIN` eliminates buses that picked up no passengers, omitting Bus 2 from the result table.
- **Unbounded Inequality Join Without Prior Bound:** Joining solely on $P.arrival\_time \le B.arrival\_time$ and counting matches counts all cumulative passengers from the beginning of time, double-counting earlier passengers on later buses.

---

## 7. Complexity Analysis

### Time Complexity
- **Sorting Buses:** Sorting $m$ buses by arrival time takes $O(m \log m)$.
- **Lag Window Function:** Evaluating `LAG` across $m$ sorted bus records takes $O(m)$ time.
- **Join & Group By:**
  - With indexed arrival times or sort-merge join, matching $p$ passengers into $m$ disjoint intervals takes $O(p \log m)$ or $O(p + m \log m)$ time.
  - Aggregating counts and sorting by `bus_id` takes $O(m \log m)$ time.
- Total time complexity is $O(m \log m + p \log m)$.

### Auxiliary Space Complexity
- Intermediate relational tables store window lag bounds for $m$ bus records and grouped counts for $m$ buses.
- Total auxiliary space complexity is $O(m + p)$ for query execution memory.
