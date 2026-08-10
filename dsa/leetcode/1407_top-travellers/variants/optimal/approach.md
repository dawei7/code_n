## General

**Begin from the table that defines who must appear**

The result needs one row for every user, including a user who has never taken a ride. That requirement determines the join direction. `Users` is the preserved table, and `Rides` supplies zero or more matching detail rows:

```sql
FROM
    Users AS u
    LEFT JOIN Rides AS r ON u.id = r.user_id
```

A regular inner join would retain only users that have a matching ride. A left join instead keeps every row from `Users`. When a user has no match, SQL creates one joined result row whose columns from `Rides` are `NULL`. That synthetic unmatched row is what allows the later aggregation to produce an output row for a non-traveller.

The join predicate `u.id = r.user_id` expresses the schema relationship exactly. A ride belongs to the user whose unique `Users.id` equals its `Rides.user_id`. Joining on `name` would be incorrect because the ride table stores no name and because names need not be safe identifiers.

**Understand the intermediate joined rows**

Before grouping, a user with several rides appears several times. If a user has ride distances 100, 120, and 230, the join produces three rows carrying that user's name and those three distances. A user with one ride appears once. A user with no ride also appears once because of the left join, but that row's `r.distance` is `NULL`.

This multiplicity is useful rather than accidental: the aggregate function can add every ride distance belonging to the same user.

**Group by identity, not by display text**

The clause

```sql
GROUP BY u.id
```

forms one group per user. Since `Users.id` contains unique values, it is the correct identity key. Two different people may have equal names; grouping by `name` would merge their rides and incorrectly return one combined traveller.

The selected `name` is functionally determined by `u.id`: every group represents exactly one Users row and therefore exactly one name. MySQL can return that name alongside the aggregate. Keeping the table alias on `u.id` also makes it unambiguous which identifier defines the group, since both input tables have a column called `id`.

**Turn each group into a travelled distance**

The selected aggregate is:

```sql
COALESCE(SUM(distance), 0) AS travelled_distance
```

For a user with rides, `SUM(distance)` adds the distances of every matched ride in that user's group. In the sample, Lee's rows contribute $100 + 120 + 230 = 450$.

SQL aggregate functions generally ignore individual `NULL` values. For a user with no rides, however, the group has no non-null distance at all, so `SUM(distance)` produces `NULL` rather than zero. The requested result needs a numeric zero. `COALESCE` returns the first non-null argument, so it returns the sum when one exists and returns the literal `0` otherwise.

The order of these functions matters. Applying `COALESCE` around the final sum handles the empty-match group directly. The alias `travelled_distance` gives the calculated column the exact output name required by the contract.

Although `distance` is written without a table alias, only `Rides` has that column in the supplied schema, so it is unambiguous. Writing `SUM(r.distance)` would be equivalent and could make the source table more explicit.

**Apply both ordering rules in the required priority**

The last clause is:

```sql
ORDER BY 2 DESC, 1;
```

In MySQL, ordinal 2 refers to the second selected expression, `travelled_distance`, and ordinal 1 refers to the first selected expression, `name`. Therefore, the primary sort is total distance in descending order. Only among rows with the same total does SQL use the name, whose omitted direction defaults to ascending.

The ordering priorities must remain in that order. Sorting names first would alphabetize the entire result and use distance only among duplicate names, which is not what the problem asks. In the sample, both Elvis and Lee have a total of 450, so the secondary ascending name order places Elvis first.

**The logical flow of the complete query**

It helps to read the query in SQL's conceptual processing order rather than top to bottom:

1. `FROM Users AS u` establishes all users as the required population.
2. `LEFT JOIN Rides AS r ON u.id = r.user_id` attaches every ride while preserving users with no rides.
3. `GROUP BY u.id` collapses all joined rows for one user into one group.
4. `SUM(distance)` calculates the group's total, and `COALESCE` replaces an absent total with zero.
5. `SELECT name, ... AS travelled_distance` shapes the two output columns.
6. `ORDER BY 2 DESC, 1` ranks totals from greatest to least and resolves equal totals alphabetically.

Each clause solves a separate requirement. Removing the left-preserving join loses non-travellers. Removing grouping returns one row per ride instead of one row per user. Removing `COALESCE` exposes `NULL` for non-travellers. Removing either sort key makes the output order incomplete.

**Why the result is correct**

For every Users row, the left join guarantees at least one intermediate row and includes exactly the Rides rows whose `user_id` matches that user's unique identifier. Grouping by that identifier creates exactly one output group for the user and never combines two distinct identifiers. The sum therefore equals the total of all and only that user's ride distances. If the matching set is empty, the aggregate is converted to zero. Finally, the two ordering expressions implement the requested descending total and ascending-name tie-break. These properties cover both the contents of every result row and the order of all rows.

## Complexity detail

Let $U$ be the number of rows in `Users` and $R$ the number of rows in `Rides`. Under the usual database execution strategy, scanning the tables and building or probing an index or hash structure for the join and grouping takes expected $O(U + R)$ work. There is one aggregate result per user.

The final ordering sorts $U$ grouped rows, which costs $O(U \log U)$ with a comparison sort. Combining the phases gives the manifest bound $O(U + R + U \log U)$. Physical database plans can vary with indexes, statistics, memory, and the optimizer, but the unavoidable requested ordering is the term that generally dominates once the grouped rows exist.

The aggregation needs up to one accumulated total per user, so its working storage is $O(U)$. A hash join may also maintain execution structures based on one input, and the sort may use memory or external temporary storage depending on the engine. The stated $O(U)$ bound describes the grouped per-user state used by the intended plan, apart from the returned result.

## Alternatives and edge cases

- **Inner join:** This is shorter but wrong for the contract because every user without a ride disappears before aggregation.
- **Correlated subquery per user:** Selecting each user and running a separate sum over `Rides` can express the same result. Without a helpful index it may repeatedly scan rides and be much slower than joining and grouping once.
- **Pre-aggregate then join:** A derived table can first group `Rides` by `user_id` and then left join those totals to `Users`. It is correct and can make the one-row-per-user relationship explicit, but the stored query achieves the same logical result compactly.
- **Window function:** `SUM(distance) OVER (PARTITION BY u.id)` would repeat the total on every joined ride row, so an additional deduplication step would be required. Plain grouping is more direct here.
- **Grouping by name:** This can silently combine different users who share a name. The unique identifier `u.id` is the safe grouping key.
- **Using `COUNT` instead of `SUM`:** Counting rides reports how many journeys occurred, not the total distance travelled.
- **A user with no rides:** The left join preserves the user, `SUM` yields `NULL` for the unmatched group, and `COALESCE` changes it to zero.
- **A user with many rides:** Every matching distance contributes once because each Rides row joins to its one matching user before aggregation.
- **Equal travelled distances:** `ORDER BY 2 DESC` ties, then `ORDER BY 1` places names in ascending order.
- **Equal names for distinct users:** Grouping preserves separate rows because their identifiers differ. Their displayed names and totals may tie completely; the contract does not require another tie-breaker.
- **Ordinal ordering syntax:** `ORDER BY 2 DESC, 1` depends on the select-column positions. Writing `ORDER BY travelled_distance DESC, name ASC` is more self-documenting and equivalent, but the exact stored solution uses ordinals correctly.
- **Null handling location:** Omitting `COALESCE` returns `NULL` rather than zero for a non-traveller. Converting the completed aggregate is the key step because there is no non-null distance to sum in that group.
