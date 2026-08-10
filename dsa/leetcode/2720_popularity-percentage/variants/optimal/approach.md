## General

**Represent an undirected friendship in both directions**

Each row of `Friends` stores two participants, but friendship is mutual. If a source row is `(2, 1)`, user two has friend one and user one has friend two. Grouping only by the original `user1` column would omit every friendship from the perspective of a participant appearing in `user2`.

The common table expression `F` fixes this by combining:

- `SELECT * FROM Friends`, which emits `(user1, user2)`;
- `SELECT user2, user1 FROM Friends`, which emits the reversed direction.

After this normalization, every row of `F` means “the user in the first column has the user in the second column as a friend.”

**Why `UNION` is meaningful**

The query uses `UNION` rather than `UNION ALL`. `UNION` removes duplicate directed pairs. The table's primary key prevents two identical source rows, but it does not necessarily forbid both `(a,b)` and `(b,a)` from appearing as separate source rows. Reversing both would otherwise duplicate the same relationship in `F`.

Deduplication ensures each directed friendship is counted once. This aligns the numerator with the number of friends rather than the number of redundant records.

**Count the platform's users from the normalized relation**

The second common table expression `T` computes:

`COUNT(DISTINCT user1) AS cnt FROM F`.

Because every participant from the original table appears as the first column in one of the two directions, distinct `F.user1` values are exactly all users represented on the platform by this dataset. A user originally appearing only in `user2` is no longer missed.

The scalar subquery `(SELECT cnt FROM T)` supplies this common denominator to every result row.

**Count friends per user with a window**

For each row of `F`, `COUNT(1) OVER (PARTITION BY user1)` counts how many normalized friendship rows have that same first-column user. Since `UNION` has removed duplicate directed pairs, this is the user's number of distinct friends.

A window function differs from `GROUP BY`: it attaches the count to every underlying row instead of collapsing the partition into one row. If user one has five friends, all five rows for user one receive count five.

The outer `SELECT DISTINCT` then collapses those identical per-user results to one output row. It selects only `user1` and the computed percentage, so all rows in a user's partition have identical selected values.

**Compute and round the percentage**

The expression multiplies the friend count by 100, divides by the total user count, and rounds to two decimal places:

$$
\operatorname{percentage}(u)
=
\operatorname{ROUND}\left(
\frac{100\cdot\operatorname{friends}(u)}
{\operatorname{users}},
2
\right).
$$

In MySQL, the arithmetic context of `ROUND` and division yields the fractional percentage required by the examples rather than truncating to an integer.

For the sample, `F` contains all nine users as first-column values, so `cnt = 9`. User one has five normalized rows, producing $100\cdot5/9=55.555\ldots$, which rounds to `55.56`. User six has two rows and produces `22.22`.

**Why every represented user receives a row**

Every original friendship contributes a direction starting from each endpoint. Therefore each endpoint occurs as `F.user1` at least once. The window function creates a percentage for each such user, and `DISTINCT` returns exactly one row per user.

The schema contains no separate `Users` table. Consequently, the only users the query can and should count are those appearing in at least one friendship row. An isolated user not present in `Friends` cannot be inferred from this input.

**Sort as required**

`ORDER BY 1` sorts by the first selected expression, which is `user1`. MySQL's default direction is ascending, so this implements the required ascending user order. Writing `ORDER BY user1 ASC` would be more explicit but semantically equivalent.

**Why the query is correct**

The CTE `F` creates one directed record for every unique undirected friendship endpoint. Thus the number of rows in each `user1` partition is exactly that user's friend count, and the number of distinct first-column users is exactly the represented user population. The percentage expression applies the problem's formula, `DISTINCT` leaves one record per partition, and `ORDER BY 1` returns those records in the required order.

**Important distinction from the editorial variant**

The exact solution does not use `COUNT(DISTINCT user2)` in the final select. Its correctness instead relies on `UNION` having already deduplicated directed pairs. Once `F` is a set of unique pairs, `COUNT(1)` per partition equals the distinct-friend count.

## Complexity detail

Let $R$ be the number of input friendship rows and $U$ the number of represented users. Expanding creates at most $2R$ candidate rows. A typical MySQL execution of `UNION` performs duplicate elimination using sorting or hashing. The window partitioning, `DISTINCT`, and final ordering also require grouping, sorting, or hash structures.

A safe engine-level summary is $O(R\log R)$ time and $O(R)$ intermediate space, matching the manifest. Exact physical costs depend on MySQL's optimizer, indexes, memory limits, and whether operations spill to disk; SQL declares the relational result rather than a fixed low-level algorithm.

The result has $U$ rows. The CTE and window processing may materialize up to $O(R)$ normalized rows. The scalar CTE `T` stores one count.

## Alternatives and edge cases

- **`UNION ALL` plus `COUNT(DISTINCT user2)`:** Also handles duplicate directions, but the total-user computation and numerator must both preserve distinct semantics explicitly.
- **Group by normalized user:** `GROUP BY user1` with a friend count can replace the window plus outer `DISTINCT` and may express the one-row-per-user intent more directly.
- **Count only original `user1` values:** Incorrect because users appearing solely in `user2` would disappear from both results and denominator.
- **Treat friendships as directed:** Incorrect for the stated mutual relationship; both endpoints must receive credit.
- **Both orientations stored:** `UNION` prevents `(a,b)` and `(b,a)` source rows from doubling the normalized friendship.
- **Single friendship:** Two users each have one friend, so each popularity is $50.00$ percent because the denominator includes both users.
- **Isolated users:** They cannot appear because the input has no user roster beyond `Friends`.
- **Rounding:** `ROUND(..., 2)` is necessary; returning the unrounded repeating decimal would violate the contract.
- **Output order:** `ORDER BY 1` means ascending `user1` because it is the first selected column.
- **Window duplication:** `SELECT DISTINCT` is essential in this exact formulation because the window count is repeated once per friendship row.
