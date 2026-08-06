## Examples

**Example 1**

- **Input:** `UserVisits = [[1, "2020-10-20"], [1, "2020-11-28"], [1, "2020-12-03"], [2, "2020-10-05"], [2, "2020-12-09"], [3, "2020-11-11"]]`

`UserVisits` table:

| user_id | visit_date |
|---:|---|
| 1 | `2020-10-20` |
| 1 | `2020-11-28` |
| 1 | `2020-12-03` |
| 2 | `2020-10-05` |
| 2 | `2020-12-09` |
| 3 | `2020-11-11` |

- **Output:** `[[1, 39], [2, 65], [3, 51]]`

| user_id | biggest_window |
|---:|---:|
| 1 | 39 |
| 2 | 65 |
| 3 | 51 |

- **Explanation:**
  - User 1:
    - `2020-10-20` to `2020-11-28`: 39 days
    - `2020-11-28` to `2020-12-03`: 5 days
    - `2020-12-03` to `2021-01-01`: 29 days
    - Biggest window = 39.
  - User 2:
    - `2020-10-05` to `2020-12-09`: 65 days
    - `2020-12-09` to `2021-01-01`: 23 days
    - Biggest window = 65.
  - User 3:
    - `2020-11-11` to `2021-01-01`: 51 days
    - Biggest window = 51.

**Example 2**

- **Input:** `user 2 visits on 2020-10-05 and 2020-12-09`
- **Output:** `(2, 65)`

- **Explanation:** The initial gap of 65 days exceeds the 23-day terminal gap to `2021-01-01`.

**Example 3**

- **Input:** `user 3 visits only on 2020-11-11`
- **Output:** `(3, 51)`

- **Explanation:** A single visit has only one window ending on `2021-01-01` (51 days).
