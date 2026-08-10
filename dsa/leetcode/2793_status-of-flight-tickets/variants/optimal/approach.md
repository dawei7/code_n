## General

**A passenger's status depends on booking order within one flight**

Each flight has its own independent seat capacity. A passenger is confirmed when their chronological position among bookings for that same flight is at most the capacity. Everyone later is waitlisted.

The exact query combines passenger rows with their flight capacities, assigns each booking a within-flight chronological rank, converts that rank to a status, and finally sorts the report by passenger ID.

**Join capacity onto each passenger**

`Passengers JOIN Flights USING (flight_id)` performs an inner join on the common flight-ID column. Every passenger row receives the corresponding `capacity`.

The result is passenger-oriented: the problem asks for one status row per passenger, not one row per flight. Therefore flights without passenger bookings do not need output rows. Starting from Passengers and using an inner join matches that shape.

The data model implies each booking references its flight. If orphan passenger rows were possible, an inner join would omit them, but no meaningful status could be calculated without capacity; such rows are outside the intended contract.

**Rank separately inside every flight**

The window expression is:

`RANK() OVER (PARTITION BY flight_id ORDER BY booking_time)`.

`PARTITION BY flight_id` restarts ranking for each flight. A first booking on flight 2 receives rank one regardless of how many earlier bookings exist on flight 1.

`ORDER BY booking_time` gives earlier requests smaller ranks. The schema guarantees booking times are distinct, so each partition has ranks `1, 2, 3, ...` without ties or gaps. Under this guarantee, `RANK`, `DENSE_RANK`, and `ROW_NUMBER` would yield the same numbers.

The distinct-time guarantee is important. If two passengers could share a booking time, `RANK` would give both the same position and could confirm more passengers than capacity at the boundary. The exact code relies on the stated uniqueness.

**Compare rank with capacity**

MySQL `IF(condition, trueValue, falseValue)` produces:

- `'Confirmed'` when rank `<= capacity`;
- `'Waitlist'` otherwise.

Capacity `C` means the first `C` chronological bookings receive seats. The inclusive comparison confirms the passenger whose rank is exactly the final available seat. Rank `C + 1` is the first waitlisted request.

The alias `Status` gives the required output column name.

**A walkthrough**

Suppose flight 1 has capacity two and booking times ordered as:

- passenger 103 at 12:00;
- passenger 101 at 16:30;
- passenger 102 at 17:45.

Their ranks inside the flight partition are one, two, and three. Comparing with capacity two marks passengers 103 and 101 Confirmed and passenger 102 Waitlist.

The final report later sorts by passenger ID, so it displays 101, 102, 103 rather than booking order. Ranking and presentation order are separate operations.

**Why final ordering cannot replace window ordering**

`ORDER BY passenger_id` at the end determines only row display order. It does not influence rank, because the window has its own `ORDER BY booking_time` inside `OVER`.

Conversely, the window's chronological order does not guarantee the final result is passenger-ID ordered. Both clauses are needed for different purposes.

**Why no aggregation is necessary**

The occupancy-count problem asks for totals per flight and uses `GROUP BY`. Here every passenger needs an individual status. A window function adds a rank while retaining each original passenger row.

Grouping by flight would collapse passenger identities and be unable to return one row for each `passenger_id`.

**Why the query is correct**

Within each flight, distinct booking times define one strict chronological sequence. `RANK` assigns position `q` to the `q`th booking. Exactly positions one through capacity can fit, so the `<= capacity` test marks exactly the confirmed passengers and every later position as waitlisted. The join supplies the correct capacity for each partition, and final ordering satisfies the reporting requirement.

Each passenger appears once because `passenger_id` is unique and each `flight_id` matches one distinct Flights row.

**Capitalization and literal output**

The exact string literals are `'Confirmed'` and `'Waitlist'`, matching the required values. SQL comparisons here concern numeric rank and capacity, so collation does not affect the status decision.

## Complexity detail

Let `P` be the number of passengers and `F` the number of flights. With indexes or hashing, joining costs about `O(P + F)`. The window function must order passengers within flight partitions. Across all partitions, comparison sorting is bounded by `O(P log P)`.

The final `ORDER BY passenger_id` may require another `O(P log P)` sort unless a plan or index supplies that order. The overall asymptotic bound remains `O(P log P + F)`, matching the manifest.

Window processing and sorting can require `O(P)` working space, while the join's flight lookup can use `O(F)` depending on the physical plan. The manifest reports `O(P)` under the usual assumption that the Flights lookup is indexed or smaller; SQL resource usage is optimizer- and index-dependent.

## Alternatives and edge cases

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
