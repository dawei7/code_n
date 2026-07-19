# Find the Subtasks That Did Not Execute

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1767 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-subtasks-that-did-not-execute/) |

## Problem Description

### Goal

The `Tasks` table records how many subtasks belong to each task. If a task has `subtasks_count = c`, its valid subtask identifiers are every integer from `1` through `c`, inclusive.

The `Executed` table records the task and subtask pairs that actually ran. Find every valid pair that has no corresponding execution record.

Return the missing pairs ordered first by `task_id` and then by `subtask_id`, both in ascending order.

### Function Contract

**Inputs**

- `Tasks(task_id, subtasks_count)`: one row per task; `task_id` is unique and `subtasks_count` is positive.
- `Executed(task_id, subtask_id)`: one row per executed subtask; each pair is unique and refers to a valid subtask of its task.

Let

$$
T=\sum_{\text{task row }r}\texttt{r.subtasks\_count}
$$

be the total number of valid task-subtask pairs.

**Return value**

- Return a table with columns `task_id` and `subtask_id`.
- Include exactly the valid pairs absent from `Executed`.
- Order rows by `task_id` ascending and then `subtask_id` ascending.

### Examples

**Example 1**

- Input: tasks `(1,3)`, `(2,2)`, and `(3,4)`; executed pairs `(1,2)` and every subtask of task `3`.
- Output: `(1,1)`, `(1,3)`, `(2,1)`, `(2,2)`.
- Explanation: Task `1` is missing two of its three subtasks, task `2` is missing both, and task `3` is complete.

**Example 2**

- Input: task `(8,1)` and no executed rows.
- Output: `(8,1)`.
- Explanation: The task's only valid subtask did not execute.

**Example 3**

- Input: task `(5,3)` with executed pairs `(5,1)`, `(5,2)`, and `(5,3)`.
- Output: an empty table.
- Explanation: Every valid subtask has an execution record.
