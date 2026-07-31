# Design a Todo List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2590 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Design, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-a-todo-list/) |

## Problem Description

### Goal

Design a `TodoList` that lets multiple users add tasks, retrieve their unfinished work, filter unfinished tasks by tag, and mark owned tasks as complete. Every added task has a description, a globally unique due date, and zero or more tags.

Task IDs start at `1` and increase globally by one for each successful addition, regardless of user. Retrieval operations return task descriptions ordered by increasing due date and never include completed tasks. Completing a task changes state only when the requested task exists, belongs to the supplied user, and is still unfinished; every other completion request does nothing.

### Function Contract

**Inputs**

- `commands`: An operation sequence beginning with `TodoList`, followed by `addTask`, `getAllTasks`, `getTasksForTag`, or `completeTask` calls.
- `inputs`: Argument lists aligned with `commands`. Construction receives `[]`; the four methods receive their arguments in the order declared below.

The native methods are:

- `addTask(userId, taskDescription, dueDate, tags)`: Store the task and return its sequential task ID.
- `getAllTasks(userId)`: Return all unfinished descriptions owned by the user in due-date order.
- `getTasksForTag(userId, tag)`: Return the user's unfinished descriptions containing `tag`, also in due-date order.
- `completeTask(userId, taskId)`: Mark the matching owned unfinished task complete, if it exists.

All numeric arguments lie between $1$ and $100$. Descriptions have length from $1$ through $50$; tags and tag queries have length from $1$ through $20$ and use only English letters and digits. Each method is called at most $100$ times. Let $q$ be the number of method calls and let $S$ be the total number of stored tag associations.

**Return value**

- A list aligned with `commands`. Construction and `completeTask` contribute `null`; additions contribute task IDs; retrieval calls contribute description lists.

### Examples

**Example 1**

- Input: `commands = ["TodoList","addTask","addTask","getAllTasks","getAllTasks","addTask","getTasksForTag","completeTask","completeTask","getTasksForTag","getAllTasks"]`, `inputs = [[],[1,"Task1",50,[]],[1,"Task2",100,["P1"]],[1],[5],[1,"Task3",30,["P1"]],[1,"P1"],[5,1],[1,2],[1,"P1"],[1]]`
- Output: `[null,1,2,["Task1","Task2"],[],3,["Task3","Task2"],null,null,["Task3"],["Task3","Task1"]]`

The invalid completion by user `5` has no effect. Completing task `2` for its owner removes that task from later results.
