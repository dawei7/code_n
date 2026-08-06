## Examples

**Example 1**

- **Input:**

`Product` table:

| product_id | name |
| --- | --- |
| 0 | ham |
| 1 | bacon |

`Invoice` table:

| invoice_id | product_id | rest | paid | canceled | refunded |
| --- | --- | --- | --- | --- | --- |
| 23 | 0 | 2 | 0 | 5 | 0 |
| 12 | 0 | 0 | 4 | 0 | 3 |
| 1 | 1 | 1 | 1 | 0 | 1 |
| 2 | 1 | 1 | 0 | 1 | 1 |
| 3 | 1 | 0 | 1 | 1 | 1 |
| 4 | 1 | 1 | 1 | 1 | 0 |

- **Output:**

| name | rest | paid | canceled | refunded |
| --- | --- | --- | --- | --- |
| bacon | 3 | 3 | 3 | 3 |
| ham | 2 | 4 | 5 | 3 |

- **Explanation:**
  - The amount of money left to pay for bacon is $1 + 1 + 0 + 1 = 3$
  - The amount of money paid for bacon is $1 + 0 + 1 + 1 = 3$
  - The amount of money canceled for bacon is $0 + 1 + 1 + 1 = 3$
  - The amount of money refunded for bacon is $1 + 1 + 1 + 0 = 3$
  - The amount of money left to pay for ham is $2 + 0 = 2$
  - The amount of money paid for ham is $0 + 4 = 4$
  - The amount of money canceled for ham is $5 + 0 = 5$
  - The amount of money refunded for ham is $0 + 3 = 3$
