## Examples

**Example 1**

- **Input:** `Tasks = [[1, 3], [2, 2], [3, 4]], Executed = [[1, 2], [3, 1], [3, 2], [3, 3], [3, 4]]`

`Tasks` table:

| task_id | subtasks_count |
|---:|---:|
| 1 | 3 |
| 2 | 2 |
| 3 | 4 |

`Executed` table:

| task_id | subtask_id |
|---:|---:|
| 1 | 2 |
| 3 | 1 |
| 3 | 2 |
| 3 | 3 |
| 3 | 4 |

- **Output:** `[[1, 1], [1, 3], [2, 1], [2, 2]]`

| task_id | subtask_id |
|---:|---:|
| 1 | 1 |
| 1 | 3 |
| 2 | 1 |
| 2 | 2 |

- **Explanation:**
  - Task 1: has 3 subtasks (1, 2, 3). Executed subtask 2. Missing subtasks: 1, 3.
  - Task 2: has 2 subtasks (1, 2). Executed subtasks: none. Missing subtasks: 1, 2.
  - Task 3: has 4 subtasks (1, 2, 3, 4). Executed all 4 subtasks. Missing subtasks: none.
  - Ordered by `task_id` ASC, `subtask_id` ASC.

**Example 2**

- **Input:** `Tasks = [[8, 1]], Executed = []`
- **Output:** `[[8, 1]]`

- **Explanation:** Task 8 has 1 subtask, and no subtasks executed, so `(8, 1)` is returned.

**Example 3**

- **Input:** `Tasks = [[5, 3]], Executed = [[5, 1], [5, 2], [5, 3]]`
- **Output:** `[]`

- **Explanation:** All valid subtasks for task 5 executed, producing an empty result table.
