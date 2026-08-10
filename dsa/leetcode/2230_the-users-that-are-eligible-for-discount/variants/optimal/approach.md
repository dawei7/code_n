## General

**Eligibility is proven by one qualifying purchase row**

A user needs at least one purchase satisfying all three predicates:

- `amount >= minAmount`;
- `time_stamp >= startDate`; and
- `time_stamp <= endDate`.

The SQL procedure filters purchase rows directly. It does not aggregate amounts across purchases because the rule applies to one purchase with at least the threshold amount, not to a user's total spending.

The exact predicate is

`amount >= minAmount AND time_stamp BETWEEN startDate AND endDate`.

In MySQL, `BETWEEN` is inclusive at both endpoints, so it expresses the two time comparisons together.

**Understand the date-to-datetime boundary exactly**

The procedure parameters `startDate` and `endDate` have type `DATE`, while `time_stamp` is `DATETIME`. When MySQL compares them, a date is treated as the start of that day at `00:00:00`.

That behavior is explicitly required by the problem. If `endDate` is `2022-03-20`, the upper endpoint is `2022-03-20 00:00:00`. A purchase at exactly midnight is included, but a purchase later that same calendar day is after the stated endpoint and is excluded.

This differs from many business reports where an ending date informally means the entire day. The solution must follow this problem's start-of-day instruction and must not rewrite the condition as “before the next day.”

Likewise, a purchase before midnight at the start date is outside, while one exactly at `startDate 00:00:00` is included.

**Apply amount and time conditions to the same row**

SQL evaluates the conjunction for each row. A user does not qualify by combining one purchase that meets the amount with another purchase that meets the date interval. One row must satisfy both.

This explains the example: user `1` has a sufficiently large amount but its timestamp is outside the interval. User `2` is inside the time interval but below `minAmount`. Only user `3` has one row meeting both predicates.

**Deduplicate users after filtering**

A user may have several qualifying purchases. `SELECT DISTINCT user_id` collapses all surviving rows for that user into one ID. It does not remove any user entirely; it only removes duplicate output occurrences.

`ORDER BY user_id` then returns IDs in increasing order. SQL result sets have no guaranteed order without an explicit ordering clause, so this final clause is required by the output contract.

**Why every returned ID is eligible**

Every result row originates from at least one `Purchases` row that survived the `WHERE` clause. That row's amount is at least `minAmount`, and its timestamp lies inclusively between the two midnight endpoints. Therefore, the associated user has the required qualifying purchase.

`DISTINCT` cannot introduce a new ID; it only collapses copies. Ordering also changes no membership. Every returned user is valid.

**Why every eligible ID is returned**

If a user is eligible, at least one of that user's purchase rows satisfies all three comparisons. The `WHERE` clause retains that row, so its `user_id` enters the selected rows. `DISTINCT` preserves one copy even if several exist. Thus, no eligible user is omitted.

**Stored-procedure structure**

The exact artifact defines

`CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)`.

The parameter names are referenced directly inside the query. `BEGIN` and `END` delimit the procedure body. The query does not need a join, group, subquery, or window function because row filtering plus deduplication expresses the entire requirement.

The primary key `(user_id, time_stamp)` guarantees a user cannot have two table rows at the exact same timestamp, but this guarantee is not required for the filtering logic. Different qualifying timestamps can still create multiple rows that `DISTINCT` must collapse.

## Complexity detail

Let `r` be the number of purchase rows. Without an index tailored to the filter, the database scans `r` rows, taking `O(r)` predicate-evaluation time.

Deduplicating and ordering up to `r` qualifying IDs can require sorting, giving a worst-case `O(r \log r)` time bound. An optimizer may use hashing for `DISTINCT` or indexes for part of the work, but the manifest's general bound is `O(r \log r)`.

Execution may use `O(r)` working space for distinct values and sorting. Exact memory, temporary tables, and disk spills depend on MySQL's plan and available indexes.

## Alternatives and edge cases

- **Group by user:** Filter rows and use `GROUP BY user_id` instead of `DISTINCT`. It can produce the same IDs, but `DISTINCT` states the intent directly because no aggregate is needed.
- **Use `EXISTS` over a users table:** This would be useful if a separate user table were required, but the only needed IDs already occur in qualifying purchase rows.
- **Aggregate each user's total amount:** That changes the contract. One purchase must individually meet `minAmount`.
- **Use an end-exclusive next-day boundary:** Common reporting logic such as `time_stamp < endDate + INTERVAL 1 DAY` would include the whole end date, contradicting the explicit midnight interpretation here.
- **Purchase exactly at `startDate 00:00:00`:** It is included by `BETWEEN`.
- **Purchase exactly at `endDate 00:00:00`:** It is also included.
- **Purchase later on the ending date:** It is excluded because the `DATE` parameter represents midnight.
- **Amount exactly equal to `minAmount`:** `>=` includes it.
- **Several qualifying purchases:** `DISTINCT` returns the user once.
- **No qualifying rows:** The procedure returns an empty result table.
- **One row meets amount and another meets time:** The user remains ineligible because `AND` applies both requirements to each individual row.
- **Required ordering:** `ORDER BY user_id` is necessary even after `DISTINCT`.
- **Null data:** The declared schema does not state nullability here; if a compared value were null, the predicate would not be true under SQL three-valued logic.
