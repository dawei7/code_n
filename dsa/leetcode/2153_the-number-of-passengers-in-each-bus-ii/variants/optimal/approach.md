## General

The exact SQL turns buses and passengers into one chronological event stream. A state variable represents either waiting passengers or unused seats from the most recent bus, allowing each capacity-limited boarding count to be computed as the stream advances.

**Encode both kinds of event in the same columns**

The derived table `a` is built with `UNION ALL`:

- a bus becomes `(bus_id, arrival_time AS dt, capacity AS cnt)`;
- a passenger becomes `(-1, arrival_time AS dt, -1 AS cnt)`.

A positive `bus_id` identifies a bus. The sentinel ID `-1` identifies a passenger. Bus `cnt` is positive capacity, while passenger `cnt` is negative one.

`UNION ALL` is necessary because every passenger event matters, including passengers sharing an arrival time. Removing duplicates would undercount waiting people.

**Order passengers before a bus at the same time**

The window expression `SUM(cnt) OVER (ORDER BY dt, bus_id)` establishes the intended chronological key. At equal `dt`, passenger events have `bus_id = -1` and therefore precede positive bus IDs. This matches the inclusive rule that a passenger arriving at the same time as a bus may board it.

The cumulative value is named `cur`. It is selected into the CTE even though the outer query does not use it directly.

**Interpret the user variable t**

The single-row derived table `(SELECT @t := 0 AS x)` initializes the MySQL session variable `@t`. The expression

`IF(@t > 0, @t := cnt, @t := @t + cnt)`

produces `cur_sum` for each intended event.

The sign of `@t` carries state:

- `@t <= 0` means `-@t` passengers are waiting;
- `@t > 0` means the previous bus had unused capacity.

Unused capacity cannot carry forward to another bus. Therefore, when the previous state is positive, the next event resets `@t` to its own `cnt`. If the next event is a passenger, the state becomes `-1`, beginning a new waiting count. If it is another bus with no intervening passenger, the state becomes that bus’s positive capacity.

When `@t <= 0`, adding passenger `cnt = -1` increases the waiting count by one. Adding a bus’s positive capacity offsets the negative waiting amount.

**Recover the number that boarded a bus**

The outer query keeps only `bus_id > 0` events. For one bus, let its capacity be `cnt`.

If `cur_sum > 0` after processing that bus, capacity exceeded the waiting count. The positive remainder is unused seats, so `cnt - cur_sum` is the number of waiting passengers who boarded.

If `cur_sum <= 0`, at least the full capacity was needed. The bus boards `cnt` passengers and a zero or negative state represents no spare seats or people still waiting.

This is encoded as

`IF(cur_sum > 0, cnt - cur_sum, cnt) AS passengers_cnt`.

Finally, `ORDER BY bus_id` produces the required presentation order, which is independent of the chronological order needed for boarding.

For two waiting passengers and a first bus of capacity one, `@t` goes from zero to minus two through passenger events, then to minus one after adding capacity. Since the result is nonpositive, the bus count is its full capacity one, and one passenger remains waiting.

**Important MySQL evaluation-order caveat**

The intended algorithm requires rows to be evaluated in `(dt, bus_id)` order when assignments to `@t` occur. However, a window function’s `ORDER BY` defines the order of that window calculation; it does not generally guarantee the evaluation order of separate select-list expressions or user-variable assignments. MySQL user-variable assignment inside a query is also order-sensitive and discouraged for deterministic stateful logic.

Therefore the arithmetic above explains the intended exact source, but the query relies on execution behavior beyond portable declarative SQL guarantees. A recursive CTE with an explicit sequence number is the safer deterministic formulation.

## Complexity detail

Let $N=B+P$ be the total number of bus and passenger events. Constructing the event stream is $O(N)$. Ordering it for the window calculation and final processing generally costs $O(N\log N)$, and the per-event arithmetic is linear. The final sort of the $B$ bus rows by ID costs $O(B\log B)$ and is covered by the same worst-case bound.

The merged events and window-processing state may require $O(N)$ intermediate space, matching the manifest. Actual cost depends on the MySQL execution plan, available indexes, and whether intermediate results are materialized.

The evaluation-order caveat is a correctness concern separate from asymptotic complexity.

## Alternatives and edge cases

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
