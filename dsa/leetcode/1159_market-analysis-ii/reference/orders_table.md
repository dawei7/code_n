## Orders Table

`Orders`

| Column Name | Type |
|---|---|
| `order_id` | `int` |
| `order_date` | `date` |
| `item_id` | `int` |
| `buyer_id` | `int` |
| `seller_id` | `int` |

`order_id` is the primary key and contains unique values. `item_id` references `Items`, while `buyer_id` and `seller_id` both reference `Users`.
