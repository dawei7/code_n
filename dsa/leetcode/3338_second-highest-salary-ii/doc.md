# Second Highest Salary II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3338 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/second-highest-salary-ii/) |

## Problem Description

### Goal

The `employees` table records each employee's identifier, salary, and department. For every department, determine its second-highest **distinct** salary. Return every employee earning that salary; if several employees tie at the second level, none of them may be discarded.

A department contributes no row when it has fewer than two distinct salary values, even if it contains several employees tied at its only salary. Report only the employee identifier and department, and order the complete result by `emp_id` in ascending order across all departments.

### Function Contract

**Inputs**

Table `employees`:

- `emp_id`: An integer that uniquely identifies an employee.
- `salary`: The employee's integer salary.
- `dept`: The employee's department as a `varchar` value.

Let $n$ be the number of rows in `employees`.

**Return value**

Return columns `emp_id` and `dept` for all employees whose salary is the second-highest distinct salary in their department. Order rows by `emp_id ASC`.

### Examples

**Example 1**

Input table:

| emp_id | salary | dept |
|---:|---:|---|
| 1 | 70000 | Sales |
| 2 | 80000 | Sales |
| 3 | 80000 | Sales |
| 4 | 90000 | Sales |
| 5 | 55000 | IT |
| 6 | 65000 | IT |
| 7 | 65000 | IT |
| 8 | 50000 | Marketing |
| 9 | 55000 | Marketing |
| 10 | 55000 | HR |

Output:

| emp_id | dept |
|---:|---|
| 2 | Sales |
| 3 | Sales |
| 5 | IT |
| 8 | Marketing |

Sales has two employees tied at its second-highest distinct salary, so both appear. HR has only one distinct salary and contributes no row.
