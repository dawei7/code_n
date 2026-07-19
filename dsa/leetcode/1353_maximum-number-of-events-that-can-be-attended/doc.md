# Maximum Number of Events That Can Be Attended

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1353 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/) |

## Problem Description

### Goal

You are given a list of events. Event `i` is described by `[startDay, endDay]` and may be attended on any one integer day $d$ satisfying $startDay \le d \le endDay$.

You may attend at most one event on a given day, and attending an event uses only the chosen day rather than its entire interval. Select which events to attend and assign each selected event a valid day so that the number attended is as large as possible. Return that maximum count.

### Function Contract

**Inputs**

- `events`: a nonempty list of inclusive `[startDay, endDay]` intervals.
- Let $n$ be the number of events.

**Return value**

- Return the maximum number of events that can be assigned distinct valid attendance days.

### Examples

**Example 1**

- Input: `events = [[1,2],[2,3],[3,4]]`
- Output: `3`

**Example 2**

- Input: `events = [[1,2],[2,3],[3,4],[1,2]]`
- Output: `4`

**Example 3**

- Input: `events = [[1,1],[1,1],[1,1]]`
- Output: `1`
