# Meeting Rooms III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2402 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Heap (Priority Queue), Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/meeting-rooms-iii/) |

## Problem Description

### Goal

There are `n` meeting rooms numbered from 0 through `n - 1`. Each meeting has
a unique original start time and occupies a half-closed interval `[start,end)`,
so a room finishing at a time is available for a meeting starting at that same
time.

Process meetings by original start time. A meeting uses the lowest-numbered
unused room. If every room is busy, delay the meeting until the earliest room
becomes free while preserving its original duration; meetings awaiting rooms
retain priority by their original start times. After every meeting has been
assigned, return the room that held the most meetings, breaking a count tie in
favor of the lowest room number.

### Function Contract

**Inputs**

- `n`: The number of rooms, with $1 \le n \le 100$.
- `meetings`: A list of $m$ pairs `[start, end]`, where
  $1 \le m \le 10^5$, $0 \le \texttt{start}<\texttt{end}\le5\cdot10^5$,
  and all start times are distinct.

**Return value**

Return the smallest room number among those with the maximum number of
assigned meetings after applying all allocation and delay rules.

### Examples

#### Example 1

- **Input:** `n = 2`, `meetings = [[0,10],[1,5],[2,7],[3,4]]`
- **Output:** `0`
- **Explanation:** Each room handles two meetings, so the smaller room wins the
  tie.

#### Example 2

- **Input:** `n = 3`, `meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]`
- **Output:** `1`
- **Explanation:** Rooms 1 and 2 each handle two meetings, while room 0 handles
  one; the smaller tied room is 1.

#### Example 3

- **Input:** `n = 1`, `meetings = [[5,8],[0,2],[3,4]]`
- **Output:** `0`
- **Explanation:** The only room necessarily hosts all three meetings, regardless
  of the input ordering.
