# Finding the Users Active Minutes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1817 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [finding-the-users-active-minutes](https://leetcode.com/problems/finding-the-users-active-minutes/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/finding-the-users-active-minutes/).

### Goal
Each log entry records a user and a minute. A user's active minutes is the number of distinct minutes appearing in their logs. Count how many users have exactly `1`, `2`, ..., `k` active minutes.

### Function Contract
**Inputs**

- `logs`: a list of `[userId, minute]` entries.
- `k`: the maximum active-minute bucket.

**Return value**

Return an array `answer` of length `k`, where `answer[i - 1]` is the number of users with exactly `i` active minutes.

### Examples
**Example 1**

- Input: `logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5`
- Output: `[0,2,0,0,0]`

**Example 2**

- Input: `logs = [[1,1],[2,2],[2,3]], k = 4`
- Output: `[1,1,0,0]`

**Example 3**

- Input: `logs = [[1,10],[1,10],[1,11]], k = 3`
- Output: `[0,1,0]`

---

## Solution
### Approach
Use a dictionary from user id to a set of minutes. After processing all logs, compute the size of each user's set and increment the corresponding bucket.

### Complexity Analysis
- **Time Complexity**: `O(len(logs))`
- **Space Complexity**: `O(len(logs))`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
