## General
**Give each store column its own projection**

Create one `SELECT` branch per store. Every branch projects `product_id`, a literal store label, and that store's price column. For example, the first branch maps `store1` into the common output names `store` and `price`.

**Filter unavailable combinations at their source**

Apply `WHERE store1 IS NOT NULL`, and analogously for the other branches. A branch then emits a product exactly when that specific store price is available. Values such as zero remain valid because the condition distinguishes `NULL` from all non-null integers.

**Concatenate without duplicate elimination**

Join the three branches with `UNION ALL`. Even when two stores charge the same price, their literal `store` labels describe different required rows. Ordinary `UNION` would spend work checking for duplicates that the `(product_id, store)` identity already rules out.

For every non-null source field, its corresponding branch emits exactly one row with the correct product, label, and value. Every emitted row comes from such a field because of the branch's null filter. This is a bijection between available product-store fields and result rows, proving the transformation is exact.

## Complexity detail
Each of the three branches scans the $R$ product rows once and performs constant work per row. Three is a fixed schema constant, so $3R$ operations are $O(R)$ time. The result contains $K$ rows and uses $O(K)$ output space; `UNION ALL` requires no duplicate set, and the logical transformation needs only constant auxiliary state when streamed.

## Alternatives and edge cases
- **Use ordinary `UNION`:** It returns the same rows under the key guarantees but adds unnecessary duplicate-elimination work.
- **Cross join store labels plus `CASE`:** A three-row label relation can drive one generalized projection, but it creates three candidates per product before filtering and is less direct for a fixed schema.
- **Vendor-specific `UNPIVOT`:** Some databases provide concise unpivot syntax, but the portable `UNION ALL` form matches the available MySQL interface.
- **All prices null:** Emit no rows for that product.
- **All stores available:** Emit exactly three rows with distinct store labels.
- **Equal store prices:** Preserve one row per store; equal numeric values do not make combinations duplicates.
- **Zero or negative prices:** They are non-null integers and must not be filtered by truthiness.
- **Output order:** The contract permits any order, so no sorting clause is required.
