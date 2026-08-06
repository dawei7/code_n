## Description

The wide `Products` table has primary-key column `product_id` followed by one
integer price column for each store. Store column names vary between test
cases, with between one and 30 stores. A `NULL` store cell means that product
is unavailable there.

Implement the MySQL procedure `UnpivotProducts` to return a normalized
three-column table: `product_id`, `store`, and `price`. Emit one row for every
non-null product-store price, use the source column name as `store`, and omit
unavailable combinations. Result row order is unrestricted.
