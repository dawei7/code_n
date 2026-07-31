## General

**Preserve the complete user population**

Start from `Users` and left-join `Rides` on `user_id`. Every ride belonging to a user becomes an joined row, while a user with no rides still produces one row whose ride columns are `NULL`. An inner join would lose precisely the users whose required total is zero.

Group the joined rows by both `u.user_id` and `u.name`, then compute `SUM(r.distance)`. For a user with rides, the group contains exactly those ride distances, so the sum is the required total. For a user without rides, the only joined distance is `NULL`; SQL's `SUM` then returns `NULL`, which `COALESCE(..., 0)` converts to the required numeric zero.

Name the aggregate column exactly `traveled distance`, including the space. Finally, order by `u.user_id` ascending. Grouping determines one result row per user, while this last sort independently satisfies the presentation requirement.

**Why every output row is correct**

Because `Users.user_id` is unique, each grouped identifier represents one and only one user. The join condition admits exactly the `Rides` rows with that identifier and no rides belonging to another user. Their aggregate is therefore the total distance for that user; the null-preserving join and `COALESCE` handle the empty set as zero. Every user supplies one group and the final ordering changes no values, so the query returns all and only the required rows in the required order.

## Complexity detail

Let $U$ and $R$ be the row counts of `Users` and `Rides`. A hash join and hash aggregation can process the relations in expected $O(U+R)$ work, while the required final ordering costs $O(U\log U)$. In the general comparison-based execution model, the combined upper bound is $O((U+R)\log(U+R))$. Join, grouping, and sorting state use $O(U+R)$ working space. Indexes and database-specific plans may reduce the physical work.

The benchmark defines `size` as $U+R$, with one ride per user. The accepted join-and-group query scales within the stated bound. A correct correlated aggregate rescans `Rides` separately for every user and completes all tiers, but fails with $O(UR+U\log U)$ scaling.

## Alternatives and edge cases

- **Pre-aggregate then join:** Group `Rides` by `user_id` in a common table expression and left-join those totals to `Users`. This is also efficient and can make the one-row-per-user relation explicit.
- **Correlated aggregate:** Compute `SUM(distance)` in a scalar subquery for each user. It is concise and correct, but without an index it may scan all $R$ rides for each of the $U$ users.
- **Inner join:** This drops users with no ride rows and therefore violates the complete-user requirement.
- **Group by name only:** Different users may share a name; grouping without `user_id` can incorrectly merge their totals.
- **Missing `COALESCE`:** `SUM` over the null-extended no-ride row returns `NULL`, not `0`.
- **Multiple rides:** Every matching distance must contribute once to the user's aggregate.
- **Duplicate names:** Equal names still produce separate rows because user identifiers are distinct.
- **Output alias:** The requested heading contains a space: `traveled distance`, not `traveled_distance`.
- **Output order:** Aggregation does not guarantee order; `ORDER BY user_id` is required explicitly.
