## General

**Preserve the complete driver set**

The output domain is defined by `driver_id`, not by passengers. Start with a
derived table containing every distinct driver. This guarantees one eventual
group for each person who drove, including drivers that never occur in
`passenger_id`.

**Attach matching passenger rides**

Left-join the driver set back to `Rides` where `passenger_id` equals
`driver_id`. Every joined ride is one occasion on which that driver rode as a
passenger. Group by the driver and count a nullable column from the joined
`Rides` side.

For a driver with passenger occurrences, the join contributes exactly one
non-null `passenger_id` per matching ride, so the count is exact. For a driver
with no match, the left join contributes one null-extended row; `COUNT` ignores
that null and returns zero. Thus every and only driver is retained with the
required count.

## Complexity detail

Let $r$ be the number of rows in `Rides`. Distinct extraction and grouping may
sort up to $r$ rows, giving $O(r\log r)$ time in the general database model;
the join can be implemented with an index or hash structure and linear
additional work. Intermediate driver and grouping state uses $O(r)$ space.
Exact plans and index use remain database-engine dependent.

## Alternatives and edge cases

- **Correlated count subquery:** Counting passenger rows separately for every driver is compact, but without a suitable index it can repeatedly scan `Rides` and take quadratic time.
- **Cartesian product with conditional aggregation:** Comparing every driver with every ride is correct but creates up to $O(r^2)$ candidate pairs.
- **Inner join:** An inner join incorrectly removes drivers who were never passengers.
- **Count all joined rows:** `COUNT(*)` reports one for an unmatched left-join row; count a nullable column from `Rides` instead.
- **Repeated driving:** Many rides by one driver still produce one output row because the driver source is distinct.
- **Passenger but never driver:** A person appearing only in `passenger_id` is not part of the output.
- **Any order:** No `ORDER BY` is required because the contract accepts any row order.
