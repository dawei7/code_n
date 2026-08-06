## Examples

**Example 1**

- **Input:** `Customers = [[1, "Alice"], [2, "Bob"], [3, "Tom"], [4, "Jerry"], [5, "John"]], Products = [[1, "keyboard", 120], [2, "mouse", 80], [3, "screen", 600], [4, "hard disk", 450]], Orders = [[1, "2020-07-31", 1, 1], [2, "2020-07-30", 2, 2], [3, "2020-08-29", 3, 3], [4, "2020-07-29", 4, 1], [5, "2020-06-10", 1, 2], [6, "2020-08-01", 2, 1], [7, "2020-08-01", 3, 3], [8, "2020-08-03", 1, 2], [9, "2020-08-07", 2, 3], [10, "2020-07-15", 1, 2]]`

`Customers` table:

| customer_id | name |
|---:|---|
| 1 | Alice |
| 2 | Bob |
| 3 | Tom |
| 4 | Jerry |
| 5 | John |

`Products` table:

| product_id | product_name | price |
|---:|---|---:|
| 1 | keyboard | 120 |
| 2 | mouse | 80 |
| 3 | screen | 600 |
| 4 | hard disk | 450 |

`Orders` table:

| order_id | order_date | customer_id | product_id |
|---:|---|---:|---:|
| 1 | `2020-07-31` | 1 | 1 |
| 2 | `2020-07-30` | 2 | 2 |
| 3 | `2020-08-29` | 3 | 3 |
| 4 | `2020-07-29` | 4 | 1 |
| 5 | `2020-06-10` | 1 | 2 |
| 6 | `2020-08-01` | 2 | 1 |
| 7 | `2020-08-01` | 3 | 3 |
| 8 | `2020-08-03` | 1 | 2 |
| 9 | `2020-08-07` | 2 | 3 |
| 10 | `2020-07-15` | 1 | 2 |

- **Output:** `[[1, 2, "mouse"], [2, 1, "keyboard"], [2, 2, "mouse"], [2, 3, "screen"], [3, 3, "screen"], [4, 1, "keyboard"]]`

| customer_id | product_id | product_name |
|---:|---:|---|
| 1 | 2 | mouse |
| 2 | 1 | keyboard |
| 2 | 2 | mouse |
| 2 | 3 | screen |
| 3 | 3 | screen |
| 4 | 1 | keyboard |

- **Explanation:**
  - Alice (`1`): ordered mouse (id 2) 3 times, keyboard (id 1) 1 time. Maximum frequency is 3 for mouse.
  - Bob (`2`): ordered keyboard, mouse, and screen 1 time each. All three are tied at maximum frequency 1.
  - Tom (`3`): ordered screen 2 times.
  - Jerry (`4`): ordered keyboard 1 time.
  - John (`5`): has no orders and is omitted.

**Example 2**

- **Input:** `one customer orders two different products twice each`
- **Output:** `two rows for that customer, one for each tied product`

- **Explanation:** All products tied at the maximum order count for a customer are returned.

**Example 3**

- **Input:** `customer with no orders in Orders table`
- **Output:** `no rows for that customer`

- **Explanation:** Aggregation begins from Orders, naturally excluding customers who never placed an order.
