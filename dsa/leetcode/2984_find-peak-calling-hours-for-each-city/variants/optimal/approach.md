## General

**Count calls at the requested granularity.** Extract the hour-of-day from
`call_time`, then group by both `city` and that hour. This produces exactly one
row per city/hour combination with its `number_of_calls`; dates and the call's
direction do not affect the grouping.

**Preserve every maximum.** Rank the hourly rows independently inside each
city by descending count. `DENSE_RANK` assigns rank `1` to every row tied for
the greatest count, so filtering to rank `1` retains all peak hours rather
than choosing an arbitrary one. Finally, order the surviving rows by hour and
city, both descending, as the output contract requires.

The grouping accounts for every call exactly once. Within a city, a row
survives precisely when no hourly count is greater than its count; therefore
the output contains all and only the city's peak hours, including ties.

## Complexity detail

Let $R$ be the number of call rows. Grouping and the required ordering take
$O(R\log R)$ time in the general comparison-based execution model. The grouped
rows and window state use $O(R)$ space in the worst case.

## Alternatives and edge cases

- **Maximum-count join:** Aggregate hourly counts, aggregate again to obtain each city's maximum, and join the two results; this is equally valid but repeats the grouped relation.
- **Correlated raw-row counts:** Counting matching calls separately for every input row is correct but can require quadratic work on duplicate-heavy hours.
- **Tied hours:** Use a tie-preserving rank or equality with the maximum; `ROW_NUMBER` would incorrectly discard tied peaks.
- **Midnight and late evening:** Extract numeric hours so `00` becomes `0` and descending order places `23` before it.
- **Multiple dates:** Calls on different days but in the same city and hour belong to the same group.
- **Ordering ties:** When peak hours match, city names must be descending as the secondary key.
