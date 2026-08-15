# Maximize Profit from Task Assignment

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3476 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-profit-from-task-assignment/) |

## Problem Description

### Goal

The integer array `workers` gives the skill level of every available worker. Each entry `tasks[i] = [required_skill, profit]` describes one task: its first value is the exact skill needed to perform it, and its second value is the profit earned if it is completed.

A regular worker may complete at most one task and is eligible only when the worker's skill is equal to that task's requirement. Every task can likewise be assigned at most once. In addition to the listed workers, one extra worker is available. This extra worker may complete any one task regardless of its required skill.

Choose which tasks to assign, which regular workers receive them, and which task—if any—is given to the extra worker. Return the maximum total profit obtainable from all completed tasks.

### Function Contract

**Inputs**

- `workers`: A list of $w$ integers, where each value is a regular worker's skill level.
- `tasks`: A list of $t$ pairs `[required_skill, profit]`.

The bounds are $1 \le w,t \le 10^5$. Every skill, requirement, and profit is between $1$ and $10^9$, inclusive. Let $a$ denote the number of tasks assigned to regular workers by an optimal assignment, so $0 \le a \le \min(w,t)$.

**Return value**

Return the maximum total profit as an integer. Each worker and each task may participate in at most one assignment; regular workers require exact skill equality, while the single extra worker ignores the skill requirement.

### Examples

#### Example 1

- **Input:** `workers = [1, 2, 3, 4, 5]`, `tasks = [[1, 100], [2, 400], [3, 100], [3, 400]]`
- **Output:** `1000`

The skill-1 and skill-2 workers earn `100` and `400`. The skill-3 worker takes one profit-`400` task, and the extra worker takes the other skill-3 task for `100`.

#### Example 2

- **Input:** `workers = [10, 10000, 100000000]`, `tasks = [[1, 100]]`
- **Output:** `100`

No regular worker has skill 1, but the extra worker can complete the only task.

#### Example 3

- **Input:** `workers = [7]`, `tasks = [[3, 3], [3, 3]]`
- **Output:** `3`

The regular worker cannot take either task. The extra worker completes one of them, and a task cannot be reused.
