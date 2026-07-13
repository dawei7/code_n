# Minimum Number of Work Sessions to Finish the Tasks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1986 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-work-sessions-to-finish-the-tasks](https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/).

### Goal
Assign every task to work sessions. A session can hold tasks whose total duration is at most `sessionTime`; minimize the number of sessions used.

### Function Contract
**Inputs**

- `tasks`: task durations.
- `sessionTime`: capacity of each work session.

**Return value**

Return the minimum number of sessions required.

### Examples
**Example 1**

- Input: `tasks = [1,2,3], sessionTime = 3`
- Output: `2`

**Example 2**

- Input: `tasks = [3,1,3,1,1], sessionTime = 8`
- Output: `2`

**Example 3**

- Input: `tasks = [1,2,3,4,5], sessionTime = 15`
- Output: `1`

---

## Solution
### Approach
Use bitmask DP. Precompute each subset's total duration, or transition from a mask with state `(sessions, remaining_capacity)`, choosing the better of adding a task to the current session or opening a new one.

### Complexity Analysis
- **Time Complexity**: `O(n * 2^n)`
- **Space Complexity**: `O(2^n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
