## General

**Every product must appear, even without an earlier change**

The `Products` table is a history of price changes rather than a separate product catalog. A product may have only rows dated after `2019-08-16`, but it still needs an output row with the initial price ten.

The first common table expression,

`T AS (SELECT DISTINCT product_id FROM Products)`,

extracts the complete product population from all history rows, regardless of date. `DISTINCT` gives exactly one row per product identifier.

Starting the final query from `T` ensures future-only products are not lost when the solution searches for changes on or before the report date.

**Find the latest applicable date for each product**

A price change remains effective until a later change replaces it. Therefore, the price on `2019-08-16` comes from the greatest `change_date` that is no later than that date.

The grouped subquery filters to

`change_date <= '2019-08-16'`

and computes `MAX(change_date)` per `product_id`. This yields one key pair for every product that has an applicable change:

`(product_id, latest_applicable_date)`.

A change on the report date itself is included because the comparison is `<=`. Changes after that date are excluded and cannot affect the historical price.

**Retrieve the price attached to that date**

The second CTE `P` filters `Products` with a row-value membership test:

`(product_id, change_date) IN (...)`.

Only a row whose product and date together match one of the grouped latest-date pairs survives. It projects `new_price AS price`.

The composite primary key `(product_id, change_date)` guarantees at most one price-change row for that product on that date. Therefore, each product contributes at most one row to `P`, and the selected `new_price` is unambiguous.

It would not be sufficient to compare `change_date` with one global maximum date. Different products can have their most recent applicable changes on different days, so the maximum must be grouped by product.

**Preserve products with no applicable change**

The final query left joins `T` to `P` using their common `product_id` column.

If `P` contains a latest applicable row, its `price` is the product's effective price.

If the product has no change on or before the report date, there is no `P` match. The left join preserves the product and supplies null for `price`. `COALESCE(price, 10)` replaces that null with the initial price ten.

This includes products whose first recorded change occurs after the report date. It also correctly ignores a future change for a product that already had an earlier applicable price.

**Trace the example**

Product one has applicable changes on August 14, 15, and 16. Its maximum applicable date is August 16, so price 35 is selected.

Product two has changes on August 14 and 17. Only August 14 survives the date filter, so its price is 50 on the report date.

Product three appears in `T` because it has a history row, but its only change is August 18. It has no row in `P`, the left join yields null, and `COALESCE` returns ten.

**Why the query is correct**

For every product, `T` guarantees one final-row candidate. If the product has applicable changes, the grouped maximum identifies the last such change, and the composite-key lookup retrieves exactly its new price. By the semantics of a change history, that value is effective on the report date.

If no applicable change exists, the product is still at its universal initial price, and the left-join null is converted to ten. These cases are exhaustive and mutually exclusive, so every product receives exactly the correct price.

The final order is unrestricted, so no `ORDER BY` is needed.

## Complexity detail

Let `r` be the number of rows in `Products`. Distinct product extraction, date filtering, grouped maximum calculation, and the joins may be implemented with sorting or hashing. Under the manifest's conservative sort-based view, time is `O(r log r)` and intermediate storage is `O(r)`.

Indexes on the composite primary key and date-aware access paths may improve physical execution. SQL complexity is plan-dependent, but the stated bounds safely cover materializing the CTEs and grouped results.

The final result size is the number of distinct products, which is at most `r`.

## Alternatives and edge cases

- **Use a window function:** Ranking each product's rows by date descending after filtering and keeping rank one also finds the latest applicable price. A separate all-product base is still needed for future-only products.
- **Use correlated subqueries:** For each product, a subquery can order applicable changes descending and take one. This can be concise but may repeat lookup work without suitable indexes.
- **Use `UNION ALL` for changed and unchanged products:** One branch can return latest prices and another initial tens. The left-join formulation expresses the two cases in one final projection.
- **Start only from filtered rows:** Products with no change by the report date disappear instead of receiving price ten.
- **Use a global maximum date:** Products have independent histories, so their latest applicable dates must be grouped separately.
- **Change exactly on `2019-08-16`:** It is included and becomes effective that day.
- **Only future changes:** The product appears through `T` and receives the initial price ten.
- **Earlier and future changes:** The latest earlier row is selected; the future row is ignored.
- **Several earlier changes:** `MAX(change_date)` selects only the most recent effective one.
- **Composite primary key:** It guarantees one price for a product-date pair, preventing ambiguity in `P`.
- **Any result order:** The query intentionally omits sorting because the contract allows it.
