## Description

Table: `Tasks`

```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| task_id        | int     |
| subtasks_count | int     |
+----------------+---------+
task_id is the column with unique values for this table.
Each row in this table indicates that task_id was divided into subtasks_count subtasks labeled from 1 to subtasks_count.
It is guaranteed that 2 <= subtasks_count <= 20.
```

Table: `Executed`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| task_id       | int     |
| subtask_id    | int     |
+---------------+---------+
(task_id, subtask_id) is the combination of columns with unique values for this table.
Each row in this table indicates that for the task task_id, the subtask with ID subtask_id was executed successfully.
It is **guaranteed** that subtask_id <= subtasks_count for each task_id.
```

Write a solution to report the IDs of the missing subtasks for each $\text{task}_{id}$.

Return the result table in **any order**.

The result format is in the following example.
### Function Contract

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

### Examples
#### Example 1

```
**Input:**
Tasks table:
+---------+----------------+
| task_id | subtasks_count |
+---------+----------------+
| 1       | 3              |
| 2       | 2              |
| 3       | 4              |
+---------+----------------+
Executed table:
+---------+------------+
| task_id | subtask_id |
+---------+------------+
| 1       | 2          |
| 3       | 1          |
| 3       | 2          |
| 3       | 3          |
| 3       | 4          |
+---------+------------+
**Output:**
+---------+------------+
| task_id | subtask_id |
+---------+------------+
| 1       | 1          |
| 1       | 3          |
| 2       | 1          |
| 2       | 2          |
+---------+------------+
**Explanation:**
Task 1 was divided into 3 subtasks (1, 2, 3). Only subtask 2 was executed successfully, so we include (1, 1) and (1, 3) in the answer.
Task 2 was divided into 2 subtasks (1, 2). No subtask was executed successfully, so we include (2, 1) and (2, 2) in the answer.
Task 3 was divided into 4 subtasks (1, 2, 3, 4). All of the subtasks were executed successfully.
```