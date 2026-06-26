# Maximum Number of Events That Can Be Attended

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1353 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Official Link | [maximum-number-of-events-that-can-be-attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/) |

## Problem Description & Examples
### Goal
Given a list of events where each event has a starting day and an ending day, attend at most one event per day and choose days so the total number of attended events is as large as possible.

### Function Contract
**Inputs**

- `events`: a list of `[startDay, endDay]` pairs.

**Return value**

The maximum number of events that can be attended.

### Examples
**Example 1**

- Input: `events = [[1,2],[2,3],[3,4]]`
- Output: `3`

**Example 2**

- Input: `events = [[1,2],[2,2],[3,3],[3,4]]`
- Output: `4`

**Example 3**

- Input: `events = [[1,4],[1,4],[1,4],[2,2]]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Greedy scheduling with sorting and a min-heap. Sweep days in increasing order, add events that have started, discard expired events, and attend the event with the earliest ending day.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n + D log n)`, where `n` is the number of events and `D` is the swept day range; an implementation that jumps between active days is commonly summarized as `O(n log n)`.
- **Space Complexity**: `O(n)`
