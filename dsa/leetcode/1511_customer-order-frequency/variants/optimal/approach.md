## General

**Combining orders with prices and customer names**

An order row contains quantity, date, customer ID, and product ID, but not unit price or customer name. The query uses two inner joins:

- `Orders JOIN Product USING (product_id)` attaches the price for each ordered product.
- `JOIN Customers USING (customer_id)` attaches the customer's name.

`USING` expresses equality on the identically named key and exposes one copy of that key in the joined result. Inner joins are appropriate because an order must have matching product and customer records to calculate and report it.

For one order, spending is `quantity * price`. The query preserves every order row and later sums these products by customer.

**Filtering the relevant year**

`WHERE YEAR(order_date) = 2020` removes orders outside 2020 before grouping. Orders from every month within 2020 remain at this stage, not only June and July.

Keeping other 2020 months is logically harmless because the conditional aggregates contribute zero for them. It is not the most selective physical predicate, but it does not affect correctness.

Applying `YEAR` to the column can make an ordinary date index less useful. A half-open range from January 1, 2020 through January 1, 2021 would express the same year more directly for index access. An even narrower June-through-August range would suffice for this particular result.

**Grouping one result candidate per customer**

`GROUP BY 1` groups by the first selected expression, `customer_id`. Every joined order for the same customer becomes part of one aggregate group.

The query also selects `name` without listing it in `GROUP BY`. In MySQL, this is valid when `customer_id` functionally determines `name` because the customer ID is unique. Other SQL modes or database systems may require grouping by both columns or applying an aggregate to the name.

Customers with no orders form no group because the query begins from `Orders` and uses inner joins.

**Computing June and July independently**

The first conditional sum is

`SUM(IF(MONTH(order_date) = 6, quantity * price, 0))`.

For each joined 2020 order, it contributes the order's spending if the month is June and zero otherwise. The result is total June spending for that customer.

The second expression uses month seven and independently computes July spending. The two conditions in `HAVING` both require a total of at least one hundred.

Using `AND` is essential. A customer who spends two hundred in June and nothing in July fails the July comparison. Spending cannot be pooled across the months.

`HAVING` is used rather than `WHERE` because the threshold applies to group aggregates, which do not exist until after grouping.

**Why the result is correct**

Any returned row comes from a customer group. Its June conditional sum is at least one hundred and its July conditional sum is independently at least one hundred, so it meets the contract.

Conversely, every customer with qualifying orders in both months has those orders joined to their prices and included in the customer's group. The quantity-price products are added to the correct monthly expressions. Both predicates pass, so the row is retained.

Orders from other 2020 months add zero to both sums. Orders from other years were already filtered out. The absence of `ORDER BY` is correct because result order is unrestricted.

**Boundary and amount semantics**

`MONTH` classifies every date from June 1 through June 30 as six and every date from July 1 through July 31 as seven. The product price is treated as the unit price, so multiplying by quantity gives order spending. The threshold comparison uses greater than or equal to, so exactly one hundred qualifies.

## Complexity detail

Let $C$ be the number of customers, $P$ the number of products, and $O$ the number of orders. A typical plan scans or indexes the relevant orders, joins dimension rows through key lookups or hashes, and groups by customer.

The manifest's $O(C+P+O\log O)$ time and $O(C+P+O)$ space are conservative sort-based logical bounds. Hash joins and hash aggregation may achieve expected near-linear work, while sorting groups can introduce the logarithmic factor.

Actual SQL cost depends on indexes, statistics, join order, memory, and engine choices. Function predicates `YEAR(order_date)` and repeated `MONTH(order_date)` require date extraction and may prevent a simple range seek. Grouping can spill intermediate data to disk.

The result itself contains at most $C$ rows. Conditional aggregation uses constant accumulators per active customer group, while join and grouping structures can scale with input sizes.

## Alternatives and edge cases

- **Half-open June-to-August range:** Filter `order_date` from June 1 inclusive to August 1 exclusive, then conditionally aggregate June and July. This is more index-friendly and excludes irrelevant 2020 months early.
- **Two monthly subqueries:** Aggregate June and July separately and inner join qualifying customer IDs. It makes the dual requirement explicit but scans or structures orders twice unless optimized.
- **Grouping by customer and month:** Produce monthly totals first, then require two qualifying month rows. This is flexible for more months but needs a second aggregation or pivot.
- **Exactly one hundred:** Greater-than-or-equal correctly includes the customer.
- **High spending in only one month:** The `AND` condition excludes the customer.
- **No July orders:** The July conditional sum is zero for a group with other 2020 orders, so the customer fails.
- **Orders only outside 2020:** They are removed before grouping, leaving no result row.
- **Several orders for one product:** Each quantity-price amount contributes independently.
- **No matching product or customer:** Inner joins discard the orphaned order.
- **Functional dependency of name:** MySQL can infer name from unique customer ID; stricter SQL may require both in `GROUP BY`.
- **Unrestricted order:** No output sort is required.
