# Meeting Rooms II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 253 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Greedy, Sorting, Heap (Priority Queue), Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/meeting-rooms-ii/) |

## Problem Description
### Goal
Given meeting intervals `[start, end]`, assign every meeting to a room so that no room hosts overlapping intervals. Intervals are half-open, so a room becomes available when one meeting ends and may host another meeting starting at that exact time.

Return the minimum number of rooms needed for the entire schedule. This equals the greatest number of meetings active simultaneously, regardless of the order in which intervals are supplied. Empty input needs zero rooms, while isolated or boundary-touching meetings can reuse one room. Return only the minimum count, not a concrete room assignment.

### Function Contract
**Inputs**

- `intervals`: meeting intervals `[start, end]`

**Return value**

The maximum number of simultaneous meetings.

### Examples
**Example 1**

- Input: `intervals = [[0,30],[5,10],[15,20]]`
- Output: `2`

**Example 2**

- Input: `intervals = [[7,10],[2,4]]`
- Output: `1`

**Example 3**

- Input: `intervals = [[1,5],[2,6],[3,7]]`
- Output: `3`

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Sort starts and endings as separate event streams**

Sort all start times and all end times separately. At the next start, reuse a room if the earliest ending is no later than that start; otherwise allocate another room.

The end pointer counts meetings already finished before the current start. Therefore `started - finished` is the number of occupied rooms, and its maximum is the required capacity.

**Peak simultaneous occupancy is the room count**

Before processing a start, every ending no later than that time can release its room. If the earliest remaining ending is later, all currently allocated rooms are still occupied and the new meeting needs another one. The sweep therefore maintains the exact number of active meetings after each event. Its maximum is necessary because those meetings overlap, and sufficient because a released room is always reused whenever possible.

#### Complexity detail

The two sorts cost $O(n \log n)$; the pointers each move at most `n` times. The two event arrays use $O(n)$ space.

#### Alternatives and edge cases

- **Check overlap at every time or against every interval:** can take $O(n^2)$ or depend on the coordinate range.
- Meetings that end exactly when another starts can share a room; an empty schedule needs zero rooms.

</details>
