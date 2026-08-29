## General

**Turn each visit into a gap to its successor**

For one user, place visit dates in ascending order. Every visit begins one candidate window: it ends at that user's next visit, except that the final visit ends at the fixed date `'2021-1-1'`.

The query first computes all such windows in common table expression `T`, then takes the maximum for each user. Separating row-level window calculation from group-level maximum aggregation keeps the two meanings clear.

**Keep users isolated with a window partition**

`LEAD(visit_date, 1, '2021-1-1') OVER (...)` asks for the `visit_date` one row ahead. Its window specification is

`PARTITION BY user_id ORDER BY visit_date`.

`PARTITION BY` gives each user an independent ordered sequence. A row for one user can never take a next date from another user. `ORDER BY visit_date` defines “next” chronologically rather than by arbitrary table storage order.

The offset argument one means immediate successor, not the second or any later visit.

**Supply today for the last visit**

On the final ordered row in a user's partition, no next row exists. The third `LEAD` argument is the default returned in that case, so the expression yields `'2021-1-1'`.

This integrates the special last-visit rule into the same expression used for ordinary consecutive visits. A user with only one visit still gets one meaningful interval—from that visit to today—instead of a null.

The literal's non-zero-padded month and day are accepted as the intended MySQL date value. `DATEDIFF` applies date semantics rather than string subtraction.

**Compute window length in days**

`DATEDIFF(next_date, visit_date)` returns the number of day boundaries from the current visit to the later date. The later date is deliberately the first argument; reversing them would produce negative values.

Inside `T`, each source row becomes `(user_id, diff)`. For a user visiting on October 20 and November 28, the October row's `LEAD` is November 28, and its `diff` is 39. The November row then measures to its own next visit.

For the last December 3 visit, `LEAD` uses January 1 and produces 29, so the tail window participates in the same maximum as all internal gaps.

**Reduce all candidate gaps to one answer per user**

The outer query groups `T` by its first projected column with `GROUP BY 1`. That column is `user_id`. `MAX(diff) AS biggest_window` selects the largest chronological window in each group.

Every user present in `UserVisits` has at least one row in `T`, and that row has a non-null difference because of the `LEAD` default. Thus every represented user produces exactly one output row.

**Return users in the required order**

`ORDER BY 1` sorts the final rows by their first projected column, again `user_id`. Unlike incidental grouping order, this is an explicit guarantee. It satisfies the statement's request to order by user ID.

**Why the query is correct**

Fix a user and sort that user's visits as $d_1\le d_2\le\cdots\le d_r$. The window expression produces

$$
d_2-d_1,\ d_3-d_2,\ \ldots,\ d_r-d_{r-1},\
\text{today}-d_r.
$$

These are exactly all windows named by the contract: every visit to the next one, with today following the last. No cross-user date can appear because of partitioning, and no chronological successor is skipped because the offset is one.

The outer `MAX` returns the largest member of exactly this set. Grouping does this independently for every user, and final ordering changes only presentation, not values.

If duplicate rows occur under the description's lack-of-primary-key wording, equal visit dates become adjacent and add zero-length gaps. One copy at the end of an equal-date run still leads to the next distinct visit or today, so such zero gaps do not increase or remove the true maximum. The local contract also describes the user-date pair as unique; the query works under either interpretation for this maximum.

## Complexity detail

Let $R$ be the number of visit rows. Once rows are ordered by user and date, computing `LEAD` and scanning the CTE for grouped maxima are linear in $R$. A hash aggregation needs up to one state per user, bounded by $O(R)$ space.

In a physical execution without a supporting `(user_id, visit_date)` order, the window function normally requires sorting, which costs $O(R\log R)$ time and $O(R)$ working space. The final `ORDER BY user_id` may require another sort of the user-level result. With a suitable index or already ordered stream, the row processing can approach the manifest's $O(R)$ time.

Thus the manifest's linear time describes the post-ordering logical scan or an order-supported plan; it is not an unconditional bound for every database execution plan. The $O(R)$ space bound covers window/sort materialization in the usual worst case.

## Alternatives and edge cases

- **Self-join on ranked dates:** Assign row numbers and join each visit to rank plus one. It works but is more verbose than `LEAD`.
- **Append today then use `LAG`:** Add one today row per user and compute backward differences. This is equivalent but requires a union and careful deduplication.
- **Correlated next-date subquery:** Find the minimum later date for each visit. Without strong indexing, repeated searches can be much slower.
- **Single visit:** The default date creates the sole window from that visit to today.
- **Duplicate visit dates:** They introduce zero-length gaps but do not inflate the maximum; the successor after the duplicate run remains represented.
- **Several users:** Partitioning prevents a user's last visit from leading into the next user's first visit.
- **Last visit:** The three-argument `LEAD` supplies today directly, avoiding null arithmetic.
- **Date argument order:** `DATEDIFF(next, current)` is required for positive window lengths.
- **Explicit output order:** `ORDER BY 1` guarantees ascending user IDs; `GROUP BY` alone would not.
- **Ordinal clauses:** Both `GROUP BY 1` and `ORDER BY 1` depend on `user_id` remaining the first select expression.
- **Visits on today in generalized data:** The last gap is zero and competes normally with earlier gaps.
- **Fixed today literal:** The solution intentionally uses `2021-01-01` rather than the database server's current date.
