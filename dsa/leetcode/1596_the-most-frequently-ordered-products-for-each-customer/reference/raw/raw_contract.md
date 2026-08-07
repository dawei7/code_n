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

**`Products`**

| Column | Type | Meaning |
|---|---|---|
| `product_id` | int | Unique product identifier. |
| `product_name` | varchar | Display name of the product. |
| `price` | int | Unit price of the product. |

**Return value**

Return columns `customer_id`, `product_id`, and `product_name`. Include every product tied for the maximum number of order rows for each customer with orders. Row order is unrestricted.
