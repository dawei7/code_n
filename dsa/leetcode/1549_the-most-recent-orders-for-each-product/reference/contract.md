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
| `order_date` | date | Date of the order. |
| `customer_id` | int | Customer who placed the order. |
| `product_id` | int | Product ordered. |

- A customer does not order the same product more than once on a single date.

**`Products`**

| Column | Type | Meaning |
|---|---|---|
| `product_id` | int | Unique product identifier. |
| `product_name` | varchar | Display name of the product. |
| `price` | int | Unit price of the product. |

**Return value**

Return columns `product_name`, `product_id`, `order_id`, and `order_date`. Include every order placed on the latest order date for each ordered product. Sort the output by `product_name` ASC, `product_id` ASC, and `order_id` ASC.
