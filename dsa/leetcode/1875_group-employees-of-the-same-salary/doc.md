# Group Employees of the Same Salary

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/group-employees-of-the-same-salary/) |
| Frontend ID | 1875 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `Employees` table records a unique identifier, name, and salary for every employee. Form teams by salary: a team must contain at least two employees, every employee with a given repeated salary belongs to the same team, and an employee whose salary occurs only once is omitted entirely.

Assign team identifiers by increasing team salary. The lowest salary that forms a team receives `team_id = 1`, the next repeated salary receives `team_id = 2`, and so on without gaps. Unique salaries do not participate in this ranking. Return every team member with their original employee data and team identifier, ordered first by `team_id` and then by `employee_id`, both ascending.

### Function Contract

**Inputs**

- `Employees(employee_id, name, salary)`: one row per employee; `employee_id` is unique.
- Let $R$ be the number of employees.

**Return value**

- Return `employee_id`, `name`, `salary`, and `team_id`.
- Include all and only employees whose salary occurs at least twice.
- Give equal salaries one team identifier; rank only repeated salaries from lowest to highest starting at one.
- Order by `team_id`, then `employee_id`, ascending.

### Examples

**Example 1**

- Input: `(2,"Meir",3000)`, `(3,"Michael",3000)`, `(7,"Addilyn",7400)`, `(8,"Juan",6100)`, `(9,"Kannon",7400)`
- Output: `[[2,"Meir",3000,1],[3,"Michael",3000,1],[7,"Addilyn",7400,2],[9,"Kannon",7400,2]]`

Salary `6100` is unique and omitted; it also creates no gap in team numbering.

**Example 2**

- Input: salaries `[100,200,100,200,300]` for employee IDs `1` through `5`
- Output: employees `1,3` in team `1`, followed by employees `2,4` in team `2`

**Example 3**

- Input: three employees with distinct salaries
- Output: `[]`

No salary has enough employees to form a team.
