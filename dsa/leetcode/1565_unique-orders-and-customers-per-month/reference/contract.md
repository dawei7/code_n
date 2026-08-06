## Function Contract

**Inputs**

- `Orders`: Table with columns `order_id` (int), `order_date` (date), `customer_id` (int), `invoice` (int).

**Return value**

Return a table with columns `month` (varchar `YYYY-MM`), `order_count` (int), and `customer_count` (int) for orders with `invoice > 20`.
