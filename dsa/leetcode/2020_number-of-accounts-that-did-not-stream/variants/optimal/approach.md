## General

**Identify subscriptions overlapping 2021**

An account bought/held a subscription in 2021 when its subscription interval overlaps that calendar year. The source tests

`YEAR(start_date) <= 2021`

and

`YEAR(end_date) >= 2021`.

Together these keep subscriptions starting no later than 2021 and ending no earlier than 2021. Under date granularity, that expresses overlap with some part of the year.

**What the left join produces**

`Subscriptions AS sub LEFT JOIN Streams USING (account_id)` joins every subscription with all of that account's stream sessions.

If an account has several sessions, it produces several rows. If it has no sessions at all, the subscription is retained once with null stream columns.

A correct anti-join solution would use this null-extended row to identify accounts with no relevant stream.

**What the exact source actually filters**

The final stream predicate is

`YEAR(stream_date) != 2021 OR stream_date > end_date`.

This keeps an individual joined session row when its year is not 2021 or when it occurs after the subscription ended. It does not prove that the account had no 2021 session.

The query then applies `COUNT(sub.account_id)` to surviving joined rows. It counts session rows, not distinct subscription accounts.

**Why accounts with no streams are incorrectly excluded**

For a null-extended left-join row, `stream_date` is SQL `NULL`. Both `YEAR(NULL) != 2021` and `NULL > end_date` evaluate to unknown, not true. Unknown OR unknown is unknown, and a `WHERE` clause discards it.

Thus an account with no stream rows—the most obvious case that should qualify—is not counted by the exact query.

**Why mixed-year accounts are incorrectly included**

Suppose an active account has one stream in 2020 and another in 2021. The 2020 joined row satisfies `YEAR(stream_date) != 2021` and survives, even though the existence of the 2021 row should disqualify the account entirely.

The 2021 row may be discarded, but filtering rows independently cannot express "no matching row exists."

**Why duplicate counting occurs**

If a qualifying-looking account has three non-2021 streams, all three joined rows may pass and `COUNT(sub.account_id)` adds three. The requested unit is accounts, so even the intended population would need one contribution per account.

`COUNT(DISTINCT sub.account_id)` would remove duplication but would not fix the mixed-year or null logic.

**Row conditions and account conditions are different**

This distinction is the central lesson in the query. A `WHERE` predicate is evaluated separately for every joined row. It can answer, “Does this particular stream fall outside 2021?” The requested property is different: “Among all streams belonging to this account, is there no stream inside 2021?” That is a statement about an entire group of possible rows.

Deleting the unwanted 2021 rows does not remember that they once existed. After the deletion, an old row from the same account looks indistinguishable from an old row belonging to an account that never streamed in 2021. An anti-join or `NOT EXISTS` keeps the existence test intact: as soon as one forbidden stream is found, the whole account is rejected. This is why changing only the aggregate cannot repair the exact query.

**The correct relational shape**

One sound pattern is to left join only 2021 streams:

`LEFT JOIN Streams st ON st.account_id = sub.account_id AND YEAR(st.stream_date) = 2021`,

then require `st.account_id IS NULL` after filtering subscriptions that overlap 2021. That null test means no 2021 stream exists.

An equivalent `NOT EXISTS` correlated subquery often states the requirement even more clearly.

**How the example hides the defect**

Accounts 4 and 9 each have a 2020 stream row, so the exact predicate counts those rows and happens to produce two. It is not actually detecting absence of a 2021 session; it is detecting the presence of particular non-2021 joined rows.

Passing that example therefore does not establish correctness on accounts with no sessions, several old sessions, or both old and 2021 sessions.

**Conclusion about the exact source**

The subscription-overlap portion is conceptually useful, but the stream logic and aggregate do not implement the problem. The exact `solution.sql` must be treated as defective rather than described as an optimal correct anti-join.

## Complexity detail

Let $S$ be subscriptions and $T$ stream rows. With hashing/indexing, a properly formulated anti-join can run in expected $O(S+T)$ time and use $O(T)$ lookup space, matching the manifest.

The exact join can materialize up to $T$ matching rows plus unmatched subscriptions and then filter them, with plan-dependent time and space. Its logical output is wrong regardless of execution efficiency.

In a real database, physical cost also depends on indexes, join selection, and whether expressions such as `YEAR(stream_date)` prevent an index range scan. Those implementation details cannot rescue the semantics. Complexity is worth discussing only after the relational expression identifies the right set of accounts.

## Alternatives and edge cases

- **`NOT EXISTS`:** For each overlapping subscription, reject it when any stream row has year 2021; this directly expresses absence.
- **Conditional left anti-join:** Put the 2021 condition in `ON` and require the joined key to be null.
- **`NOT IN`:** Can work with a nonnull account subquery, but null semantics make `NOT EXISTS` safer.
- **No streams at all:** Should qualify if the subscription overlaps 2021; the exact query incorrectly drops it.
- **Both 2020 and 2021 streams:** Should not qualify; the exact query can count the 2020 row.
- **Several old streams:** One account should count once; the exact query can count several rows.
- **Only a 2021 stream:** Correctly should be excluded.
- **Subscription spanning the full year:** Meets both overlap conditions.
- **Subscription ending in 2020:** Does not overlap 2021.
- **SQL null logic:** Comparisons with null are unknown, not true.
- **Counting unit:** The requested result counts accounts, not sessions.
- **Exact-source status:** Its filter is not a valid absence test.
