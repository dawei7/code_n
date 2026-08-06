## Examples

**Example 1**

- **Input:** `Customers = [[1, "Winston"], [2, "Jonathan"], [3, "Annabelle"], [4, "Marwan"], [5, "Khaled"]], Products = [[1, "keyboard", 20], [2, "mouse", 10], [3, "screen", 200], [4, "hard disk", 50]], Orders = [[1, "2020-07-31", 1, 1], [2, "2020-07-30", 2, 2], [3, "2020-08-29", 3, 3], [4, "2020-07-29", 4, 1], [5, "2020-06-10", 1, 2], [6, "2020-08-01", 2, 1], [7, "2020-08-01", 3, 1], [8, "2020-08-03", 1, 2], [9, "2020-08-07", 2, 3]]`

`Customers` table:

| customer_id | name |
|---:|---|
| 1 | Winston |
| 2 | Jonathan |
| 3 | Annabelle |
| 4 | Marwan |
| 5 | Khaled |

`Products` table:

| product_id | product_name | price |
|---:|---|---:|
| 1 | keyboard | 20 |
| 2 | mouse | 10 |
| 3 | screen | 200 |
| 4 | hard disk | 50 |

`Orders` table:

| order_id | order_date | customer_id | product_id |
|---:|---|---:|---:|
| 1 | `2020-07-31` | 1 | 1 |
| 2 | `2020-07-30` | 2 | 2 |
| 3 | `2020-08-29` | 3 | 3 |
| 4 | `2020-07-29` | 4 | 1 |
| 5 | `2020-06-10` | 1 | 2 |
| 6 | `2020-08-01` | 2 | 1 |
| 7 | `2020-08-01` | 3 | 1 |
| 8 | `2020-08-03` | 1 | 2 |
| 9 | `2020-08-07` | 2 | 3 |

- **Output:** `[["keyboard", 1, 6, "2020-08-01"], ["keyboard", 1, 7, "2020-08-01"], ["mouse", 2, 8, "2020-08-03"], ["screen", 3, 3, "2020-08-29"]]`

| product_name | product_id | order_id | order_date |
|---|---:|---:|---|
| keyboard | 1 | 6 | `2020-08-01` |
| keyboard | 1 | 7 | `2020-08-01` |
| mouse | 2 | 8 | `2020-08-03` |
| screen | 3 | 3 | `2020-08-29` |

- **Explanation:**
  - `keyboard` (`1`): latest order date is `2020-08-01`. Both orders 6 and 7 occurred on this date and are included.
  - `mouse` (`2`): latest order date is `2020-08-03` (order 8).
  - `screen` (`3`): latest order date is `2020-08-29` (order 3).
  - `hard disk` (`4`): never ordered, so omitted.
  - Sorted by `product_name` ASC, `product_id` ASC, `order_id` ASC.

**Example 2**

- **Input:** `one product with orders 10 and 11 on its latest day`
- **Output:** `both rows included, ordered by order_id`

- **Explanation:** All orders placed on a product's latest date are returned rather than selecting an arbitrary single row.

**Example 3**

- **Input:** `two products named "pen" with IDs 2 and 1`
- **Output:** `product with ID 1 appears before product with ID 2`

- **Explanation:** Product ID in ascending order breaks ties between products sharing the same name.
