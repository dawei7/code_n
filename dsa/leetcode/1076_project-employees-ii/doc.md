# Project Employees II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1076 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [project-employees-ii](https://leetcode.com/problems/project-employees-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/project-employees-ii/).

### Goal
Report the project or projects that have the largest number of assigned employees.

### Query Contract
**Input table**

- `Project(project_id, employee_id)`: Employee assignments to projects.

**Output columns**

- `project_id`

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

Output:

| project_id |
|---:|
| 1 |

---

## Solution
### Approach
Count employees per `project_id`, then keep the project rows whose count equals the maximum count among all projects.

This can be done with a grouped subquery, a window rank over grouped counts, or a `HAVING COUNT(*) >= ALL (...)` style condition.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query groups all project-assignment rows.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
