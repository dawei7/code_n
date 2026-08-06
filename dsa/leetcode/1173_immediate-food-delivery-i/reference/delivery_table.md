## Delivery Table

`Delivery`

| Column Name | Type |
|---|---|
| `delivery_id` | `int` |
| `customer_id` | `int` |
| `order_date` | `date` |
| `customer_pref_delivery_date` | `date` |

`delivery_id` is the table's primary key and therefore contains unique values. Each row records a food order, the customer who placed it, its order date, and the customer's preferred delivery date. The preferred date is either the order date or a later date.
