## Examples

**Example 1**

- Input: `reactions table (15 rows)`
- Output: `users 3 and 1 with their dominant reactions and reaction ratios`
- Explanation: The input table is:

| `user_id` | `content_id` | `reaction` |
|---:|---:|---|
| 1 | 101 | `like` |
| 1 | 102 | `like` |
| 1 | 103 | `like` |
| 1 | 104 | `wow` |
| 1 | 105 | `like` |
| 2 | 201 | `like` |
| 2 | 202 | `wow` |
| 2 | 203 | `sad` |
| 2 | 204 | `like` |
| 2 | 205 | `wow` |
| 3 | 301 | `love` |
| 3 | 302 | `love` |
| 3 | 303 | `love` |
| 3 | 304 | `love` |
| 3 | 305 | `love` |

The result is:

| `user_id` | `dominant_reaction` | `reaction_ratio` |
|---:|---|---:|
| 3 | `love` | 1.00 |
| 1 | `like` | 0.80 |

- **User 1:** There are five reactions in total. Four are `like`, so the ratio is `4 / 5 = 0.80`; this reaches the 60% requirement.
- **User 2:** There are five reactions in total. The highest frequency of any reaction type is two, giving `2 / 5 = 0.40`; this user is not consistent enough to be returned.
- **User 3:** All five reactions are `love`, so the ratio is `5 / 5 = 1.00`; this user meets the requirement.

The result places user 3 before user 1 because `1.00` is greater than `0.80`. If two returned ratios were equal, the smaller `user_id` would appear first.
