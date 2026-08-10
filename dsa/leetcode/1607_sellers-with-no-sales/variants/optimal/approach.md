## General

**Start from every seller**

The result must include sellers who made no 2020 sale, including sellers with no orders at all. The query therefore starts from `Seller` and uses:

`LEFT JOIN Orders USING (seller_id)`.

A left join preserves every seller. Sellers with orders produce one joined row per order. A seller without any order still produces one null-extended joined row whose order columns, including `sale_date`, are `NULL`.

The `Customer` table is irrelevant because the result depends only on seller identity and order dates; no customer information is selected or filtered.

**Group all records for one seller**

`GROUP BY seller_id` collects a seller’s joined order rows into one group. Since `Seller.seller_id` is unique, it functionally determines one `seller_name`, so selecting the name is well-defined in MySQL.

Grouping is necessary because the condition concerns whether any order in the entire seller history occurred during 2020.

**Turn the year test into a numeric count**

MySQL evaluates the Boolean expression:

`YEAR(sale_date) = 2020`

as one when true and zero when false. `SUM` over that expression therefore counts the seller’s 2020 order rows.

An order in 2019 or 2021 contributes zero. An order on any date from January 1 through December 31, 2020 contributes one because `YEAR` returns 2020.

The exact order count is not requested; only whether the count is zero matters.

**Why `COALESCE` is necessary**

For a seller with no orders, the left join’s `sale_date` is `NULL`. `YEAR(NULL)` is `NULL`, and comparing it with 2020 is also `NULL`. `SUM` ignores null inputs, but if every input is null, its result is null rather than numeric zero.

The source wraps the aggregate:

`COALESCE(SUM(YEAR(sale_date) = 2020), 0)`.

`COALESCE` returns the sum when it is non-null and returns zero otherwise. This treats a seller with no orders as having zero 2020 sales, which is correct.

A seller with orders only outside 2020 already gets an ordinary numeric sum of zero, so `COALESCE` leaves it unchanged.

**Filtering groups with `HAVING`**

The condition is:

`HAVING COALESCE(...) = 0`.

`HAVING` is used rather than `WHERE` because the decision depends on the aggregate across each seller group. Filtering rows with `WHERE YEAR(sale_date) != 2020` would be wrong: a seller with both a 2020 order and a 2019 order would retain the 2019 row and incorrectly appear to have no 2020 sale.

With aggregation, any 2020 row makes the sum positive and excludes the whole seller. A sum of zero means no group row represents a 2020 sale.

**Ordering the output**

The select list contains only `seller_name`. `ORDER BY 1` refers positionally to that first selected expression, so it sorts names in ascending order by default.

This meets the explicit ordering requirement. Writing `ORDER BY seller_name ASC` would be equivalent and more descriptive.

**Following the sample**

Daniel has one 2020 order, so his Boolean sum is one and the `HAVING` test fails. Elizabeth has two 2020 orders and one 2019 order, producing one plus one plus zero equals two, so she is excluded.

Frank has one 2019 order. Its condition evaluates to zero, the aggregate equals zero, and Frank is included. A seller with no order would have a null sum converted to zero and would also be included.

**Why the query is correct**

If a seller is returned, the aggregate is zero after null normalization. No joined order row can have a 2020 date, because each such row would add one and make the sum positive. The seller therefore made no 2020 sale.

Conversely, if a seller made no 2020 sale, every actual order contributes zero. If there are no orders, `COALESCE` supplies zero. In both cases the `HAVING` equality succeeds, so every qualifying seller is returned.

Grouping by unique seller ID produces one result row per qualifying seller, and ordering completes the required relation.

## Complexity detail

Let $S$ be the number of sellers and $R$ the number of orders.

Physical SQL complexity depends on indexes and execution plans. A sort-based left join and grouping plan fits the manifest bound $O((S+R)\log(S+R))$. With a hash join or an index on `Orders.seller_id` and efficient aggregation, expected work can approach $O(S+R)$ before the required output sort.

Grouping and join intermediates may use $O(S+R)$ space in a general materialized plan. The output contains at most $S$ names. Database `EXPLAIN` is required for exact operational costs.

## Alternatives and edge cases

- **`NOT EXISTS` anti-join:** Select sellers for whom no correlated order has a 2020 date. It directly expresses absence and avoids aggregation.
- **`NOT IN` subquery:** It can exclude seller IDs found in 2020 orders, but nullable subquery values can create three-valued-logic hazards unless the key is guaranteed non-null.
- **Left join only 2020 orders and test null:** Put the date predicate in the join condition, then keep sellers with a null joined order ID. This is another clean anti-join formulation.
- **Filter non-2020 rows in `WHERE`:** This is incorrect for sellers having both 2020 and other-year orders, because it removes evidence of the disqualifying sale while leaving another row.
- **Seller with no orders:** The left join preserves the seller, and `COALESCE` turns the null aggregate into zero.
- **Only sales before 2020:** Every Boolean contributes zero, so the seller is included.
- **Only sales after 2020:** The same zero aggregate includes the seller.
- **At least one 2020 sale:** The aggregate is positive, excluding the seller regardless of other dates.
- **Several 2020 sales:** Each contributes one, but any positive total has the same exclusion effect.
- **Boundary dates:** `YEAR` classifies both `2020-01-01` and `2020-12-31` as 2020.
- **Functional dependency:** Unique `seller_id` determines `seller_name`. Stricter portable SQL can group by both columns explicitly.
- **Required ordering:** `ORDER BY 1` sorts the only selected column ascending; no tie-breaking is necessary for identical names unless the schema permits them.
- **Unused customer table:** Customer data cannot change whether a seller made a 2020 sale, so excluding it is intentional.
