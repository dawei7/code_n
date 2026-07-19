# The Number of Employees Which Report to Each Employee

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1731 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/) |

## Problem Description

### Goal

The `Employees` table contains one row per employee. Besides the employee's identifier, name, and age, a row may store the identifier of the manager to whom that employee reports. A null `reports_to` value means that the employee does not report to anyone.

For this task, an employee is a manager only when at least one other employee reports directly to them. Return every such manager's identifier and name, the number of direct reports, and the direct reports' average age rounded to the nearest integer. Indirect descendants in the reporting hierarchy do not contribute. Order the result by `employee_id`.

### Function Contract

**Inputs**

- `Employees(employee_id, name, reports_to, age)`: `employee_id` is unique; `reports_to` is either another employee identifier or null.

Let $E$ be the number of employee rows and $M$ the number of employees having at least one direct report.

**Return value**

- Return a table with columns `employee_id`, `name`, `reports_count`, and `average_age`.
- Include one row per manager, with `average_age` rounded to the nearest integer, ordered by `employee_id` in ascending order.

### Examples

**Example 1**

- Input: Hercy (`9`, age `43`) has direct reports Alice (age `41`) and Bob (age `36`); Winston reports to nobody.
- Output: `(9, "Hercy", 2, 39)`
- Explanation: Hercy's direct reports average $(41 + 36) / 2 = 38.5$, which rounds to $39$.

**Example 2**

- Input: Michael manages Alice and Bob; Alice manages Charlie and David; Bob manages Eve.
- Output: Michael with `(2, 40)`, Alice with `(2, 37)`, and Bob with `(1, 37)`, in employee-ID order.
- Explanation: Each manager's count and average use only that manager's immediate reports.

**Example 3**

- Input: employee `20` reports to employee `10`, and employee `30` reports to employee `20`.
- Output: one row for employee `10` based only on employee `20`, and one row for employee `20` based only on employee `30`.
- Explanation: The grandchild employee `30` is not included in employee `10`'s aggregate.
