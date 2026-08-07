## Function Contract

**Database Schema**

**`Customers`**

| Column | Type | Meaning |
|---|---|---|
| `customer_id` | int | Customer identifier; composite primary key with `year`. |
| `year` | int | Calendar year. |
| `revenue` | int | Customer's revenue for that year (can be negative, zero, or positive). |

- `(customer_id, year)` is unique.

**Return value**

Return a table with the single column `customer_id`. Include each `customer_id` whose row in `Customers` has `year = 2021` and `revenue > 0`. Row order is unrestricted.
