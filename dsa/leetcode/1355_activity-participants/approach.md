## General

The query needs activities whose participant count is strictly between the smallest and largest activity counts. It first reduces the friend rows to one count per activity, then filters those aggregated rows against the two extremes.

**Count participants per activity once**

The common table expression `t` groups `Friends` by `activity` and computes `COUNT(1) AS cnt`. Each friend row represents one participant and has a primary-key `id`, so counting rows gives the number of participants in that activity. `COUNT(DISTINCT id)` would produce the same result but is unnecessary.

The CTE yields one row such as `(activity, cnt)` for every activity appearing in `Friends`.

The query does not read `Activities`. This is correct because the contract guarantees every catalog activity is performed by at least one friend. Consequently, every activity that must participate in the minimum and maximum comparison already appears as a group in `Friends`. If zero-participant catalog activities were allowed, ignoring `Activities` would incorrectly omit them and could change the minimum.

**Compute the global extremes from grouped counts**

`SELECT MIN(cnt) FROM t` returns the smallest participant count among all activity groups. `SELECT MAX(cnt) FROM t` returns the largest.

The outer predicate requires both:

- `cnt > minimum`, excluding every activity tied for the minimum.
- `cnt < maximum`, excluding every activity tied for the maximum.

Strict comparisons are important. The task does not ask to remove only one minimum activity and one maximum activity; all activities whose count equals either extreme must be excluded.

In the example, counts are three for Eating, two for Singing, and one for Horse Riding. Only two is strictly greater than one and strictly less than three, so Singing is returned.

**Why the filter is exact**

Every catalog activity has one count row in `t`. If its count lies strictly between the extrema, both comparisons are true and the activity is selected. If its count equals the minimum or maximum, at least one comparison is false and it is excluded. No other reason can include or exclude a row.

If all activities have the same number of participants, the minimum equals the maximum. No count can be both greater than and less than that value, so the correct result is empty. With only two distinct count levels, both levels are extremes and the result is also empty.

The result may appear in any order, so no `ORDER BY` is necessary. The selected column is named `activity` directly from the grouped friend data.

Depending on the MySQL optimizer, the CTE may be materialized once and reused by both scalar subqueries, or its logic may be transformed into an equivalent plan. Logically, both extrema must be computed over the same complete set of grouped counts.

## Complexity detail

Let $F$ be the number of friend rows and $A$ the number of activities.

Grouping with a sort-based plan costs $O(F\log F)$ time; a hash aggregate can do expected $O(F)$ work. Scanning the $A$ grouped rows to obtain minimum, maximum, and filtered output is $O(A)$. With $N = F + A$, the comparison-sort upper bound is $O(N\log N)$.

The grouped CTE holds up to $A$ rows, so its principal working storage is $O(A)$. Sort or hash implementation details may require additional plan-dependent memory. The output contains at most $A$ activity names.

## Alternatives and edge cases

- **Window functions:** Compute each count together with `MIN(count) OVER ()` and `MAX(count) OVER ()`, then filter in an outer query. This makes the single grouped pass explicit.
- **Ranking both directions:** Assign ascending and descending ranks to counts and keep rows whose two ranks are not one. Ties are handled naturally.
- **Anti-join against extreme counts:** Build a two-row set containing minimum and maximum, then keep grouped activities that do not join it.
- **Using `Activities` with a left join:** Required if catalog activities could have zero participants. The current guarantee makes that extra work unnecessary.
- **Tied minimum:** Every activity with that count fails the strict lower comparison.
- **Tied maximum:** Every activity with that count fails the strict upper comparison.
- **All counts equal:** Minimum and maximum coincide, so no activity qualifies.
- **Only two count levels:** Both levels are extremes, leaving an empty answer.
- **Several middle levels:** Every activity on any strictly intermediate level is returned.
- **No output order:** The query intentionally omits sorting because any order is accepted.
- **Friend names:** They do not affect participant totals; each row counts once regardless of name text.
- **Catalog guarantee:** Omitting `Activities` is safe only while every catalog activity has at least one matching friend.
- **Activity name identity:** Grouping uses the activity text stored in `Friends`. The data contract must keep that text aligned with the unique catalog activity names; inconsistent spellings would form separate groups.
- **Null activity outside the intended model:** A null activity would form its own SQL group and influence the extrema. The problem describes every friend as taking part in a named catalog activity, so the intended data excludes that ambiguity.
- **Repeated scalar subqueries:** Both extrema read `t`. A materialized CTE avoids regrouping `Friends`, while an optimizer may produce another equivalent plan; the logical answer is unchanged.
