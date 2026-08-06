## Function Contract

**Database Schemas**

**`Customers`**

| Column | Type | Meaning |
|---|---|---|
| `customer_id` | int | Unique customer identifier. |
| `name` | varchar | Customer's name. |

**`Orders`**

| Column | Type | Meaning |
|---|---|---|
| `order_id` | int | Unique order identifier. |
| `order_date` | date | Date of the order; at most one per customer per day. |
| `customer_id` | int | Customer who placed the order. |
| `cost` | int | Order cost (not projected in output). |

**Return value**

Return columns `customer_name`, `customer_id`, `order_id`, and `order_date`. For each customer with orders, return at most their 3 newest orders by date. Order the output by `customer_name` ASC, `customer_id` ASC, and `order_date` DESC.
