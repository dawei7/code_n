# The Earliest Moment When Everyone Become Friends

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1101 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Union-Find, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [the-earliest-moment-when-everyone-become-friends](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/).

### Goal
Friendship events connect pairs of people at specific timestamps. Return the earliest timestamp at which all `n` people belong to one connected friendship group. If that never happens, return `-1`.

### Function Contract
**Inputs**

- `logs`: List of `[timestamp, person_a, person_b]` friendship events.
- `n`: Number of people labeled `0` through `n - 1`.

**Return value**

Earliest timestamp when everyone is connected, or `-1`.

### Examples
**Example 1**

- Input: `logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6`
- Output: `20190301`

**Example 2**

- Input: `logs = [[0,2,0],[1,0,1],[3,0,3]], n = 4`
- Output: `3`

**Example 3**

- Input: `logs = [[1,0,1]], n = 3`
- Output: `-1`

---

## Solution
### Approach
Sort the logs by timestamp and process them in chronological order with union-find. Each successful union reduces the number of connected components by one. As soon as the component count becomes `1`, the current timestamp is the earliest possible answer.

If all logs are processed and more than one component remains, not everyone becomes connected.

### Complexity Analysis
- **Time Complexity**: `O(m log m + m alpha(n))`, where `m` is the number of logs.
- **Space Complexity**: `O(n)` for union-find.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
