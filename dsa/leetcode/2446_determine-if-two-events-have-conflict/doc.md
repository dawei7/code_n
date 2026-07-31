# Determine if Two Events Have Conflict

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2446 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Determine if Two Events Have Conflict](https://leetcode.com/problems/determine-if-two-events-have-conflict/) |

## Problem Description

### Goal

Two inclusive events occur on the same day. Each event is represented as `[startTime, endTime]`, and every endpoint is a valid 24-hour time string in fixed-width `"HH:MM"` format. Each start time is no later than its corresponding end time.

The events conflict when their inclusive time intervals have a non-empty intersection, meaning at least one moment belongs to both events. Return `true` when such a common moment exists and `false` otherwise. Sharing only an endpoint still counts as a conflict.

### Function Contract

**Inputs**

- `event1`: Two `"HH:MM"` strings giving the inclusive start and end of the first same-day event.
- `event2`: Two `"HH:MM"` strings giving the inclusive start and end of the second same-day event.

Each string has length five, uses valid 24-hour time, and each event's start is no later than its end.

**Return value**

- `true` if the inclusive events share at least one moment; otherwise `false`.

### Examples

**Example 1**

- Input: `event1 = ["01:15", "02:00"], event2 = ["02:00", "03:00"]`
- Output: `true`
- Explanation: Both events include `"02:00"`.

**Example 2**

- Input: `event1 = ["01:00", "02:00"], event2 = ["01:20", "03:00"]`
- Output: `true`
- Explanation: Their common interval runs from `"01:20"` through `"02:00"`.

**Example 3**

- Input: `event1 = ["10:00", "11:00"], event2 = ["14:00", "15:00"]`
- Output: `false`
- Explanation: The first event ends before the second begins.
