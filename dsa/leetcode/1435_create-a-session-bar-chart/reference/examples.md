## Examples

**Example 1**

- **Input:** `Sessions = [[1,30],[2,199],[3,299],[4,580],[5,1000]]`

| session_id | duration |
|---:|---:|
| 1 | 30 |
| 2 | 199 |
| 3 | 299 |
| 4 | 580 |
| 5 | 1000 |

- **Output:** `[["[0-5>",3],["[5-10>",1],["[10-15>",0],["15 or more",1]]`

| bin | total |
|---|---:|
| `[0-5>` | 3 |
| `[5-10>` | 1 |
| `[10-15>` | 0 |
| `15 or more` | 1 |

- **Explanation:** Sessions `1`, `2`, and `3` last at least 0 minutes but less than 5 minutes. Session `4` lasts at least 5 minutes but less than 10 minutes. No session lies from 10 minutes inclusive to 15 minutes exclusive. Session `5` lasts at least 15 minutes.
