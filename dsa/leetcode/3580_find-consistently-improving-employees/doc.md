# Find Consistently Improving Employees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3580 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-consistently-improving-employees/) |

## Problem Description

### Goal

An employee table stores each employee's identifier and name. A performance-review table records dated ratings from `1` through `5` for those employees.

Find employees who have at least three reviews and whose three most recent ratings improve strictly from the oldest of those three reviews to the newest. Reviews older than the latest three do not affect eligibility.

For every qualifying employee, calculate `improvement_score` as the newest rating minus the oldest rating among those three reviews. Return the employee identifier, name, and score, ordered by decreasing score and then increasing employee name.

### Function Contract

**Inputs**

- `employees`: A table keyed by `employee_id`, with the employee's `name`.
- `performance_reviews`: A table keyed by `review_id`, with `employee_id`, `review_date`, and integer `rating` from `1` through `5`.

**Return value**

Return columns `employee_id`, `name`, and `improvement_score` for employees whose last three chronologically ordered ratings are strictly increasing. Sort by `improvement_score` descending and `name` ascending.

### Examples

**Example 1**

- Input: Five employees with review histories of varying lengths and trends.
- Output: Bob Smith with score `3`, followed by Alice Johnson and Carol Davis with score `2`.
- Explanation: Each included employee's latest three ratings rise strictly. David's ratings are flat, and Emma has only two reviews.

---
