## General
**Build a complete month spine.** A recursive common table expression generates integers 1 through 12. Starting from this fixed relation guarantees that months with neither rides nor new drivers still appear in the output.

**Count accepted rides by request month.** Join `AcceptedRides` to `Rides` on `ride_id`, restrict `requested_at` to calendar year 2020, and group by its numeric month. This deliberately uses the request date; `AcceptedRides` has no independent acceptance date. Left join those counts onto the month spine and replace missing counts with zero.

**Count drivers through each month end.** For month $m$, count drivers whose `join_date` is earlier than the first day of month $m+1$. The exclusive next-month cutoff includes every date in the current month without depending on month length. Drivers who joined before 2020 remain active in all twelve rows; drivers joining after 2020 appear in none.

The month spine establishes exactly the required output domain. The cutoff predicate counts precisely the drivers present by each month end, while the accepted-rides aggregation counts precisely the accepted requests whose request dates fall in that month. Combining the independent counts by month yields every requested statistic once.

## Complexity detail
The month spine has constant size 12. With ordinary database join and grouping support, scanning $r$ rides and $a$ acceptance rows takes $O(r+a)$ time, and driver cutoff counts across twelve fixed months take $O(d)$ time because 12 is constant. Total time is $O(d+r+a)$. The accepted-ride grouping can retain up to $O(a)$ join/aggregation state; the month relation is constant-sized.

## Alternatives and edge cases
- **Group only existing ride months:** This omits months with zero rides and cannot produce the required twelve rows without a calendar relation.
- **Count all requested rides:** Left joining `Rides` without filtering through `AcceptedRides` incorrectly includes rejected requests.
- **Month-name comparisons:** Comparing formatted strings is less direct and can mishandle year boundaries; use explicit date ranges and numeric months.
- Drivers who joined before 2020 count as active starting in January.
- A driver joining on the last day of a month counts in that month.
- Rides outside 2020 do not contribute even when accepted.
- The request date determines the accepted ride's reported month.
