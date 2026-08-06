## Examples

**Example 1**

- **Input:** `Employee = [[1,1,20],[2,1,20],[1,2,30],[2,2,30],[3,2,40],[1,3,40],[3,3,60],[1,4,60],[3,4,70],[1,7,90],[1,8,90]]`

| id | month | salary |
|---:|---:|---:|
| 1 | 1 | 20 |
| 2 | 1 | 20 |
| 1 | 2 | 30 |
| 2 | 2 | 30 |
| 3 | 2 | 40 |
| 1 | 3 | 40 |
| 3 | 3 | 60 |
| 1 | 4 | 60 |
| 3 | 4 | 70 |
| 1 | 7 | 90 |
| 1 | 8 | 90 |

- **Output:** `[[1,7,90],[1,4,130],[1,3,90],[1,2,50],[1,1,20],[2,1,20],[3,3,100],[3,2,40]]`

| id | month | Salary |
|---:|---:|---:|
| 1 | 7 | 90 |
| 1 | 4 | 130 |
| 1 | 3 | 90 |
| 1 | 2 | 50 |
| 1 | 1 | 20 |
| 2 | 1 | 20 |
| 3 | 3 | 100 |
| 3 | 2 | 40 |

- **Explanation:** For employee `1`, exclude the most recent recorded month, `8`. The five remaining summary rows are:

| id | month | salary |
|---:|---:|---:|
| 1 | 7 | 90 |
| 1 | 4 | 130 |
| 1 | 3 | 90 |
| 1 | 2 | 50 |
| 1 | 1 | 20 |

Their calculations are `90 + 0 + 0 = 90` for month `7`, `60 + 40 + 30 = 130` for month `4`, `40 + 30 + 20 = 90` for month `3`, `30 + 20 + 0 = 50` for month `2`, and `20 + 0 + 0 = 20` for month `1`. In particular, months `5` and `6` have no records, so month `7` does not include the salary from month `4`.

Employee `2` has only month `1` left after excluding its latest month, `2`:

| id | month | salary |
|---:|---:|---:|
| 2 | 1 | 20 |

That summary is `20 + 0 + 0 = 20`.

For employee `3`, exclude latest month `4`; months `3` and `2` remain:

| id | month | salary |
|---:|---:|---:|
| 3 | 3 | 100 |
| 3 | 2 | 40 |

The corresponding sums are `60 + 40 + 0 = 100` and `40 + 0 + 0 = 40`.
