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

### Required Complexity

- **Time:** $O(R\log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Count at project grain:** Group `Project` by `project_id` and compute `COUNT(*)` for each group. Because `(project_id, employee_id)` is a primary key, every row represents one distinct employee assignment within that project. Joining `Employee` would add no information needed for this count.

**Compare every count with one maximum:** Materialize the grouped results as `project_counts`. A scalar subquery takes `MAX(employee_count)` over that compact relation, and the outer query retains every row whose count equals it. Equality, rather than choosing one row with `LIMIT 1`, is what preserves ties.

Every returned project has a count equal to the maximum by the filter. Every project achieving that maximum satisfies the same equality and is therefore returned, so the result contains exactly all projects with the largest workforce. Ordering by `project_id` affects only deterministic local presentation.

#### Complexity detail

Let $R$ be the number of rows in `Project`. A sort-based grouping and final ordering take $O(R\log R)$ time and up to $O(R)$ execution space. Hash aggregation can make the grouping phase expected $O(R)$, while indexes and the optimizer may choose other physical plans.

#### Alternatives and edge cases

- **Dense rank over grouped counts:** Apply `DENSE_RANK()` in descending count order and keep rank one. It preserves ties but introduces a window step when a maximum comparison is sufficient.
- **Correlated count per assignment:** Count the matching project rows separately for every source row and then deduplicate. It is correct but can rescan `Project` repeatedly and approach quadratic time.
- **`ORDER BY COUNT(*) DESC LIMIT 1`:** It returns only one project and is incorrect when several projects share the maximum.
- **Tied maximum:** Every tied `project_id` must appear once in the output.
- **Employee shared across projects:** Each assignment belongs to its own project and counts once in each corresponding group.
- **Employee attributes:** Names and experience years do not affect which project has the most assignments.

</details>
