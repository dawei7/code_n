## General

Join each passenger to the capacity of their requested flight. Inside a common table expression, assign

`ROW_NUMBER() OVER (PARTITION BY p.flight_id ORDER BY p.booking_time)`

to each booking. Partitioning restarts the sequence for every flight, while ordering by the unique booking timestamp gives the exact chronological seat position.

In the outer query, compare that position with `capacity`. Positions from $1$ through the capacity are labeled `Confirmed`; larger positions are labeled `Waitlist`. Finally, sort by `passenger_id`, which is a separate requirement from the chronological order used to award seats.

**Why the window rank matches ticket status**

For a passenger on flight $f$, the row number equals one plus the number of passengers who booked $f$ earlier. Therefore it is at most the flight's capacity exactly when fewer than `capacity` bookings precede it, meaning a seat remains. If the row number is larger, the earlier bookings already occupy every seat and the passenger must be waitlisted. Each passenger joins one flight and receives one row number, so the query returns exactly one correct status row per passenger.

## Complexity detail

Let $P$ be the number of passenger rows and $F$ the number of flight rows. Joining by `flight_id` is $O(P+F)$ with normal indexing or hashing. Ordering each flight partition for the window function costs at most $O(P\log P)$ overall, and the final passenger ordering has the same upper bound. Thus the general running-time bound is $O(P\log P+F)$, with $O(P)$ working space for ranked rows and sorting. Suitable composite indexes can reduce physical sorting, but the manifest records the general bound.

## Alternatives and edge cases

- **Correlated earlier-booking count:** Count earlier passengers in a scalar subquery for every row. It is correct but can rescan `Passengers` $P$ times and take $O(P^2)$ without a supporting index.
- **Self-join and group:** Join each passenger to all earlier passengers on the same flight, then count. This materializes the same potentially quadratic relation.
- **`RANK` instead of `ROW_NUMBER`:** Unique booking times make their results coincide here, but `ROW_NUMBER` states the one-seat-per-position rule directly.
- **Passenger identifier order:** A smaller `passenger_id` does not imply an earlier booking; use `booking_time` for status and `passenger_id` only for final output order.
- **Exactly full flight:** Every booking is confirmed when the number of requests equals capacity.
- **Under capacity:** All passengers for that flight are confirmed.
- **Flight with no passengers:** It produces no result row because the requested output is passenger status, not flight occupancy.
- **Independent flights:** Capacity and row numbering reset for each `flight_id`.
