## Description

The `Tasks` table records how many subtasks belong to each task. If a task has `subtasks_count = c`, its valid subtask identifiers are every integer from `1` through `c`, inclusive.

The `Executed` table records the task and subtask pairs that actually ran. Find every valid pair that has no corresponding execution record.

Return the missing pairs ordered first by `task_id` and then by `subtask_id`, both in ascending order.
