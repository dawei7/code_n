## Function Contract

**Database Schemas**

**`Tasks`**

| Column | Type | Meaning |
|---|---|---|
| `task_id` | int | Unique task identifier. |
| `subtasks_count` | int | Total number of subtasks for the task (numbered 1..subtasks_count). |

**`Executed`**

| Column | Type | Meaning |
|---|---|---|
| `task_id` | int | Task identifier. |
| `subtask_id` | int | Subtask identifier that executed. |

- `(task_id, subtask_id)` in `Executed` is unique.

**Return value**

Return a table with columns `task_id` and `subtask_id`. Include every valid subtask `1 <= subtask_id <= subtasks_count` for each task that is absent from `Executed`. Sort the output by `task_id` ASC, `subtask_id` ASC.
