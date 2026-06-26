## Problem Description & Examples
### Goal
You are given an integer `n`. There are `n` rooms numbered from `0` to `n - 1`.

You are given a 2D integer array `meetings` where `meetings[i] = [start_i, end_i]` means a meeting will be held during the half-closed time interval `[start_i, end_i)`. All the values of `start_i` are unique.

Meetings are allocated to rooms in the following manner:
1. Each meeting will take place in the unused room with the lowest number.
2. If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
3. When a room becomes unused, meetings that have been delayed should be given the room in the order of their original start-times.

Return the room number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

### Function Contract
**Inputs**

- `n`: int
- `meetings`: List[List[int]]

**Return value**

int - room number holding the most meetings

### Examples
**Example 1**

- Input: `n = 2, meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]`
- Output: `0`

**Example 2**

- Input: `n = 2, meetings = [[1, 6], [8, 13], [16, 24]]`
- Output: `0`

**Example 3**

- Input: `n = 2, meetings = [[8, 13], [3, 11]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
- [Activity selection / interval choice](greedy_01_activity-selection.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
