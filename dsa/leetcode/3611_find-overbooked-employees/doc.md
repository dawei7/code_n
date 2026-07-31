# Find Overbooked Employees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3611 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-overbooked-employees/) |

## Problem Description
### Goal

The `employees` table identifies each employee by name and department. The `meetings` table records meetings attended by employees, including each meeting's date, type, and duration in hours. A standard working week contains 40 hours.

Treat each calendar week as Monday through Sunday and total every employee's meeting duration within that week. A week is meeting-heavy only when its total is strictly greater than 20 hours, which is more than half of the standard work week. Count each employee's meeting-heavy weeks and keep employees whose count is at least two.

Return the qualifying employees with their identity, department, and meeting-heavy-week count. Sort larger counts first, then sort equal counts by employee name in ascending order.

### Function Contract

**Inputs**

- `employees`: rows with unique `employee_id`, `employee_name`, and `department` values.
- `meetings`: rows with unique `meeting_id`, an `employee_id`, `meeting_date`, `meeting_type`, and `duration_hours`.

Every meeting describes attendance by one employee. Meeting types may be `Team`, `Client`, or `Training`; all types contribute equally to the weekly duration.

**Return value**

Return an ordered table with columns `employee_id`, `employee_name`, `department`, and `meeting_heavy_weeks`. Include only employees with at least two Monday–Sunday weeks totaling more than 20 meeting hours each.

### Examples

**Example 1**

Alice has 21 meeting hours in each of two consecutive weeks, so her `meeting_heavy_weeks` value is `2` and she qualifies.

**Example 2**

Bob has 23 meeting hours in one week but only 10 in the next. He is excluded because only one week exceeds 20 hours.

**Example 3**

Two weekly totals of exactly 20 hours do not qualify because the threshold is strict. A total must be greater than 20.
