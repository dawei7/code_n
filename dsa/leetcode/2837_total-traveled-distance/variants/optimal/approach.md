## General

**Begin from every user, not every ride.** The result must include users who have never completed a ride. Therefore, `Users` must be the preserved side of the join. The query writes

`Users LEFT JOIN Rides USING (user_id)`.

A left join emits every row from `Users`. When matching ride rows exist, it emits one joined row per ride. When none exist, it still emits one user row whose ride columns, including `distance`, are null.

An inner join would lose users without rides and could never later recover their required zero totals.

**Why `USING` is appropriate.** Both tables name the join key `user_id`. `USING (user_id)` is concise syntax for equality on those columns and exposes one joined `user_id` column rather than two ambiguous copies.

The uniqueness of `Users.user_id` means each ride joins to at most one user. The uniqueness of `Rides.ride_id` allows a user to have many distinct rides.

**Aggregate all ride distances per user.** `GROUP BY 1` groups by the first selected expression, `user_id`. `SUM(distance)` then adds the distances of every matching ride for that user.

The query also selects `name`. Since `user_id` uniquely identifies a row in `Users`, the name is functionally dependent on the grouped user ID. MySQL can permit this under functional-dependency rules. Writing `GROUP BY user_id, name` would make the dependency explicit and be more portable across SQL systems.

**Replace the no-ride null with zero.** For a user without rides, the left join supplies one row with null distance. SQL aggregate `SUM` ignores null inputs, and when every input in the group is null its result is null rather than numeric zero.

`COALESCE(SUM(distance), 0)` returns the sum when it exists and otherwise substitutes zero. This distinction is necessary: the left join preserves the user, while `COALESCE` supplies the required numeric meaning for missing ride data.

**Name the output column exactly.** `AS 'traveled distance'` gives the result the requested display label containing a space. In MySQL, single quotes are accepted for this alias usage, though backticks are often preferred for identifier quoting in portable style.

**Sort after aggregation.** `ORDER BY 1` orders by the first selected output column, `user_id`, in ascending order by default. Sorting after grouping produces one correctly positioned row per user.

**A user with several rides.** If one user has distances 197 and 196, the join yields two rows sharing that user's ID and name. Grouping combines them, and `SUM` returns 393. A user with no matching ride yields the one null-extended row and becomes zero through `COALESCE`.
The left join establishes exactly one joined group for every user and associates that group with all and only rides bearing the same `user_id`. Summation gives the total of those distances. For an empty ride set, null replacement gives zero. Grouping returns one row per unique user, and ordering satisfies the output contract. Therefore, every user appears exactly once with the correct total.

**Rows with an unmatched ride user.** A ride whose `user_id` does not exist in `Users` would not appear because the preserved table is `Users`. A normalized database would normally enforce the relationship. The task asks for totals of users in `Users`, so excluding orphan rides is consistent with the output domain.

**The query does not mutate either table.** It is a read-only selection, join, aggregate, and sort.

## Complexity detail

Let $U$ be the number of user rows and $R$ the number of ride rows. Physical complexity depends on indexes and the MySQL execution plan.

With a hash join and hash aggregation, logical join and aggregation work can approach $O(U+R)$, followed by $O(U\log U)$ sorting for the required order. With sort-merge or unindexed strategies, sorting and join work may be described conservatively as $O((U+R)\log(U+R))$, matching the manifest.

Intermediate join rows are proportional to $U+R$ because each ride matches one user and each no-ride user contributes one null-extended row. Group state is $O(U)$. A sort may need $O(U)$ memory or spill to temporary storage. The manifest's $O(U+R)$ working-space upper bound is reasonable, but database engines manage this storage internally.

Indexes on `user_id` can materially improve the join, but logical correctness does not depend on them.

## Alternatives and edge cases

- **Pre-aggregate rides before joining:** Group `Rides` by user first, then left-join the smaller totals table to `Users`. This can reduce join volume when users have many rides and still requires null replacement.
- **Correlated scalar subquery:** Compute one sum for each user. It is concise but may be slower without optimizer decorrelation or an index.
- **Inner join:** It is incorrect because users without rides disappear.
- **No rides for a user:** `SUM` is null over the null-extended group, and `COALESCE` changes it to zero.
- **One ride:** Its distance passes through as the total.
- **Many rides:** Every matching row contributes once to `SUM`.
- **Zero distance:** If allowed, it is a real numeric input and remains zero; it is distinct from null, though both display zero after aggregation.
- **Grouping by ordinal:** `GROUP BY 1` means `user_id` here, but explicit column names are often clearer and safer during query maintenance.
- **Functional dependency of name:** The unique user ID determines one name. Explicitly grouping both columns improves portability.
- **Alias with spaces:** MySQL accepts the quoted alias; other SQL dialects may prefer double quotes.
- **Required ordering:** Without `ORDER BY`, relational result order is unspecified even if an execution plan happens to emit sorted rows.
