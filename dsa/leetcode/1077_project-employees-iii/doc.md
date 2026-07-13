# Project Employees III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1077 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [project-employees-iii](https://leetcode.com/problems/project-employees-iii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/project-employees-iii/).

### Goal
For each project, report the employee or employees assigned to that project who have the greatest experience.

### Query Contract
**Input tables**

- `Project(project_id, employee_id)`: Employee assignments to projects.
- `Employee(employee_id, name, experience_years)`: Employee details.

**Output columns**

- `project_id`
- `employee_id`

### Examples
**Example 1**

`Project`

| project_id | employee_id |
|---:|---:|
| 1 | 1 |
| 1 | 2 |
| 1 | 3 |
| 2 | 1 |
| 2 | 4 |

`Employee`

| employee_id | name | experience_years |
|---:|---|---:|
| 1 | Khaled | 3 |
| 2 | Ali | 2 |
| 3 | John | 1 |
| 4 | Doe | 2 |

Output:

| project_id | employee_id |
|---:|---:|
| 1 | 1 |
| 2 | 1 |

---

## Solution
### Approach
Join assignments to employee details, then rank employees within each project by `experience_years` descending. Keep every row with rank `1`, so ties for most experience are preserved.

The same logic can also be expressed by comparing each employee's experience with the maximum experience for that project.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query joins assignments with employees and computes a per-project maximum or rank.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
