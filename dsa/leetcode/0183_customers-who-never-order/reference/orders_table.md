## Orders Table

| Column Name | Type |
|---|---|
| `id` | int |
| `customerId` | int |

`id` is the primary key. `customerId` is a foreign key referencing `Customers.id`; each row identifies an order and the customer who placed it.
