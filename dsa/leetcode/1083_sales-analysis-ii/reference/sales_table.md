## Sales Table

| Column Name | Type |
|---|---|
| `seller_id` | int |
| `product_id` | int |
| `buyer_id` | int |
| `sale_date` | date |
| `quantity` | int |
| `price` | int |

`product_id` is a foreign key that references the `Product` table. The table may contain repeated rows. Both `buyer_id` and `sale_date` are guaranteed to be non-`NULL`, and every row records information about one sale.
