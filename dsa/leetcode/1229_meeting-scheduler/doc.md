# Meeting Scheduler

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1229 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [meeting-scheduler](https://leetcode.com/problems/meeting-scheduler/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/meeting-scheduler/).

### Goal
Find the earliest time interval of length `duration` that is available in both people's schedules.

### Function Contract
**Inputs**

- `slots1: List[List[int]]` - Available half-open time intervals for the first person.
- `slots2: List[List[int]]` - Available half-open time intervals for the second person.
- `duration: int` - Required meeting length.

**Return value**

`List[int]` - `[start, start + duration]` for the earliest valid meeting, or `[]` if none exists.

### Examples
**Example 1**

- Input: `slots1 = [[10, 50], [60, 120], [140, 210]], slots2 = [[0, 15], [60, 70]], duration = 8`
- Output: `[60, 68]`

**Example 2**

- Input: `slots1 = [[10, 50], [60, 120], [140, 210]], slots2 = [[0, 15], [60, 70]], duration = 12`
- Output: `[]`

**Example 3**

- Input: `slots1 = [[1, 2]], slots2 = [[3, 4]], duration = 1`
- Output: `[]`

---

## Solution
### Approach
Sort both slot lists by start time and walk them with two pointers. At each step, compute the overlap between the current intervals. If the overlap length is at least `duration`, return the earliest meeting starting at the overlap start. Otherwise advance the pointer whose interval ends first, because that interval cannot overlap any later slot more usefully.

### Complexity Analysis
- **Time Complexity**: `O(n log n + m log m)` for sorting, plus `O(n + m)` for the two-pointer scan.
- **Space Complexity**: `O(1)` auxiliary space if the slot lists are sorted in place.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
