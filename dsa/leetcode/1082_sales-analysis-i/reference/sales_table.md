## Sales Table

| Column Name | Type |
|---|---|
| `seller_id` | int |
| `product_id` | int |
| `buyer_id` | int |
| `sale_date` | date |
| `quantity` | int |
| `price` | int |

`product_id` is a foreign key that references the `Product` table. Each row describes one sale. The table has no stated primary key and may contain repeated rows, so every occurrence of a repeated sale row remains a separate contribution to its seller's total.
