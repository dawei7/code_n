# Project Employees III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1077 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/project-employees-iii/) |

## Problem Description

### Goal

The `Project` table records the employees assigned to each project and uses `(project_id, employee_id)` as its composite primary key. Each assignment's `employee_id` refers to one row in `Employee`, where the employee's name and non-null number of experience years are stored.

For every project represented in `Project`, find the employee or employees with the greatest number of experience years among that project's assignees. Return each qualifying pair as `project_id` and `employee_id`. If several employees tie for the greatest experience on one project, include all of them. Result rows may be returned in any order.

### Function Contract

**Inputs**

- `Project(project_id, employee_id)`: $R$ assignment rows with composite primary key `(project_id, employee_id)`.
- `Employee(employee_id, name, experience_years)`: $E$ employee rows keyed by `employee_id`; `experience_years` is not null.

**Return value**

- Columns `project_id` and `employee_id`.
- For each project, one row for every assigned employee whose experience equals that project's maximum experience.
- Result order is unrestricted; the local reference orders by both output columns for deterministic validation.

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

Employee 1 has the greatest experience on both projects: three years versus two and one on project 1, and three versus two on project 2.
