## General

The unit of measurement is a trip, so compute `distance_km / fuel_consumed` before applying `AVG`. Averaging total distance divided by total fuel would weight trips by fuel consumption and would implement a different statistic.

Group `trips` once by `driver_id`. Inside that aggregation, use one conditional expression for January through June and another for July through December. `AVG` ignores the null produced outside its chosen half, yielding two independent per-trip means in one grouped pass. Preserve those unrounded values in a common table expression.

Join the aggregated row to `drivers` for the name. Requiring both averages to be non-null removes drivers missing either half, and comparing the unrounded second-half average with the unrounded first-half average enforces strict improvement without a rounding-boundary error. Only in the final projection round both averages and their difference to two decimal places. Order the projected improvement descending, then the driver name ascending.

## Complexity detail

Let $T$ be the number of trip rows and $D$ the number of driver rows. Without assuming indexes or hash aggregation, grouping the trips can require $O(T\log T)$ comparison work, and ordering at most $D$ qualifying rows costs $O(D\log D)$. Total time is $O(T\log T+D\log D)$ with $O(T+D)$ working space. A database may reduce the grouping work with hashing or a suitable index.

The benchmark defines $S=D$ and gives every driver four trips, so $T=4S$. The accepted strategy aggregates the trip relation once. A calibrated correct alternative evaluates correlated half-year aggregates repeatedly for each driver, causing quadratic rescanning when no supporting index exists.

## Alternatives and edge cases

- **Correlated aggregates per driver:** Separate subqueries for both half-years are compact, but they may rescan all trips for every driver and become quadratic.
- **Ratio of totals:** `SUM(distance_km) / SUM(fuel_consumed)` is a fuel-weighted rate, not the required arithmetic mean of individual trip efficiencies.
- **Round each trip first:** Early rounding changes the averages; preserve full precision until the final output expressions.
- **Compare rounded averages:** A small genuine improvement can disappear when both halves round to the same value, so filter with the unrounded aggregates.
- **Only one half represented:** Conditional `AVG` returns null for the missing half, and that driver must be excluded.
- **Equal or declining efficiency:** The second-half average must be strictly greater; equality and negative improvement do not qualify.
- **June and July:** June belongs to the first half and July belongs to the second, so the month boundary must be inclusive on both sides.
- **Ordering ties:** Equal reported improvements are resolved by ascending `driver_name`.
