## General

**Begin from flights because every flight needs a row**

The output is one aggregate row per flight, including a flight with no passenger requests. The exact query therefore uses `Flights` as the left side of a `LEFT JOIN` and attaches matching `Passengers` rows through the shared `flight_id` column:

`Flights LEFT JOIN Passengers USING (flight_id)`.

An inner join would remove flights that have no passengers. A left join preserves them by producing one joined row whose passenger columns are null.

`USING (flight_id)` is shorthand for equality of the same-named columns and exposes one merged `flight_id` column rather than two qualified copies.

**Aggregate demand once per flight**

`GROUP BY 1` groups by the first selected expression, which is `flight_id`. Every joined passenger row for one flight enters the same group.

The request count is `COUNT(passenger_id)`. SQL `COUNT(column)` counts only non-null values. This distinction is essential for an empty flight: its left-join placeholder has `passenger_id = NULL`, so the count is zero. `COUNT(*)` would count that placeholder as one and incorrectly invent a booking.

The schema says `passenger_id` is unique, so counting rows and counting distinct passenger IDs are equivalent for real matches. No `DISTINCT` is needed.

**Clamp confirmed bookings to capacity**

For one flight, let `P` be `COUNT(passenger_id)` and `C` be `capacity`. The number of passengers receiving seats is:

$$
\min(P,C).
$$

The SQL expression `LEAST(COUNT(passenger_id), capacity)` computes that minimum and aliases it `booked_cnt`.

If demand is below capacity, all `P` passengers are confirmed. If demand equals or exceeds capacity, only `C` seats can be assigned. The calculation does not need passenger booking order because this problem asks only for totals, not which individuals received the seats.

**Clamp the excess to a nonnegative waitlist**

Raw excess demand is `P - C`. When capacity exceeds demand, this difference is negative, but a waitlist count cannot be negative. The query uses:

`GREATEST(COUNT(passenger_id) - capacity, 0)`.

This returns zero for an underfilled or exactly full flight and returns `P - C` when demand exceeds capacity.

The booked and waitlist formulas partition all requests:

$$
\min(P,C) + \max(P-C,0) = P.
$$

That identity is a useful consistency check on the result.

**Why capacity need not appear explicitly in the group list**

`flight_id` contains unique values in `Flights`, so one flight ID determines exactly one capacity. Within each group, every joined row originates from that one flight row and therefore has the same `capacity`.

MySQL can select and use this functionally dependent column while grouping by the unique flight ID. In SQL engines with stricter syntactic rules or without functional-dependency recognition, `capacity` could be added to the `GROUP BY` clause without changing the result.

**A no-passenger walkthrough**

Suppose flight 9 has capacity 100 and no matching passenger. The left join still creates its group. `COUNT(passenger_id)` returns zero because the placeholder ID is null.

- `LEAST(0, 100)` gives zero confirmed bookings.
- `GREATEST(0 - 100, 0)` gives zero waitlisted passengers.

The flight appears as `(9, 0, 0)`, which is why starting from `Flights` and counting a nullable passenger column are both necessary.

**An overbooked walkthrough**

For a flight of capacity two with three passenger rows, `P = 3` and `C = 2`. `LEAST` returns two, while `GREATEST(1, 0)` returns one. The query computes these values in the same grouped row rather than first materializing a separate passenger-count table.

**Ordering the report**

`ORDER BY 1` sorts by the first selected column, again `flight_id`, in ascending order by default. This satisfies the explicit output-order requirement.

Positional references are concise but coupled to select-list order. Here the first column is visibly the required sort and grouping key, so the meaning is stable in the exact query.

**Why the query is correct**

The left join produces every flight and all of its requests. Grouping isolates one flight at a time. The non-null count gives exact demand `P`, including zero for an empty flight. At most `C` requests can be confirmed, so `min(P,C)` is the exact confirmed total; every request beyond `C` is waitlisted, giving `max(P-C,0)`. Finally, sorting places all exact per-flight rows in required ID order.

## Complexity detail

Let `F` be the number of flight rows and `P` the number of passenger rows. With a hash join or an index on `Passengers.flight_id` plus hash aggregation, joining and grouping require `O(F + P)` expected processing. The final ordering of `F` grouped rows can cost `O(F log F)` unless the database can produce groups in flight-ID order from an index or ordered plan.

A complete plan-independent upper description is therefore `O(F + P + F log F)`, while the manifest's `O(F + P)` assumes ordering is available or treats the required output sort separately. Database optimizers may choose different physical plans, so SQL complexity is plan- and index-dependent.

Aggregation state has one group per flight, using `O(F)` working space in a hash plan. A sort-based plan can also require storage proportional to input or grouped rows. The result itself has `F` rows.

## Alternatives and edge cases

- **Pre-aggregate passengers in a subquery:** Count requests by flight first, then left-join those counts to Flights and replace null with zero. It is equivalent but more verbose.
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
