## Examples

**Example 1**

- **Input:** `Employee = [[1,8],[2,8],[3,8],[4,7],[5,9],[6,9]]`

`Employee`:

| employee_id | team_id |
|---:|---:|
| 1 | 8 |
| 2 | 8 |
| 3 | 8 |
| 4 | 7 |
| 5 | 9 |
| 6 | 9 |

- **Output:** `[[1,3],[2,3],[3,3],[4,1],[5,2],[6,2]]`

Result:

| employee_id | team_size |
|---:|---:|
| 1 | 3 |
| 2 | 3 |
| 3 | 3 |
| 4 | 1 |
| 5 | 2 |
| 6 | 2 |

- **Explanation:** Employees `1`, `2`, and `3` belong to team `8`, so each receives size `3`. Employee `4` is the only member of team `7` and receives size `1`. Employees `5` and `6` share team `9`, so each receives size `2`.
