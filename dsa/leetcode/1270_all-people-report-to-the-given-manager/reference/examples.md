## Examples

**Example 1**

- **Input:** `Employees = [[1,"Boss",1],[3,"Alice",3],[2,"Bob",1],[4,"Daniel",2],[7,"Luis",4],[8,"Jhon",3],[9,"Angela",8],[77,"Robert",1]]`

`Employees`:

| employee_id | employee_name | manager_id |
|---:|---|---:|
| 1 | Boss | 1 |
| 3 | Alice | 3 |
| 2 | Bob | 1 |
| 4 | Daniel | 2 |
| 7 | Luis | 4 |
| 8 | Jhon | 3 |
| 9 | Angela | 8 |
| 77 | Robert | 1 |

- **Output:** `[[2],[77],[4],[7]]`

Result:

| employee_id |
|---:|
| 2 |
| 77 |
| 4 |
| 7 |

- **Explanation:** Employee `1` is the company head. Employees `2` and `77` report directly to the head. Employee `4` reaches the head through `4 -> 2 -> 1`, while employee `7` reaches the head through `7 -> 4 -> 2 -> 1`. Employees `3`, `8`, and `9` belong to a separate reporting hierarchy, so none of them reports to employee `1` directly or indirectly.
