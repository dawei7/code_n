## Examples

**Example 1**

- Input: `Employee = [[1,"Joe",85000,1],[2,"Henry",80000,2],[3,"Sam",60000,2],[4,"Max",90000,1],[5,"Janet",69000,1],[6,"Randy",85000,1],[7,"Will",70000,1]], Department = [[1,"IT"],[2,"Sales"]]`

| id | name | salary | departmentId |
|---:|---|---:|---:|
| 1 | Joe | 85000 | 1 |
| 2 | Henry | 80000 | 2 |
| 3 | Sam | 60000 | 2 |
| 4 | Max | 90000 | 1 |
| 5 | Janet | 69000 | 1 |
| 6 | Randy | 85000 | 1 |
| 7 | Will | 70000 | 1 |

| id | name |
|---:|---|
| 1 | IT |
| 2 | Sales |

- Output: `[["IT","Max",90000],["IT","Joe",85000],["IT","Randy",85000],["IT","Will",70000],["Sales","Henry",80000],["Sales","Sam",60000]]`

| Department | Employee | Salary |
|---|---|---:|
| IT | Max | 90000 |
| IT | Joe | 85000 |
| IT | Randy | 85000 |
| IT | Will | 70000 |
| Sales | Henry | 80000 |
| Sales | Sam | 60000 |

- Explanation: In IT, `90000`, `85000`, and `70000` are the top three unique salaries; both Joe and Randy share the second value. Sales has only two salaries, so Henry and Sam both qualify.
