# Reschedule Meetings for Maximum Free Time I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3439 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/) |

## Problem Description

### Goal

An event occupies the interval from time $0$ through `eventTime`. Within it are $n$ non-overlapping meetings listed in chronological order; meeting $i$ occupies `[startTime[i], endTime[i]]`.

You may move the start time of at most `k` meetings while preserving every moved meeting's duration. All meetings must remain inside the event, non-overlapping, and in their original relative order. Determine the greatest possible length of one continuous interval containing no meeting.

### Function Contract

**Inputs**

- `eventTime`: The event endpoint, from $1$ through $10^9$.
- `k`: The maximum number of meetings that may move, from $1$ through $n$.
- `startTime`: The ordered meeting start times.
- `endTime`: The corresponding meeting end times.

Both arrays have the same length $n$, where $2\le n\le10^5$. Every meeting has positive duration, lies inside the event, and ends no later than the next meeting starts.

**Return value**

Return the maximum achievable length of one continuous free-time interval.

### Examples

#### Example 1

- **Input:** `eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]`
- **Output:** `2`

#### Example 2

- **Input:** `eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]`
- **Output:** `6`

#### Example 3

- **Input:** `eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]`
- **Output:** `0`
