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

### Required Complexity

- **Time:** $O(E+R\log R)$
- **Space:** $O(E+R)$

<details>
<summary>Approach</summary>

#### General

**Attach experience before comparing assignments:** Join `Project` with `Employee` on `employee_id`. Each assignment then carries the experience value that must be compared only with other assignments in the same project.

**Rank within each project:** Apply `DENSE_RANK()` partitioned by `project_id` and ordered by `experience_years` descending. The greatest value receives rank one. Dense rank deliberately assigns the same rank to equal experience values, so it does not discard tied employees.

**Keep the complete top rank:** Select every row whose computed rank is one and return only `project_id` and `employee_id`. For each project, no employee with smaller experience can receive rank one, while every employee whose experience equals the project maximum does receive rank one. The filter therefore returns exactly the required employees for every project.

#### Complexity detail

A hash join can build an $E$-row employee lookup and attach experience in expected $O(E+R)$ time. Partitioning and ordering the $R$ joined assignments for the window function takes $O(R\log R)$ time in a sort-based plan. The join state, sorted rows, and window result use up to $O(E+R)$ execution space; indexes and the optimizer may alter the physical plan.

#### Alternatives and edge cases

- **Grouped maximum then join back:** Compute `MAX(experience_years)` per project and join that result to the assignments. It is also efficient and naturally preserves ties, but requires a second relational step to recover employee identifiers.
- **Correlated project maximum:** Recompute the maximum for each assignment. It is correct but can repeatedly rescan assignments and approach quadratic time.
- **`ROW_NUMBER()`:** It arbitrarily chooses one row among equal experience values and is incorrect when the maximum is tied.
- **Tied experience:** Every employee tied at the project maximum must appear.
- **Employee on several projects:** The employee is ranked independently within each project's partition.
- **Single assignment:** That employee is necessarily the most experienced for the project.
- **Employee name:** Names do not participate in either the join identity or the experience comparison.

</details>
