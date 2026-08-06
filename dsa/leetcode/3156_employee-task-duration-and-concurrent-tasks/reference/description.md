## Description

The `Tasks` table records work intervals. Each row identifies a task and employee together with the task's start and end timestamps. The pair (`task_id`, `employee_id`) uniquely identifies a row.

For every employee, report two measures. First, find the total amount of time covered by at least one of that employee's tasks, counting overlapping time only once, and round this duration down to a whole number of hours. Second, find the greatest number of the employee's tasks active concurrently at any point. Treat intervals as half-open: a task that starts exactly when another ends does not overlap the ending task.

Return one row per employee, ordered by `employee_id` in ascending order.
