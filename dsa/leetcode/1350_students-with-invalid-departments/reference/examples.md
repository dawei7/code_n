## Examples

**Example 1**

- **Input:** `Departments = [[1,"Electrical Engineering"],[7,"Computer Engineering"],[13,"Bussiness Administration"]], Students = [[23,"Alice",1],[1,"Bob",7],[5,"Jennifer",13],[2,"John",14],[4,"Jasmine",77],[3,"Steve",74],[6,"Luis",1],[8,"Jonathan",7],[7,"Daiana",33],[11,"Madelynn",1]]`

`Departments`:

| id | name |
|---:|---|
| 1 | Electrical Engineering |
| 7 | Computer Engineering |
| 13 | Bussiness Administration |

`Students`:

| id | name | department_id |
|---:|---|---:|
| 23 | Alice | 1 |
| 1 | Bob | 7 |
| 5 | Jennifer | 13 |
| 2 | John | 14 |
| 4 | Jasmine | 77 |
| 3 | Steve | 74 |
| 6 | Luis | 1 |
| 8 | Jonathan | 7 |
| 7 | Daiana | 33 |
| 11 | Madelynn | 1 |

- **Output:** `[[2,"John"],[7,"Daiana"],[4,"Jasmine"],[3,"Steve"]]`

| id | name |
|---:|---|
| 2 | John |
| 7 | Daiana |
| 4 | Jasmine |
| 3 | Steve |

- **Explanation:** John, Daiana, Steve, and Jasmine refer to department IDs `14`, `33`, `74`, and `77`, respectively. None of those four IDs occurs in `Departments`, whereas every other student's recorded department is present.
