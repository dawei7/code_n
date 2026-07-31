# Find Overlapping Shifts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3262 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-overlapping-shifts/) |

## Problem Description

### Goal

The `EmployeeShifts` table records work shifts on one date. Each row contains an employee identifier together with that shift's start and end times, and the pair `(employee_id, start_time)` is unique.

For every employee, count the pairs of that employee's shifts that overlap. When the shifts are ordered by start time, a pair overlaps exactly when the earlier shift ends later than the later shift begins. Equality does not count: one shift ending at the instant another starts is merely adjacent.

Return only employees who have at least one overlapping pair. Name the count `overlapping_shifts` and order the result by `employee_id` in ascending order.

### Function Contract

**Inputs**

- `EmployeeShifts`: A table with integer `employee_id` and time-valued `start_time` and `end_time` columns. `(employee_id, start_time)` uniquely identifies a row.

Let $m$ be the number of shift rows.

**Return value**

- A table with columns `employee_id` and `overlapping_shifts`.
- `overlapping_shifts` is the number of distinct overlapping shift pairs for that employee.
- Employees with a zero count are omitted, and the remaining rows are ordered by `employee_id` ascending.

### Examples

**Example 1**

- Input: Employee 1 works `08:00-12:00`, `11:00-15:00`, and `14:00-18:00`; employee 2 works `09:00-17:00` and `16:00-20:00`; employee 3 has three separated shifts; employee 4 works `08:00-10:00` and `09:00-11:00`.
- Output: `[[1,2],[2,1],[4,1]]`

Employee 1 has two overlapping pairs, employees 2 and 4 have one each, and employee 3 is omitted.

**Example 2**

- Input: One employee has shifts `08:00-10:00`, `10:00-12:00`, and `12:00-14:00`.
- Output: `[]`

Every pair only touches at an endpoint or is separated, so none overlaps.

**Example 3**

- Input: One employee has nested shifts `08:00-18:00`, `09:00-17:00`, and `10:00-16:00`.
- Output: `[[1,3]]`

All three possible pairs overlap.
