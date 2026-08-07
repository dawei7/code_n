## Function Contract

**Database Schemas**

**`Customers`**

| Column | Type | Meaning |
|---|---|---|
| `customer_id` | int | Unique customer identifier. |
| `name` | varchar | Customer's name. |
| `country` | varchar | Customer's country. |

**`Product`**

| Column | Type | Meaning |
|---|---|---|
| `product_id` | int | Unique product identifier. |
| `description` | varchar | Product description. |
| `price` | int | Unit price of the product. |

**`Orders`**

| Column | Type | Meaning |
|---|---|---|
| `order_id` | int | Unique order identifier. |
| `customer_id` | int | Customer who placed the order. |
| `product_id` | int | Product purchased. |
| `order_date` | date | Date of the order. |
| `quantity` | int | Quantity purchased. |

**Return value**

Return columns `customer_id` and `name` for customers whose total spending is at least 100 in June 2020 (`2020-06-01` through `2020-06-30`) and independently at least 100 in July 2020 (`2020-07-01` through `2020-07-31`). Row order is unrestricted.
