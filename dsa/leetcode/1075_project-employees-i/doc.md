# Project Employees I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1075 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/project-employees-i/) |

## Problem Description

### Goal

The `Project` table records which employees work on which projects and uses `(project_id, employee_id)` as its composite primary key. Each `employee_id` refers to one row in `Employee`, which supplies the employee's name and non-null number of experience years.

For every project represented in `Project`, report the average experience years of all employees assigned to it. Return `project_id` and the average under the name `average_years`, rounded to two decimal places. Result rows may be returned in any order.

### Function Contract

**Inputs**

- `Project(project_id, employee_id)`: $R$ assignment rows with composite primary key `(project_id, employee_id)`.
- `Employee(employee_id, name, experience_years)`: $E$ employee rows keyed by `employee_id`; `experience_years` is not null.

**Return value**

- Columns `project_id` and `average_years`.
- One row per project, with the arithmetic mean of its assigned employees' `experience_years` rounded to two decimal places.
- Result order is unrestricted; the local reference orders by `project_id` for deterministic validation.

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

Project 1 averages `(3 + 2 + 1) / 3 = 2.00`, while project 2 averages `(3 + 2) / 2 = 2.50`.
