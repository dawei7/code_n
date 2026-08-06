## Examples

**Example 1**

- **Input:** `Customers = [[1, "Winston", "USA"], [2, "Jonathan", "Peru"], [3, "Moustafa", "Egypt"]], Product = [[10, "LC Book", 45], [20, "LC T-Shirt", 10], [30, "LC Keychain", 5], [40, "LC Phone", 300]], Orders = [[1, 1, 10, "2020-06-10", 1], [2, 1, 20, "2020-07-01", 1], [3, 1, 30, "2020-07-08", 2], [4, 2, 10, "2020-06-15", 2], [5, 2, 40, "2020-07-01", 10], [6, 3, 20, "2020-06-24", 2], [7, 3, 30, "2020-06-25", 2]]`

`Customers` table:

| customer_id | name | country |
|---:|---|---|
| 1 | Winston | USA |
| 2 | Jonathan | Peru |
| 3 | Moustafa | Egypt |

`Product` table:

| product_id | description | price |
|---:|---|---:|
| 10 | LC Book | 45 |
| 20 | LC T-Shirt | 10 |
| 30 | LC Keychain | 5 |
| 40 | LC Phone | 300 |

`Orders` table:

| order_id | customer_id | product_id | order_date | quantity |
|---:|---:|---:|---|---:|
| 1 | 1 | 10 | `2020-06-10` | 1 |
| 2 | 1 | 20 | `2020-07-01` | 1 |
| 3 | 1 | 30 | `2020-07-08` | 2 |
| 4 | 2 | 10 | `2020-06-15` | 2 |
| 5 | 2 | 40 | `2020-07-01` | 10 |
| 6 | 3 | 20 | `2020-06-24` | 2 |
| 7 | 3 | 30 | `2020-06-25` | 2 |

- **Output:** `[[1, "Winston"]]`

| customer_id | name |
|---:|---|
| 1 | Winston |

- **Explanation:**
  - Winston (`1`) spent 300 in June and 100 in July (at least 100 in both months).
  - Jonathan (`2`) spent 600 in June but only 20 in July.
  - Moustafa (`3`) spent 30 in June and 0 in July.
  - Therefore, Winston is the only qualifying customer.

**Example 2**

- **Input:** `customer spends 100 on 2020-06-01 and 100 on 2020-07-31`
- **Output:** `customer qualifies`

- **Explanation:** A customer spending exactly 100 on June 1 and exactly 100 on July 31 satisfies both inclusive month thresholds.

**Example 3**

- **Input:** `customer spends 200 in June, 99 in July, 500 in August`
- **Output:** `[]`

- **Explanation:** August spending cannot make up for the July shortfall of 99 (< 100).
