## Examples

**Example 1**

- **Input:** `Customers = [[1, "Winston"], [2, "Jonathan"], [3, "Annabelle"], [4, "Marwan"]], Orders = [[1, "2020-07-31", 1, 30], [2, "2020-07-30", 2, 40], [3, "2020-07-31", 3, 70], [4, "2020-07-29", 4, 100], [5, "2020-06-10", 1, 1010], [6, "2020-08-01", 2, 1020], [7, "2020-08-01", 3, 111], [8, "2020-08-03", 1, 99], [9, "2020-08-07", 2, 32], [10, "2020-07-15", 1, 2]]`

`Customers` table:

| customer_id | name |
|---:|---|
| 1 | Winston |
| 2 | Jonathan |
| 3 | Annabelle |
| 4 | Marwan |

`Orders` table:

| order_id | order_date | customer_id | cost |
|---:|---|---:|---:|
| 1 | `2020-07-31` | 1 | 30 |
| 2 | `2020-07-30` | 2 | 40 |
| 3 | `2020-07-31` | 3 | 70 |
| 4 | `2020-07-29` | 4 | 100 |
| 5 | `2020-06-10` | 1 | 1010 |
| 6 | `2020-08-01` | 2 | 1020 |
| 7 | `2020-08-01` | 3 | 111 |
| 8 | `2020-08-03` | 1 | 99 |
| 9 | `2020-08-07` | 2 | 32 |
| 10 | `2020-07-15` | 1 | 2 |

- **Output:** `[["Annabelle", 3, 7, "2020-08-01"], ["Annabelle", 3, 3, "2020-07-31"], ["Jonathan", 2, 9, "2020-08-07"], ["Jonathan", 2, 6, "2020-08-01"], ["Jonathan", 2, 2, "2020-07-30"], ["Marwan", 4, 4, "2020-07-29"], ["Winston", 1, 8, "2020-08-03"], ["Winston", 1, 1, "2020-07-31"], ["Winston", 1, 10, "2020-07-15"]]`

| customer_name | customer_id | order_id | order_date |
|---|---:|---:|---|
| Annabelle | 3 | 7 | `2020-08-01` |
| Annabelle | 3 | 3 | `2020-07-31` |
| Jonathan | 2 | 9 | `2020-08-07` |
| Jonathan | 2 | 6 | `2020-08-01` |
| Jonathan | 2 | 2 | `2020-07-30` |
| Marwan | 4 | 4 | `2020-07-29` |
| Winston | 1 | 8 | `2020-08-03` |
| Winston | 1 | 1 | `2020-07-31` |
| Winston | 1 | 10 | `2020-07-15` |

- **Explanation:**
  - Annabelle has 2 orders (Aug 1, Jul 31); both are returned.
  - Jonathan has 3 orders (Aug 7, Aug 1, Jul 30); all 3 are returned.
  - Marwan has 1 order (Jul 29); it is returned.
  - Winston has 4 orders (Aug 3, Jul 31, Jul 15, Jun 10); the 3 newest (Aug 3, Jul 31, Jul 15) are returned and Jun 10 is excluded.
  - The rows are ordered by `customer_name` ASC, `customer_id` ASC, and `order_date` DESC.

**Example 2**

- **Input:** `customer with fewer than 3 orders`
- **Output:** `all orders returned for that customer`

- **Explanation:** A customer with fewer than 3 orders retains every order.

**Example 3**

- **Input:** `two customers share a name`
- **Output:** `ordered by customer_id ascending when names tie`

- **Explanation:** Ties in customer name are broken by customer ID in ascending order.
