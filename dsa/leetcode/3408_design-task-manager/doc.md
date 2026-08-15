# Design Task Manager

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3408 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Design, Heap (Priority Queue), Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-task-manager/) |

## Problem Description

### Goal

Build a task-management system shared by multiple users. Every active task has a globally unique task ID, an owning user, and a priority. The system must support adding tasks, changing an existing task's priority, removing a task, and executing the highest-ranked active task.

Execution first maximizes priority. If several tasks share that priority, the task with the greatest task ID wins. Executing a task removes it and returns its owner's user ID; execution on an empty system returns `-1`. One user may own multiple tasks, and a task ID that has been removed may later be added again.

### Function Contract

**Operations**

- `TaskManager(tasks)`: Initializes the system from `[userId, taskId, priority]` triples.
- `add(userId, taskId, priority)`: Adds a task whose ID is not currently active.
- `edit(taskId, newPriority)`: Replaces the priority of an active task without changing its owner.
- `rmv(taskId)`: Removes an active task.
- `execTop()`: Removes the task maximizing `(priority, taskId)` and returns its `userId`, or returns `-1` when no task remains.

The initial list contains between 1 and $10^5$ tasks. User and task IDs lie in $[0,10^5]$, priorities lie in $[0,10^9]$, and at most $2\cdot10^5$ method calls follow construction. Every operation that requires an existing or absent task ID satisfies that precondition.

**Return value**

For the app-local trace adapter, return one result per operation: `null` for construction, `add`, `edit`, and `rmv`; the owning user ID or `-1` for `execTop`.

### Examples

#### Example 1

- **Input:** `operations = ["TaskManager","add","edit","execTop","rmv","add","execTop"]`, `arguments = [[[[1,101,10],[2,102,20],[3,103,15]]],[4,104,5],[102,8],[],[101],[5,105,15],[]]`
- **Output:** `[null,null,null,3,null,null,5]`

After task 102 is reduced to priority 8, task 103 has the greatest priority and returns user 3. Task 101 is then removed; the newly added task 105 wins the final execution and returns user 5.

#### Example 2

- **Input:** `operations = ["TaskManager","execTop","execTop","execTop","execTop"]`, `arguments = [[[[1,10,5],[2,20,5],[3,15,6]]],[],[],[],[]]`
- **Output:** `[null,3,2,1,-1]`

Task 15 wins by priority. Tasks 20 and 10 then tie on priority, so the larger task ID executes first; the final call sees an empty manager.

#### Example 3

- **Input:** `operations = ["TaskManager","edit","add","execTop","execTop"]`, `arguments = [[[[1,1,5]]],[1,3],[2,2,8],[],[]]`
- **Output:** `[null,null,null,2,1]`

Editing task 1 leaves its old heap rank obsolete. Task 2 executes first at priority 8, followed by task 1 at its current priority 3.
