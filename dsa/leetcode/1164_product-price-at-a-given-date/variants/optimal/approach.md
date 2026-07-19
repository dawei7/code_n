## General
**Preserve the complete product set.** Start with the distinct `product_id` values from all rows. Filtering the table to dates on or before `2019-08-16` too early would erase products whose first change is later, even though those products must appear with price `10`.

**Locate the effective change date.** Among eligible rows, group by `product_id` and take `MAX(change_date)`. Because `(product_id, change_date)` is the primary key, this date identifies exactly one price-change row for each product that had changed by the target date.

**Restore prices and defaults.** Left join every product to its latest eligible date, then join that pair back to `Products` to obtain `new_price`. When no eligible date exists, the joins yield null, so `COALESCE(new_price, 10)` supplies the initial price. A change on `2019-08-16` is eligible because the comparison is inclusive. An `ORDER BY product_id` may stabilize local fixtures even though the source accepts any output order.

## Complexity detail
Grouping and joining $r$ rows take $O(r \log r)$ time under a comparison-based plan; indexed or hash-based execution may be faster in practice. The distinct product set, grouped latest dates, and join state require $O(r)$ working space in the worst case.

## Alternatives and edge cases
- **Window ranking:** Rank eligible changes per product by `change_date` descending and retain rank one; this is equally expressive but still needs a separate complete product set for unchanged products.
- **Correlated latest-price lookup:** A subquery ordered by date for every product is concise, but without a suitable index it can rescan `Products` for each product and become quadratic.
- **Union changed and unchanged products:** Two branches can return latest prices and default prices separately, but the exclusion logic is easier to get wrong than a left join.
- **Only future changes:** The product remains present and receives the initial price `10`.
- **Change on the target date:** The `change_date <= '2019-08-16'` condition includes it.
- **Several earlier changes:** Only the row at the maximum eligible date determines the reported price.
