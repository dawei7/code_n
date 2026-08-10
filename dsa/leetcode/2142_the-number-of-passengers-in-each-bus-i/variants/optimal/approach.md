## General

A passenger boards the earliest bus whose arrival time is not earlier than the passenger’s arrival. Equivalently, for each bus, its boarding passengers are those who have arrived by this bus but were not already eligible for an earlier bus.

The SQL query expresses this as a difference of cumulative passenger counts.

**Build the cumulative eligible set for every bus**

The join condition is

`p.arrival_time <= b.arrival_time`.

For one bus row `b`, this matches every passenger who has arrived by that bus’s time. This includes passengers who actually boarded an earlier bus, so the joined set is cumulative rather than the final per-bus group.

The join is a `LEFT JOIN`, not an inner join. Consequently, every bus remains in the result even if no passenger has arrived by its time. In that case, passenger columns in the joined row are `NULL`.

**Count passengers without counting the synthetic null row**

After the join, `GROUP BY 1` groups by the first selected expression, `bus_id`. Since `bus_id` is unique, each group corresponds to exactly one bus.

The aggregate `COUNT(passenger_id)` counts non-null passenger IDs. It does not count the null placeholder produced by the left join. Therefore it yields zero for a bus with no eligible passenger and otherwise yields the number of passengers whose arrival time is at most that bus’s arrival time.

Let this cumulative count for the bus at arrival time $t_i$ be $C_i$. Because later buses have later arrival times, their eligible passenger sets contain the earlier sets, so $C_i$ is non-decreasing in bus arrival order.

**Subtract the previous cumulative count**

The window expression

`LAG(COUNT(passenger_id), 1, 0) OVER (ORDER BY b.arrival_time)`

retrieves the preceding bus’s cumulative count when buses are ordered by arrival time. The offset `1` means one preceding row. The default `0` is used for the first arriving bus because it has no predecessor.

The selected result is

`COUNT(passenger_id) - previous cumulative count`.

For the first bus, this is $C_1-0$, so every passenger who arrived by that time boards it. For each later bus, $C_i-C_{i-1}$ counts passengers whose arrival time is after the previous bus and at or before the current bus. Those are exactly the passengers who have waited since the preceding departure and have not caught any earlier bus.

In the sample, cumulative counts in bus-arrival order are one, one, and four. Their differences are one, zero, and three, matching the required passenger counts.

**Why calculation order and output order differ**

Passenger assignment depends on chronological bus order, so the `LAG` window uses `ORDER BY b.arrival_time`. The requested presentation order is ascending `bus_id`, so the final query uses `ORDER BY 1`, where the first output column is `bus_id`.

These orders need not be the same. The window difference is calculated according to arrival time before the final result rows are displayed according to ID. This is why replacing the window order with `bus_id` would be incorrect unless IDs happened to follow chronology.

**How aggregate and window evaluation cooperate**

The `GROUP BY` first reduces the joined rows to one row per bus with a cumulative `COUNT`. The window function then sees those grouped bus rows and applies `LAG` to their aggregate counts in arrival order. SQL permits an aggregate expression to appear as the argument of a window function at this query level because aggregation logically precedes window evaluation.

**Why the cumulative difference is correct**

No two buses share an arrival time, so every bus has a unique chronological predecessor except the first. A passenger with arrival time $t_p$ belongs to every cumulative count for which $t_p \le t_b$. The passenger first appears in the count of the earliest qualifying bus and remains in all later cumulative counts. Taking consecutive differences counts that passenger exactly once, at the first bus it can use.

Passengers arriving exactly when a bus arrives satisfy `<=` and are included in that bus’s new cumulative portion, as required.

## Complexity detail

Let $B$ be the number of buses, $P$ the number of passengers, and $J$ the number of rows produced by the inequality join. In the worst case, every passenger arrives before every bus, so $J=BP$. The exact written query may therefore require $O(BP)$ join-row processing, followed by grouping and window work. Sorting the $B$ grouped bus rows for the window and final output costs up to $O(B\log B)$.

The precise execution plan depends on the MySQL optimizer and available indexes. An index on passenger arrival time can improve range matching, but the SQL text does not itself guarantee the manifest’s `O(N log N)` event-sweep behavior. The stored query is an inequality join with cumulative aggregation, not an explicit union-and-scan event algorithm.

Intermediate space can be as large as $O(J)$ for materialized join or grouping work plus $O(B)$ grouped/window rows, though a database engine may stream or optimize portions. SQL complexity should therefore be described in terms of the actual plan rather than assuming a particular implementation.

## Alternatives and edge cases

- **Event sweep:** Combine bus and passenger arrival events, order them once, maintain a waiting count, and reset it at each bus. This can realize the manifest’s near-$O(N\log N)$ strategy but is not the exact stored query.
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
