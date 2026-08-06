## Examples

**Example 1**

- **Input:** `Project = [[1,1],[1,2],[1,3],[2,1],[2,4]], Employee = [[1,"Khaled",3],[2,"Ali",2],[3,"John",1],[4,"Doe",2]]`

`Project`:

| project_id | employee_id |
|---:|---:|
| 1 | 1 |
| 1 | 2 |
| 1 | 3 |
| 2 | 1 |
| 2 | 4 |

`Employee`:

| employee_id | name | experience_years |
|---:|---|---:|
| 1 | Khaled | 3 |
| 2 | Ali | 2 |
| 3 | John | 1 |
| 4 | Doe | 2 |

- **Output:** `[[1]]`

| project_id |
|---:|
| 1 |

- **Explanation:** Project 1 has three assigned employees, whereas project 2 has two, so project 1 alone has the largest employee count.
