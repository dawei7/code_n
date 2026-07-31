## Examples

**Example 1**

- Input: `activity` table (17 rows)

| `user_id` | `action_date` | `action` |
|---:|---|---|
| 1 | `2024-01-01` | `login` |
| 1 | `2024-01-02` | `login` |
| 1 | `2024-01-03` | `login` |
| 1 | `2024-01-04` | `login` |
| 1 | `2024-01-05` | `login` |
| 1 | `2024-01-06` | `logout` |
| 2 | `2024-01-01` | `click` |
| 2 | `2024-01-02` | `click` |
| 2 | `2024-01-03` | `click` |
| 2 | `2024-01-04` | `click` |
| 3 | `2024-01-01` | `view` |
| 3 | `2024-01-02` | `view` |
| 3 | `2024-01-03` | `view` |
| 3 | `2024-01-04` | `view` |
| 3 | `2024-01-05` | `view` |
| 3 | `2024-01-06` | `view` |
| 3 | `2024-01-07` | `view` |

- Output: users 3 and 1 with their selected streaks

| `user_id` | `action` | `streak_length` | `start_date` | `end_date` |
|---:|---|---:|---|---|
| 3 | `view` | 7 | `2024-01-01` | `2024-01-07` |
| 1 | `login` | 5 | `2024-01-01` | `2024-01-05` |

- Explanation:

  - **User 1:** `login` is the user's only action on each date from January 1 through January 5, and those five dates are consecutive. The length-five run therefore reaches the minimum. The January 6 action is `logout`, so the `login` run ends before that date.
  - **User 2:** The four consecutive `click` dates form a same-action run, but its length is only four. This user is excluded.
  - **User 3:** The user performs only `view` on seven consecutive dates. This is the user's longest valid run, so it is included.

The seven-day result precedes the five-day result because rows are sorted by decreasing `streak_length`; equal lengths would use increasing `user_id`.
