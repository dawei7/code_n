## Examples

**Example 1**

- **Input:** `Customers = [[1, 2018, 50], [1, 2021, 30], [1, 2020, 70], [2, 2021, -50], [3, 2018, 10], [3, 2016, 50], [4, 2021, 20]]`

`Customers` table:

| customer_id | year | revenue |
|---:|---:|---:|
| 1 | 2018 | 50 |
| 1 | 2021 | 30 |
| 1 | 2020 | 70 |
| 2 | 2021 | -50 |
| 3 | 2018 | 10 |
| 3 | 2016 | 50 |
| 4 | 2021 | 20 |

- **Output:** `[[1], [4]]`

| customer_id |
|---:|
| 1 |
| 4 |

- **Explanation:**
  - Customer 1: Has a 2021 row with revenue 30 (positive). Qualifies.
  - Customer 2: Has a 2021 row with revenue -50 (negative). Excluded.
  - Customer 3: Has positive revenue in 2018 and 2016, but no 2021 row. Excluded.
  - Customer 4: Has a 2021 row with revenue 20 (positive). Qualifies.

**Example 2**

- **Input:** `customer 2 has a 2021 row with revenue -50`
- **Output:** `excluded`

- **Explanation:** The revenue in 2021 must be strictly positive (`revenue > 0`); negative or zero revenue is excluded.

**Example 3**

- **Input:** `customer 3 has positive revenue in 2018 and 2016, but no row for 2021`
- **Output:** `excluded`

- **Explanation:** Revenue in other years does not satisfy the requirement for positive revenue in 2021.
