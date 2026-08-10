## General

**Filter the correct year before aggregating.** The result must ignore every login outside 2020, even for a user who also has a qualifying login. `WHERE YEAR(time_stamp) = 2020` extracts the calendar year from each timestamp and retains only rows in that year. Performing this filter before grouping ensures an out-of-year timestamp can neither make a user appear nor become that user's maximum.

**Group the retained rows by user.** `GROUP BY 1` groups by the first expression in the `SELECT` list, which is `user_id`. Every qualifying login for one user enters the same group. A user with no retained row has no group at all and is therefore absent automatically, exactly matching the exclusion rule. The primary key allows a user to have many timestamps but prevents the same `(user_id, time_stamp)` pair from being duplicated.

**Use maximum timestamp as latest timestamp.** Within one user's 2020 group, `MAX(time_stamp)` selects the greatest datetime. Datetime ordering is chronological, so the greatest value is the latest login. The alias `AS last_stamp` gives this aggregate the output column name required by the result schema.

**Walk through the query's logical order.** SQL conceptually begins with all rows from `Logins`. The `WHERE` clause removes 2019, 2021, and every other year. `GROUP BY` partitions the remaining rows by `user_id`. `MAX` produces one value for each partition. Finally, `SELECT` emits the user and that value. Understanding this order prevents a common mistake: computing each user's all-time maximum first and then filtering that maximum to 2020 would wrongly omit a user whose latest-ever login is in 2021 but who also logged in during 2020.

**Trace the example.** User six has three rows, but only `2020-06-30 15:06:07` survives the year predicate, so that is the group's maximum. User eight has February and December 2020 rows; chronological maximum chooses `2020-12-30 00:46:50`. User two retains its January 2020 row. User fourteen's 2019 and 2021 rows are both filtered out, leaving no group and therefore no result row.

**Why one aggregate row per user is guaranteed.** A grouped query emits one row per distinct grouping key. `MAX` reduces every retained timestamp in that group to one scalar. No `DISTINCT` is needed: grouping itself creates unique result users. Likewise, no join back to `Logins` is needed because the requested output contains only the user identifier and latest timestamp, both already available from the aggregate.

**Any result order is acceptable.** The statement allows rows in any order, so the source deliberately has no `ORDER BY`. A database may return groups in an order influenced by its execution plan, index layout, or hashing strategy, and callers must not assume a stable sequence. Adding an order would be valid but would impose work not requested by the contract.

**Why the query is correct.** For each returned user, every input to `MAX` has year 2020 because of the `WHERE` predicate, and every 2020 login for that user is included because no other filter removes it. The maximum is therefore exactly that user's latest 2020 login. A user is returned if and only if at least one qualifying row remains. These two facts establish both value correctness and membership correctness.

**Positional grouping is exact but order-dependent.** `GROUP BY 1` is concise MySQL syntax referring to the first selected expression. In this query that is `user_id`, so it behaves like `GROUP BY user_id`. If the `SELECT` order changed, the positional reference could silently mean something else; the current fixed query is unambiguous.

## Complexity detail

Let $R$ be the number of rows in `Logins` and $U$ the number of users with at least one 2020 login. Evaluating `YEAR` and the predicate across a general scan costs $O(R)$. With hash aggregation, maintaining one maximum per retained user also costs expected $O(R)$ time, giving the manifest's overall $O(R)$ bound.

The grouping state stores up to one user key and current maximum for each qualifying user, requiring $O(U)$ working memory under hash aggregation. The result also contains $U$ rows. A database may instead choose sort-based aggregation, which can cost $O(R\log R)$ time and may spill to disk; SQL complexity depends on the physical plan and available indexes.

Applying `YEAR(time_stamp)` to the column can prevent a conventional index on raw `time_stamp` from being used as a simple range seek unless the engine has a matching functional index. A half-open range predicate could be more index-friendly. The exact source still has correct semantics and a linear-scan high-level analysis.

## Alternatives and edge cases

- **Half-open datetime range:** `time_stamp >= '2020-01-01' AND time_stamp < '2021-01-01'` expresses the same year and can be sargable with an index on `time_stamp`. It also avoids concerns about end-of-year fractional seconds.
- **Window function:** Rank retained logins per user by timestamp descending and keep rank one. This is more machinery than a simple `MAX` when only the timestamp is requested.
- **Correlated subquery:** Selecting rows equal to each user's latest 2020 timestamp can work but may repeat scans and is unnecessary for the two-column aggregate result.
- **User with one 2020 login:** That row is both the group's minimum and maximum and is returned unchanged.
- **User with logins in several years:** Only 2020 rows enter the group. Later logins in 2021 cannot displace the required value.
- **No 2020 logins at all:** The filter leaves no rows, grouping creates no groups, and the result is empty.
- **Boundary timestamps:** Midnight on `2020-01-01` and the end of `2020-12-31` both have year 2020 and qualify; `2021-01-01 00:00:00` does not.
- **No ordering guarantee:** The absence of `ORDER BY` is intentional because any order is accepted. Application code should not rely on the sample's row sequence.
- **Positional `GROUP BY`:** `GROUP BY 1` means `user_id` only because it is selected first. Naming the column explicitly would be more maintainable but returns the same result here.
