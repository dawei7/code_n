# Project Employees I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1075 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [project-employees-i](https://leetcode.com/problems/project-employees-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/project-employees-i/).

### Goal
For each project, report the average years of experience among employees assigned to that project, rounded to two decimal places.

### Query Contract
**Input tables**

- `Project(project_id, employee_id)`: Employee assignments to projects.
- `Employee(employee_id, name, experience_years)`: Employee details.

**Output columns**

- `project_id`
- `average_years`

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

| project_id | average_years |
|---:|---:|
| 1 | 2.00 |
| 2 | 2.50 |

---

## Solution
### Approach
Join `Project` with `Employee` on `employee_id`, group by `project_id`, and compute the rounded average of `experience_years`.

The rounding belongs in the projection so the output has exactly the required precision.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query joins project assignments with employee rows and groups by project.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
