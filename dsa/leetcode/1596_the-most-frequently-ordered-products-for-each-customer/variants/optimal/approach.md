## General
Let $r$ be the number of order rows and $g$ the number of distinct `(customer_id, product_id)` pairs present in `Orders`.

**Count each customer's product orders once.** Group `Orders` by customer and product, producing one row per observed pair and its `COUNT(*)`. Neither the order date nor product price affects frequency, and customers without orders disappear naturally because the aggregation starts from `Orders`.

**Keep every maximum, including ties.** Apply `DENSE_RANK()` within each customer, ordering the grouped count from greatest to least. Every product with rank `1` has that customer's maximum count. Unlike `ROW_NUMBER()`, a ranking function assigns the same leading rank to equal counts and therefore preserves all required ties.

**Attach the product name after ranking.** Join the rank-one rows to `Products` by `product_id`. The grouped relation already proves that each returned pair was ordered, while the final join supplies exactly the requested descriptive column. Grouping covers all observed pairs, ranking selects precisely the maxima in each customer partition, and retaining every rank-one row proves the result is both complete and free of lower-frequency products.

## Complexity detail
Under a portable comparison-based model, grouping and ranking require $O(r\log r)$ time; the join over indexed or sortable identifiers remains within that bound. The grouped and ranked intermediate relations contain $g$ rows, so they use $O(g)$ working space. A database engine may use hash aggregation and approach linear expected time, but the stated bound does not assume that optimization.

## Alternatives and edge cases
- **Correlated frequency subqueries:** Counting matching orders again for each outer order can be correct, but repeatedly rescans `Orders` and may require quadratic work.
- **`ROW_NUMBER()` per customer:** This incorrectly discards all but one product when the maximum frequency is tied.
- **Aggregate then compare with a per-customer maximum CTE:** This is also correct and avoids window functions, but requires an additional grouping and join over the count relation.
- A customer with exactly one ordered product returns that product regardless of how many times it was ordered.
- Every product tied at the maximum frequency must appear; there is no product-ID or name tie-breaker.
- Customers with no orders and products never ordered do not appear in the result.
- Dates and prices do not affect frequency; each `Orders` row contributes one occurrence.
