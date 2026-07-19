# Meeting Rooms

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 252 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/meeting-rooms/) |

## Problem Description
### Goal
Given a collection of meeting intervals `[start, end]`, determine whether one person can attend every meeting. Each interval is half-open: the meeting occupies its start time up to, but not including, its end time.

Return `True` when no two meetings overlap in time and `False` when any pair requires simultaneous attendance. A meeting ending exactly when another begins is compatible and does not count as an overlap. Input order does not indicate chronological order, so all intervals must be considered. Empty and one-meeting schedules are always attendable.

### Function Contract
**Inputs**

- `intervals`: meeting intervals `[start, end]`

**Return value**

`True` exactly when no two meetings overlap.

### Examples
**Example 1**

- Input: `intervals = [[0,30],[5,10],[15,20]]`
- Output: `false`

**Example 2**

- Input: `intervals = [[7,10],[2,4]]`
- Output: `true`

**Example 3**

- Input: `intervals = [[1,2],[2,3]]`
- Output: `true`
