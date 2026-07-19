# Employee Free Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 759 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Sweep Line, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/employee-free-time/) |

## Problem Description

### Goal

Each employee has a sorted list of non-overlapping busy intervals. Given all schedules, find the intervals of finite, positive length during which every employee is free at the same time.

Return the common free intervals in chronological order. Time covered by even one employee's busy interval is unavailable, and touching busy intervals leave no positive-length gap. Do not report the unbounded free time before the earliest scheduled work or after the latest scheduled work.

### Function Contract

**Inputs**

- `schedule`: a list of employee schedules; each schedule is a list of inclusive-start, exclusive-end pairs `[start, end]` describing busy time.

**Return value**

- A sorted list of finite `[start, end]` pairs representing gaps in the union of all busy intervals.

### Examples

**Example 1**

- Input: `schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]`
- Output: `[[3,4]]`
- Explanation: The combined busy union leaves only the finite gap from `3` to `4`.

**Example 2**

- Input: `schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]`
- Output: `[[5,6],[7,9]]`
- Explanation: No employee is busy during either gap between consecutive merged busy blocks.
