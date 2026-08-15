# Employees With Deductions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2394 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/employees-with-deductions/) |

## Problem Description

### Goal

The `Employees` table gives every employee's monthly work requirement in
whole hours. The `Logs` table records zero or more work sessions for an
employee, using the session's starting and ending timestamps. Every timestamp
is in October 2022, although a session that begins before midnight may end on
the following day.

Compute each session's duration in minutes and round that session upward
independently whenever any seconds remain. Add the rounded session durations
for each employee. Report the identifiers of employees whose total is less
than their required number of hours; this must include an employee with no
logged sessions. The result rows may be returned in any order.

### Function Contract

**Input tables**

- `Employees(employee_id, needed_hours)`: One row per employee;
  `employee_id` is unique and `needed_hours` is the minimum monthly work
  requirement in hours.
- `Logs(employee_id, in_time, out_time)`: Work sessions identified by the
  composite primary key `(employee_id, in_time, out_time)`. Each `out_time` is
  later than its `in_time` and may fall on the next calendar day.

Let $E$ be the number of employees and $L$ the number of logged sessions.

**Return value**

Return a one-column table named `employee_id`. It contains exactly those
employees whose sum of individually rounded-up session durations is less than
`needed_hours * 60`. Employees without logs have a total of zero. Row order is
unrestricted.

### Examples

#### Example 1

Employee 1 records sessions of 8 hours, 8 hours 4 minutes, and 4 hours
1 minute after the required per-session rounding. The resulting 20 hours
5 minutes meets a 20-hour requirement. Employee 2 records only 11 hours
59 minutes against a 12-hour requirement, while employee 3 has no sessions:

| employee_id |
|---:|
| 2 |
| 3 |

#### Example 2

Two sessions lasting 30 minutes 1 second each are rounded separately to
31 minutes. Their combined credited duration is therefore 62 minutes, which
meets a one-hour requirement, so that employee is not returned.
