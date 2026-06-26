# Determine if Two Events Have Conflict

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2446 |
| Difficulty | Easy |
| Topics | Array, String |
| Official Link | [determine-if-two-events-have-conflict](https://leetcode.com/problems/determine-if-two-events-have-conflict/) |

## Problem Description & Examples
### Goal
Given two time intervals representing events, each defined by a start and end time in "HH:MM" format, determine if the two events overlap. An overlap occurs if there is any point in time that belongs to both intervals, including their boundaries.

### Function Contract
**Inputs**

- `event1`: A list of two strings representing the start and end time of the first event (e.g., `["01:15", "02:00"]`).
- `event2`: A list of two strings representing the start and end time of the second event (e.g., `["02:00", "03:00"]`).

**Return value**

- `bool`: Returns `True` if the intervals overlap, otherwise `False`.

### Examples
**Example 1**

- Input: `event1 = ["01:15", "02:00"], event2 = ["02:00", "03:00"]`
- Output: `True`

**Example 2**

- Input: `event1 = ["01:00", "02:00"], event2 = ["02:12", "03:00"]`
- Output: `False`

**Example 3**

- Input: `event1 = ["10:00", "11:00"], event2 = ["14:00", "15:00"]`
- Output: `False`

---

## Underlying Base Algorithm(s)
The problem relies on interval comparison logic. Since the time strings are in "HH:MM" format, they are lexicographically sortable. Two intervals `[start1, end1]` and `[start2, end2]` overlap if and only if the maximum of the start times is less than or equal to the minimum of the end times (i.e., `max(start1, start2) <= min(end1, end2)`).

---

## Complexity Analysis
- **Time Complexity**: `O(1)`, as the input size is fixed (two intervals with two strings each), and string comparison takes constant time.
- **Space Complexity**: `O(1)`, as no additional data structures proportional to input size are required.
