## General

**Start from products, not invoices**

The result must include every product, even one that has no invoice. That requirement determines the join direction:

`Product LEFT JOIN Invoice USING (product_id)`.

Every row from `Product` survives a left join. Matching invoice rows are attached by equal `product_id`. If no invoice matches, SQL still produces one null-extended joined row for that product. Starting from `Invoice` or using an inner join would incorrectly omit invoice-free products.

`USING (product_id)` is concise join syntax for the equality between the two tables’ same-named `product_id` columns. It also presents the join key as one merged column to later clauses.

**Aggregate each monetary category independently**

The query groups joined rows by `product_id`. For a product with several invoices, all of its invoice rows enter one group. The four aggregates then compute:

- `SUM(rest)`: total amount still due;
- `SUM(paid)`: total amount paid;
- `SUM(canceled)`: total amount canceled;
- `SUM(refunded)`: total amount refunded.

Each category must be summed separately because the requested output preserves their meanings. Adding them together or subtracting one from another would answer a different accounting question.

The product name is selected directly. Since `Product.product_id` is unique, one grouped product ID determines exactly one name. MySQL can therefore return that functionally dependent `name` alongside the aggregates.

**Why `COALESCE` is required**

For a product with no invoices, the left join supplies nulls for every invoice column. SQL’s `SUM` ignores null inputs, and when there is no non-null value to add, its result is `NULL` rather than numeric zero.

The contract expects totals of zero for such a product. `COALESCE(SUM(rest), 0)` returns the sum when it is non-null and substitutes zero otherwise. The source applies this separately to all four aggregate columns.

For products that do have invoices, `SUM` returns their normal totals and `COALESCE` leaves those values unchanged.

**One output row per product**

`GROUP BY product_id` collapses all joined invoice records for a product into one result row. The unique product key ensures distinct products never merge, even if the data model allowed equal names; the description additionally guarantees names are unique.

The aliases `AS rest`, `AS paid`, `AS canceled`, and `AS refunded` assign the exact required output column names. `name` already has its desired label.

Finally, `ORDER BY name` sorts rows in ascending product-name order, which is SQL’s default when no direction is written. Since names are unique, the requested order has no ties.

**Trace the example**

Product `ham` joins to two invoice rows. The grouped sums are rest `2 + 0 = 2`, paid `0 + 4 = 4`, canceled `5 + 0 = 5`, and refunded `0 + 3 = 3`.

Product `bacon` joins to four rows, producing three in each category. Ordering by name places `bacon` before `ham`, independently of their numeric product IDs.

If a third product had no invoice, its left-joined group would contain null invoice fields. All four `SUM` results would be null and all four `COALESCE` calls would output zero, preserving that product in the result.

**Why the query is correct**

The left join creates exactly the invoice associations belonging to each product while preserving products without associations. Grouping by the unique product key isolates those associations. Each sum adds all and only the values in its named category for that product, and `COALESCE` converts the no-data aggregate to the required zero.

No `WHERE` clause filters rows after the left join, so invoice-free products are not accidentally removed. The final ordering changes only result sequence. Therefore every product appears once with its correct four totals and in ascending name order.

## Complexity detail

Let `P` be the number of products and `I` the number of invoices. With an index or hash strategy on `product_id`, forming join associations and aggregating them can be $O(P+I)$ expected time. Producing the required name order costs $O(P\log P)$ when a separate sort is needed. This gives the manifest bound $O(I + P\log P)$, with the `P` scan absorbed.

Aggregation state contains one group per product, so it uses $O(P)$ working space under hash aggregation. A sort-based database plan can use different time and temporary-storage behavior; SQL physical complexity depends on indexes and optimizer choices.

The result itself contains `P` rows and is normally excluded from auxiliary-space accounting.

## Alternatives and edge cases

- **Correlated subqueries:** Four subqueries per product can compute the totals but may rescan invoices repeatedly unless the optimizer rewrites them.
- **Pre-aggregate invoices first:** Group `Invoice` by `product_id` in a derived table, then left join those totals to `Product`. This is equally valid and can make the one-row-per-product structure explicit.
- **Inner join:** It is incorrect because products without invoices would disappear.
- **Filter invoice rows in `WHERE`:** Conditions on nullable invoice columns after a left join can accidentally turn it into inner-join behavior; such filters belong in the join condition when preservation is required.
- **No invoices for a product:** The left join retains it, and `COALESCE` changes each null aggregate to zero.
- **Zero-valued invoices:** Their sums are numeric zero, not null, and `COALESCE` leaves them unchanged.
- **Several invoices per product:** Grouping combines all of them without duplicating the product row.
- **Invoice referencing a product:** The intended schema relationship makes the join meaningful; an orphan invoice would not create an output product because `Product` is the preserved side.
- **Unique product names:** Ordering has no ties, so no secondary key is necessary.
- **Functional dependency:** Selecting `name` while grouping by `product_id` is sound because one unique ID determines one product row; stricter SQL modes or other databases may prefer grouping by both fields.
- **Null amounts outside the stated model:** `SUM` ignores individual nulls. If every invoice value in one category were null, `COALESCE` would output zero, which may or may not match a different business rule.
