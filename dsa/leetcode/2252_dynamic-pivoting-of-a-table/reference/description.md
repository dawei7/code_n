## Description

The `Products` table contains one row for each available `(product_id, store)`
pair, together with that product's `price` at the store. The pair is the
primary key, and the table contains at most 30 distinct store names.

Implement the MySQL procedure `PivotProducts` so each output row represents
one product. After `product_id`, create one column for every store found in the
current table, with store columns sorted in lexicographical order. A cell
contains the product's price at that store or `null` when the store does not
sell the product. Output row order is unrestricted.
