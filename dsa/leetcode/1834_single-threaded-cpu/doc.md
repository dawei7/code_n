# Single-Threaded CPU

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/single-threaded-cpu/) |
| Frontend ID | 1834 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

There are $n$ tasks labeled from 0 through $n-1$. For task $i$, `tasks[i] = [enqueueTime, processingTime]` states when it becomes available and how long it occupies a single-threaded CPU.

Whenever the CPU is idle and one or more tasks are available, it chooses the task with the shortest processing time; equal processing times are resolved by the smaller original index. A chosen task runs to completion without preemption, and another task may start at that exact completion time. When no task is available, the CPU remains idle. Return the task indices in execution order.

### Function Contract

**Inputs**

- `tasks`: an array of $n$ pairs `[enqueueTime, processingTime]`, where $1 \le n \le 10^5$.
- Every enqueue and processing time is between 1 and $10^9$, inclusive.
- Array position $i$ is the task's fixed index and final tie breaker.

**Return value**

- Return all task indices in the exact order in which the CPU starts them.

### Examples

**Example 1**

- Input: `tasks = [[1,2],[2,4],[3,2],[4,1]]`
- Output: `[0,2,3,1]`

Task 0 finishes at time 3. Tasks 1 and 2 are then available, so the shorter task 2 runs next.

**Example 2**

- Input: `tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]`
- Output: `[4,3,2,0,1]`

All tasks arrive together and are selected by processing time.

**Example 3**

- Input: `tasks = [[5,2],[100,1]]`
- Output: `[0,1]`

The CPU jumps across two idle intervals before the respective tasks arrive.
