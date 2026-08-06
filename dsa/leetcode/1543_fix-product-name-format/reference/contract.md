## Function Contract

**Inputs**

- `Sales`: A table with columns `sale_id` (int), `product_name` (varchar), `sale_date` (date).

**Return value**

Return a table with columns `product_name` (varchar), `sale_date` (varchar `YYYY-MM`), and `total` (int). Results must be grouped by normalized `product_name` and `sale_date` month, and ordered ascending by `product_name` then `sale_date`.
