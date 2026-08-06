## Orders Table

| Column Name | Type |
|---|---|
| `order_id` | int |
| `customer_id` | int |
| `product_name` | varchar |

`order_id` contains unique values, so it identifies one purchase row. Each row associates the customer identified by `customer_id` with the product named by `product_name`.
