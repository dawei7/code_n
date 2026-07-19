# Project Employees II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1076 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/project-employees-ii/) |

## Problem Description

### Goal

The `Project` table records employee assignments to projects. Its composite primary key is `(project_id, employee_id)`, so one employee appears at most once within a particular project, although the same employee may work on several projects. The related `Employee` table stores each employee's name and experience years.

Find the project or projects that have the greatest number of assigned employees. Return the `project_id` for every project tied at that maximum; no tied project may be omitted. The result rows may be returned in any order.

### Function Contract

**Inputs**

- `Project(project_id, employee_id)`: $R$ assignment rows with composite primary key `(project_id, employee_id)`.
- `Employee(employee_id, name, experience_years)`: employee details keyed by `employee_id`; these attributes are not needed to count assignments.

**Return value**

- One column named `project_id`.
- One row for each project whose assignment count equals the maximum assignment count among all projects.
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

Output:

| project_id |
|---:|
| 1 |

Project 1 has three assigned employees, which is more than project 2's two.
