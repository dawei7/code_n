## General
Maintain one hash table from active passenger ID to `(start_station, start_time)`. A check-in inserts or replaces that passenger's active record. A checkout removes the record, subtracts its start time from the checkout time, and identifies the ordered route `(start_station, end_station)`.

Maintain a second hash table from each completed route to two sufficient statistics: total duration and trip count. Add the new duration and increment the count at checkout. An average query divides those two stored values.

Each completed trip enters exactly one ordered route accumulator with its true elapsed time. The accumulator's total is therefore the sum of all and only the route's durations, and its count is the corresponding number of trips. Their quotient is the requested average. Removing an active check-in on checkout also allows the same passenger ID to begin a later independent trip.

## Complexity detail
With expected constant-time hash operations, all $q$ calls take $O(q)$ total time. The active table holds at most $A$ passengers and the aggregate table holds $R$ routes, using $O(A + R)$ space.

## Alternatives and edge cases
- **Store every trip duration:** Keeping a list per route is correct, but re-summing that list for every query can make repeated averages quadratic in the trip count.
- **Store a precomputed average:** Updating only an average risks accumulated floating-point error; integer total and count preserve exact source data until division.
- **Ordered routes:** `("A", "B")` and `("B", "A")` are distinct keys.
- **Repeated passenger:** An ID may travel again after checkout, so its previous active record must be removed.
- **Interleaved passengers:** Active trips may overlap and must remain associated with their own IDs.
- **Changing average:** Every later checkout on a route must affect subsequent queries immediately.
