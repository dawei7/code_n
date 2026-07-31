## Examples

**Example 1**

- Input: `Employee = [[1,"Joe",70000,1],[2,"Jim",90000,1],[3,"Henry",80000,2],[4,"Sam",60000,2],[5,"Max",90000,1]], Department = [[1,"IT"],[2,"Sales"]]`

| id | name | salary | departmentId |
|---:|---|---:|---:|
| 1 | Joe | 70000 | 1 |
| 2 | Jim | 90000 | 1 |
| 3 | Henry | 80000 | 2 |
| 4 | Sam | 60000 | 2 |
| 5 | Max | 90000 | 1 |

| id | name |
|---:|---|
| 1 | IT |
| 2 | Sales |

- Output: `[["IT","Jim",90000],["Sales","Henry",80000],["IT","Max",90000]]`

| Department | Employee | Salary |
|---|---|---:|
| IT | Jim | 90000 |
| Sales | Henry | 80000 |
| IT | Max | 90000 |

- Explanation: Jim and Max share the highest salary in IT, while Henry has the highest salary in Sales.
