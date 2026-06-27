# Reschedule Meetings for Maximum Free Time II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3440 |
| Difficulty | Medium |
| Topics | Array, Greedy, Enumeration |
| Official Link | [reschedule-meetings-for-maximum-free-time-ii](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/) |

## Problem Description & Examples
### Goal
Given the total time available in a day and a list of scheduled meetings, determine the maximum possible duration of a single continuous block of free time that can be achieved by moving exactly one meeting to a different position. The moved meeting must not overlap with any other existing meetings.

### Function Contract
**Inputs**

- `eventTime` (int): The total duration of the day (from time 0 to `eventTime`).
- `startTime` (List[int]): A list of start times for each meeting.
- `endTime` (List[int]): A list of end times for each meeting.

**Return value**

- `int`: The maximum length of a continuous free time interval achievable after relocating one meeting.

### Examples
**Example 1**

- Input: `eventTime = 5, startTime = [1, 3], endTime = [2, 4]`
- Output: `3`
- Explanation: Moving the meeting [1, 2] to [4, 5] creates a free block from 0 to 3.

**Example 2**

- Input: `eventTime = 10, startTime = [0, 7, 9], endTime = [1, 8, 10]`
- Output: `5`

**Example 3**

- Input: `eventTime = 5, startTime = [0, 1, 2, 3, 4], endTime = [1, 2, 3, 4, 5]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved using a greedy approach combined with prefix/suffix maximums. We first identify all existing gaps between meetings. To determine if a meeting can be moved into a gap, we check if the gap size is at least the duration of the meeting. We use a prefix maximum array to track the largest gaps to the left of a meeting and a suffix maximum array for gaps to the right, allowing us to efficiently calculate the potential free time created by shifting a meeting.

---

## Complexity Analysis
- **Time Complexity**: O(N log N) due to sorting the meetings by start time, where N is the number of meetings. The subsequent linear scans are O(N).
- **Space Complexity**: O(N) to store the gaps and the prefix/suffix maximum arrays.
