## Examples

**Example 1**

- **Input:** `Transactions = [[8, "2021-04-03 15:57:28", 57], [9, "2021-04-28 08:47:25", 21], [1, "2021-04-29 13:28:30", 58], [5, "2021-04-28 16:39:59", 40], [6, "2021-04-29 23:39:28", 58]]`

`Transactions` table:

| transaction_id | day | amount |
|---:|---|---:|
| 8 | `2021-04-03 15:57:28` | 57 |
| 9 | `2021-04-28 08:47:25` | 21 |
| 1 | `2021-04-29 13:28:30` | 58 |
| 5 | `2021-04-28 16:39:59` | 40 |
| 6 | `2021-04-29 23:39:28` | 58 |

- **Output:** `[[1], [5], [6], [8]]`

| transaction_id |
|---:|
| 1 |
| 5 |
| 6 |
| 8 |

- **Explanation:**
  - `2021-04-03`: Transaction 8 (amount 57). Maximum is 57 -> ID 8.
  - `2021-04-28`: Transactions 9 (21) and 5 (40). Maximum is 40 -> ID 5.
  - `2021-04-29`: Transactions 1 (58) and 6 (58). Tied maximum is 58 -> IDs 1 and 6.
  - Sorted by `transaction_id` ASC: 1, 5, 6, 8.

**Example 2**

- **Input:** `(4, "2022-01-01 23:59:59", 10)` and `(2, "2022-01-02 00:00:00", 5)`
- **Output:** `[[2], [4]]`

- **Explanation:** The two timestamps fall on different calendar dates (`2022-01-01` vs `2022-01-02`), so both transactions are daily maxima for their respective dates.

**Example 3**

- **Input:** `date containing only one transaction`
- **Output:** `that transaction's ID is returned`

- **Explanation:** A single transaction on a date is automatically the maximum transaction for that day.
