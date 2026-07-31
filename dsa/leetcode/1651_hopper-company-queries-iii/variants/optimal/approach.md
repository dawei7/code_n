## General
**Construct every month before joining activity.** Generate a twelve-row month relation for calendar year 2020. This fixed spine ensures that a month with no accepted rides has distance and duration totals of zero rather than disappearing from the computation.

**Aggregate accepted rides by request month.** Left join each month to `Rides` by the request's extracted year and month, then join matching `AcceptedRides` rows by `ride_id`. Summing `ride_distance` and `ride_duration` counts accepted rides only; rejected requests contribute null acceptance values and therefore add nothing. Requests outside 2020 do not match the required year.

**Average each three-month forward window.** Apply a window average ordered by month with a frame from the current row through the next two rows. Compute that window over all twelve monthly totals, then keep starting months 1 through 10 so every retained frame has exactly three months. Round each average to two decimal places.

The month aggregation assigns every accepted ride in 2020 to exactly one request month. Each final row then includes exactly the three required aggregates, including explicit zeros, so its two arithmetic means match the contract.

## Complexity detail
The month spine and ten windows have fixed sizes. With ordinary join and grouping support, associating $r$ requests with $a$ acceptance rows and aggregating them takes $O(r+a)$ time. The join or aggregation can retain up to $O(a)$ accepted-ride state; all calendar and window relations use constant space.

## Alternatives and edge cases
- **Self-join three monthly rows:** Joining each start month to months $m+1$ and $m+2$, adding their totals, and dividing by 3 is correct, but the explicit window frame states the rolling-average operation more directly.
- **Correlated three-month subqueries:** Summing accepted rides separately for each of ten fixed date ranges is correct, but repeats the ride join and obscures the reusable monthly totals.
- **Average accepted rides directly:** `AVG(ride_distance)` would compute a per-ride average, not the required average of monthly totals divided by three.
- Rejected requests have no matching acceptance row and contribute neither distance nor duration.
- The request date, not the driver's join date, determines the month.
- Accepted rides requested before or after 2020 do not enter any window.
- Empty months contribute zero while still occupying one of the three divisor positions.
- Multiple accepted rides in one month are summed before the window divides by 3.
- November and December can contribute to the October window even though neither is an output starting month.
