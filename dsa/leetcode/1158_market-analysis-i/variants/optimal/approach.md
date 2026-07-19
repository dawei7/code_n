## General
**Preserve every user.** Begin with `Users` and use a `LEFT JOIN` to `Orders`. An inner join would discard members who bought nothing in 2019, even though they must appear with zero.

**Filter inside the join condition.** Restrict joined orders to `order_date >= '2019-01-01'` and `order_date < '2020-01-01'`. Keeping this predicate in `ON` preserves the null-extended row for a user with no match. Moving it to `WHERE` would remove that row and effectively undo the outer join. The half-open interval also expresses the entire calendar year without applying a function to the date column.

**Count matched orders, not joined rows.** Group by the user's ID and join date, then use `COUNT(o.order_id)`. Because `order_id` is non-null for a real order but null on an unmatched outer-join row, the count becomes zero for non-buyers. Counting `*` would incorrectly report one. Alias the requested columns and order by `buyer_id` only to make the app fixture output deterministic; the source contract itself permits any row order.

## Complexity detail
A comparison-based join and grouping plan can sort or index the $r$ relevant rows in $O(r \log r)$ time and retain $O(r)$ working state. A database may instead use indexes or hash aggregation for expected linear work. `Items` is not read because neither item identity nor brand changes the requested buyer count.

## Alternatives and edge cases
- **Correlated count per user:** A scalar subquery is concise, but without a supporting index it can rescan all orders for every user and take quadratic time.
- **Filter in `WHERE`:** This loses users with zero 2019 orders because their joined order date is null.
- **Use `COUNT(*)`:** An unmatched user still has one null-extended join row, producing the wrong count of one.
- **Seller-only activity:** Orders where a user appears only as `seller_id` must not increase that user's buyer count.
- **Year boundaries:** Both `2019-01-01` and `2019-12-31` qualify; dates before 2019 or on and after `2020-01-01` do not.
- **Unused item data:** Missing or unrelated brand information cannot affect this report because the requested fields depend only on users and buyer-side orders.
