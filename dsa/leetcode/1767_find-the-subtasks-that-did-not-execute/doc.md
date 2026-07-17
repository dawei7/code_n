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

### Required Complexity

- **Time:** $O(T)$
- **Space:** $O(T)$

<details>
<summary>Approach</summary>

#### General

**Generate each task's complete subtask domain**

Begin a recursive common table expression with subtask `1` for every row of `Tasks`. Retain `subtasks_count` in the recursive state, then repeatedly increment `subtask_id` while it remains below that task's count. Each task therefore produces exactly its legal identifiers and cannot cross into another task's range.

**Let all task sequences advance independently**

The recursive member operates on every current row of the common table expression. A task with a small count stops when it reaches its own limit, while larger tasks continue producing rows. After recursion finishes, the relation contains each of the $T$ possible `(task_id, subtask_id)` pairs once.

**Exclude pairs that have execution evidence**

For each generated pair, use `NOT EXISTS` to test for a matching row in `Executed` on both columns. A composite-key lookup succeeds precisely for executed work, so retaining only failed lookups yields exactly the missing subtasks. This form also expresses the anti-join directly without relying on nullable data columns.

**Specify the requested output order**

Sort the remaining rows by `task_id` and `subtask_id`. Recursive production order is an implementation detail and cannot replace an explicit `ORDER BY`.

Every output row comes from a task's inclusive range and lacks a matching execution record, so it is a valid missing subtask. Conversely, recursion generates every valid pair, and any pair not executed survives the anti-join; therefore no required row is omitted.

#### Complexity detail

The recursive relation creates exactly $T$ rows. With the unique executed-pair key, each anti-join probe takes constant expected or indexed time, so enumeration and filtering take $O(T)$ time. The recursive intermediate relation and result can contain $O(T)$ rows, giving $O(T)$ space. Since every executed row represents one of these valid pairs, its count is at most $T$.

#### Alternatives and edge cases

- **Fixed numbers table:** Joining `Tasks` to a permanent sequence table is efficient and avoids recursion, but assumes that auxiliary table exists in the submission environment.
- **Hard-coded union of integers:** This only works for a known small maximum and is brittle when the supported subtask bound changes.
- **Left anti-join:** A `LEFT JOIN` followed by a null check on the executed key is equivalent when the key columns are non-null.
- **Task with no executions:** Every generated subtask for that task must appear.
- **Task fully executed:** All of its generated pairs are removed, contributing no rows.
- **Gaps between executed IDs:** Missing identifiers need not form one interval; each absent pair is returned independently.
- **Several tasks:** Subtask identifiers restart at `1` for every task.
- **Unsorted source rows:** Input storage order does not affect the explicitly sorted result.

</details>
