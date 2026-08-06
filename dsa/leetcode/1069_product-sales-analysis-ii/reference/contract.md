## Function Contract

**Input tables**

- `Sales(sale_id, product_id, year, quantity, price)`: the sale records whose quantities are aggregated.
- `Product(product_id, product_name)`: the referenced product metadata table.

The output grain is one row for each distinct `product_id` occurring in `Sales`. Product metadata and per-unit price do not change the requested quantity total, and a product with no sale row contributes no output group.

**Return value**

- Columns `product_id` and `total_quantity`, where `total_quantity` is the sum of `quantity` over all `Sales` rows for that `product_id`.
- Result order is unrestricted.
