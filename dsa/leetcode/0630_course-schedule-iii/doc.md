# Course Schedule III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 630 |
| Difficulty | Hard |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/course-schedule-iii/) |

## Problem Description
### Goal
You are given `n` different online courses, where `courses[i] = [duration_i, lastDay_i]`. Taking course `i` continuously occupies `duration_i` days, and that course must be finished before or on `lastDay_i`.

Starting on the first day, choose and order the maximum number of courses you can take. You cannot take two or more courses simultaneously, and you do not need to take every course. Each selected course must meet its own deadline in the resulting sequential schedule, not merely the final course's deadline.

### Function Contract
**Inputs**

- `courses`: pairs `[duration, deadline]`; courses cannot overlap and the first selected course starts on day 1

**Return value**

- The maximum number of courses that can all finish by their respective deadlines

### Examples
**Example 1**

- Input: `courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]`
- Output: `3`

**Example 2**

- Input: `courses = [[1,2]]`
- Output: `1`

**Example 3**

- Input: `courses = [[3,2],[4,3]]`
- Output: `0`
