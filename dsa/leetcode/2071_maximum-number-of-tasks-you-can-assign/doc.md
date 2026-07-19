# Maximum Number of Tasks You Can Assign

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2071 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Greedy, Queue, Sorting, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/) |

## Problem Description

### Goal

There are $n$ tasks with individual strength requirements and $m$ workers with individual strengths. A worker can complete a task when the worker's strength is at least its requirement. Each task and each worker may participate in at most one assignment.

Up to `pills` workers may each receive one magical pill. A pill increases that worker's strength by exactly `strength` for the assignment; no worker may take more than one pill. Pills need not all be used.

Choose the assignments and pill recipients to maximize the number of completed tasks. Return that maximum count, including zero when no task can be matched.

### Function Contract

**Inputs**

- `tasks`: an array of $n$ task requirements, where $1 \le n \le 5\cdot10^4$.
- `workers`: an array of $m$ worker strengths, where $1 \le m \le 5\cdot10^4$.
- `pills`: the available pill count, where $0 \le \texttt{pills}\le m$.
- `strength`: the nonnegative strength added by one pill.

Every task requirement, worker strength, and `strength` lies between $0$ and $10^9$. Let $r=\min(n,m)$.

**Return value**

- Return the greatest number of one-to-one task-worker assignments achievable under the pill rules.

### Examples

**Example 1**

- Input: `tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1`
- Output: `3`
- Explanation: Boost worker `0` to complete task `1`; the two strength-`3` workers complete requirements `2` and `3`.

**Example 2**

- Input: `tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5`
- Output: `1`
- Explanation: One boosted worker can complete one task, but only one pill is available.

**Example 3**

- Input: `tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10`
- Output: `2`
- Explanation: Two boosted workers can meet requirements `10` and `15`; no worker can reach `30`.
