## Function Contract

**Database Schemas**

**`Customer`**

| Column | Type | Meaning |
|---|---|---|
| `customer_id` | int | Unique customer identifier. |
| `customer_name` | varchar | Customer's name. |

**`Seller`**

| Column | Type | Meaning |
|---|---|---|
| `seller_id` | int | Unique seller identifier. |
| `seller_name` | varchar | Seller's name. |

**`Orders`**

| Column | Type | Meaning |
|---|---|---|
| `order_id` | int | Unique order identifier. |
| `sale_date` | date | Date of the sale. |
| `order_cost` | int | Cost of the order. |
| `customer_id` | int | Customer who placed the order. |
| `seller_id` | int | Seller who made the sale. |

**Return value**

Return a table with the single column `seller_name`. Include sellers for whom no matching order has `sale_date` between `2020-01-01` and `2020-12-31`, ordered by `seller_name` ASC.
