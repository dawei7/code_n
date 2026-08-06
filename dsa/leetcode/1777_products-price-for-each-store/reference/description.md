## Description

The `Products` table records prices in row form. Each row identifies a product, one of the stores `"store1"`, `"store2"`, or `"store3"`, and that product's price at the store. The pair `(product_id, store)` is unique, so a product has at most one recorded price per store.

Pivot these rows into one row per product. The result must contain `product_id` followed by columns `store1`, `store2`, and `store3`. Put each recorded price in its store's column and use `NULL` when the product is not available at that store. The rows may be returned in any order.
