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

### Required Complexity

- **Time:** $O(R\log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Identify only salaries that can form teams**

Group `Employees` by `salary` and count each group. Retain salaries whose count exceeds one. Joining this compact relation back to `Employees` removes unique-salary employees while preserving every member of each valid team and their original columns.

**Number the filtered salary groups**

Apply `DENSE_RANK()` ordered by salary to the filtered employee rows. Equal salary values receive the same rank, and the next distinct repeated salary receives the next integer. Because filtering happens before the window function, unique salaries do not consume ranks.

**Produce the contractual row order**

Order by the calculated `team_id` and then `employee_id`. This groups each team together in increasing salary order and makes member ordering deterministic.

#### Complexity detail

Hash grouping and joining can process the $R$ rows in $O(R)$ expected work. Ranking and producing the required order may sort the eligible rows, yielding $O(R\log R)$ total time in the general plan. Group state, join state, window state, sorting workspace, and returned rows use $O(R)$ space. Existing salary and identifier indexes may reduce physical sorting work.

#### Alternatives and edge cases

- **Correlated count per employee:** It is correct but can rescan the table for every row and degrade to $O(R^2)$.
- **Self-join on equal salary:** It can detect teammates, but every employee may match several peers and requires deduplication.
- **`RANK()` instead of `DENSE_RANK()`:** `RANK()` would create gaps based on team size; team IDs must be consecutive across salaries.
- **Unique salary between teams:** It is omitted and consumes no team ID.
- **Team larger than two:** Every member receives the same identifier.
- **Several repeated salaries:** Their numeric salary order, not discovery order, controls team IDs.
- **Output order:** Members are ordered by employee ID within each team.

</details>
