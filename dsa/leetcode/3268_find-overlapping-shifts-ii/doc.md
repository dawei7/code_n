# Find Overlapping Shifts II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3268 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-overlapping-shifts-ii/) |

## Problem Description

### Goal

The `EmployeeShifts` table records employees' shift start and end datetimes. The pair `(employee_id, start_time)` uniquely identifies a shift. Two shifts for the same employee are eligible to overlap only when their start datetimes fall on the same date, and their time intervals intersect for positive duration. Merely touching at one endpoint is not an overlap.

For every employee, report the greatest number of eligible shifts active simultaneously at any instant. Also report the total overlap duration in minutes, summing the intersection duration of every overlapping shift pair. When three shifts share an interval, that interval contributes once for each of the three pairs.

Include employees who never overlap: their maximum is one and their total overlap duration is zero. Order the result by `employee_id` ascending.

### Function Contract

**Inputs**

- `EmployeeShifts`: A table with integer `employee_id` and datetime columns `start_time` and `end_time`. `(employee_id, start_time)` is unique.

Let $m$ be the number of shift rows.

**Return value**

- A table with columns `employee_id`, `max_overlapping_shifts`, and `total_overlap_duration`.
- `max_overlapping_shifts` is the largest simultaneous active-shift count within one employee and shift-start date.
- `total_overlap_duration` is the sum, in minutes, of all eligible pairwise intersections.
- Rows are ordered by `employee_id` ascending.

### Examples

**Example 1**

- Input: Employee 1 has shifts `09:00-17:00`, `15:00-23:00`, and `16:00-00:00`; employee 2 has `09:00-17:00` and `11:00-19:00`; employee 3 has one shift.
- Output: `[[1,3,600],[2,2,360],[3,1,0]]`

Employee 1 reaches three simultaneous shifts and its three pair intersections total ten hours.

**Example 2**

- Input: One employee has shifts `08:00-10:00` and `10:00-12:00` on the same date.
- Output: `[[1,1,0]]`

The endpoint equality creates no positive overlap.

**Example 3**

- Input: One employee has nested shifts `08:00-18:00`, `09:00-17:00`, and `10:00-16:00`.
- Output: `[[1,3,1200]]`

All three pairs overlap for 480, 360, and 360 minutes respectively.
