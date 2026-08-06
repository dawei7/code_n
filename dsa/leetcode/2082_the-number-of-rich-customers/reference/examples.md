## Examples

**Example 1**

- **Input:** `Store = [[6, 1, 549], [8, 1, 834], [4, 2, 394], [11, 3, 657], [13, 3, 257]]`

`Store` table:

| bill_id | customer_id | amount |
|---:|---:|---:|
| 6 | 1 | 549 |
| 8 | 1 | 834 |
| 4 | 2 | 394 |
| 11 | 3 | 657 |
| 13 | 3 | 257 |

- **Output:** `[[2]]`

| rich_count |
|---:|
| 2 |

- **Explanation:**
  - Customer 1 has two bills > 500 (549 and 834), so customer 1 qualifies (counts as 1).
  - Customer 2 has no bills > 500 (394 <= 500). Excluded.
  - Customer 3 has one bill > 500 (657), so customer 3 qualifies (counts as 1).
  - Total distinct rich customers $= 2$.

**Example 2**

- **Input:** `Store = [[1, 7, 500], [2, 8, 501]]`
- **Output:** `[[1]]`

- **Explanation:** Amount of 500 is not strictly greater than 500, so customer 7 is excluded while customer 8 (501 > 500) qualifies.

**Example 3**

- **Input:** `Store = [[1, 4, 100], [2, 4, 900], [3, 5, 300]]`
- **Output:** `[[1]]`

- **Explanation:** One bill > 500 (bill 2 for customer 4) is sufficient to make customer 4 rich.
