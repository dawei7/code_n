# Reschedule Meetings for Maximum Free Time II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3440 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/) |

## Problem Description

### Goal

An event spans time $0$ through `eventTime` and contains $n$ non-overlapping meetings listed in chronological order. Meeting $i$ occupies `[startTime[i], endTime[i]]`.

You may reschedule at most one meeting by changing its start time while preserving its duration. The moved meeting must remain inside the event and cannot overlap another meeting. Unlike the first version of this problem, moving it may change the meetings' relative order. Return the greatest possible length of one continuous period containing no meeting.

### Function Contract

**Inputs**

- `eventTime`: The event endpoint, from $1$ through $10^9$.
- `startTime`: The ordered start times of the meetings.
- `endTime`: The corresponding end times.

Both arrays have length $n$, where $2\le n\le10^5$. Each meeting has positive duration, lies within the event, and ends no later than the following meeting starts.

**Return value**

Return the maximum achievable length of a continuous free-time interval after moving at most one meeting.

### Examples

#### Example 1

- **Input:** `eventTime = 5, startTime = [1,3], endTime = [2,5]`
- **Output:** `2`

#### Example 2

- **Input:** `eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]`
- **Output:** `7`

#### Example 3

- **Input:** `eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]`
- **Output:** `6`

#### Example 4

- **Input:** `eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]`
- **Output:** `0`
