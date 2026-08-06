## Examples

**Example 1**

- **Input:** `Calls = [[1, 2, 59], [2, 1, 11], [1, 3, 20], [3, 4, 100], [3, 4, 200], [3, 4, 200], [4, 3, 499]]`

`Calls` table:

| from_id | to_id | duration |
|---:|---:|---:|
| 1 | 2 | 59 |
| 2 | 1 | 11 |
| 1 | 3 | 20 |
| 3 | 4 | 100 |
| 3 | 4 | 200 |
| 3 | 4 | 200 |
| 4 | 3 | 499 |

- **Output:** `[[1, 2, 2, 70], [1, 3, 1, 20], [3, 4, 4, 999]]`

| person1 | person2 | call_count | total_duration |
|---:|---:|---:|---:|
| 1 | 2 | 2 | 70 |
| 1 | 3 | 1 | 20 |
| 3 | 4 | 4 | 999 |

- **Explanation:**
  - Pair `(1, 2)`: 2 calls (`1->2` for 59, `2->1` for 11). `call_count = 2`, `total_duration = 70`.
  - Pair `(1, 3)`: 1 call (`1->3` for 20). `call_count = 1`, `total_duration = 20`.
  - Pair `(3, 4)`: 4 calls (`3->4` for 100, 200, 200, and `4->3` for 499). `call_count = 4`, `total_duration = 999`.

**Example 2**

- **Input:** `calls between 3 and 4 with durations 100, 200, 200, and 499`
- **Output:** `(3, 4, 4, 999)`

- **Explanation:** Two identical rows `[3, 4, 200]` represent separate calls and both contribute to `call_count` and `total_duration`.

**Example 3**

- **Input:** `one call 7 -> 2 lasting 30`
- **Output:** `(2, 7, 1, 30)`

- **Explanation:** The smaller ID `2` is assigned to `person1` and the larger ID `7` to `person2`.
