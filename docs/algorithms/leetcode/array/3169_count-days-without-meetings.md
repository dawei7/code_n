# Count Days Without Meetings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3169 |
| Difficulty | Medium |
| Topics | Array, Sorting |
| Official Link | [count-days-without-meetings](https://leetcode.com/problems/count-days-without-meetings/) |

## Problem Description & Examples
### Goal
Given a total number of days in a period (labeled 1 to `days`) and a list of scheduled meeting intervals, calculate the number of days within that period where no meetings are scheduled.

### Function Contract
**Inputs**

- `days`: An integer representing the total number of days in the period.
- `meetings`: A list of lists, where each inner list `[start, end]` represents a meeting spanning from day `start` to day `end` inclusive.

**Return value**

- An integer representing the count of days that are not covered by any meeting interval.

### Examples
**Example 1**

- Input: `days = 10, meetings = [[5,7],[1,3],[9,10]]`
- Output: `2`

**Example 2**

- Input: `days = 5, meetings = [[2,4]]`
- Output: `3`

**Example 3**

- Input: `days = 6, meetings = [[1,6]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved using the **Interval Merging** technique. By sorting the meeting intervals by their start times, we can iterate through them to merge overlapping or contiguous intervals. Once merged, the total number of days occupied by meetings is the sum of the lengths of these disjoint intervals. Subtracting this sum from the total `days` yields the result.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of meetings, due to the sorting step. The subsequent linear scan takes `O(N)`.
- **Space Complexity**: `O(1)` or `O(N)` depending on the sorting implementation's space requirements, as we only store a few variables to track the current merged interval.
