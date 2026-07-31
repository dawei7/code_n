# Find Latest Salaries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2668 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database, Window Function |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-latest-salaries/) |

## Problem Description

### Goal

The `Salary` table stores one or more yearly salary records for each employee. Older rows may therefore contain amounts that are no longer current. Salaries are guaranteed to increase from year to year, so an employee's latest record is the row having that employee's greatest numeric salary.

Return one current row per employee with `emp_id`, `firstname`, `lastname`, `salary`, and `department_id`. Sort the result by `emp_id` in ascending order. Employees having only one stored record must still appear, because that row is already their latest salary.

### Function Contract

**Inputs**

- `Salary`: Rows with integer `emp_id` and text columns `firstname`, `lastname`, `salary`, and `department_id`. The pair `(emp_id, salary)` is unique.

Although `salary` is stored as text, comparison must follow its numeric value.

**Return value**

- Return columns `emp_id`, `firstname`, `lastname`, `salary`, and `department_id`, with one maximum-salary row per employee and rows ordered by increasing `emp_id`.

### Examples

**Example 1**

- Input: Employee 1 has salaries `110000` and `106119`; employee 2 has `128922` and `130000`; other employees likewise have one or more records.
- Output: Employee 1's row with `110000`, employee 2's row with `130000`, and the greatest numeric salary row for every remaining employee, ordered by ID.
- Explanation: Under the increasing-salary assumption, each maximum amount identifies the most recent record.
