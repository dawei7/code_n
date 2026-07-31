## General

Start from `Flights` and left-join `Passengers` by `flight_id`. Starting from the flight table is essential: it preserves flights with no matching passenger, while passenger rows for nonexistent flights have no flight row from which to produce output.

Group the joined rows by the unique flight identifier and its capacity. Use `COUNT(p.passenger_id)` for the number of requests. Counting this non-null passenger key, rather than `COUNT(*)`, makes an unmatched left-join row contribute zero. Let this count be $r$ and capacity be $c$. The booked count is $\min(c,r)$, while the waitlist count is $\max(r-c,0)$. The app-local SQLite query expresses both clamps with `CASE`; the accepted MySQL artifact uses `LEAST` and `GREATEST`.

Finally, order by `flight_id` ascending as required.

**Why one aggregate row gives both requested counts**

Every valid passenger request joins exactly one flight because `flight_id` is unique in `Flights`. Thus the grouped count $r$ includes every and only the requests for that flight. At most $c$ of them can be booked, so exactly $\min(c,r)$ receive seats. Any remainder is $r-\min(c,r)=\max(r-c,0)$, which is precisely the waitlist count. The left join creates one null passenger row for an empty flight, and counting the passenger key correctly maps it to $r=0$.

## Complexity detail

With an indexed or hash-assisted join, reading $F$ flights and $P$ passenger rows and forming the grouped counts costs $O(F+P)$ time. The aggregation keeps one state record per flight, using $O(F)$ working space; the required output also contains $F$ rows. Ordering can be served by the unique flight key, or otherwise adds $O(F\log F)$ sorting work in a general execution plan.

## Alternatives and edge cases

- **Correlated count per flight:** A scalar subquery can count passengers separately for every flight, but without an index it repeatedly scans `Passengers` and can take $O(FP)$ time.
- **Inner join:** It omits flights with zero passenger requests and therefore violates the one-row-per-flight requirement.
- **Count all joined rows:** `COUNT(*)` reports one passenger for an empty flight because of the null-extended left-join row; count `p.passenger_id` instead.
- **Orphan passenger rows:** Requests for a `flight_id` absent from `Flights` must not create result rows.
- **Exactly full flight:** When $r=c$, all requests are booked and the waitlist count is zero.
- **Under capacity:** The booked count is $r$, not the full capacity.
- **Zero capacity:** Every matching request is waitlisted and none is booked.
- **Ordering:** The final `ORDER BY flight_id` is required even when the input rows happen to be sorted.
