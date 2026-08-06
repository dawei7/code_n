## Examples

**Example 1**

- **Input:** `Customer = [[101, "Alice"], [102, "Bob"], [103, "Charlie"]], Seller = [[1, "Daniel"], [2, "Elizabeth"], [3, "Frank"]], Orders = [[1, "2020-03-01", 20, 101, 1], [2, "2020-05-15", 30, 102, 2], [3, "2019-12-25", 50, 101, 3]]`

`Customer` table:

| customer_id | customer_name |
|---:|---|
| 101 | Alice |
| 102 | Bob |
| 103 | Charlie |

`Seller` table:

| seller_id | seller_name |
|---:|---|
| 1 | Daniel |
| 2 | Elizabeth |
| 3 | Frank |

`Orders` table:

| order_id | sale_date | order_cost | customer_id | seller_id |
|---:|---|---:|---:|---:|
| 1 | `2020-03-01` | 20 | 101 | 1 |
| 2 | `2020-05-15` | 30 | 102 | 2 |
| 3 | `2019-12-25` | 50 | 101 | 3 |

- **Output:** `[["Frank"]]`

| seller_name |
|---|
| Frank |

- **Explanation:**
  - Daniel (`1`) has a sale on `2020-03-01` (in 2020), so excluded.
  - Elizabeth (`2`) has a sale on `2020-05-15` (in 2020), so excluded.
  - Frank (`3`) has a sale on `2019-12-25` (outside 2020) and no sales in 2020, so Frank qualifies.

**Example 2**

- **Input:** `seller with orders on 2020-01-01 and 2020-12-31`
- **Output:** `excluded`

- **Explanation:** The 2020 interval is inclusive of both boundary dates `2020-01-01` and `2020-12-31`.

**Example 3**

- **Input:** `seller with no rows in Orders table`
- **Output:** `included`

- **Explanation:** A seller with no order history in `Orders` made no sales in 2020 and is included.
