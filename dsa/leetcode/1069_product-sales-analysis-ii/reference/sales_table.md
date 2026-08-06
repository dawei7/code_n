## Sales Table

| Column Name | Type |
|---|---|
| `sale_id` | int |
| `product_id` | int |
| `year` | int |
| `quantity` | int |
| `price` | int |

The pair `(sale_id, year)` is the composite primary key, so each combination of those two values is unique. `product_id` is a foreign key that references the `Product` table. Every row records a sale of the identified product in a particular year, and `price` is the price per unit.
