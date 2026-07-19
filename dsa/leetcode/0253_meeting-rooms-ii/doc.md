# Meeting Rooms II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 253 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Greedy, Sorting, Heap (Priority Queue), Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/meeting-rooms-ii/) |

## Problem Description
### Goal
Given meeting intervals `[start, end]`, assign every meeting to a room so that no room hosts overlapping intervals. Intervals are half-open, so a room becomes available when one meeting ends and may host another meeting starting at that exact time.

Return the minimum number of rooms needed for the entire schedule. This equals the greatest number of meetings active simultaneously, regardless of the order in which intervals are supplied. Empty input needs zero rooms, while isolated or boundary-touching meetings can reuse one room. Return only the minimum count, not a concrete room assignment.

### Function Contract
**Inputs**

- `intervals`: meeting intervals `[start, end]`

**Return value**

The maximum number of simultaneous meetings.

### Examples
**Example 1**

- Input: `intervals = [[0,30],[5,10],[15,20]]`
- Output: `2`

**Example 2**

- Input: `intervals = [[7,10],[2,4]]`
- Output: `1`

**Example 3**

- Input: `intervals = [[1,5],[2,6],[3,7]]`
- Output: `3`
