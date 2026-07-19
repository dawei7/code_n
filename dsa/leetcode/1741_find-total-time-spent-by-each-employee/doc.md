# Find Total Time Spent by Each Employee

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1741 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-total-time-spent-by-each-employee/) |

## Problem Description

### Goal

The `Employees` table records office visits. Each row identifies an employee and calendar day, along with the minute when that visit began and the later minute when it ended. The combination `(emp_id, event_day, in_time)` is unique. Visit intervals belonging to the same day never overlap, although an employee may enter and leave several times that day.

For every employee-day pair represented in the table, calculate the total number of minutes the employee spent in the office. One visit contributes `out_time - in_time` minutes. Return the day as `day`, the employee identifier, and the summed duration as `total_time`; result rows may appear in any order.

### Function Contract

**Inputs**

- `Employees(emp_id, event_day, in_time, out_time)`: office visit rows with $1 \le \texttt{in_time} < \texttt{out_time} \le 1440$ and nonintersecting same-day intervals.

Let $R$ be the number of visit rows and $G$ the number of distinct `(event_day, emp_id)` groups.

**Return value**

- Return a table with columns `day`, `emp_id`, and `total_time`.
- Include one row per distinct employee-day pair, where `total_time` is the sum of `out_time - in_time` over that group's visits.

### Examples

**Example 1**

- Input: employee `1` visits on `2020-11-28` during minutes `4..32` and `55..200`.
- Output: `("2020-11-28", 1, 173)`
- Explanation: The two durations are $28$ and $145$ minutes, totaling $173$.

**Example 2**

- Input: employee `1` has one visit on `2020-12-03` from minute `1` to minute `42`.
- Output: `("2020-12-03", 1, 41)`
- Explanation: A group containing one visit keeps that visit's duration.

**Example 3**

- Input: employees `1` and `2` each visit on `2020-11-28`.
- Output: one independently aggregated row for each employee.
- Explanation: Sharing a day does not combine different employee identifiers.
