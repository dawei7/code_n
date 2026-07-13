# Count Unhappy Friends

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1583 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-unhappy-friends](https://leetcode.com/problems/count-unhappy-friends/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-unhappy-friends/).

### Goal
Count friends who would prefer someone else over their assigned partner, where
that other person also prefers them over their own partner.

### Function Contract
**Inputs**

- `n`: the number of friends.
- `preferences`: each friend's ordered preference list.
- `pairs`: the assigned friend pairs.

**Return value**

The number of unhappy friends.

### Examples
**Example 1**

- Input: `n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]`
- Output: `2`

**Example 2**

- Input: `n = 2, preferences = [[1], [0]], pairs = [[1, 0]]`
- Output: `0`

**Example 3**

- Input: `n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]`
- Output: `4`

---

## Solution
### Approach
Build a rank table where `rank[x][y]` gives how much friend `x` prefers friend
`y`, and build the current partner map. For each friend `x`, inspect only the
friends ranked above `x`'s partner; if any such friend `u` also ranks `x` above
their own partner, mark `x` unhappy.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`.
- **Space Complexity**: `O(n^2)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
