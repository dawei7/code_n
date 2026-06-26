# Number of Students Doing Homework at a Given Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1450 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [number-of-students-doing-homework-at-a-given-time](https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/) |

## Problem Description & Examples
### Goal
Count students whose homework interval includes the given query time.

### Function Contract
**Inputs**

- `startTime`: start times for each student.
- `endTime`: end times for each student.
- `queryTime`: the time to check.

**Return value**

The number of intervals `[startTime[i], endTime[i]]` containing `queryTime`.

### Examples
**Example 1**

- Input: `startTime = [1,2,3], endTime = [3,2,7], queryTime = 4`
- Output: `1`

**Example 2**

- Input: `startTime = [4], endTime = [4], queryTime = 4`
- Output: `1`

**Example 3**

- Input: `startTime = [9,8,7], endTime = [10,9,8], queryTime = 6`
- Output: `0`

---

## Underlying Base Algorithm(s)
Direct interval counting.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
