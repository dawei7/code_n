# Employee Task Duration and Concurrent Tasks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3156 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/employee-task-duration-and-concurrent-tasks/) |

## Problem Description
### Goal
The `Tasks` table records work intervals. Each row identifies a task and employee together with the task's start and end timestamps. The pair (`task_id`, `employee_id`) uniquely identifies a row.

For every employee, report two measures. First, find the total amount of time covered by at least one of that employee's tasks, counting overlapping time only once, and round this duration down to a whole number of hours. Second, find the greatest number of the employee's tasks active concurrently at any point. Treat intervals as half-open: a task that starts exactly when another ends does not overlap the ending task.

Return one row per employee, ordered by `employee_id` in ascending order.

### Function Contract
**Inputs**

- `Tasks`: A table with integer columns `task_id` and `employee_id` plus `DATETIME` columns `start_time` and `end_time`. (`task_id`, `employee_id`) is the primary key.

Each row represents one task interval for its employee. Input row order has no semantic meaning.

**Return value**

Return a table with columns `employee_id`, `total_task_hours`, and `max_concurrent_tasks`. The duration column is the floor of the employee's union task duration measured in hours, and the concurrency column is the maximum number of simultaneously active tasks. Sort rows by `employee_id` ascending.

### Examples
**Example 1**

For employee 1001, tasks cover 08:00–10:30, 11:00–12:00, and 13:00–15:30 after overlaps are merged. For employee 1002, two overlapping tasks cover 09:00–11:30. Employee 1003 has one task from 14:00–16:00.

| employee_id | total_task_hours | max_concurrent_tasks |
|---:|---:|---:|
| 1001 | 6 | 2 |
| 1002 | 2 | 2 |
| 1003 | 2 | 1 |

**Example 2**

Two tasks for one employee cover 08:00–09:00 and 09:00–10:00. They touch but do not overlap, so the result is `total_task_hours = 2` and `max_concurrent_tasks = 1`.

**Example 3**

Three tasks share the exact interval 08:00–10:00. Their union lasts two hours and all three are active together, producing `total_task_hours = 2` and `max_concurrent_tasks = 3`.
