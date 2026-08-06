## Orders Table

`Orders` records the customer, date, item, and quantity for each placed order.

| Column Name | Type |
|---|---|
| `order_id` | `int` |
| `customer_id` | `int` |
| `order_date` | `date` |
| `item_id` | `varchar` |
| `quantity` | `int` |

The combination `(order_id, item_id)` uniquely identifies a row. The
`order_date` is the date on which `customer_id` ordered `item_id`.
