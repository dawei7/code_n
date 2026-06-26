# Two Best Non-Overlapping Events

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2054 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Dynamic Programming, Sorting, Heap (Priority Queue) |
| Official Link | [two-best-non-overlapping-events](https://leetcode.com/problems/two-best-non-overlapping-events/) |

## Problem Description & Examples
### Goal
Choose at most two events with non-overlapping inclusive time intervals, maximizing total value.

### Function Contract
**Inputs**

- `events`: entries `[start, end, value]`.

**Return value**

Return the maximum value obtainable from one or two compatible events.

### Examples
**Example 1**

- Input: `events = [[1,3,2],[4,5,2],[2,4,3]]`
- Output: `4`

**Example 2**

- Input: `events = [[1,3,2],[4,5,2],[1,5,5]]`
- Output: `5`

**Example 3**

- Input: `events = [[1,5,3],[6,6,5],[2,3,4]]`
- Output: `8`

---

## Underlying Base Algorithm(s)
Sort events by start time and build a suffix array of maximum event value from each position onward. For each event, binary-search the first event whose start is greater than the current end and combine the current value with that suffix maximum.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`
