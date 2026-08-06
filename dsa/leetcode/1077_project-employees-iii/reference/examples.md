## Examples

**Example 1**

- **Input:** `Project = [[1,1],[1,2],[1,3],[2,1],[2,4]], Employee = [[1,"Khaled",3],[2,"Ali",2],[3,"John",3],[4,"Doe",2]]`

Project:

| project_id | employee_id |
|---:|---:|
| 1 | 1 |
| 1 | 2 |
| 1 | 3 |
| 2 | 1 |
| 2 | 4 |

Employee:

| employee_id | name | experience_years |
|---:|---|---:|
| 1 | Khaled | 3 |
| 2 | Ali | 2 |
| 3 | John | 3 |
| 4 | Doe | 2 |

- **Output:** `[[1,1],[1,3],[2,1]]`

| project_id | employee_id |
|---:|---:|
| 1 | 1 |
| 1 | 3 |
| 2 | 1 |

- **Explanation:** On project 1, employees 1 and 3 each have three years of experience, exceeding employee 2's two years, so both tied employees are reported. On project 2, employee 1 has three years while employee 4 has two, so only employee 1 is reported there.
