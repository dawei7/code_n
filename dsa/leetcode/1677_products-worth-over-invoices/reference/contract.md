## Function Contract

**Inputs**

- `Product`: Table containing `product_id` (primary key) and `name`.
- `Invoice`: Table containing `invoice_id` (primary key), `product_id`, `rest`, `paid`, `canceled`, and `refunded`.

**Return value**

Return a table with columns `name`, `rest`, `paid`, `canceled`, and `refunded` containing the aggregated sums for all products, ordered by `name` ascending.
